from django.shortcuts import render
from .funcs import arName
from .models import Bible
from django.contrib import messages


def bible(request):
    if request.method == "GET":
        book = request.GET.get('book')
        chapter = request.GET.get('chapter')
        verse = request.GET.get('verse')
        if Bible.objects.filter(book=book, chapter=chapter, verse=verse).count() > 0:
            m = Bible.objects.get(book=book, chapter=chapter, verse=verse)
            text = m.text
            messages.success(request, f"found")
        else:
            text = "null"
    else:
        text = "null"
    print("text is: ", text)
    # arName(request)
    # x = Bible.objects.get(engName="Genesis")
    # y = Chapter.objects.get(book=x, chapter='1')
    # z = Verse.objects.get(book=x, chapter=y, verse='5')

    context = {
        'text': text
    }

    return render(request, 'bible/bible.html', context)
