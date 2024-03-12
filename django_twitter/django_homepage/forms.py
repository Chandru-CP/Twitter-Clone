from django import forms
from .models import Post, Comment



class PostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'your-css-class', 'rows': 3, 'cols': 40}),
                              max_length=100)
    hashtags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'your-css-class','rows': 3,
                                                                             'cols': 40}))

    class Meta:
        model = Post
        fields = ['hashtags','message', 'picture']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']