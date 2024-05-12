from django.shortcuts import render
from django.template import loader
from .models import Produit
from .models import Commande
from .models import Fournisseur
from django.http import HttpResponse
from .forms import ProduitForm
from django.shortcuts import redirect,get_object_or_404
from .forms import CommandeForm
from .forms import FournisseurForm,UserRegistrationForm ,UserCreationForm,LoginForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



def home(request):
    template=loader.get_template('Magfum/mesParfum.html')
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'Magfum/mesParfum.html ',context )

def index(request):
    template=loader.get_template('Magfum/index.html')
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'Magfum/index.html ',context )

def admin(request):
    template=loader.get_template('Magfum/admin.html')
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'Magfum/admin.html ',context )

def AjoutProd(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Magfum')
    else :
        form = ProduitForm() #créer formulaire vide
        return render(request,'Magfum/ajoutProduit.html',{'form':form}) 
    
def AjoutFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Magfum')
    else:
        form = FournisseurForm() #créer formulaire vide
        list=Fournisseur.objects.all()
    return render(request,'Magfum/ajoutFournisseur.html',{'form':form })

def AjoutCommande(request):
    if request.method == "POST" : 
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Magfum')
    else:
        form = CommandeForm() #créer formulaire vide
        list=Commande.objects.all()
    return render(request,'Magfum/ajoutCommande.html',{'form':form })

def mesfour(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Magfum')
    else:
        list=Fournisseur.objects.all()
        return render(request,'Magfum/ListF.html',{'list':list})
    
def mesCommande(request):
    if request.method == "POST" : 
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Magfum')
    else:
        list=Commande.objects.all()
        return render(request,'Magfum/ListC.html',{'list':list})
    
def pub(request):
    template=loader.get_template('Magfum/pub.html')
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'Magfum/pub.html ',context )


def produits_par_categorie(request):
    if request.method == 'GET':
        lib = request.GET.get('marque')
        products = Produit.objects.filter(libellé=lib)
        context={'products':products}
    else:
        products = Produit.objects.all()
        context={'products':products}
    return render(request, 'Magfum/product.html',context)

def search_produits(request):
    query = request.GET.get('query')
    if query:
        results = Produit.objects.filter(description__icontains=query)
    else:
        results = Produit.objects.all()
    context = {'results': results} 
    return render(request, 'Magfum/search_results.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger vers une page après la connexion réussie
                return render(request, 'Magfum/index.html')  # Remplacez 'magasin:home' par l'URL de la page à rediriger
            else:
                # Si l'authentification échoue, afficher un message d'erreur
                error_message = "Nom d'utilisateur ou mot de passe incorrect."
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Rediriger vers une page de confirmation de déconnexion ou une autre page
    return render(request,'Magfum/index.html') 

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return render(request,'registration/register.html')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})
   

def mesP(request):
    template=loader.get_template('Magfum/adprod.html')
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'Magfum/adprod.html ',context )

class ModifierProduit(UpdateView):
    model = Produit
    template_name = 'Magfum/edit_prod.html'
    form_class = ProduitForm  
    success_url = reverse_lazy('magfum:mesP')


class SupprimerProduit(DeleteView):
    model = Produit
    template_name = 'Magfum/del_prod.html'
    success_url = reverse_lazy('magfum:mesP')

def detail(request, myid):
    product_object = Produit.objects.get(id=myid)
    return render(request, 'Magfum/detail.html', {'product': product_object}) 

def soumettre_rating(request, product_id):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        produit = get_object_or_404(Produit, pk=product_id)
        produit.rating = rating
        produit.save()
        return redirect('magfum:home') 