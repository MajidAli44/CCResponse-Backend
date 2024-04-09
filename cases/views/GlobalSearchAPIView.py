from functools import reduce
from operator import or_

from django.db.models import Q
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from cases.models import Case
from parties.models import Insurer, Introducer, Solicitor, Provider
from vehicles.models import HireVehicle


class GlobalSearchAPIView(APIView):

    search_settings = {
        'vehicle': {
            'model': HireVehicle,
            'fields': [
                'vrn', 'make_model', 'mot_expiry', 'tax_expiry',
                'registration', 'date_purchased', 'purchase_price',
                'service_due', 'tax_cost', 'mot_cost',
                'notes'
            ]
        },
        'insurer': {
            'model': Insurer,
            'fields': [
                'name', 'phone_number', 'email'
            ]
        },
        'introducer': {
            'model': Introducer,
            'fields': [
                'name', 'company_number', 'contact_number',
                'office_number', 'hire_fee', 'pi_fee',
                'address'
            ]
        },
        'solicitor': {
            'model': Solicitor,
            'fields': [
                'name', 'fullname', 'hotkey_number', 'contact_number',
                'pi_fee', 'address', 'notes'
            ]
        },
        'provider': {
            'model': Provider,
            'fields': [
                'name'
            ]
        },
        'case': {
            'model': Case,
            'fields': [
                'pk',
                'client__name',
                'client__vehicle__vrn',
                'client__email',
                'client__address'
            ]
        }
    }

    def build_search_query(self, model_ref, term):
        return reduce(or_, [Q(**{f'{field}__icontains': term}) for field in self.search_settings[model_ref]['fields']])

    search_parameter = openapi.Parameter('keywords', openapi.IN_QUERY, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[search_parameter])
    def get(self, request, *args, **kwargs):
        keywords = request.query_params['keywords']
        results = []
        if len(keywords.strip()) < 3:
            return JsonResponse({'results': []})

        if len(keywords.strip()) > 3 and keywords.lower().startswith('cc/'):
            id_for_search = int(keywords.lower().split('cc/')[1])
            cases = Case.objects.filter(id=id_for_search)
            for case in cases:
                results.append({
                    'type': 'case',
                    'id': case.pk,
                    'title': case.cc_ref,
                    'subtitle': case.client.name if case.client is not None else '-'
                })
        else:
            for model_ref, fields in self.search_settings.items():
                qs = fields['model'].objects.filter(self.build_search_query(model_ref, keywords))
                for current_model in qs:
                    if model_ref == 'vehicle':
                        results.append({
                            'type': 'vehicle',
                            'id': current_model.pk,
                            'title': current_model.vrn,
                            'subtitle': current_model.make_model
                        })
                    elif model_ref == 'insurer':
                        results.append({
                            'type': 'contact',
                            'subtype': 'insurer',
                            'id': current_model.pk,
                            'title': 'Insurer',
                            'subtitle': current_model.name
                        })
                    elif model_ref == 'introducer':
                        results.append({
                            'type': 'contact',
                            'subtype': 'introducer',
                            'id': current_model.pk,
                            'title': 'Introducer',
                            'subtitle': current_model.name
                        })
                    elif model_ref == 'solicitor':
                        results.append({
                            'type': 'contact',
                            'subtype': 'solicitor',
                            'id': current_model.pk,
                            'title': 'Solicitor',
                            'subtitle': current_model.name
                        })
                    elif model_ref == 'provider':
                        results.append({
                            'type': 'contact',
                            'subtype': 'provider',
                            'id': current_model.pk,
                            'title': 'Provider',
                            'subtitle': current_model.name
                        })
                    elif model_ref == 'case':
                        results.append({
                            'type': 'case',
                            'id': current_model.pk,
                            'title': current_model.cc_ref,
                            'subtitle': current_model.client.name if current_model.client is not None else '-'
                        })
        return JsonResponse({'results': results})
