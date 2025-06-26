from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'IT Jobs'),
        ('GOVT', 'Govt Jobs'),
        ('INTERN', 'Internship'),
    ]
    title = models.CharField(max_length=255)
    date_posted = models.DateField()
    is_popular = models.BooleanField(default=False)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='IT')
    short_description = RichTextField(blank=True)
    detailed_job_description = RichTextField(blank=True)
    attachment = models.FileField(upload_to='job_attachments/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True)
    job_type = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    key_responsibilities = RichTextField(blank=True)
    required_qualification_and_skills = RichTextField(blank=True)
    application_link = models.URLField(blank=True)
    seo_tags = models.CharField(max_length=255, blank=True)
    # Add more fields as needed

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])

class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.date_submitted.strftime('%Y-%m-%d %H:%M')}"
