from django import forms
ge=(('male','male'),('female','female'))
lan=(('english','english'),('tamil','tamil'),('telegu','telegu'))
class emplyoee(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    number=forms.IntegerField()
    email=forms.EmailField()
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=ge,widget=forms.RadioSelect)
    language=forms.MultipleChoiceField(choices=lan,widget=forms.CheckboxSelectMultiple)
