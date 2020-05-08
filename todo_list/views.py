from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . models import List
from . forms import ListForms
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForms(request.POST or None )

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,("Item has been added to the list"))
            return render(request, 'home.html', {'all_items': all_items})

    else:
         all_items = List.objects.all
         return render(request, 'home.html', {'all_items': all_items})



def about(request):
    return render(request,'about.html',{'Name': "Drishty and Khyaithy"})


def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted to the list"))
    return redirect('home')



def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def cross_on(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForms(request.POST or None, instance=item )

        if form.is_valid():
            form.save()
            messages.success(request,("Item has been edited to the list"))
            return redirect('home')

    else:
         item = List.objects.get(pk=list_id)
         return render(request, 'edit.html', {'item': item})









