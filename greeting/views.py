from django.shortcuts import render

def birthday_view(request):
    context = {
        'name': 'Mandarina',  # Puedes cambiar esto al nombre de la persona
        'age': 30,  # Puedes cambiar esto a la edad de la persona
    }
    return render(request, 'greeting/birthday.html', context)
