from django.urls import path

from .views import ArticleListView, ArticleDetailView, AboutView

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("articles/<pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("about/", AboutView.as_view(), name="about"),
]