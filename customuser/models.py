from django.contrib.auth.models import AbstractUser
from django.db import models
# managers.py

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, username=None, password=None, **extra_fields):
        if not email and not username:
            raise ValueError('At least one of email or username is required.')

        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


# class customUser(AbstractUser):
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    pic_image = models.ImageField(blank=True, null=True, upload_to='profile')
    phone_number = models.CharField(blank=True, null=True, max_length=20)
    partners = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='partner_of')

    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.username


class PartnerRequest(models.Model):
    sender = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='sent_partner_requests')
    receiver = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='received_partner_requests')
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(null=True,
                                      default=False)  # True if approved, False if disapproved, None if pending

    def set_approval(self, approval_status):
        self.is_approved = approval_status
        if approval_status:  # If the request is approved
            self.sender.partners.add(self.receiver)
            self.receiver.partners.add(self.sender)

    def save(self, *args, **kwargs):
        if self.is_approved is not None:  # If the approval status is set
            self.set_approval(self.is_approved)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
