from django.urls import re_path as url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView, TokenObtainPairView
)

from core.views import ResetPasswordSendMailAPIView, ResetPasswordVerifyTokenAPIView, ResetPasswordSetPasswordAPIView, \
    UserDetailAPIView, UserLogoutAPIView, UserRetrieveUpdateDestroyAPIView, UserListCreateAPIView, \
    UserChangePasswordAPIView, EmailVerifyAPIView, RegistrationVerifyAPIView, CreatePasswordAPIView, DashboardAPIView, \
    UserListAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# TODO: Remove after refactor
# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet, basename='users')
# router.register(r'cases/scheduled-to-chase', ScheduledToChaseCaseModelViewSet, basename='scheduled-to-chase-cases')
# router.register(r'vehicles', VehiclesModelViewSet, basename='vehicles')
# router.register(r'vehicle-hires', VehicleHireViewSet, basename='vehicle-hires')
# router.register(r'cases/documents', CaseDocumentViewSet, basename='case-documents')
# router.register(r'expenses', ExpensesViewSet, basename='expenses')
# router.register(r'injuries', InjuriesViewSet, basename='injuries')
# router.register(r'addresses', AddressViewSet, basename='addresses')
# router.register(r'contacts/insurers', ContactsInsurersViewSet, basename='contact-insurers')

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', UserLogoutAPIView.as_view(), name='auth_logout'),
    path('user/', include([
        path('', UserListCreateAPIView.as_view(), name='user_list_create'),
        path('public/', UserListAPIView.as_view(), name='user_public_list'),
        path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_update_retrieve_delete'),
        path('me/', UserDetailAPIView.as_view(), name='user_detail'),
        path('password_change/', UserChangePasswordAPIView.as_view(), name='change_password'),
        path('email_verify/', EmailVerifyAPIView.as_view(), name='email_verify'),
        path('registration_verify/', RegistrationVerifyAPIView.as_view(), name='registration_verify'),
        path('create_password/', CreatePasswordAPIView.as_view(), name='create_password'),
    ])),

    path('auth/reset-password/send-mail/', ResetPasswordSendMailAPIView.as_view(), name='reset-password-send-mail'),
    path('auth/reset-password/verify-token/', ResetPasswordVerifyTokenAPIView.as_view(),
         name='reset-password-verify-token'),
    path('auth/reset-password/set-password/', ResetPasswordSetPasswordAPIView.as_view(),
         name='reset-password-set-password'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),

    # path('cases/', CasesAPI.as_view(), name='cases-list'),  # Cached for every 5 seconds
    # path('cases/filtering-data/', CaseFilteringDataAPIView().as_view(), name='case_filtering_data'),
    # path('cases/case-creation-data/', CaseCreationDataAPIView.as_view(), name='case_creation_data'),
    # path('cases/<int:pk>/details/', CaseDetailAPIView.as_view(), name='cases-detail'),
    # path('cases/<int:pk>/financials/', CaseFinancialsAPIView.as_view(), name='case-financials'),
    # path('cases/<int:pk>/hire-sr/', CaseHireSRAPIView.as_view(), name='case-hire-sr'),
    # path('cases/<int:pk>/notes/', CaseNoteAPIView.as_view(), name='case_notes'),
    # path('cases/<int:pk>/documents/', CaseDocumentsAPIView.as_view(), name='case_documents'),
    # path('cases/<int:pk>/communications/', CommunicationAPIView.as_view(), name='communications'),
    # path('cases/<int:pk>/injury/', CaseInjuryAPIView.as_view(), name='case-injury'),
    # path('cases/<int:case_id>/set-chase-date/', ScheduledToChaseCaseSetAPIView.as_view(), name='case-set-chase-date'),
    #
    # path('vehicles/filtering-data/', VehicleFilteringDataAPIView.as_view(), name='vehicles-filtering-data'),
    #
    # path(
    #     'invoices/<int:pk>/change-settled-amount/', ChangeInvoiceSettledAmount.as_view(),
    #     name='change-invoice-settled-amount'
    # ),
    #
    # path('customers/data-for-assign/', CustomersAssignData.as_view(), name='customers-data-for-assign'),
    # path('solicitors/data-for-assign/', SolicitorsAssignData.as_view(), name='solicitors-data-for-assign'),
    # path('vehicles/data-for-assign/', VehiclesAssignData.as_view(), name='vehicles-data-for-assign'),
    #
    # path('cases/documents/templates/', DocumentTemplatesAPIView.as_view(), name='document_templates'),
    # path(
    #     'cases/<int:pk>/documents/generate-from-template/',
    #     CaseDocumentFromTemplateAPIView.as_view(),
    #     name='case-document-generate-from-template'
    # ),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# urlpatterns += router.urls
