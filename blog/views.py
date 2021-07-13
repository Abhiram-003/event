from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests
from .models import Favourites
from django.template import loader

# Create your views here.

@login_required(login_url='blog-login')
def home(request):
    API_KEY = 'api_key=1cf50e6248dc270629e802686245c2c8'
    BASE_URL = 'https://api.themoviedb.org/3'
    API_URL = BASE_URL + '/discover/movie?sort_by=popularity.desc&'+API_KEY
    IMG_URL = 'https://image.tmdb.org/t/p/w500'
    searchURL = BASE_URL + '/search/movie?'+API_KEY
    
    var3= requests.get(API_URL).json()
    if request.method == 'POST':
        username = request.POST.get('searchstring')
        print(username)
        var3 = requests.get(searchURL+'&query='+username).json()
        temp = loader.get_template('blog/x.html')
        context = {
            'data':var3['results'][:8]
        }
        if request.is_ajax():
            print('hello')
            return HttpResponse(temp.render(context, request), content_type='application/xhtml+xml')
    return render(request, 'blog/home.html',{
        'data':var3['results'], 
    })

def fav(request, movie_id):
    API_KEY = 'api_key=1cf50e6248dc270629e802686245c2c8'
    BASE_URL = 'https://api.themoviedb.org/3/movie/'
    API_URL = BASE_URL + '/discover/movie?sort_by=popularity.desc&'+API_KEY
    IMG_URL = 'https://image.tmdb.org/t/p/w500'
    searchURL = BASE_URL + '/search/movie?'+API_KEY
    

    fav_mv= request.user.fav_movies.filter(mv_id=movie_id)
    if len(fav_mv)==0:
        var30 = requests.get(BASE_URL + f'{movie_id}?' + API_KEY + '&language=en-US').json()
        poster_URL=IMG_URL+ var30['poster_path']
        var31 = Favourites(
            user=request.user,
            mv_id=var30["id"],
            mv_name=var30["original_title"],
            mv_poster=poster_URL,
            mv_over=var30["overview"],
            mv_rating=var30["vote_average"]
            )
        var31.save()
    else:
        fav_mv[0].delete()
    
    return redirect('blog-home')
    
def favourite(request):
    var33=request.user.fav_movies.all()
    return render(request, 'blog/favourite.html', {
        'information':var33
    })

    