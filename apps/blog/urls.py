from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = "blog"
urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("article/<pk>/", ArticleDetailView.as_view(), name="article"),
]