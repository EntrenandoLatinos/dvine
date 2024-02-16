from django import forms
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, Testimonial, Partner, Faq, Privacy, WorkImage, SocialMedia

SOCIAL_MEDIA_CHOICES = [
    ('01', 'Facebook'),
    ('02', 'Twitter'),
    ('03', 'Instagram'),
    ('04', 'TikTok'),
    ('05', 'YouTube'),
    ('06', 'LinkedIn'),
]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['location', 'phone1', 'phone2', 'email']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
        }

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'title', 'subtitle', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image', 'about', 'mision', 'vision']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title1', 'description1', 'title2', 'description2', 'title3', 'description3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'description1': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'description2': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'description3': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['title1', 'number1', 'title2', 'number2', 'title3', 'number3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'number1': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'number3': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['image', 'title', 'description', 'description_finish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description_finish': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class ServiceDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())

class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['service', 'image', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['image', 'name', 'location', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class TestimonialDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['image']

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkImage
        fields = ['image']

class SocialMediaForm(forms.ModelForm):
    name = forms.ChoiceField(choices=SOCIAL_MEDIA_CHOICES, label='Name', required=True)
    class Meta:
        model = SocialMedia
        fields = ['name', 'url']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'fom-rcontrol', 'type': 'url'}),
        }