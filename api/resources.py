from django.db import IntegrityError
from django.db.models import signals
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.models import create_api_key
from tastypie.resources import ModelResource
from accounts.models import AppUser, Specialty, Review
from .exceptions import ApiBadRequest

# This creates API keys for every users, keys are used to access the API
signals.post_save.connect(create_api_key, sender=AppUser)


class AppAuthorization(Authorization):  # custom auth to only show data relevant to the user
    def read_list(self, object_list, bundle):
        return object_list.filter(api_key=bundle.request.user.api_key)


class UserResource(ModelResource):
    """
    API resource that provides user data according to API keys
    """
    class Meta:
        queryset = AppUser.objects.all()
        resource_name = 'users'
        fields = ['first_name', 'last_name', 'email', 'latitude', 'longitude']
        allowed_methods = ['get', 'put']
        authorization = AppAuthorization()
        authentication = ApiKeyAuthentication()


class CreateUserResource(ModelResource):
    class Meta:
        queryset = AppUser.objects.all()
        resource_name = 'create'
        object_class = AppUser
        allowed_methods = ['post']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        include_resource_uri = False

    def hydrate(self, bundle):
        required_fields = ('first_name', 'last_name', 'username', 'email')
        for field in required_fields:
            if field not in bundle.data:
                raise ApiBadRequest(
                    code='missing_key',
                    message='Must provide {missing_key} when creating a user'.format(missing_key=field)
                )
        return bundle

    def obj_create(self, bundle, **kwargs):
        username = bundle.data['username']
        password = bundle.data['password']
        first_name = bundle.data['first_name']
        last_name = bundle.data['last_name']
        email = bundle.data['email']
        try:
            bundle.obj = AppUser.objects.create_user(email, username, first_name, last_name, password=password)
        except IntegrityError as e:
            error_message = str(e)
            if 'username' in error_message:
                message_key = 'username'
            elif 'email' in error_message:
                message_key = 'email'
            else:
                message_key = ''
            raise ApiBadRequest(
                code='Unique {message_key} fail'.format(message_key=message_key),
                message='It seems user with this {message_key} already exists'.format(message_key=message_key)
            )
        return bundle


class UniqueUsernameResource(ModelResource):
    """
    API resource that verifies that username is unique
    """
    class Meta:
        object_class = AppUser
        resource_name = 'unique'
        allowed_methods = ['post']
        fields = ['username']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        username = bundle.data['username']
        try:
            query = AppUser.objects.filter(username=username)
            if query.exists():
                bundle.obj = query.first()
        except AttributeError as e:
            raise ApiBadRequest(code='Server error', message=str(e))
        return bundle


class UniqueEmailResource(ModelResource):
    """
    API resource that verifies that username is unique
    """
    class Meta:
        object_class = AppUser
        resource_name = 'unique'
        allowed_methods = ['post']
        fields = ['email']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        email = bundle.data['email']
        try:
            query = AppUser.objects.filter(email=email)
            if query.exists():
                bundle.obj = query.first()
        except AttributeError as e:
            raise ApiBadRequest(code='Server error', message=str(e))
        return bundle


class SpecialtyResource(ModelResource):
    class Meta:
        queryset = Specialty.objects.all()
        resource_name = 'specs'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()


class ReviewResource(ModelResource):
    class Meta:
        queryset = Review.objects.all()
        resource_name = 'r'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
