from django.db import connection
from reports.models import Report
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler

from core.mail import ReportService
from client.models import Client

from cases.models import Case
from cases.filters import CaseFilter


email_service = ReportService


def get_cases(filters):
    search_arg = str(filters.get('search', '')).lower()
    if len(search_arg.strip()) > 3 and search_arg.startswith('cc/'):
        id_for_search = int(search_arg.split('cc/')[1])
        cases = Case.objects.filter(id=id_for_search)
    else:
        cases = Case.objects.all()
    keys_filter = ['services']
    for key in keys_filter:
        if type(filters.get(key)) == list and len(filters.get(key)) == 1:
            filters[key] = filters[key][0]
    if filters:
        case_filter = CaseFilter(filters, queryset=cases)
        cases = case_filter.qs
    return cases


def send_reports(tenant=None):
    if tenant:
        connection.set_tenant(tenant)
    reports = Report.objects.all()
    for report in reports:
        last_run_at = report.last_run_at
        time_frequency = report.time_frequency
        time_unit = report.time_unit
        time_in_seconds = 0
        if time_unit == 'daily':
            time_in_seconds = time_frequency * 60 * 60 * 24
        elif time_unit == 'weekly':
            time_in_seconds = time_frequency * 60 * 60 * 24 * 7
        elif time_unit == 'monthly':
            time_in_seconds = time_frequency * 60 * 60 * 24 * 30
        else:
            time_in_seconds = 60 * 60 * 24
        current_time = timezone.now()
        if (current_time - last_run_at).total_seconds() >= time_in_seconds or not report.has_run:
            print(f'Sending report ({report.id}) at: {timezone.now()}')
            filters = report.filters
            cases = get_cases(filters)
            email_service.send_report_mail(
                report_title=report.title,
                recipients=report.email_list,
                cases=cases,
            )
            report.last_run_at = current_time
            report.has_run = True
            report.save()


def send_reports_tenants():
    print(f'Cronjob started at: {timezone.now()}')
    send_reports()
    tenants = Client.objects.all()
    for tenant in tenants:
        send_reports(tenant)


def start():
    run_every = 30
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=send_reports_tenants,
        trigger="interval",
        seconds=run_every
    )
    scheduler.start()
