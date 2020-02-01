from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q
from .models import Tutorial, TutorialSeries, TutorialCategory
from .forms import NewUserForm

# Create your views here.


def homepage(request):
    context = {}

    query = ''
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    context['categories'] = TutorialCategory.objects.all()

    return render(request, 'main/categories.html', context)


def about(request):
    return render(request, 'main/about.html', {})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'New Account Created: {username}')
            login(request, user)
            messages.info(request, f'You are now logged in as {username}')
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

    form = NewUserForm
    return render(request, 'main/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('main:homepage')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, 'main/login2.html', {'form': form})


def single_slug(request, single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(
            category__slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(
                series__series=m.series).earliest('published')
            series_urls[m] = part_one.slug
        return render(request, 'main/category.html', {'part_ones': series_urls})

    tutorials = [t.slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(
            series__series=this_tutorial.series).order_by('published')
        this_tutorial_index = list(tutorials_from_series).index(this_tutorial)
        context = {
            'tutorial': this_tutorial,
            'sidebar': tutorials_from_series,
            'this_tutorial_index': this_tutorial_index
        }
        return render(request, 'main/tutorial.html', context)

    # HttpResponse.status_code = 404
    return HttpResponse(f'{single_slug} does not correspond to anything.')
    # return bad_request(request)


def get_tutorial_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Tutorial.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))


# HTTP Error 404 (handles any bad request)
def error_404(request, exception):
    HttpResponse.status_code = 404
    return render(request, 'main/404.html', {})
