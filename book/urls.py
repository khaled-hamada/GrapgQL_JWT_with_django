from django.urls import path

#like django rest grapg ql view will give us a browsable
# api 
from graphene_django.views import GraphQLView

from book.schema import schema

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
