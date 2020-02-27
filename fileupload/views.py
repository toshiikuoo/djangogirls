# 参考　https://codor.co.jp/django/how-to-upload-file

from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import FileModel

def file_list(request):
    files = FileModel.objects.order_by('uploaded_date')
    return render(request, 'fileupload/file_list.html', {'files': files})

def form_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
        else:
            # エラーが画面が必要
            form = UploadForm()
    else:
        form = UploadForm()
    return render(request, 'fileupload/form_upload.html', {'form': form})
