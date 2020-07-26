from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
import json
from .serializers import UserSerializer
# from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

User = get_user_model()



class UserName(APIView):
    # permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return JsonResponse({
            'data' : serializer.data
        }, status=201)


class RegisterApi(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        return JsonResponse({
            "nd" : 'asdf'
        })

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        user = User.objects.create_user(
            username=data["username"],
            password=data["password"]
        )
        serializer = UserSerializer(user)
        return JsonResponse({
            "status": "Created",
            # "token": user.auth_token.key,
            "data": serializer.data
        }, status=201)



# def register_view(request):
#     if request.method == 'GET':
#         context = {}
#         context['form'] = RegisterForm()
#         return render(request,'index.html',context)
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(request.POST.get('password'))
#             user.save()
#             return JsonResponse({
#                 'status' : "OK"
#             })
#
# def login_view(request):
#     if request.method == "GET":
#         form = LoginForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'login.html', context)
#
#     if request.method == 'POST':
#
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("logged in")
#
#
#
# def logout_view(request):
#     logout(request)
#     return HttpResponse('logout-view')
#
