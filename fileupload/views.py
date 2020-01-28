from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import FileModel

def form_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UploadForm()
        return render(request, 'fileupload/form_upload.html', {'form': form})
