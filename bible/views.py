from django.shortcuts import render
from .funcs import biBuild
from .models import Bible, NA27Bible
from django.contrib import messages
import re
from django.views import View


class BibleV(View):

    def __init__(self, arg):
        super(Bible, self).__init__()
        self.arg = arg

    def is_OT(self):
        if self.engName == "Matthew" or "Mark" or "Luke" or "John" or "Acts" or "Romans" or "1 Corinthians" or "2 Corinthians" or "Galatians" or "Ephesians" or "Philippians" or "Colossians" or "1 Thessalonians" or "2 Thessalonians" or "1 Timothy" or "2 Timothy" or "Titus" or "Philemon" or "Hebrews" or "James" or "1 Peter" or "2 Peter" or "1 John" or "2 John" or "3 John" or "Jude" or "Revelation":
            return True
        else:
            return False

    def is_NT(self):
        NT = NA27Bible.objects.values_list('engName', flat=True).distinct()
        #["Matthew" , "Mark" , "Luke" , "John" , "Acts" , "Romans" , "1 Corinthians" , "2 Corinthians" , "Galatians" , "Ephesians" , "Philippians" , "Colossians" , "1 Thessalonians" , "2 Thessalonians" , "1 Timothy" , "2 Timothy" , "Titus" , "Philemon" , "Hebrews" , "James" , "1 Peter" , "2 Peter" , "1 John" , "2 John" , "3 John" , "Jude" , "Revelation"]
        if self.engName in NT:
            return True
        else:
            return False

    def scholarBible(request):
        if request.method == "POST":
            q = request.POST.get('query')
            verse = q.split(':', 1)[1]
            verse = verse.strip()
            chap = q.split(':', 1)[0]
            code = chap.split(' ')[0]
            code = code.strip()
            chapter = chap.split(' ')[1]
            chapter = chapter.strip()
            if Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() == 1:
                queryset = Bible.objects.get(code=code, chapter=chapter, verse=verse)
                book = queryset.book
                text = queryset.text
                engName = queryset.engName
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                else:
                    pass

            elif Bible.objects.filter(code=code, chapter=chapter, verse=verse).count() > 1:
                queryset = Bible.objects.filter(code=code, chapter=chapter, verse=verse)[0]
                book = queryset.book
                text = queryset.text
                engName = queryset.engName
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                else:
                    pass
            else:
                book = 'يوحنا'
                code = 'يو'
                chapter = '1'
                verse = '1'
                queryset = Bible.objects.get(book=book, chapter=chapter, verse=verse)
                text = queryset.text
                engName = queryset.engName
                if BibleV.is_NT(queryset):
                    greek = NA27Bible.objects.get(engName=engName, chapter=chapter, verse=verse)
                    greek = greek.text
                messages.warning(request, f"Not found")

        elif request.method == 'GET':
            book = 'يوحنا'
            code = 'يو'
            chapter = '1'
            verse = '1'
            queryset = Bible.objects.get(book=book, chapter=chapter, verse=verse)
            text = queryset.text
            engName = queryset.engName
            if BibleV.is_NT(queryset):
                greek = NA27Bible.objects.get(engName=engName, chapter=chapter, verse=verse)
                greek = greek.text
        if BibleV.is_NT(queryset):
            context = {
                'book': book,
                'code': code,
                'chapter': chapter,
                'verse': verse,
                'text': text,
                'greek': greek,
            }
        else:
            context = {
                'book': book,
                'code': code,
                'chapter': chapter,
                'verse': verse,
                'text': text, }

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
