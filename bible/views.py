from django.shortcuts import render
from .funcs import biBuild
from .models import Bible, GreekBible
from django.contrib import messages
import re
from django.views import View


class BibleV(View):
    """docstring for Bible"""

    def __init__(self, arg):
        super(Bible, self).__init__()
        self.arg = arg

    def oT(self):
        pass
    def oT(self):
        pass

    def scholarBible(request):
        biBuild(request)
        context = {}
        # if request.method == "POST":
        #     q = request.POST.get('query')
        #     verse = q.split(':', 1)[1]
        #     verse = verse.strip()
        #     chap = q.split(':', 1)[0]
        #     code = chap.split(' ')[0]
        #     code = code.strip()
        #     chapter = chap.split(' ')[1]
        #     chapter = chapter.strip()
        #     if Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() == 1:
        #         queryset = Bible.objects.get(code=code, chapter=chapter, verse=verse)
        #         book = queryset.book
        #         text = queryset.text
        #     elif Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() > 1:
        #         queryset = Bible.objects.filter(code=code, chapter=chapter, verse=verse)[0]
        #         book = queryset.book
        #         text = queryset.text
        #     else:
        #         book = 'يوحنا'
        #         code = 'يو'
        #         chapter = '1'
        #         verse = '1'
        #         queryset = Bible.objects.get(book=book, chapter=chapter, verse=verse)
        #         text = queryset.text
        #         messages.alert(request, f"Not found")

        # elif request.method == 'GET':
        #     book = 'يوحنا'
        #     code = 'يو'
        #     chapter = '1'
        #     verse = '1'
        #     queryset = Bible.objects.get(book=book, chapter=chapter, verse=verse)
        #     text = queryset.text
        # context = {
        #     'book': book,
        #     'code': code,
        #     'chapter': chapter,
        #     'verse': verse,
        #     'text': text,

        # }
        return render(request, 'bible/scholar.html', context)

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
                elif BibleV.special_match(verse) == False:
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

    def coder(request):
        codes = []
        cds = Bible.objects.all()
        for cd in cds:
            code = cd.code
            codes.append(code)
        context = {
            'codes': codes,
        }
