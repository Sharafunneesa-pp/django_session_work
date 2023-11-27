from django.shortcuts import render
from . models import movies
from . forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            frm=MovieForm()    

       
       


    return render(request,'create.html',{'frm':frm})




# HOW SESSION WORKS

def list(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
   
    count=int(count)
    count=count+1
    # movie_set=movies.objects.all()
    request.session['count']=count
    recent_movie_set=movies.objects.filter(pk__in=recent_visits)
    movie_set=movies.objects.all()
    print(movie_set)
    response=render(request,'list.html',{
        'movies':movie_set,
        'recent_movies':recent_movie_set,
        'visits':count})
    return response






def edit(request,pk):
    
    instance_to_be_edited = movies.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        
        frm=MovieForm(instance=instance_to_be_edited)
    return render(request,'create.html',{'frm':frm})

       
       


def delete(request,pk):
    instance=movies.objects.get(pk=pk)
    instance.delete()
    movie_set=movies.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})


