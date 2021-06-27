from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['descripcion'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Post
        fields = ('titulo', 'descripcion')