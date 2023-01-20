from django.urls import path,include
from . import views

urlpatterns = [
    path('index', views.indexfun, name='index')
    # path('programs', views.programfun, name='programs'),
    # path('placements', views.placefun, name='placement'),
    # path('about_up', views.aboutfun, name='about')
]