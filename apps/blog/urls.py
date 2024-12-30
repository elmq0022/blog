from django.urls import path

from apps.blog.views import ArticleListView, ArticleDetailView, ContactView

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("articles/<pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
]
