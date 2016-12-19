#!/usr/bin/python
# -*- coding:Utf-8 -*-

import hashlib
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.views import generic

from .models import Utilisateur, Famille, Arbre, Fait_historique, UtilisateurForm

global fam

def InscriptionForm(request):
	if request.method == 'POST':
		#On s'occupe du formulaire d'inscription
		FormInscription = UtilisateurForm(request.POST)
		if FormInscription.is_valid():
			
			mdp_session = FormInscription.cleaned_data['mdp']
			email_session = FormInscription.cleaned_data['email']
			nom_session = FormInscription.cleaned_data['nom']
			prenom_session = FormInscription.cleaned_data['prenom']

			"""FormInscription = UtilisateurForm(
				nom = FormInscription.cleaned_data['nom'],
				prenom = FormInscription.cleaned_data['prenom'],
				genre = FormInscription.cleaned_data['genre'],
				ddn = FormInscription.cleaned_data['ddn'],
				email = FormInscription.cleaned_data['email'],
				mdp = hashlib.sha1(mdp_session).hexdigest())"""

			FormInscription.save()

			user = User.objects.create_user(email_session, email=email_session, password=mdp_session)
			user.firstname = prenom_session
			user.lastname = nom_session
			user.save()

			#Connexion automatique lors de l'inscription
			util = authenticate(username=email_session, password=mdp_session)
			login(request, util)

			#Vérifier si une famille existe lors de la création de l'utilisateur
			try:
				fam = Famille.objects.get(nom = nom_session)
			except ObjectDoesNotExist:
				return redirect('Form_famille') #creation famille
			
			#Demande à l'utilisateur si il veut être dans une famille existante ou si il veut en créer une
			#form.moderateur = 0
			#On rajoute l'id de la famille à l'utilisateur
			#form.famille_id = fam.id
			#form.save()
			#rajouter autorisation de rentrer dans la famille
			
		return redirect('Rejoindre_famille')
	else: 
		FormInscription = UtilisateurForm()
	return render(request, 'InscriptionForm.html', {'FormInscription':FormInscription})

#Connexion d'un utilisateur
def accueilForm(request):
	if request.method == 'POST':
		FormConnection = UtilisateurForm(request.POST)
		if FormConnection.is_valid():
			mail = FormConnection.cleaned_data['email']
			mdp = FormConnection.cleaned_data['mdp']
			user = authenticate(username = mail, password = mdp)
			if user is not None:
				login(request, user)
				return redirect('Menu')
			else:
				#mot = 'hello'
				return render_to_response('Menu.html', {'FormConnection':FormConnection})
	else: 

		FormConnection = UtilisateurForm()
	return render(request, 'accueilForm.html', {'FormConnection':FormConnection})


@login_required
def modificationForm(request):
	if request.method == 'POST':
		FormModif = UtilisateurForm(request.POST)
		if FormModif.is_valid():
			"""nom = FormModif.cleaned_data['nom']
			prenom = FormModif.cleaned_data['prenom']
			prenoms_autre = FormModif.cleaned_data['prenoms_autre']
			genre = FormModif.cleaned_data['genre']
			ddn = FormModif.cleaned_data['ddn']
			email = FormModif.cleaned_data['email']
			postal = FormModif.cleaned_data['postal']
			profession = FormModif.cleaned_data['profession']
			description = FormModif.cleaned_data['description']
			mdp = FormModif.cleaned_data['mdp']"""

			FormModif.save()

			print(FormModif.errors)
			return render_to_response('Menu.html', {'FormModif':FormModif})
	else: 
		FormModif = UtilisateurForm()
	return render(request, 'modificationForm.html', {'FormModif':FormModif})


def Felicitations(request):
	return render(request, 'Felicitations.html')

def Menubis(request):
	return render(request, 'Menubis.html')

@login_required
def Menu(request):
	return render(request, 'Menu.html')

@login_required
def Form_famille(request):
	if request.method == 'POST':
		ajoutFamille = Famille(request.POST)
		if ajoutFamille.is_valid():
			form = Famille(
				nom = ajoutFamille.cleaned_data['nom'],
				nb_personnes = 1)
			form.save()
			return redirect('Menu')
	else :
		ajoutFamille = Famille()
	return render(request, 'Form_famille.html', {'ajoutFamille':ajoutFamille})

@login_required
def Rejoindre_famille(request):
	nom_session = (request.user).last_name
	#famille = Famille.objects.get(nom = nom_session)
	#famille = serializers.serialize("json", Famille.objects.all(), fields=('nom'))
	famille = Famille.objects.all()
	return render(request, 'Rejoindre_famille.html', {'famille':famille})

@login_required
def Form_famille_ajoutmembre(request):
	return render(request, 'Form_famille_ajoutmembre.html')

def Form_event(request):
	return render(request, 'Form_event.html')

def Confirm_ajoutevent(request):
	return render(request, 'Confirm_ajoutevent.html')


#fonction de déconnexion
def logout_view(request):
	logout(request)
	return redirect('accueilForm')