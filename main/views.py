from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

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
    subtitle = form["books_subtitle"]
    description = form["books_description"]
    price = form["books_price"]
    genre = form["books_genre"]
    author = form["books_author"]
    year = form["books_year"]
    book = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)
    # return HttpResponse("Форма получена")

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def mark_books(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)

def unmark_books(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(books)

def delete_books(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(books)

def books_detail(request, id):
    books_detail = Books.objects.get(id=id)
    return render(request, "books_detail.html", {"books_detail": books_detail})

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
