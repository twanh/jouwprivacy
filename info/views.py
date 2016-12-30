from django.shortcuts import render
from .models import Article

# Shows a (list) index vieuw from all the articles
def article_index(request):
    aricles = Article.objects.all()
    args = {}
    # args.update(csrf(request))
    args['articles'] = aricles
    return render(request, 'info/articles/index.html', context=args)

# Show a detail view of the wanted article
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'info/articles/details.html', context={'article': article})

