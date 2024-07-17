from django import forms
from .models import DevTool, Post, get_devtool_choices

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']

class PostForm(forms.ModelForm):
    devtool = forms.ChoiceField(choices=[])

    class Meta:
        model = Post
        fields = ['title', 'image', 'devtool', 'content', 'interest']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['devtool'].choices = get_devtool_choices()




