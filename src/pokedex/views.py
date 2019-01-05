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
        'type': 'type.raw',
    }
 
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'title.raw',
        'type': 'author_id',
    }

    # Specify default ordering
    ordering = ('id', 'created',) 

