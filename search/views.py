
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from .models import Company, Song, UserProfile
from django.db.models import Q
from django.core import serializers


# Create your views here.


def index(request):
    companies_list = Company.objects.order_by('name')[:]
    template = loader.get_template('search/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def favorites(request):
    template = loader.get_template('search/favorites.html')
    user_profile = UserProfile.objects.filter(user=request.user)[0]
    favorites_list = user_profile.favorites.order_by('title')
    context = RequestContext(request, {
            'songs_list': favorites_list[:],
        })
    return HttpResponse(template.render(context))


def search(request):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        if search_text is not None:
            if search_text != "":
                songs_list = Song.objects.filter(Q(title__icontains=search_text) |
                                                 Q(artist__icontains=search_text),
                                                 approved=True).order_by('title')
            else:
                songs_list = []
            if request.user.is_authenticated() and not request.user.is_superuser:
                user_profile = UserProfile.objects.filter(user=request.user)[0]
                favorites_list = user_profile.favorites.order_by('title')
            else:
                favorites_list = []
            template = loader.get_template('search/search.html')
            context = RequestContext(request, {
                'favorites_list': favorites_list[:],
                'songs_list': songs_list[:50],
            })
            '''
            return JsonResponse(serializers.serialize('json', songs_list[:50]), safe=False)
            return HttpResponse(template.render(context))
            '''
            return HttpResponse(template.render(context))


def like(request):
    if request.is_ajax():
        song_id = int(request.POST.get('song_id'))
        if song_id is not None:
            if request.user.is_authenticated():
                user_profile = UserProfile.objects.filter(user=request.user)[0]
                song_to_like = Song.objects.get(pk=song_id)
                if song_to_like in user_profile.favorites.all():
                    user_profile.favorites.remove(song_to_like)
                else:
                    user_profile.favorites.add(song_to_like)
                return HttpResponse('success')
