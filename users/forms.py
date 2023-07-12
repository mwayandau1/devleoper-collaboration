from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skills


class UserCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {"first_name":"Name"}
    
    def __init__(self, *args, **kargs):
        super(UserCustomForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'short_intro', 'bio','profile_image','social_github', 
                  'social_twitter','social_linkedIn', 'social_youtube', 'social_website']
    def __init__(self, *args, **kargs):
        super(ProfileForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields =['name', 'description',]
    def __init__(self, *args, **kargs):
        super(SkillsForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

