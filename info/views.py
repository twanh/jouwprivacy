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
        # Checks if the posted data contains a search query and saves it
        if request.POST['query']:
            search_query = request.POST['query']
        else:
            # If there is no post of query save an empty search query
            search_query = ''
        # Checks if there is a category list in POST and saves it
        if request.POST.getlist('category'):
            category = request.POST.getlist('category')
        else:
            # If there is not post of category save an empty list
            category = []
    else:
        # If there is no post save empty variables
        search_query = ''
        category = []

    # Checks if there is a , in the search query wich would indicate that the query is tag based
    if ',' in search_query:
        # Gets all the articles from the database and compares there tags to the queries tags
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
        # If the search query is not tag based the query is title based
        articles = Article.objects.filter(title__icontains=search_query)

    # Checks if there is a category and filters articles on category
    if category != []:
        if category[0] != 'all':
            articles = articles.filter(category=category[0])

    # Returns the ajax template with the needed articles
    return render(request, 'info/articles/ajax_search.html', {'articles': articles})


# Show a detail view of the wanted article
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'info/articles/details.html', context={'article': article})

