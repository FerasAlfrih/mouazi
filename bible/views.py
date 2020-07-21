from django.shortcuts import render
from .funcs import biReader
from .models import Bible
from django.contrib import messages
import re


def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))


def bible(request):
    if request.method == "POST":
        book = request.POST.get('book')
        chapter = request.POST.get('chapter')
        if request.POST.get('verse'):
            verse = request.POST.get('verse')
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
            elif special_match(verse) == False:
                ver1 = verse.split('-', 1)[0]
                ver2 = verse.split('-', 1)[1]
                cd = Bible.objects.get(book=book, chapter=chapter, verse=ver1)
                code = cd.code
                texts = []
                vers = range(int(ver1), int(ver2) + 1, +1)
                for vr in vers:
                    vrt = Bible.objects.get(book=book, chapter=chapter, verse=vr)
                    txt = vrt.text
                    vrs = vrt.verse
                    text = vrs + txt
                    texts.append(text)
                context = {
                    'texts': texts,
                    'ver1': ver1,
                    'ver2': ver2,
                    'code': code,
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
                    txt = m.text
                    vrs = m.verse
                    text = vrs + txt
                    texts.append(text)
                    vers.append(vrs)
                context = {
                    'texts': texts,
                    'code': code,
                    'chap': chapter,
                    'ver1': vers[0],
                    'ver2': vers[-1],

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
                'ver': verse,
            }

    return render(request, 'bible/bible.html', context,)
