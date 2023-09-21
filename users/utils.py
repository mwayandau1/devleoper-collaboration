from .models import Skills, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfile(request):
    search_query = ''
    

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skills.objects.distinct().filter(name__icontains=search_query)
    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) |
        Q(username__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(bio__icontains=search_query)|
        Q(skills__in=skills)
    )
    return profiles, search_query


def paginateProfiles(request, profiles, results):
    page=request.GET.get('page')
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    leftIndex = (int(page)-1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages +1
    custom_pag = range(leftIndex, rightIndex)
    
    return profiles, custom_pag
