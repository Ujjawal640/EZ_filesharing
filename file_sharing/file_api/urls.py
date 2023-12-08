from django.urls import path
from .views import CustomUserCreateView, FileListView, FileUploadView, TokenObtainView, FileDownloadView

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('token/', TokenObtainView.as_view(), name='token-obtain'),
    path('download-file/<int:pk>/', FileDownloadView.as_view(), name='file-download'),
]
