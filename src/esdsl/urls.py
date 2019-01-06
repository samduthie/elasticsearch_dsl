from django.conf.urls import include, url
from django.contrib import admin

from pokedex import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pokemon/', include('pokedex.urls')),
    url(r'^', views.random_pokemon_image),
]
