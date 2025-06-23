from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
def public_api(request):
    return Response({'message': '✅ This is a public API'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_api(request):
    return Response({'message': f'🔐 Hello {request.user.username}, this is a secure API'})





# 👉  Login View


from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from .forms import Loginform


def home(request):
    return HttpResponse("Successfully login")



def sign(request):
    form=Loginform()
    if request.method =="POST":
        form=Loginform(request.POST)

        if form.is_valid():
            uname=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"] 

            user=authenticate(username=uname , password=pwd)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                form.add_error(None,"invalid username")

    return render(request,"sign.html",{"form":form})










