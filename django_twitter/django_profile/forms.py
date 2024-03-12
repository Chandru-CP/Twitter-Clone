from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['content']
