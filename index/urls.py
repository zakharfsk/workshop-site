from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from index import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/', views.auth_page, name='auth_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('jobs/', views.experience_job, name='experience_job'),
    path('jobs/<int:job_id>', views.detail_job, name='detail_job'),
    path('skills/', views.skills_page, name='skills'),
    path('skills/<int:skill_id>', views.skill_detail, name='skill_detail'),
    path('projects/', views.projects_page, name='projects')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
