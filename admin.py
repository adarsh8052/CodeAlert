from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import Job, ContactQuery

class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'category', 'location', 'job_type', 'experience',
            'date_posted',
            'key_responsibilities', 'required_qualification_and_skills', 'detailed_job_description',
            'application_link', 'seo_tags'
        ]
        widgets = {
            'key_responsibilities': CKEditorWidget(),
            'required_qualification_and_skills': CKEditorWidget(),
            'detailed_job_description': CKEditorWidget(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detailed_job_description'].required = False

    class Media:
        js = ('admin/js/job_category_fields.js',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobAdminForm
    list_display = ('title', 'category', 'location', 'job_type', 'experience', 'date_posted', 'application_link')
    search_fields = ('title', 'location', 'job_type', 'experience', 'seo_tags')
    list_filter = ('category',)
    fieldsets = (
        (None, {'fields': (
            'title', 'category', 'location', 'job_type', 'experience', 'date_posted',
            'application_link', 'seo_tags'
        )}),
        ('Detailed Job Description', {'fields': (
            'key_responsibilities', 'required_qualification_and_skills', 'detailed_job_description',
        )}),
    )

admin.site.register(ContactQuery)

admin.site.site_header = 'CodeAlert Admin'
admin.site.site_title = 'CodeAlert Admin Portal'
admin.site.index_title = 'Welcome to CodeAlert Admin'
