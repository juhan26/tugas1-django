from django.shortcuts import render, redirect
from .models import MyProject, GuestBook, Blog

def home(request):
    # services = Service.objects.all()  # Menampilkan layanan di home (opsional)
    return render(request, 'home.html')

# , {'services': services}

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def my_projects(request):
    projects = MyProject.objects.all()
    return render(request, 'my_projects.html', {'projects': projects})

def guest_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        message = request.POST['message']
        GuestBook.objects.create(name=name, address=address, message=message)
        return redirect('guest_book')
    
    guest_book = GuestBook.objects.all()
    return render(request, 'guest_book.html', {'guest_book': guest_book})

def blog(request):
    blogs = Blog.objects.all().order_by('-date_published')
    return render(request, 'blog.html', {'blogs': blogs})
