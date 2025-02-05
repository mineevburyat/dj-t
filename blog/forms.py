from django import forms
from .models import Category, Post

TEST_CHOICE = (
    (1,'rfrfz-nj'), 
    (2, 'dsgfdg')
)

class PostAddForm(forms.ModelForm):
    # title = forms.CharField(max_length=160,
    #                         widget=forms.TextInput())
    # content = forms.CharField(widget=forms.Textarea())
    # # category = forms.ChoiceField(choices=TEST_CHOICE)
        
    # image = forms.ImageField(required=False,
    #                          widget=forms.FileInput())
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={
                "rows": "15",
                "class": "form-control"
            }),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={
                "rows": "15",
                "class": "form-control"
            }),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }
