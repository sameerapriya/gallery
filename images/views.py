from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from PIL import Image
from .forms import ImageTagForm
from .models import ImageTag

# Create your views here.

def image_upload(request):
    """ Method for uploading image """
    if request.method == 'POST':
        form = ImageTagForm(request.POST,request.FILES) 
        if form.is_valid():
            tags = form.cleaned_data.get('tag')
            tags_image = [i.id for i in tags] # to pass the many to many field in the model.
            for key in request.FILES.keys():
                for imagefield in request.FILES.getlist(key): #iterating through multiple images
                    image = ImageTag.objects.create(picture=imagefield)
                    image.tag.set(tags_image) # assigning tags
                    image.save()
            return HttpResponse('Successfully uploaded')
        return render(request,'images/upload_image.html',{'form':form}) # if not valid form throws an error.
    else : # for get method
        return render(request, 'images/upload_image.html',{'form':ImageTagForm()})


def album_view(request):
    """ Method for Album """
    if request.method == 'GET':
        objects = ImageTag.objects.all()
        p = Paginator(objects,8) 
        page_number = request.GET.get('page')
        objects = p.get_page(page_number)
        return render(request, 'images/album.html',{'imagetags':objects})


def image_id(request,id):
    """ Method for particular Image """
    imagetag = get_object_or_404(ImageTag,id=id)
    if request.method == 'GET':
        return render(request,"images/image.html",{'imagetag':imagetag})
    
    if request.POST.get('clockwise', False):
        image = imagetag.picture
        imagepil = Image.open(image)
        imagepil = imagepil.rotate(-90,expand=True) # Rotating the picture
        imagepil.save(imagetag.picture.file.name,overwrite=True) # overwriting the saved picture 
        return HttpResponse('Rotated Image successfully saved ')

    if request.POST.get('anticlockwise', False):
        image = imagetag.picture
        imagepil = Image.open(image)
        imagepil = imagepil.rotate(90,expand=True)
        imagepil.save(imagetag.picture.file.name,overwrite=True)
        return HttpResponse('Rotated Image successfully saved(AntiClockwise)')


def index(request):
    """ Method for homepage """
    if request.method == 'GET':
        return render(request,'images/index.html')