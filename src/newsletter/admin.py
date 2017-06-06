from django.contrib import admin
from .models import SignUp
from .forms import SignUpModelForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "created", "updated"]
	form = SignUpModelForm

admin.site.register(SignUp, SignUpAdmin)
