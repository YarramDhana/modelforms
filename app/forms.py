from django import forms
from app.models import *

class Topicform (forms.ModelForm):
    class Meta:
        model=Topic
        fields = '__all__'



 
class webpageform (forms.ModelForm):
    class Meta:
        model=Webpage 
        fields='__all__'
        exclude=['name']
        labels={'topic_name':'tname','location':'loc'}
        







class Accessform (forms.ModelForm):
    class  Meta:
        model=Access
        fields='__all__'
        #fields=['name','author']
        #exclude=['author','name']
        labels={'date':'dt'}
       # widgets={'date':forms.PasswordInput}
       






