from django.shortcuts import render
# from .funcs import arName
from .models import Bible
from django.contrib import messages
import re


def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))


def bible(request):
    if request.method == "GET":
        book = request.GET.get('book')
        chapter = request.GET.get('chapter')
        if request.GET.get('verse'):
            verse = request.GET.get('verse')
            if Bible.objects.filter(book=book, chapter=chapter, verse=verse).count() > 0:
                m = Bible.objects.get(book=book, chapter=chapter, verse=verse)
                text = m.text
                code = m.code
                messages.success(request, f"Found")
                context = {
                    'text': text,
                    'code': code,
                    'chap': chapter,
                    'ver': verse
                }
            else:
                text = ""
                code = ""
                messages.success(request, f"Not Found")
                context = {
                }
        else:
            if Bible.objects.filter(book=book, chapter=chapter).count() > 0:
                ds = Bible.objects.get(book=book, chapter=chapter, verse="1")
                code = ds.code
                ms = Bible.objects.filter(book=book, chapter=chapter)
                texts = []
                vers = []
                for m in ms:
                    text = m.text
                    vrs = m.verse
                    texts.append(text: vrs)
                context = {
                    'text': texts,
                    'code': code,
                    'chap': chapter,
                    'ver1': vers[0],
                    'ver2': vers[-1],
                    'ver': vers,
                }
            else:
                text = ""
                code = ""
                messages.success(request, f"Not Found")
                context = {
                }
    else:
        book = "يوحنا"
        chapter = "1"
        verse = "1"
        if Bible.objects.filter(book=book, chapter=chapter, verse=verse).count() > 0:
            m = Bible.objects.get(book=book, chapter=chapter, verse=verse)
            text = m.text
            code = m.code
            messages.success(request, f"Found")
            context = {
                'text': text,
                'code': code,
                'chap': chapter,
                'ver': verse
            }

    # x = Bible.objects.get(engName="Genesis")
    # y = Chapter.objects.get(book=x, chapter='1')
    # z = Verse.objects.get(book=x, chapter=y, verse='5')

    return render(request, 'bible/bible.html', context)
