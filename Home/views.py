from django.shortcuts import render
from .models import home_page
from .models import about_me
from .models import my_resume
# Create your views here.
def home(request):
    home_page_data = home_page.objects.all()
    about_me_data = about_me.objects.all()
    my_resume_data = my_resume.objects.all()
    return render(request, 'Home/home.html', {'home_page_data': home_page_data,'about_me_data':about_me_data, 'my_resume_data': my_resume_data })