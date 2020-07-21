from django.urls import path
from .views import BibleV


urlpatterns = [
    path('', BibleV.bible, name='bible'),
    path('StudyBible/', BibleV.scholarBible, name='scholar'),

    #

]
