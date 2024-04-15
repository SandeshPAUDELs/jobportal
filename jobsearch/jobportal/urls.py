from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from jobportal import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('addjobs/',views.addjobs, name='addjobs'),
    # path('delete/<int:job_id>', views.delete_home_data, name='delete_home_data'),
    path('success/', views.success_page, name='success_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)