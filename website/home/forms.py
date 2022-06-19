from django import forms

# Create forms here
class DemoForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    phone_no = forms.IntegerField(min_value=8000000000, max_value=9999999999, required=True)
    profile_pic = forms.ImageField(required=True)