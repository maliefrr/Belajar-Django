from django import forms

class ContactForm(forms.Form):
    Nama = forms.CharField()
    Email = forms.EmailField()
    Subject = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(widget=forms.HiddenInput,required=False)

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        
        if len(honeypot):
            raise forms.ValidationError('Get Out here You Damn BOT')
        return honeypot