from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["tckn",  "ziyaret",  "aciklama", "kart_no"]  # no "user" field (we set it automatically)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tckn"].widget.attrs.update({"class": "form-control"})
        self.fields["ziyaret"].widget.attrs.update({"class": "form-control"})
        self.fields["aciklama"].widget.attrs.update({"class": "form-control"})
        self.fields["kart_no"].widget.attrs.update({"class": "form-control"})

class CikisForm(forms.Form):
    tckn = forms.CharField(label="TCKN", max_length=11)
    tckn.widget.attrs.update({"class": "form-control"})

    