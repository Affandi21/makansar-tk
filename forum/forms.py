from django import forms
from .models import Discussion, Reply

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'message']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']