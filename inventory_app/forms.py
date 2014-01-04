from inventory_app.models import *

__author__ = 'Waheed'

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'off'}), label="Password", max_length=128)

    class Meta:
      fields = ('username', 'password')
      model = User

    def __init__(self, *args, **kwargs):
      css_class="col-lg-7"
      super(LoginForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs={'class': css_class,'placeholder':'Username'}
      self.fields['password'].widget.attrs={'class': css_class,'placeholder':'Password'}

    def clean(self):
      cleaned_data = self.cleaned_data
      username = cleaned_data.get('username', '').strip()
      password = cleaned_data.get('password', '')


      return cleaned_data


class EquipmentForm(forms.ModelForm):


  class Meta:
      fields = ('tag', 'description', 'location')
      model = Equipment


  def __init__(self, *args, **kwargs):
    super(EquipmentForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs={'rows': 4, 'cols': 80}
    self.fields['location'].widget.attrs={'rows': 4, 'cols': 80}


class PartForm(forms.ModelForm):


  class Meta:
      fields = ('code', 'part_number', 'quantity', 'max_level', 'min_level', 'reorder_point', 'last_price', 'currency', 'description', 'location',
                'vendor_detail')
      model = Part


  def __init__(self, *args, **kwargs):
    super(PartForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs={'rows': 4, 'cols': 80}
    self.fields['location'].widget.attrs={'rows': 4, 'cols': 80}
    self.fields['vendor_detail'].widget.attrs={'rows': 4, 'cols': 80}

  def set_read_only(self, is_read_only):
    self.fields['code'].widget.attrs={'readonly': is_read_only}
    self.fields['part_number'].widget.attrs={'readonly': is_read_only}


class IssueForm(forms.ModelForm):


  class Meta:
      fields = ('issued_to',)
      model = Part


class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'off'}), label="Password", max_length=128)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'off'}), label="Confirm Password", max_length=128)

    class Meta:
      fields = ('username', "email", 'password')
      model = User

    def __init__(self, *args, **kwargs):
      css_class="col-lg-7"
      super(AddUserForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs={'class': css_class,'placeholder':'Username'}
      self.fields['email'].widget.attrs={'class': css_class,'placeholder':'Email'}
      self.fields['password'].widget.attrs={'class': css_class,'placeholder':'Password'}
      self.fields['confirm_password'].widget.attrs={'class': css_class,'placeholder':'Confirm Password'}