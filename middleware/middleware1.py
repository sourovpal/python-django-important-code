# my_app/authentication.py
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').replace('Bearer', '').strip()
        print("+++++++++++++ ExampleAuthentication ++++++++++++")
        print(token)
        return (None, None)
        # username = request.META.get('X_USERNAME') # get the username request header
        # if not username: # no username passed in request headers
        #     return None # authentication did not succeed

        # try:
        #     user = User.objects.get(username=username) # get the user
        # except User.DoesNotExist:
        #     raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        # return (user, None) # authentication successful






from django.utils.timezone import now
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("_________________++++++++++++++++++________________")
        token = request.META.get('HTTP_AUTHORIZATION', '').replace('Bearer', '').strip()
        print(token)
        if token != "123456":
            return JsonResponse({"message" : "Please login"}, status=401)
        else:
            # print(request.headers)
            response = self.get_response(request)
            return response






from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from home.middlewares.LastRequestMiddleware import RequestMiddleware
@api_view(["POST"])
# @authentication_classes([JWTAuthentication])
def home(request):
    return Response({"message": "Hello, world!"})



INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'home',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'home.middlewares.authentication.ExampleAuthentication',
    ]
}



MIDDLEWARE = [
    'home.middlewares.LastRequestMiddleware.RequestMiddleware',
]










