
from django.conf import settings
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import Case, Customer, Invoice, VehicleHire
from .VehicleActionSerializer import VehicleActionSerializer
from .VehicleHireCustomerSerializer import VehicleHireCustomerSerializer


class VehicleHireSerializer(VehicleActionSerializer):
    customer = VehicleHireCustomerSerializer()
    case = serializers.PrimaryKeyRelatedField(
        required=False, allow_null=True, queryset=Case.objects.get_queryset()
    )
    invoice = serializers.PrimaryKeyRelatedField(
        required=False, allow_null=True, queryset=Invoice.objects.get_queryset()
    )

    class Meta:
        model = VehicleHire
        fields = (
            'id', 'case', 'invoice', 'vehicle', 'customer', 'daily_hire_rate',
            'start_hire_latitude', 'start_hire_longitude',
            'end_hire_latitude', 'end_hire_longitude',
            'start_date', 'end_date', 'notes', 'created_at'
        )

    def get_customer_from_data(self, customer_data):
        customer_obj = None

        if customer_data:
            try:
                customer_id = customer_data.pop('id', None)
                customer_name = customer_data.pop('name', None)
                if customer_id:
                    customer_obj = Customer.objects.get(pk=customer_id)
                elif customer_name:
                    customer_obj = Customer.objects.get(name=customer_name)
            except Customer.DoesNotExist:
                raise serializers.ValidationError({'customer': 'Specified customer not found'})
            except Customer.MultipleObjectsReturned:
                raise serializers.ValidationError({'customer': 'Multiple customers with specified name exist'})

        return customer_obj

    def validate(self, attrs):
        attrs = super().validate(attrs)

        start_date, end_date, vehicle_id = attrs['start_date'], attrs.get('end_date', None), attrs['vehicle'].pk
        if end_date:
            q = (
                    Q(start_date__lte=start_date) & (Q(end_date__gte=start_date) | Q(end_date__isnull=True))
                    | Q(start_date__lte=end_date) & (Q(end_date__gte=end_date) | Q(end_date__isnull=True))
            )
        else:
            q = Q(end_date__gte=start_date)
        qs = VehicleHire.objects.filter(q, vehicle_id=vehicle_id)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if hire := qs.first():
            err_msg = 'Hire for this vehicle for these dates already exists. Dates: {} - {}'.format(
                hire.start_date.strftime(settings.DEFAULT_DATE_FORMAT),
                (hire.end_date and hire.end_date.strftime(settings.DEFAULT_DATE_FORMAT)) or ''
            )
            raise ValidationError({'start_date': err_msg, 'end_date': err_msg})

        if invoice := attrs.get('invoice', None):
            if invoice.invoice_type != Invoice.InvoiceType.hire:
                raise ValidationError({'invoice': 'Specified invoice is not of the type hire'})
            if (
                    self.instance and invoice.vehicle_hire != self.instance.pk
                    or not self.instance and invoice.vehicle_hire
            ):
                raise ValidationError({'invoice': 'Invoice already have a booking assigned'})
        return attrs

    def create(self, validated_data):
        customer_data = validated_data.pop('customer', None)

        hire_object = super().create(validated_data)

        if customer := self.get_customer_from_data(customer_data):
            hire_object.customer_id = customer.pk
            hire_object.save()

        return hire_object

    def update(self, instance, validated_data):
        customer_data = validated_data.pop('customer', None)

        instance = super().update(instance, validated_data)

        if customer_data is not None:
            # Do not change customer if its data is not specified
            customer = self.get_customer_from_data(customer_data)
            if instance.customer_id != customer.pk:
                instance.customer = customer
                instance.save()

        return instance
