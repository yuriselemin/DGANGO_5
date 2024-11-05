from django.shortcuts import render

def main(request):
    return render(request, 'fourth_task/main.html')

def store(request):
    context = {
        'items':[
            'Item 1',
            'Item 2',
            'Item 3',
        ]
    }
    return render(request, 'fourth_task/store.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')


