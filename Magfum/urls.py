from django.urls import path ,include
from . import views
from .views import ModifierProduit
from .views import SupprimerProduit

app_name = 'magfum'

urlpatterns = [
path('home/', views.home ,name='home'),
path('',views.index,name='ind'),
path('admin/',views.admin,name='admin'),
path('AjoutP/',views.AjoutProd,name='AjoutP'),
path('AjoutF/',views.AjoutFournisseur,name='AjoutF'),
path('AjoutC/',views.AjoutCommande,name='AjoutC'),
path('ListC/',views.mesCommande,name='ListC'),
path('ListF/',views.mesfour,name='ListF'),
path('publicité/',views.pub,name='pub'),
path('pp/',views.produits_par_categorie,name='pp'),
path('search/', views.search_produits, name='search'),
path('register/',views.register, name = 'register'),
path('logout/', views.logout_view, name='logout'),
path('login/', views.user_login, name='login'),
path('<int:pk>/modifier/',ModifierProduit.as_view(), name='modifier_produit'),  
path('<int:pk>/supprimer/',SupprimerProduit.as_view(), name='supprimer_produit'),
path('ProduitList/', views.mesP, name='mesP'),
path('<int:myid>', views.detail, name="detail"),
path('soumettre_rating/<int:product_id>/', views.soumettre_rating, name='soumettre_rating'),
 ]