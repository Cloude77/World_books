from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('admin/', admin.site.urls),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),



]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/create/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]


