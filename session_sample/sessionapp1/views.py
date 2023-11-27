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

        # title=(request.POST.get('title'))
        # year=request.POST.get('year')
        # desc=request.POST.get('description')
        # movie_obj=movies(title=title,year=year,description=desc)
        # movie_obj.save()


    return render(request,'create.html',{'frm':frm})
# def list(request):

#     # movie_set=movies.objects.all()
#     movie_set=movies.objects.filter(year=1990)
#     print(movie_set)
#     return render(request,'list.html',{'movies':movie_set})


# how cookies work
# def list(request):
#     print(request.COOKIES)
#     visits=int(request.COOKIES.get('visits',0))
#     visits=visits+1
#     # movie_set=movies.objects.all()
#     movie_set=movies.objects.filter(year=1990)
#     print(movie_set)
#     response=render(request,'list.html',{'movies':movie_set,'visits':visits})
#     response.set_cookie('visits',visits)
#     return response


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



# def edit(request,pk):
#     instance_to_be_edited = movies.objects.get(pk=pk)
#     if request.POST:
#         frm=MovieForm(request.POST,instance=instance_to_be_edited)
#         if frm.is_valid():
#             instance_to_be_edited.save()
#     else:
#         frm=MovieForm(instance=instance_to_be_edited)
#     return render(request,'create.html',{'frm':frm})



# using session

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

        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # description=request.POST.get('description')
        # instance_to_be_edited.title=title
        # instance_to_be_edited.year=year
        # instance_to_be_edited.description=description
        # instance_to_be_edited.save()



    
    
    # return render(request,'edit.html')



def delete(request,pk):
    instance=movies.objects.get(pk=pk)
    instance.delete()
    movie_set=movies.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})


