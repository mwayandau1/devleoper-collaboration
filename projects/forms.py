from .models import Projects, Review
from django import forms
from django import forms


class ProjectsForm(forms.ModelForm):
   class Meta:
       model = Projects
       fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link',]
       
       widgets = {'tags': forms.CheckboxSelectMultiple(),}

    
   def __init__(self, *args, **kargs):
        super(ProjectsForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class' : 'input', 'placeholder':'Add Title'})
        # self.fields['description'].widget.attrs.update({'class' : 'input', })


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body':'Add a comment to your vote',
        }
    def __init__(self, *args, **kargs):
        super(ReviewForm, self).__init__(*args, **kargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})