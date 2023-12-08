from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("classes/", views.classes, name="classes"),
    path("events/", views.events, name="events"),
    path("about/", views.about, name="about"),
    path("contact-us/", views.contact, name="contact")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)