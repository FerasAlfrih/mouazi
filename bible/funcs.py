import requests
from bs4 import BeautifulSoup
from .models import Bible
from django.contrib import messages


def biReader(args):
    b, c, v = args.splite()
    pass


def biSearch(request):
    pass


def arName(request):
    bibles = Bible.objects.filter(engName="Leviticus")
    count = Bible.objects.filter(engName="Leviticus", book="").count()
    if count > 0:
        for b in bibles:
            b.book = "الخروج"
            b.code = "خر"
            Bible.save(b)
    messages.success(request, f"database successfully updated")

    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()
    # elif Bible.objects.filter(engName=""):
    #     bi = Bible.objects.create(book="",
    #         code="")
    #     bi.save()


def biBuild():
    Bible.objects.all().delete()
    # Chapter.objects.all().delete()
    # Verse.objects.all().delete()
    soup = BeautifulSoup(open('static/files/arbible.xml', encoding='utf8'), "lxml")

    books = soup.findAll("b")

    for book in books:
        engName = book['n']
        enCode = book['id']
        # bi = Bible(engName=engName,
        #            enCode=enCode)
        # bi.save()
        chapters = book.findAll('c')
        for chapt in chapters:
            chapter = chapt['n']

            # ch = Chapter(chapter=chapter,
            #              book=Bible.objects.get(engName=book))
            # ch.save()
            verses = chapt.findAll('v')
            for ver in verses:
                verse = ver['n']
                text = ver.text
                chapter = chapter
                book = engName
                vr = Bible(chapter=chapter,
                           engName=engName,
                           verse=verse,
                           text=text,
                           enCode=enCode)
                vr.save()
