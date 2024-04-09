from django.urls import path, include

from cases.views import (
    CaseListCreateAPIView, CaseUpdateAPIView,
    UserDisplayCaseColumnCreateAPIView, CaseNoteListCreateAPIView,
    FollowUpListCreateAPIView, FollowUpUpdateAPIView,
    CaseNoteDeleteAPIView, InstructEngineerAPIView,
    CaseFieldsDefaultPriceAPIView, ZapierCreateAPIView, CaseHireDetailCreateAPIView, GlobalSearchAPIView, CaseNoteUpdateAPIView,
    FollowUpDashboardListCreateAPIView,
)

follow_up_urls = [
    path('', FollowUpListCreateAPIView.as_view(),
         name='follow_up_list_create'),
    path('dashboard/', FollowUpDashboardListCreateAPIView.as_view(),
         name='follow_up_list_create'),
    path('<int:follow_up_pk>/', FollowUpUpdateAPIView.as_view(),
         name='follow_up_update'),

]

case_note_urls = [
    path('', CaseNoteListCreateAPIView.as_view(),
         name='case_note_list_create'),
    path('<int:case_note_pk>/', CaseNoteDeleteAPIView.as_view(),
         name='case_note_delete'),
    path('<int:case_note_pk>/update/', CaseNoteUpdateAPIView.as_view(),
         name='case_note_update'),
]

urlpatterns = [
    path('', CaseListCreateAPIView.as_view(), name='case_list_create'),
    path('search/', GlobalSearchAPIView.as_view()),
    path('hire_details/', CaseHireDetailCreateAPIView.as_view()),
    path('zapier/', ZapierCreateAPIView.as_view()),
    path('<int:case_pk>/', include([
        path('', CaseUpdateAPIView.as_view(), name='case_update'),
        path('instruct_engineer/', InstructEngineerAPIView.as_view(),
             name='instruct_engineer'),
        path('notes/', include(case_note_urls)),
        path('invoices/', include('invoices.urls')),
    ])),
    path('follow_ups/', include(follow_up_urls)),
    path('columns/', UserDisplayCaseColumnCreateAPIView.as_view(),
         name='display_columns'),
    path('default_prices/', CaseFieldsDefaultPriceAPIView.as_view(),
         name='vehicle_default_prices'),
]
