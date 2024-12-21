from django.views.generic import DetailView, ListView

from apps.blog.models import Article

class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 20