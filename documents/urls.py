from django.urls import path

from documents.views import DocumentListAPIView, DocumentSelectAPIView, DocumentDeleteAPIView, DocumentCallbackView, \
    DocumentSignatureListCreateAPIView, DocumentDownloadAPIView, DocumentTemplatesListAPIView, \
    ZapierDocumentCreateAPIView, DocumentRenameAPIView

urlpatterns = [
    path('', DocumentListAPIView.as_view()),
    path('templates/', DocumentTemplatesListAPIView.as_view()),
    path('select/<int:pk>/', DocumentSelectAPIView.as_view(), name='document_select'),
    path('rename/<int:document_pk>/', DocumentRenameAPIView.as_view(), name='document_rename'),
    path('<int:pk>/', DocumentDeleteAPIView.as_view(), name='document_delete'),
    path('docusign_callback/', DocumentCallbackView.as_view(), name='docusign_callback'),
    path('document_signature/', DocumentSignatureListCreateAPIView.as_view(), name='document_signature_list_create'),
    path('download/', DocumentDownloadAPIView.as_view(),  name='documents_download'),
    path('zapier/', ZapierDocumentCreateAPIView.as_view())
]
