from django.core.mail import send_mail
from django.shortcuts import render
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, WorkImage, Testimonial, Partner, Faq, Privacy, SocialMedia


def index(request):
  contact = Contact.objects.all().last()
  banner = Banner.objects.all().last()
  about = About.objects.all().last()
  skills = Skill.objects.all().last()
  indicators = Counter.objects.all().last()
  servicios = Service.objects.all()
  works = WorkImage.objects.all().order_by('?')[:6]
  testimonials = Testimonial.objects.all()
  partners = Partner.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    'contact':contact,
    'banner':banner,
    'about':about,
    'skills':skills,
    'indicators':indicators,
    'servicios':servicios,
    'works':works,
    'testimonials':testimonials,
    'partners':partners,
    'social_media':social_media
    }
  
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/index.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/index.html', context)

def about(request):
  contact = Contact.objects.all().last()
  about = About.objects.all().last()
  skills = Skill.objects.all().last()
  servicios = Service.objects.all()
  social_media = SocialMedia.objects.all()
  context = {'contact':contact, 'servicios':servicios, 'about':about, 'skills':skills, 'social_media':social_media}
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/about.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/about.html', context)

def services(request):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  social_media = SocialMedia.objects.all()
  context = {'contact':contact, 'servicios':servicios, 'social_media':social_media}
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/services.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/services.html', context)

def services_view(request, pk):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  servicio = Service.objects.get(pk=pk)
  subservicios = SubService.objects.filter(service=pk)
  social_media = SocialMedia.objects.all()
  context = {'contact':contact, 'servicio':servicio, 'servicios':servicios, 'subservicios':subservicios, 'social_media':social_media}
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/service.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/service.html', context)

def works(request):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  gallery = WorkImage.objects.all().order_by('?')
  social_media = SocialMedia.objects.all()
  context = {
    'contact':contact,
    'servicios':servicios,
    'gallery':gallery,
    'social_media':social_media
  }
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/works.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/works.html', context)

def faq(request):
  contact = Contact.objects.all().last()
  faqs = Faq.objects.all()
  servicios = Service.objects.all()
  social_media = SocialMedia.objects.all()
  context = {'contact':contact, 'servicios':servicios, 'faqs':faqs, 'social_media':social_media}
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/faq.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/faq.html', context)

def contact(request):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  testimonials = Testimonial.objects.all()
  social_media = SocialMedia.objects.all()
  context = {'servicios':servicios, 'contact':contact, 'testimonials':testimonials, 'social_media':social_media}
  if request.method == 'POST':
    print(f"Veamos si entra en el metyhod post")
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/contact.html', context)
    elif 'contact_us_form' in request.POST:
      print(f"Veweamos si entyra aqui boton de contact us form")
      username = request.POST.get('userName')
      message = request.POST.get('userMessage')
      email = request.POST.get('userEmail')
      
      # y enviar el correo electrónico correspondiente
      send_msg_contact_us(username, message, email)
      print(f"En este momentro el mensaje yua se envio")
      return render(request, 'app_core/pages/contact.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/contact.html', context)

def privacy(request):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  privacy = Privacy.objects.all().last()
  social_media = SocialMedia.objects.all()
  context = {'contact':contact, 'servicios':servicios, 'privacy':privacy, 'social_media':social_media}
  if request.method == 'POST':
    if 'stay_connected' in request.POST:
      username = request.POST.get('userName')
      company = request.POST.get('companyName')
      email = request.POST.get('email')
      
      # y enviar el correo electrónico correspondiente
      send_msg_stay_connected(username, company, email)
      return render(request, 'app_core/pages/privacy.html', context)
  else:
    # Renderizar el template con ambos formularios
    return render(request, 'app_core/pages/privacy.html', context)

def send_msg_stay_connected(username, company, email):
  subject = 'Stay Connected M2J'
  message = f'Hello, M2J you have a new subscriber: \nUsername: {username} \nCompany: {company} \nEmail: {email}.'
  from_email = 'ideafix.mensajeria@gmail.com'
  recipient_list = ['libardoentrenandolatinos@gmail.com']
  send_mail(subject, message, from_email, recipient_list)

def send_msg_contact_us(username, get_message, email):
  subject = 'Contact Us M2J'
  message = f'Hello, M2J you have a new message: \nUsername: {username} \nMessage: {get_message} \nEmail: {email}.'
  from_email = 'ideafix.mensajeria@gmail.com'
  recipient_list = ['libardoentrenandolatinos@gmail.com']
  send_mail(subject, message, from_email, recipient_list)