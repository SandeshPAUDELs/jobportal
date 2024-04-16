from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Application, Job, SaveJob


#       views for the jobportal app
@login_required(login_url='loginPage')
def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})


#     views for admin to add the job 

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
        return render(request, 'index.html', {'jobs': Job.objects.all()})
    
    else:
        ndata = Application.objects.all().order_by('-id')  
        return render(request, 'adminPages/add_job.html', {'application': ndata})


#     views for admin to delete the job  only admin can delete the job
@login_required
def delete_jobs(request, job_id):
    jobdata = Job.objects.get(id=job_id)
    jobdata.delete()
    return redirect('home')

#     views for user to apply the job where there will be forms to be filed

def jobPortal_home_jobs(request, job_id): 
    saveddata = Job.objects.filter(id=job_id)  # Assuming job_id is a field in the Job model

    context = {'data': saveddata}  

    return render(request, 'applyjob.html', context)


#     views for user to apply the job where there will be forms to be filed and the data will be saved in the database and reddirect to the home page

def applydata_submit(request, job_id):
    if request.method == 'POST':
        user = request.user
        job = Job.objects.get(id=job_id)

        # Check if the user has already applied for the job
        if Application.objects.filter(job=job, user=user).exists():
            return HttpResponseForbidden("You have already applied for this job.")
        else:

            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            experience = request.POST.get('experience')
            resume = request.FILES['resume']
            
            # Create and save the application
            application = Application.objects.create(
                job=job, user=user, fullname=fullname, email=email, phone=phone, 
                experience=experience, resume=resume
            )
            application.save()
            
            return render(request,'index.html')
    else:
        pass

#    since user can save tge job so when they want to see which jobs they have seen so far wordk like add to cart in ecommerrse

@login_required
def savehome_submit(request, job_id):
    if request.user.is_authenticated:
        user = request.user
        job = get_object_or_404(Job, id=job_id)
        
        if not SaveJob.objects.filter(user=user, job=job).exists():
            save_job = SaveJob(user = request.user,job=job)
            save_job.save() 
        return redirect('home') 
    else:
        return redirect('home')
    




#   views where the user saved jobs are displayed

@login_required
def save_job(request):
        if request.user.is_authenticated:
            saveddata = SaveJob.objects.filter(user=request.user).order_by('-id')
            return render(request, 'savedjobs.html', {'saveddata': saveddata})
        else:
            return redirect('login')
        
#  views where the user can delete the saved jobs  this is the part of the above page where the saved jobs are displayed
@login_required
def delete_saved_jobs(request, savedjob_id):   
    saved_job = get_object_or_404(SaveJob, id=savedjob_id)
    saved_job.delete()
    
    return redirect('save_job')