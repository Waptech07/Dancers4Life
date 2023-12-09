from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("classes/", views.classes, name="classes"),
    path("events/", views.events, name="events"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.user_profile, name="profile"),
    path('events/<int:event_id>/purchase/', views.purchase_ticket, name='purchase_ticket'),
    path('success/', views.purchase_success, name='purchase_success')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)