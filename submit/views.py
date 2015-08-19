
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .forms import SubmitForm
from search.models import Song, Company

# Create your views here.


def index(request):
    # If this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            code = form.cleaned_data['code']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            company_name = form.cleaned_data['company']
            company = Company.objects.filter(name=company_name)[0]
            new_song = Song(code=code, title=title, artist=artist, company=company, approved=False)
            new_song.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/submit/thanks/')
    # If a GET (or any other method) we'll create a blank form
    else:
        form = SubmitForm()
    template = loader.get_template('submit/index.html')
    context = RequestContext(request, {
        'form': form,
    })
    return HttpResponse(template.render(context))


def thanks(request):
    template = loader.get_template('submit/thanks.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

