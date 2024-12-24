from django.urls import path

from apps.blog.views import ArticleListView, ArticleDetailView, AboutView, ContactView

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("articles/<pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
