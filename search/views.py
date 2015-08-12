
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from .models import Company, Song
from django.db.models import Q

# Create your views here.


def index(request):
    companies_list = Company.objects.order_by('name')[:]
    template = loader.get_template('search/index.html')
    context = RequestContext(request, {
        'current_company': 'All',
        'companies_list': companies_list,
    })
    return HttpResponse(template.render(context))


def search(request):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        if search_text is not None:
            if search_text != "":
                songs_list = Song.objects.filter(Q(title__contains=search_text) | Q(artist__contains=search_text)).order_by('title')
            else:
                songs_list = []
            template = loader.get_template('search/search.html')
            context = RequestContext(request, {
                'songs_list': songs_list[:10],
            })
            return HttpResponse(template.render(context))

