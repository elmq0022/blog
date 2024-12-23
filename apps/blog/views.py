from django.views.generic import DetailView, ListView, TemplateView

from apps.blog.models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/post.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = 5


class AboutView(TemplateView):
    template_name = "blog/about.html"