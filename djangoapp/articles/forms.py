from django import forms
from .import models
#model forms 
# something like usercreation form 
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']
        #we created our model form which will take 4 fields
