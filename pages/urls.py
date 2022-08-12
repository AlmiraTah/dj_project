from django.urls import path
from .views import AboutPageView, SchoolPageView


urlpatterns=[
    path('', AboutPageView.as_view(), name="about_me"),
    path('school/', SchoolPageView.as_view(), name="school"),
]