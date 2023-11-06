from django.shortcuts import get_object_or_404  # pylint: disable=W0611 # noqa
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def home(request):
    """
    A view that provides links to relevant API routes on the home page.
    """
    routes = [
        "/services/api/authentication/registration/",
        "/services/api/authentication/",
    ]
    return Response(routes)
