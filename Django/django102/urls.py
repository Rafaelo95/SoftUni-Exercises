from django.urls import path

from django102.views import index as index_view, GamesListView, something

urlpatterns = [
    path('', index_view),
    path('games/', GamesListView.as_view()),
    path('smth/', something)
]