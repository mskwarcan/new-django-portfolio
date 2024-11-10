from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from django.shortcuts import reverse
from django.core.validators import EmailValidator
from .models import Project, Tag
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    context = dict()
    context['projects'] = Project.objects.prefetch_related('image_set').prefetch_related('tag_set').order_by('?')
    context['tags'] = Tag.objects.all()
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')
    
def get_project(request, id):
    project = Project.objects.get(id=id)
    return JsonResponse(project.as_json(), safe=False)
    
class SuccessView(TemplateView):
    template_name = "success.html"

class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("success")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
