from django.urls import path
from . import views

urlpatterns = [
    path('fileupload/', views.form_upload, name ='form_upload'),
    path('fileupload/list/', views.file_list, name="file_list"),
]
