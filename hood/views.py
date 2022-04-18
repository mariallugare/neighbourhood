from django.shortcuts import render
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Business, Post, Profile, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm, NewNeighbourhoodForm, PostForm, NewBusinessForm
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
