from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Application, Job

@login_required(login_url='loginPage')
def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})



@login_required
def addjobs(request):
    if request.method == 'POST':
        

        ndata = Application.objects.all().order_by('-id')  



        # Extract form data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        # Create a new Job instance and save it to the database
        new_job = Job(title=title, description=description, photo=photo, location=location, salary=salary)
        new_job.save()
        # Redirect to a success page or wherever you want
        return render(request, 'adminPages/add_job.html', {'application': ndata})
    
    else:
        ndata = Application.objects.all().order_by('-id')  
        return render(request, 'adminPages/add_job.html', {'application': ndata})


def success_page(request):
    return render(request, 'adminPages/successpage.html')