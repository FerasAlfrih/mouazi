from django.db import models

# Create your models here.


class Bible(models.Model):
    book = models.CharField(max_length=300)
    engName = models.CharField(max_length=300)
    code = models.CharField(max_length=5)
    enCode = models.CharField(max_length=5)
    chapter = models.CharField(max_length=3)
    verse = models.CharField(max_length=3)
    text = models.TextField()

    def __str__(self):
        return (self.engName)


class NA27Bible(models.Model):
    book = models.CharField(max_length=300)
    code = models.CharField(max_length=5)
    engName = models.CharField(max_length=300)
    chapter = models.CharField(max_length=3)
    verse = models.CharField(max_length=3)
    text = models.TextField()

    def __str__(self):
        return (self.engName)


class LXXBible(models.Model):
    book = models.CharField(max_length=300)
    code = models.CharField(max_length=5)
    engName = models.CharField(max_length=300)
    chapter = models.CharField(max_length=3)
    verse = models.CharField(max_length=3)
    text = models.TextField()

    def __str__(self):
        return (self.engName)


class VULBible(models.Model):
    book = models.CharField(max_length=300)
    code = models.CharField(max_length=5)
    engName = models.CharField(max_length=300)
    chapter = models.CharField(max_length=3)
    verse = models.CharField(max_length=3)
    text = models.TextField()

    def __str__(self):
        return (self.engName)


# class Chapter(models.Model):
#     book = models.ForeignKey(Bible, on_delete=models.CASCADE)
#     chapter = models.CharField(max_length=3)

#     def __str__(self):
#         return(self.chapter)


# class Verse(models.Model):
#     book = models.ForeignKey(Bible, on_delete=models.CASCADE)
#     chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
#     verse = models.CharField(max_length=3)
#     text = models.TextField()

#     def __str__(self):
#         return(self.verse)
