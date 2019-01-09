from elasticsearch_dsl import analyzer

from django_elasticsearch_dsl import DocType, Index, fields 

from pokedex import models as pokemon_models

pokemon_index = Index('pokemon')
pokemon_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@pokemon_index.doc_type
class PokemonDocument(DocType):

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )

    type1 = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    type2 = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    total_stats = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    generation = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    is_legendary = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    created = fields.DateField()

    class Meta:
        model = pokemon_models.Pokemon