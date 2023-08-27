from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from . import views
from django.contrib.auth import views as auth_views
from . import views_api
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # CRUD
    path("users/sign_up", views_api.signup, name='sign_up'),
    path("users/update", views_api.update, name='update'),
    path("search", views_api.search_user, name='search'),
    path("create_item", views_api.create_item, name='create_item'),
    path("search_item", views_api.search_items, name='search_item'),
    path("delete_user", views_api.delete_user, name='delete_user'),
    # path("delete_item", views_api.delete_item, name='delete_item'),
    path('delete_item/<int:item_id>', views_api.delete_item, name='delete_item'),
    path("update_item", views_api.update_item, name='update_item'),
    path("obtain-token", obtain_auth_token, name="login"),
    path('check-token', views_api.check_token),
    path('search_one',views_api.search_this_user, name='search_one')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)