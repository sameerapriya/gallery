from django import forms
from .models import ImageTag, Tag

class ImageTagForm(forms.ModelForm):
    picture = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),label='Image',help_text='Multiple Images allowed')
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple,label='Tags',help_text='Tags for your images')
    class Meta:
        model = ImageTag
        fields = ('tag','picture',)
    
    # def save(self, commit=True):
    #     images = self.cleaned_data.pop('picture')
    #     tags = self.cleaned_data.pop('tag')
    #     for image in images:
    #         imagetag = ImageTag.objects.create(picture=image)
    #         imagetag.save()
    #         # for tag in tags:
    #         imagetag.tag.add(list(tags))
            
    #     return cleaned_data



