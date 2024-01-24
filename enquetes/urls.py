from django.urls import path
from . import views

# mapeamento das url's da aplicação enquetes
# name é utilizado nas renderizações:
# { url enquetes:index [params] }

app_name="enquetes" # namespace enquetes
urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("visualizarEnquete/<int:pergunta_id>/", views.visualizarEnquete, name="visualizarEnquete"),
    path("criarEnquete/", views.criarEnquete, name="criarEnquete"),
    path("criarEnquetePost/", views.criarEnquetePost, name="criarEnquetePost" ),
    path("deletarEnquete/<int:pergunta_id>", views.deletarEnquete, name="deletarEnquete" ),
    path("editarEnquetePatch/<int:pergunta_id>", views.editarEnquetePatch, name="editarEnquetePatch")
]

