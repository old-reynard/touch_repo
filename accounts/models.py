from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from constants import TEXT_FIELD_SIZE, CHAR_FIELD_SIZE


class AppUserManager(BaseUserManager):
    def create_user(self, email, username,
                    first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must provide an email address')
        if not password:
            raise ValueError('Users must provide a password')
        if not first_name or not last_name:
            raise ValueError('Users must provide their first and last names')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staff_user(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_admin=True,
        )
        return user


class AppUser(AbstractBaseUser):
    email = models.EmailField(max_length=CHAR_FIELD_SIZE, unique=True)
    first_name = models.CharField(max_length=CHAR_FIELD_SIZE)
    last_name = models.CharField(max_length=CHAR_FIELD_SIZE)
    username = models.CharField(unique=True, max_length=CHAR_FIELD_SIZE)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # staff member
    admin = models.BooleanField(default=False)  # admin member
    created_at = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    latitude = models.DecimalField(blank=True, null=True, decimal_places=6, max_digits=9)
    longitude = models.DecimalField(blank=True, null=True, decimal_places=6, max_digits=9)
    position = models.CharField(max_length=CHAR_FIELD_SIZE, blank=True)  # place of employment
    bio = models.TextField(max_length=TEXT_FIELD_SIZE, blank=True, null=True)
    finder = models.BooleanField(default=True)  # is this user a finder or a giver

    def __str__(self):
        return '%s, %s' % (self.full_name, self.email)

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = AppUserManager()

    class Meta:
        ordering = ['last_name']


class Specialty(models.Model):
    spec_name = models.CharField(max_length=CHAR_FIELD_SIZE)
    spec_description = models.TextField(max_length=TEXT_FIELD_SIZE, blank=True)
    givers = models.ManyToManyField(AppUser)

    def __str__(self):
        return self.spec_name

    class Meta:
        verbose_name_plural = 'specialties'


class Review(models.Model):
    header = models.CharField(max_length=CHAR_FIELD_SIZE)
    content = models.TextField(max_length=TEXT_FIELD_SIZE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    from_whom = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=1, related_name='from_whom', editable=False)
    to_whom = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=2, related_name='to_whom', editable=False)

    def __str__(self):
        return self.header



