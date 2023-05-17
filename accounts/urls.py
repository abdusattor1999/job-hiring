from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('create/', register, name='create'),
    path('login/', login_view, name='login'),
    path('company/<int:id>', company_detail, name="company_detail"),
    path('company/', company_create, name="company_create"),
    path('edit-profile/<int:id>', edit, name="profile_edit"),
    path('edit-user/', user_edit, name="user_edit"),
    path('confirm-delete/', confirm_delete, name="confirm_delete"),
    path('user-delete/', user_delete, name="user_delete"),
    path('user/', user_details, name="profile_details"),
    path('profile/', profile_list, name="profile_list"),
    path('add-profile/', add_profile, name="add_profile"),
]
