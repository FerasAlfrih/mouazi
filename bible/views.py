from django.shortcuts import render
from django.contrib import messages
from django.views import View

import re
import requests
from bs4 import BeautifulSoup

from .models import Bible, NA27Bible, LXXBible, VULBible


class BibleV(View):

    def __init__(self, arg):
        super(Bible, self).__init__()
        self.arg = arg

    def is_OT(self):
        OT = LXXBible.objects.values_list('engName', flat=True).distinct()
        if self.engName in OT:
            return True
        else:
            return False

    def is_NT(self):
        NT = NA27Bible.objects.values_list('engName', flat=True).distinct()
        if self.engName in NT:
            return True
        else:
            return False

    @staticmethod
    def scholarBible(request):
        if request.method == "POST":
            q = request.POST.get('query')
            verse = q.split(':', 1)[1]
            verse = verse.strip()
            verse = int(verse)
            chap = q.split(':', 1)[0]
            code = chap.split(' ')[0]
            code = code.strip()
            chapter = chap.split(' ')[1]
            chapter = chapter.strip()
            chapter = int(chapter)
            if Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() == 1:
                queryset = Bible.objects.get(
                    code=code, chapter=chapter, verse=verse)
                book = queryset.book
                text = queryset.text
                engName = queryset.engName
                vulgata = VULBible.objects.get(
                    engName=engName, chapter=chapter, verse=verse)
                latin = vulgata.text
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(
                        engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                elif BibleV.is_OT(queryset):
                    lxgreek = LXXBible.objects.get(
                        engName=engName, chapter=chapter, verse=verse)
                    lxgreek = lxgreek.text
                else:
                    pass

            elif Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() > 1:
                queryset = Bible.objects.filter(
                    code=code, chapter=chapter, verse=verse)[0]
                book = queryset.book
                text = queryset.text
                engName = queryset.engName
                vulgata = VULBible.objects.get(
                    engName=engName, chapter=chapter, verse=verse)
                latin = vulgata.text
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(
                        engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                elif BibleV.is_OT(queryset):
                    lxgreek = LXXBible.objects.get(
                        engName=engName, chapter=chapter, verse=verse)
                    lxgreek = lxgreek.text
                else:
                    pass
            else:
                book = 'يوحنا'
                code = 'يو'
                chapter = '1'
                verse = '1'
                queryset = Bible.objects.get(
                    book=book, chapter=chapter, verse=verse)
                text = queryset.text
                engName = queryset.engName
                vulgata = VULBible.objects.get(
                    engName=engName, chapter=chapter, verse=verse)
                latin = vulgata.text
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(
                        engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                messages.warning(request, f"Not found")

        elif request.method == 'GET':
            book = 'يوحنا'
            code = 'يو'
            chapter = '1'
            verse = '1'
            queryset = Bible.objects.get(
                book=book, chapter=chapter, verse=verse)
            text = queryset.text
            engName = queryset.engName
            vulgata = VULBible.objects.get(
                engName=engName, chapter=chapter, verse=verse)
            latin = vulgata.text
            greek = NA27Bible.objects.get(
                engName=engName, chapter=chapter, verse=verse)
            greek = greek.text
        print(BibleV.is_OT(queryset))
        if BibleV.is_NT(queryset):
            context = {
                'book': book,
                'code': code,
                'chapter': chapter,
                'verse': verse,
                'text': text,
                'greek': greek,
                'VUL': latin
            }
        elif BibleV.is_OT(queryset):
            context = {
                'book': book,
                'code': code,
                'chapter': chapter,
                'verse': verse,
                'text': text,
                'LXX': lxgreek,
                'VUL': latin
            }
        else:
            context = {
                'book': book,
                'code': code,
                'chapter': chapter,
                'verse': verse,
                'text': text, }

        return render(request, 'bible/scholar.html', context)

    @staticmethod
    def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
        return not bool(search(strg))

    @staticmethod
    def bible(request):
        if request.method == "POST":
            book = request.POST.get('book')
            chapter = request.POST.get('chapter')
            chapter = int(chapter)
            if request.POST.get('verse'):
                verse = request.POST.get('verse')
                if BibleV.special_match(verse) == False:
                    ver1 = verse.split('-', 1)[0]
                    ver1 = int(ver1)
                    ver2 = verse.split('-', 1)[1]
                    ver2 = int(ver2)
                    cd = Bible.objects.get(
                        book=book, chapter=chapter, verse=ver1)
                    code = cd.code
                    texts = []
                    vers = range(int(ver1), int(ver2) + 1, +1)
                    for vr in vers:
                        vrt = Bible.objects.get(
                            book=book, chapter=chapter, verse=vr)
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
                elif Bible.objects.filter(book=book, chapter=chapter, verse=verse).count() > 0:
                    verse = int(verse)
                    m = Bible.objects.get(
                        book=book, chapter=chapter, verse=verse)
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
                    ds = Bible.objects.get(
                        book=book, chapter=chapter, verse="1")
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
