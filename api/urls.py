from django.urls import re_path, include
from api.resources import UserResource, SpecialtyResource, ReviewResource, CreateUserResource, UniqueUsernameResource

user_resources = UserResource()
specialty_resources = SpecialtyResource()
review_resource = ReviewResource()
create_user_resource = CreateUserResource()
uniqueUsernameResource = UniqueUsernameResource()

urlpatterns = [
    re_path(r'^app_user/', include(user_resources.urls)),
    re_path(r'^specialty/', include(specialty_resources.urls)),
    re_path(r'^reviews/', include(review_resource.urls)),
    re_path(r'^create_user/', include(create_user_resource.urls)),
    re_path(r'^username/', include(uniqueUsernameResource.urls))
]