from django.shortcuts import render


posts = [
    {
        'author': 'Valeria Meza',
        'title': 'Some Blog',
        'content': 'My first post',
        'date_posted': 'November 11, 2020'
    },
    {
        'author': 'Valeria Something',
        'title': 'Some Other Blog',
        'content': 'This post',
        'date_posted': 'November 1, 2019'
    }
]

def home(request):
    data = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', data)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
