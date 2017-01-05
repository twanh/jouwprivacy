from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from .models import Article

# Shows a (list) index vieuw from all the articles
def article_index(request):
    aricles = Article.objects.all()
    args = {}
    args.update(csrf(request))
    args['articles'] = aricles
    return render(request, 'info/articles/index.html', context=args)

def article_search(request):
    # Checks if the request method = POST so we can receive the data possted by ajax
    if  request.method == 'POST':
        # Checks if the posted data contains a search query
        if request.POST['query']:
            search_query = request.POST['query']
        else:
            search_query = ''
        if request.POST.getlist('category'):
            category = request.POST.getlist('category')
        else:
            category = []
    else:
        search_query = ''
        category = []

    if ',' in search_query:
        articles = Article.objects.all()
        matching = []
        qtags = search_query.replace(' ', '').split(',')
        for article in articles:
            a_tags = article.return_tags().replace(' ', '')
            for qtag in qtags:
                if qtag in a_tags:
                    matching.append(article)

        articles = matching
    else:
        articles = Article.objects.filter(title__icontains=search_query)

    if category != []:
        if category[0] != 'all':
            articles = articles.filter(category=category[0])
    return render(request, 'info/articles/ajax_search.html', {'articles': articles})


# Show a detail view of the wanted article
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'info/articles/details.html', context={'article': article})

