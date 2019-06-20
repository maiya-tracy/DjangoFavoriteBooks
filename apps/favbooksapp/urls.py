from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^$', views.index),
    url(r'^register$', views.addUserToDB),
    url(r'^login$', views.loginUserToDB),
    url(r'^logout$', views.logout),
    url(r'^books/add_book$', views.add_book),
    url(r'^books/(?P<bookid>\d+)$', views.book_click),
    url(r'^books/update/(?P<bookid>\d+)$', views.update_book),
    url(r'^books/delete/(?P<bookid>\d+)$', views.delete_book),
    url(r'^books/unfavorite/(?P<bookid>\d+)$', views.unlike_book),
    url(r'^books/favorite/(?P<bookid>\d+)$', views.like_book),
    url(r'^books/myfavs$', views.myfavs),
]
