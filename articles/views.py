from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ArticleCreateForm
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all()
    paginate_by = 3
    template_name = "articles/home.html"
    context_object_name = "articles"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
    login_url = reverse_lazy("author:login")


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = "articles/article_update.html"
    login_url = reverse_lazy("author:login")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/article_create.html"
    form_class = ArticleCreateForm
    login_url = reverse_lazy("author:login")
    success_url = reverse_lazy("articles:home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("articles:home")
    login_url = reverse_lazy("author:login")


class Search(View):
    template_name = "articles/search.html"

    def get(self, request, *args, **kwargs):
        context = {}
        search = request.GET["search"]
        articles = Article.objects.filter(title__icontains=search)
        context["articles"] = articles
        return render(request, self.template_name, context)


template_name = "articles/search.html"


def first(request, *args, **kwargs):
    context = {}
    search = "Notebooks"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def second(request, *args, **kwargs):
    context = {}
    search = "Smartphones"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def third(request, *args, **kwargs):
    context = {}
    search = "Cars"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def fourth(request, *args, **kwargs):
    context = {}
    search = "Cameras"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def fivth(request, *args, **kwargs):
    context = {}
    search = "Home appliances"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def sixth(request, *args, **kwargs):
    context = {}
    search = "Apartments"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)


def other(request, *args, **kwargs):
    context = {}
    search = "Other"
    articles = Article.objects.filter(description__icontains=search)
    context["articles"] = articles
    return render(request, template_name, context)
