from django.urls import path
from .views import UploadedFileView, ListFilesView, DetailFilesView

urlpatterns = [
    path('file/', UploadedFileView.as_view(), name="upload"),
    path('files/', ListFilesView.as_view(), name="filelist"),
    path('files/<int:pk>', DetailFilesView.as_view(), name='delete')
]