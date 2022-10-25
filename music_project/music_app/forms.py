from django import forms
from .models import CommentDB


class CommentAbout(forms.ModelForm):
    class Meta:
        model = CommentDB
        fields = '__all__'
        # fields = ['name', 'surname', 'comment', 'rating']