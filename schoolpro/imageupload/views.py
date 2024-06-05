from django.shortcuts import render, redirect
from django.views import View
from .forms import ImageUploadForm
from .models import ImageUpload

class UploadImageView(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, 'image/image_upload.html', {'form': form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
        return render(request, 'image/image_upload.html', {'form': form})
      
      
class ImageListView(View):
    def get(self, request):
        images = ImageUpload.objects.all()
        return render(request, 'image/image_list.html', {'images': images})
