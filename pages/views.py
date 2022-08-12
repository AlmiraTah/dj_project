from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name="about_me.html"

class SchoolPageView(TemplateView):
    template_name="school.html"