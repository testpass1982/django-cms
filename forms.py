from django import forms

class PostWizardForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []