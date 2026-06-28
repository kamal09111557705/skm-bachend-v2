from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('REGULAR', 'کاربر عادی'),
        ('BRONZE', 'برنزی'),
        ('SILVER', 'نقره‌ای'),
        ('GOLD', 'طلایی'),
        ('PARTNER', 'همکار'),
        ('TECHNICIAN', 'تکنسین'),
        ('ADMIN', 'مدیریت'),
    )
    mobile = models.CharField(max_length=11, unique=True)
    national_id = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='REGULAR')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['national_id', 'address']

    def __str__(self):
        return self.mobile

class OTPCode(models.Model):
    mobile = models.CharField(max_length=11)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    purpose = models.CharField(max_length=10, choices=[('LOGIN', 'ورود'), ('REGISTER', 'ثبت‌نام')])

    def __str__(self):
        return f"{self.mobile} - {self.code}"
