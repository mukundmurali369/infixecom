from ast import Return
from email.message import Message
from multiprocessing import context
from operator import imod
from django.shortcuts import render,redirect
from .models import *
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'signin.html')
def cart(request):
    return render(request,'cart.html')
def shop(request):
    return render(request,'shop.html')
def checkout(request):
    return render(request,'checkout.html')
def login(request):
    return render(request,'signin.html')