from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Job, ContactQuery
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    query = request.GET.get('q', '').strip()
    if query:
        it_jobs = Job.objects.filter(category='IT', title__icontains=query).order_by('-date_posted')[:10]
        govt_jobs = Job.objects.filter(category='GOVT', title__icontains=query).order_by('-date_posted')[:10]
        internships = Job.objects.filter(category='INTERN', title__icontains=query).order_by('-date_posted')[:10]
        latest_posts = Job.objects.filter(title__icontains=query).order_by('-date_posted')[:5]
    else:
        it_jobs = Job.objects.filter(category='IT').order_by('-date_posted')[:20]
        govt_jobs = Job.objects.filter(category='GOVT').order_by('-date_posted')[:20]
        internships = Job.objects.filter(category='INTERN').order_by('-date_posted')[:20]
        latest_posts = Job.objects.order_by('-date_posted')[:5]
    popular_jobs = Job.objects.filter(is_popular=True).order_by('-date_posted')[:5]
    year = datetime.now().year

    context = {
        'it_jobs': it_jobs,
        'govt_jobs': govt_jobs,
        'internships': internships,
        'popular_jobs': popular_jobs,
        'latest_posts': latest_posts,
        'year': year,
    }
    return render(request, 'jobs/home.html', context)

def about(request):
    year = datetime.now().year
    return render(request, 'jobs/about.html', {'year': year})

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'contact-input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'contact-input'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'contact-textarea', 'rows': 4}))

def contact(request):
    year = datetime.now().year
    success = False
    error = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"New Contact Query from {form.cleaned_data['name']}"
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}"
            try:
                # Save to ContactQuery model
                ContactQuery.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    message=form.cleaned_data['message']
                )
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
                success = True
                form = ContactForm()  # Reset the form after successful submission
            except Exception as e:
                error = "There was an error sending your message. Please try again later."
    else:
        form = ContactForm()
    return render(request, 'jobs/contact.html', {'year': year, 'form': form, 'success': success, 'error': error})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})

def privacy(request):
    year = datetime.now().year
    return render(request, 'jobs/privacy.html', {'year': year})

def job_search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(title__icontains=query)
    if category:
        jobs = jobs.filter(category=category)
    paginator = Paginator(jobs.order_by('-date_posted'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    year = datetime.now().year
    return render(request, 'jobs/search_results.html', {'query': query, 'page_obj': page_obj, 'year': year, 'category': category})
