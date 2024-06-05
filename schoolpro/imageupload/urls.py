from django.urls import path
from .views import UploadImageView, ImageListView

urlpatterns = [
    path('upload/', UploadImageView.as_view(), name='upload_image'),
    path('images/', ImageListView.as_view(), name='image_list'),
]
