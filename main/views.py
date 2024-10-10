from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'team' : 'D04',
    }

    return render(request, "main.html", context)


