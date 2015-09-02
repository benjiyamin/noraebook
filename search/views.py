
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .models import Song, UserProfile
from django.db.models import Q


# Create your views here.


def favorites(request):
    if request.user.is_authenticated():
        template = loader.get_template('search/favorites.html')
        user_profile = UserProfile.objects.filter(user=request.user)[0]
        favorites_list = user_profile.favorites.order_by('title')
        context = RequestContext(request, {
            'songs_list': favorites_list[:],
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')


def search(request):
    max_results = 20
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        search_list = search_text.split()
        sort_text = request.GET.get('sort_text').lower()
        results_length = int(request.GET.get('results_length'))
        if sort_text == "rank":
            sort_text = "-likes"
        if search_text != "":
            songs_list = Song.objects.filter(Q(title__icontains=search_list[0]) |
                                             Q(artist__icontains=search_list[0]),
                                             approved=True).order_by(sort_text)
            if len(search_list) > 1:
                for i in range(1, len(search_list)):
                    songs_list = songs_list.filter(Q(title__icontains=search_list[i]) |
                                                   Q(artist__icontains=search_list[i]))
        else:
            songs_list = Song.objects.order_by(sort_text)
        if songs_list.count() > max_results:
            scrollable = True
        else:
            scrollable = False
        songs_list = songs_list[results_length:results_length + max_results]
        template = loader.get_template('search/search.html')
    else:
        songs_list = Song.objects.order_by('-likes')
        if songs_list.count() > max_results:
            scrollable = True
        else:
            scrollable = False
        songs_list = songs_list[:max_results]
        template = loader.get_template('search/index.html')

    if request.user.is_authenticated() and not request.user.is_superuser:
        user_profile = UserProfile.objects.filter(user=request.user)[0]
        favorites_list = user_profile.favorites.all()
    else:
        favorites_list = []

    context = RequestContext(request, {
        'favorites_list': favorites_list[:],
        'songs_list': songs_list,
        'scrollable': scrollable
    })
    return HttpResponse(template.render(context))


def like(request):
    if request.is_ajax():
        song_id = int(request.POST.get('song_id'))
        if song_id is not None:
            if request.user.is_authenticated():
                user_profile = UserProfile.objects.filter(user=request.user)[0]
                song_to_like = Song.objects.get(pk=song_id)
                if song_to_like in user_profile.favorites.all():
                    # Unlike
                    user_profile.favorites.remove(song_to_like)
                    song_to_like.likes -= 1
                    song_to_like.save()
                else:
                    # Like
                    user_profile.favorites.add(song_to_like)
                    song_to_like.likes += 1
                    song_to_like.save()
                return HttpResponse('success')
