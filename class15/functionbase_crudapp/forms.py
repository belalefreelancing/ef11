from django import forms
from ef11_app.models import Banner


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'