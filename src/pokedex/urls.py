from rest_framework.routers import SimpleRouter

from pokedex import views
 

app_name = 'articles' 

router = SimpleRouter()
router.register(
    prefix=r'',
    base_name='pokemon',
    viewset=views.PokemonViewSet
)
urlpatterns = router.urls