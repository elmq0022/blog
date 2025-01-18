from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.views.generic.edit import FormView

from apps.blog.models import Article
from apps.blog.forms import ContactForm

import logging
logger = logging.getLogger("django")

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/post.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = 2
    ordering = "-published_date"
    queryset = Article.objects.filter(is_published=True)



class ContactView(FormView):
    template_name = "blog/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form:ContactForm):
        try:
            logging.info("the form is valid, call form.mail()")
            form.mail()
            logging.info("successfully called form.mail()")
            messages.success(self.request, "Your message was sent successfully")
        except Exception:
            messages.error(self.request, "Unable to send your message")
        return super().form_valid(form)
