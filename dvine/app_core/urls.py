from django.urls import path
from app_core.views import general

app_name = 'app_core'
urlpatterns = [
    path('', general.index, name='index'),
    path('about/', general.about, name='about'),
    path('services/<int:pk>/', general.services_view, name='services_view'),
    path('works/', general.works, name='works'),
    path('faq/', general.faq, name='faq'),
    path('contact/', general.contact, name='contact'),
    path('privacy/', general.privacy, name='privacy'),
    path('mail/', general.mail_view, name='mail'),
]