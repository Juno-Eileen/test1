from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import WeChatUser,Status,User,Reply
# Create your views here.
def home(request):
        return render(request,"homepage.html")
def show_user(request):
        user = WeChatUser.objects.get(user = request.user)
            return render(request,'user.html',{"u":user})
