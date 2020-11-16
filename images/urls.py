from django.urls import path
from .views import image_upload, album_view, image_id, index

app_name = 'images'

urlpatterns = [
    path('upload/',image_upload, name='upload'),
    path('album/',album_view, name='album'),
    path('image/<int:id>/',image_id, name='image_id'),
    path('',index,name='index'),
]

