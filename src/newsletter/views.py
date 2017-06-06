from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, SignUpModelForm
from django.core.mail import send_mail
# Create your views here.

def home(request):
	title = "Sign Up Now"
	form = SignUpModelForm(request.POST or None)
	# if request.user.is_authenticated():
	# 	title = "User Name %s" %(request.user)
	# if request.method == "POST":
	# 	print request.POST
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "jayant"
		instance.save()
		title = "Thanks"

	context = {
	'title':title,
	'form':form
	}
	return render(request, "home.html", context)

def contact(request):
	"""
	"""
	form = ContactForm(request.POST or None)
	context = {'form':form,
	}
	if form.is_valid():
		# send_mail('Subject here', 'Here is the message.', 'from@example.com',
  #   	['to@example.com'], fail_silently=False)

		# for k, v in form.cleaned_data.iteritems():
		# 	print k,v 
		email = form.cleaned_data.get('email')
		full_name = form.cleaned_data.get('full_name')
		message = form.cleaned_data.get('message')

		subject = 'Contact Form information'
		message = """
		%s:%s via %s
		""" %(full_name, message, email)
		from_mail = settings.EMAIL_HOST_USER
		to_email = [from_mail, 'hijayant15@gmail.com']
		send_mail(subject, 
					message, 
					from_mail,
					to_email, 
					fail_silently=False)

	return render(request, 'contact.html', context)


def about(request):
	context = {}
	return render(request, "about.html", context)