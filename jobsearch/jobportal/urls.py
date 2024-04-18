from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from jobportal import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addjobs/',views.addjobs, name='addjobs'),  # admin can add the job
    path('delete/<int:job_id>', views.delete_jobs, name='delete_jobs'),  # admin can only delete the job so delte is  not shown to the user 
    path('savejobhome/<int:job_id>/',views.savehome_submit,name='savehome_submit'), # user can save the job
    path('applieddata/<int:job_id>', views.applydata_submit, name='applydata_submit'), # user can apply the job
    path('savejobs/', views.save_job, name='save_job'),  # this is same like add to cart user can save the jobs and can see the saved jobs
    path('savedelete/<int:savedjob_id>/',views.delete_saved_jobs,name='delete_saved_jobs'), # user can delete the saved jobs
    path("search/", views.search, name="search"),
    path('applyjobhome/<int:job_id>/',views.jobPortal_home_jobs,name='jobPortal_home_jobs'),  # user can apply the job from saved

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)