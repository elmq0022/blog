from django.urls import path

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article"),
]