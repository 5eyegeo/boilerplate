from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("Username"), max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.userprofile.first_name + " " + self.userprofile.last_name

    def get_short_name(self):
        return self.userprofile.first_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    dob = models.DateField(_("D.O.B"), auto_now=False, auto_now_add=False, blank=False, null=False)
    profile_image = models.ImageField(_("Profile picture"), upload_to='user/profile/', blank=True)
    webiste_link = models.URLField(_("Websites"), max_length=200, null=True, blank=True)
    facebook = models.URLField(_("Facebook Profile"), max_length=200, null=True, blank=True)
    twitter = models.URLField(_("Twitter Profile"), max_length=200, null=True, blank=True)
    instagram = models.URLField(_("Instagram Profile"), max_length=200, null=True, blank=True)
    linkedin = models.URLField(_("LinkedIn Profile"), max_length=200, null=True, blank=True)
    about = models.TextField(_("About"))

    class Meta:
        verbose_name = _("User profile")
        verbose_name_plural = _("User profiles")

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("userprofile_detail", kwargs={"pk": self.pk})
