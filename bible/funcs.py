import requests
from bs4 import BeautifulSoup
from .models import Bible
from django.contrib import messages
from django.http import HttpResponseRedirect



def biReader(args):
    args.split('-', 1)
    pass


def biSearch(request):

    pass


def arName(request):
    # Old Testament
    #  if bl.engName == "Genesis":
    # bs = Bible.objects.filter(engName="Genesis")
    # for b in bs:
    #     b.book = "تكوين"
    #     b.code = "تك"
    #     Bible.save(b)
    # messages.success(request, f"done")
    # elif bl.engName == "Exodus":
    # bs = Bible.objects.filter(engName="Exodus")
    # for b in bs:
    #     b.book = "خروج"
    #     b.code = "خر"
    #     Bible.save(b)
    # messages.success(request, f"done")
    # elif bl.engName == "Leviticus":
    # bs = Bible.objects.filter(engName="Leviticus")
    # for b in bs:
    #     b.book = "لاويين"
    #     b.code = "لا"
    #     Bible.save(b)
    # messages.success(request, f"done")
    # elif bl.engName == "Numbers":
    # bs = Bible.objects.filter(engName="Numbers")
    # for b in bs:
    #     b.book = "عدد"
    #     b.code = "عد"
    #     Bible.save(b)
    # messages.success(request, f"done  {b.enCode}")
    # elif bl.engName == "Deuteronomy":
    # bs = Bible.objects.filter(engName="Deuteronomy")
    # for b in bs:
    #     b.book = "تثنية"
    #     b.code = "تث"
    #     Bible.save(b)
    #     messages.success(request, f"done {b.enCode}")
    # elif bl.engName == "Joshua":
    # bs = Bible.objects.filter(engName="Joshua")
    # for b in bs:
    #     b.book = "يشوع"
    #     b.code = "يش"
    #     Bible.save(b)
    # messages.success(request, f"done {b.enCode}")
    # elif bl.engName == "Judges":
    # bs = Bible.objects.filter(engName="Judges")
    # for b in bs:
    #     b.book = "قضاة"
    #     b.code = "قض"
    #     Bible.save(b)
    # messages.success(request, f"done {b.enCode}")
    # elif bl.engName == "Ruth":
    # bs = Bible.objects.filter(engName="Ruth")
    # for b in bs:
    #     b.book = "راعوث"
    #     b.code = "را"
    #     Bible.save(b)
    # messages.success(request, f"done {b.enCode}")

    bls = Bible.objects.filter(book="")
    for bl in bls:
        if bl.engName == "1 Samuel" and bl.book=="":
            if Bible.objects.filter(engName="1 Samuel", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Samuel")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "صموئيل الأول"
                    b.code = "1صم"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Samuel" and bl.book=="":
            if Bible.objects.filter(engName="2 Samuel", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Samuel")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "صموئيل الثاني"
                    b.code = "2صم"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Kings" and bl.book=="":
            if Bible.objects.filter(engName="1 Kings", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Kings")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "الملوك الأول"
                    b.code = "1مل"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Kings" and bl.book=="":
            if Bible.objects.filter(engName="2 Kings", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Kings")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "الملوك الثاني"
                    b.code = " 2مل"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Chronicles" and bl.book=="":
            if Bible.objects.filter(engName="1 Chronicles", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Chronicles")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أخبار الأيام الأول"
                    b.code = " 1أخبار"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Chronicles" and bl.book=="":
            if Bible.objects.filter(engName="2 Chronicles", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Chronicles")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أخبار الأيام الثاني"
                    b.code = "2أخبار"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Ezra" and bl.book=="":
            if Bible.objects.filter(engName="Ezra", book="").count()>0:
                bs = Bible.objects.filter(engName="Ezra")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "عزرا"
                    b.code = "عز"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Nehemiah" and bl.book=="":
            if Bible.objects.filter(engName="Nehemiah", book="").count()>0:
                bs = Bible.objects.filter(engName="Nehemiah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "نحميا"
                    b.code = "نح"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Esther" and bl.book=="":
            if Bible.objects.filter(engName="Esther", book="").count()>0:
                bs = Bible.objects.filter(engName="Esther")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أستير"
                    b.code = "اس"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Job" and bl.book=="":
            if Bible.objects.filter(engName="Job", book="").count()>0:
                bs = Bible.objects.filter(engName="Job")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أيوب"
                    b.code = "أي"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Psalms" and bl.book=="":
            if Bible.objects.filter(engName="Psalms", book="").count()>0:
                bs = Bible.objects.filter(engName="Psalms")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "مزامير"
                    b.code = "مز"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Proverbs" and bl.book=="":
            if Bible.objects.filter(engName="Proverbs", book="").count()>0:
                bs = Bible.objects.filter(engName="Proverbs")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أمثال"
                    b.code = "أم"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Ecclesiastes" and bl.book=="":
            if Bible.objects.filter(engName="Ecclesiastes", book="").count()>0:
                bs = Bible.objects.filter(engName="Ecclesiastes")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "جامعة"
                    b.code = "جا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Song of Solomon" and bl.book=="":
            if Bible.objects.filter(engName="Song of Solomon", book="").count()>0:
                bs = Bible.objects.filter(engName="Song of Solomon")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "نشيد الإنشاد"
                    b.code = "نش"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Isaiah" and bl.book=="":
            if Bible.objects.filter(engName="Isaiah", book="").count()>0:
                bs = Bible.objects.filter(engName="Isaiah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "اشعيا"
                    b.code = "اش"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Jeremiah" and bl.book=="":
            if Bible.objects.filter(engName="Jeremiah", book="").count()>0:
                bs = Bible.objects.filter(engName="Jeremiah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أرميا"
                    b.code = "ار"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Lamentations" and bl.book=="":
            if Bible.objects.filter(engName="Lamentations", book="").count()>0:
                bs = Bible.objects.filter(engName="Lamentations")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "مراثي أرميا"
                    b.code = "مرا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Ezekiel" and bl.book=="":
            if Bible.objects.filter(engName="Ezekiel", book="").count()>0:
                bs = Bible.objects.filter(engName="Ezekiel")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "حزقيال"
                    b.code = "حز"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Daniel" and bl.book=="":
            if Bible.objects.filter(engName="Daniel", book="").count()>0:
                bs = Bible.objects.filter(engName="Daniel")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "دانيال"
                    b.code = "دا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Hosea" and bl.book=="":
            if Bible.objects.filter(engName="Hosea", book="").count()>0:
                bs = Bible.objects.filter(engName="Hosea")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "هوشع"
                    b.code = "هو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Joel" and bl.book=="":
            if Bible.objects.filter(engName="Joel", book="").count()>0:
                bs = Bible.objects.filter(engName="Joel")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يوئيل"
                    b.code = "يؤ"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Amos" and bl.book=="":
            if Bible.objects.filter(engName="Amos", book="").count()>0:
                bs = Bible.objects.filter(engName="Amos")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "عاموس"
                    b.code = "عا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Obadiah" and bl.book=="":
            if Bible.objects.filter(engName="Obadiah", book="").count()>0:
                bs = Bible.objects.filter(engName="Obadiah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "عوبديا"
                    b.code = "عو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Jonah" and bl.book=="":
            if Bible.objects.filter(engName="Jonah", book="").count()>0:
                bs = Bible.objects.filter(engName="Jonah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يونان"
                    b.code = "يو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Micah" and bl.book=="":
            if Bible.objects.filter(engName="Micah", book="").count()>0:
                bs = Bible.objects.filter(engName="Micah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "ميخا"
                    b.code = "مي"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Nahum" and bl.book=="":
            if Bible.objects.filter(engName="Nahum", book="").count()>0:
                bs = Bible.objects.filter(engName="Nahum")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "ناحوم"
                    b.code = "نا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Habakkuk" and bl.book=="":
            if Bible.objects.filter(engName="Habakkuk", book="").count()>0:
                bs = Bible.objects.filter(engName="Habakkuk")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "حبقوق"
                    b.code = "حب"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Zephaniah" and bl.book=="":
            if Bible.objects.filter(engName="Zephaniah", book="").count()>0:
                bs = Bible.objects.filter(engName="Zephaniah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "صفنيا"
                    b.code = "صف"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Haggai" and bl.book=="":
            if Bible.objects.filter(engName="Haggai", book="").count()>0:
                bs = Bible.objects.filter(engName="Haggai")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "حجي"
                    b.code = "حج"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Zechariah" and bl.book=="":
            if Bible.objects.filter(engName="Zechariah", book="").count()>0:
                bs = Bible.objects.filter(engName="Zechariah")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "زكريا"
                    b.code = "زك"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Malachi" and bl.book=="":
            if Bible.objects.filter(engName="Malachi", book="").count()>0:
                bs = Bible.objects.filter(engName="Malachi")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "ملاخي"
                    b.code = "ملا"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        # New Testament
        elif bl.engName == "Matthew" and bl.book=="":
            if Bible.objects.filter(engName="Matthew", book="").count()>0:
                bs = Bible.objects.filter(engName="Matthew")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "متى"
                    b.code = "مت"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Mark" and bl.book=="":
            if Bible.objects.filter(engName="Mark", book="").count()>0:
                bs = Bible.objects.filter(engName="Mark")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "مرقس"
                    b.code = "مر"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Luke" and bl.book=="":
            if Bible.objects.filter(engName="Luke", book="").count()>0:
                bs = Bible.objects.filter(engName="Luke")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "لوقا"
                    b.code = "لو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "John" and bl.book=="":
            if Bible.objects.filter(engName="John", book="").count()>0:
                bs = Bible.objects.filter(engName="John")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يوحنا"
                    b.code = "يو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Acts" and bl.book=="":
            if Bible.objects.filter(engName="Acts", book="").count()>0:
                bs = Bible.objects.filter(engName="Acts")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "أعمال"
                    b.code = "أع"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Romans" and bl.book=="":
            if Bible.objects.filter(engName="Romans", book="").count()>0:
                bs = Bible.objects.filter(engName="Romans")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "رومية"
                    b.code = "رو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Corinthians" and bl.book=="":
            if Bible.objects.filter(engName="1 Corinthians", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Corinthians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "كورنثوس الأولى"
                    b.code = "1كو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Corinthians" and bl.book=="":
            if Bible.objects.filter(engName="2 Corinthians", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Corinthians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = " كورنثوس الثانية"
                    b.code = "2كو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Galatians" and bl.book=="":
            if Bible.objects.filter(engName="Galatians", book="").count()>0:
                bs = Bible.objects.filter(engName="Galatians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "غلاطية"
                    b.code = "غل"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Ephesians" and bl.book=="":
            if Bible.objects.filter(engName="Ephesians", book="").count()>0:
                bs = Bible.objects.filter(engName="Ephesians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "افسس"
                    b.code = "اف"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Philippians" and bl.book=="":
            if Bible.objects.filter(engName="Philippians", book="").count()>0:
                bs = Bible.objects.filter(engName="Philippians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "فيلبي"
                    b.code = "في"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Colossians" and bl.book=="":
            if Bible.objects.filter(engName="Colossians", book="").count()>0:
                bs = Bible.objects.filter(engName="Colossians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "كولوسي"
                    b.code = "كو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Thessalonians" and bl.book=="":
            if Bible.objects.filter(engName="1 Thessalonians", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Thessalonians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "تسالونيكي الأولى"
                    b.code = "1تس"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Thessalonians" and bl.book=="":
            if Bible.objects.filter(engName="2 Thessalonians", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Thessalonians")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "تسالونيكي الثانية"
                    b.code = "2تس"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Timothy" and bl.book=="":
            if Bible.objects.filter(engName="1 Timothy", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Timothy")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "تيموثاوس الأولى"
                    b.code = "1تي"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Timothy" and bl.book=="":
            if Bible.objects.filter(engName="2 Timothy", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Timothy")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = " تيموثاوس الثانية"
                    b.code = "2تي"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Titus" and bl.book=="":
            if Bible.objects.filter(engName="Titus", book="").count()>0:
                bs = Bible.objects.filter(engName="Titus")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "تيطس"
                    b.code = "تي"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Philemon" and bl.book=="":
            if Bible.objects.filter(engName="Philemon", book="").count()>0:
                bs = Bible.objects.filter(engName="Philemon")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "فيلمون"
                    b.code = "فل"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Hebrews" and bl.book=="":
            if Bible.objects.filter(engName="Hebrews", book="").count()>0:
                bs = Bible.objects.filter(engName="Hebrews")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "عبرانيين"
                    b.code = "عب"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "James" and bl.book=="":
            if Bible.objects.filter(engName="James", book="").count()>0:
                bs = Bible.objects.filter(engName="James")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يعقةب"
                    b.code = "يع"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 Peter" and bl.book=="":
            if Bible.objects.filter(engName="1 Peter", book="").count()>0:
                bs = Bible.objects.filter(engName="1 Peter")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "بطرس الأولى"
                    b.code = "1بط"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 Peter" and bl.book=="":
            if Bible.objects.filter(engName="2 Peter", book="").count()>0:
                bs = Bible.objects.filter(engName="2 Peter")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "بطرس الثانية"
                    b.code = "2بط"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "1 John" and bl.book=="":
            if Bible.objects.filter(engName="1 John", book="").count()>0:
                bs = Bible.objects.filter(engName="1 John")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يوحنا الأولى"
                    b.code = "1يو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "2 John" and bl.book=="":
            if Bible.objects.filter(engName="2 John", book="").count()>0:
                bs = Bible.objects.filter(engName="2 John")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يوحنا الثانية"
                    b.code = "2يو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "3 John" and bl.book=="":
            if Bible.objects.filter(engName="3 John", book="").count()>0:
                bs = Bible.objects.filter(engName="3 John")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يوحنا الثالثة"
                    b.code = "3يو"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Jude" and bl.book=="":
            if Bible.objects.filter(engName="Jude", book="").count()>0:
                bs = Bible.objects.filter(engName="Jude")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "يهوذا"
                    b.code = "يه"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        elif bl.engName == "Revelation" and bl.book=="":
            if Bible.objects.filter(engName="Revelation", book="").count()>0:
                bs = Bible.objects.filter(engName="Revelation")
                for b in bs:
                    print({b.enCode}, {b.chapter}, ":", {b.verse})
                    b.book = "رؤيا يوحنا"
                    b.code = "رؤ"
                    Bible.save(b)
            else:
                arName(request)
            messages.success(request, f"done {b.enCode}")
        else:
            break

    # messages.success(request, f"database successfully updated")


def biBuild():
    Bible.objects.all().delete()
    soup = BeautifulSoup(open('static/files/arbible.xml', encoding='utf8'), "lxml")

    books = soup.findAll("b")

    for book in books:
        engName = book['n']
        enCode = book['id']
        chapters = book.findAll('c')
        for chapt in chapters:
            chapter = chapt['n']
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
