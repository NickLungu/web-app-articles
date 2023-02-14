from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


def add_article(request):
    error_message = ''
    if request.method == 'POST':
        form_ = ArticleForm(request.POST)
        if form_.is_valid():
            form_.save()
            return redirect('home')
        else:
            error_message = "Data is not valid"

    form_ = ArticleForm()
    data_ = {
        'form': form_,
        'error': error_message
    }
    return render(request, "news/add_article.html", data_)


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/update_article.html'
    form_class = ArticleForm


class NewsListView(ListView):
    model = Article
    template_name = "news/news_home.html"
    context_name = 'news'


class NewsDeleteView(DeleteView):
    model = Article
    success_url = "/news/"
    template_name = "news/delete_article.html"
