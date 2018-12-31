from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from accounts.models import AppUser, Specialty, Review


class AppAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        return request.user.active

    # def get_identifier(self, request):
    #     return request.user.full_name


class UserResource(ModelResource):
    class Meta:
        queryset = AppUser.objects.all()
        resource_name = 'users'
        fields = ['first_name', 'last_name', 'email', 'latitude', 'longitude']
        authorization = Authorization()
        authentication = AppAuthentication()


class SpecialtyResource(ModelResource):
    class Meta:
        queryset = Specialty.objects.all()
        resource_name = 'specs'
        authorization = Authorization()
        authentication = AppAuthentication()


class ReviewResource(ModelResource):
    class Meta:
        queryset = Review.objects.all()
        resource_name = 'r'
        authorization = Authorization()
        authentication = AppAuthentication()