from django import forms

from .models import Group, Post


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Текст')
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label='Группа'
    )

    class Meta:
        model = Post
        fields = ('text', 'group')
