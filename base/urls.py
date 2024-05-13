

# accounts/urls.py
from django.urls import path
from .views import SignUpView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from base.views import ActivateAccount
from django.views.generic import TemplateView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("findpeople/", views.findpeople, name="findpeople"),
    path("myroom/", views.myroom, name="myroom"),
    path("logout/", views.user_logout, name="user_logout"),
    path(
        "about",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "activate/<uidb64>/<token>/",
        ActivateAccount.as_view(),
        name="activate",
    ),
    path("", views.home, name="home"),
]

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
