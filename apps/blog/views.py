from django.views.generic import DetailView, ListView, TemplateView
from django.contrib import messages
from django.views.generic.edit import FormView

from apps.blog.models import Article
from apps.blog.forms import ContactForm

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/post.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = 2
    ordering = "-published_date"
    queryset = Article.objects.filter(is_published=True)


class AboutView(TemplateView):
    template_name = "blog/about.html"


class ContactView(FormView):
    template_name = "blog/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form:ContactForm):
        try:
            form.send_email()
            messages.success(self.request, "Your message was sent successfully")
        except Exception:
            messages.error(self.request, "Unable to send your message")
        return super().form_valid(form)
