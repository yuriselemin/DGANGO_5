from django.shortcuts import render

def main(request):
    return render(request, 'third_task/main.html')

def store(request):
    items = [
        {'name': 'Item 1'},
        {'name': 'Item 2'},
        {'name': 'Item 3'},
    ]
    return render(request, 'third_task/store.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
