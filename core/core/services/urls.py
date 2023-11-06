from django.urls import include, path



# Define the URL patterns for your application.

urlpatterns = [
    # Include authentication and registration routes from dj_rest_auth
    path("api/authentication/", include("dj_rest_auth.urls")),
    path("api/authentication/registration/", include("dj_rest_auth.registration.urls")),

]
