from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout

from .models import Weapon, Artifact, Character, Element


class MainView(View):

    def get(self, request):
        weapons = Weapon.objects.all()
        artifacts = Artifact.objects.all()
        characters = Character.objects.all()
        elements = Element.objects.all()

        context = {
            "weapons": weapons, "artifacts": artifacts, "characters": characters, "elements": elements
        }

        return render(request, 'constructor/constructor.html', context)


class BuildView(View):

    def get(self, request):

        weapons = Weapon.objects.all()
        artifacts = Artifact.objects.all()
        character = Character.objects.all()

        context = {
            "weapons": weapons, "artifacts": artifacts, "character": character
        }

        return render(request, 'constructor/home.html', context)


class ProfileView(View):

    def get(self, request):

        weapons = Weapon.objects.all()
        artifacts = Artifact.objects.all()
        character = Character.objects.all()

        context = {
            "weapons": weapons, "artifacts": artifacts, "character": character
        }

        return render(request, 'constructor/home.html', context)


class LoginView(View):

    def get(self, request):

        weapons = Weapon.objects.all()

        context = {
            "weapons": weapons
        }

        return render(request, 'constructor/home.html', context)

    # def post(self, request):
    #     form = LoginForm(request.POST or None)
    #
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             login(request, user)
    #             return HttpResponseRedirect('/')
    #     context = {'form': form}
    #
    #     return render(request, 'constructor/home.html', context)


class LogoutView(View):

    def get(self, request):
        auth_logout(request)
        return redirect('/')
