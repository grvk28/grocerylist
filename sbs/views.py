from django.shortcuts import render,redirect,get_object_or_404
from .forms import m,m1
from .models import Items
#, ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
#from django.urls import reverse


# Create your views here.
@login_required
def index(request):
    user=request.user
    myitems=Items.objects.filter(user=user)
    context={
        'It': myitems
        #"Quantity":myitems.Quantity
        #'status': myitems.status
    }
    return render(request,"index.html",context)

def i(request):
    return render(request,"index.html")

@login_required
def add(request):
    user=request.user
    list1 = m() 
    if request.method =="POST":
        form = m(request.POST) 
        if form.is_valid():
            Item=form.cleaned_data.get('Item')
            Quantity=form.cleaned_data.get('Quantity')
            status=form.cleaned_data.get('status')
            date=form.cleaned_data.get('date')
            Items.objects.create(user=user,Item=Item, Quantity=Quantity,slug=user.username, status=status,date=date)
            #obj = views.objects.get('index')
            return redirect(index)
      
    return render(request,"add.html",{'form':list1})

@login_required
def update(request,id):
    It=Items.objects.filter(id=id)
    if request.method=="POST":
        form=m1(id,request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
            
    else:
        form=m1(id,request.POST)
        context={
            "It1":form
        }
        return render(request,"update.html",context)

@login_required
def delete(request,id):
    obj=Items.objects.filter(id=id).delete()
    return redirect(index)
            #print(form.errors)
    #return reverse("index")

@login_required  
def filter(request):
    query=request.GET.get('q')
    result=Items.objects.filter(date=query)
    user=request.user
    re=result.filter(user=user)
    context={
        'It':re
    }
    
    return render(request,"index.html",context)