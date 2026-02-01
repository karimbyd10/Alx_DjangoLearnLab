from django.http import HttpResponse

def secure_view(request):
    response = HttpResponse("Secure Content")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('articles.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


@permission_required('articles.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content)
        return redirect('article_list')

    return render(request, 'articles/article_form.html')


@permission_required('articles.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('article_list')

    return render(request, 'articles/article_form.html', {'article': article})


@permission_required('articles.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.delete()
        return redirect('article_list')

    return render(request, 'articles/article_confirm_delete.html', {'article': article})
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # REQUIRED variable name
    return render(request, 'bookshelf/book_list.html', {'books': books})

