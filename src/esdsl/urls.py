from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pokemon/', include('pokedex.urls')),
    url(r'^', include('pokedex.urls')),
]
