from django.db import models
from django.urls import reverse


# Create your models here.


class MyProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    github_repo_url = models.URLField(blank=True)
    time_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MyJobExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    time_start = models.DateField()
    time_end = models.DateField(blank=True, null=True)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_job', kwargs={'job_id': self.id})


class MySkills(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'skill_id': self.id})
