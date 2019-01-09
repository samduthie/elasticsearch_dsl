from django.http import HttpResponse
from django.views import *

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
 
from pokedex import documents as pokemon_documents
from pokedex import serializers as pokemon_serializers

from pokedex.models import Pokemon


def random_pokemon_image(request):
	from pokedex.helpers import get_image

	from random import randint
	id = randint(0,799)

	pokemon = None
	while pokemon is None:
		try:
			pokemon = Pokemon.objects.get(pokedex_index=id)
		except:
			pass

	html = "<a href='pokemon/?search={}'>".format(pokemon.name) + get_image(pokemon.name.lower()) + "</a>"

	return HttpResponse(html)


class PokemonViewSet(DocumentViewSet):
    document = pokemon_documents.PokemonDocument
    serializer_class = pokemon_serializers.PokemonDocumentSerializer
 
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
 
    # Define search fields
    search_fields = (
        'name',
    )
 
    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'name': 'name.raw',
        'type1': 'type1.raw',
        'type2': 'type2.raw',

        'total_stats': 'total_stats.raw',
        'generation': 'generation.raw',
        'is_legendary': 'is_legendary.raw',

        'created': 'created',
        'modified': 'modified',
        'pub_date': 'pub_date',
    }
 
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'name.raw',
        'type': 'type.raw',
    }

    # Specify default ordering
    ordering = ('id', 'created',) 

