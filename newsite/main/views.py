from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Say', 'Hello', '12345'],
        'obj':{
            'car': 'Porshe',
            'name': 'Jasper',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')