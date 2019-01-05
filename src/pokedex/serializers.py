from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from pokedex import documents as pokemon_documents
 
 
class PokemonDocumentSerializer(DocumentSerializer):
    class Meta:
        document = pokemon_documents.PokemonDocument
        fields = (
            'name',
            'type',
        ) 