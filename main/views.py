from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Books

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This the page test3")

def page1(request):
    return render(request, "page1.html")

def page2(request):
    return render(request, "page2.html")

def page3(request):
    return render(request, "page3.html")

def books(request):
    books_shop = Books.objects.all()
    return render(request, "books.html", {"books_shop": books_shop})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    #print(form)
    # return HttpResponse("Форма получена")
    return redirect(test)

def add_books(request):
    form = request.POST
    title = form["books_title"]
    books = Books(title=title)
    books.save()
    # return redirect(books)
    # subtitle = form["books_subtitle"]
    # books = Books(sutitle=subtitle)  
    # description = 
    # price = 
    # genre = 
    # author = 
    # year = 
    return HttpResponse("Форма получена")