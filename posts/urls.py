from django.urls import path
from .views import *
from accounts.views import arizani_yuborish
app_name = 'posts'

urlpatterns = [
    path('vacancies/<int:id>/', post_detail, name='post_detail'),
    path('vacancies/<slug:category_slug>/', post_list, name='post_list_with_category'),
    path('vacancies/', post_list, name='post_list'),
    path('search/', search_view, name='search'),
    path('send-application/<int:company>', arizani_yuborish, name='send_app'),
    path('send-application/', arizani_yuborish, name='send_app'),
    path('', home_page, name='home_page'),
]   
