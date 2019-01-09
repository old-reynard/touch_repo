from django.urls import re_path, include
import api.resources as res

user_resources = res.UserResource()
specialty_resources = res.SpecialtyResource()
review_resource = res.ReviewResource()
create_user_resource = res.CreateUserResource()
uniqueUsernameResource = res.UniqueUsernameResource()
uniqueEmailResource = res.UniqueEmailResource()

urlpatterns = [
    re_path(r'^app_user/', include(user_resources.urls)),
    re_path(r'^specialty/', include(specialty_resources.urls)),
    re_path(r'^reviews/', include(review_resource.urls)),
    re_path(r'^create_user/', include(create_user_resource.urls)),
    re_path(r'^username/', include(uniqueUsernameResource.urls)),
    re_path(r'^email/', include(uniqueEmailResource.urls)),
]