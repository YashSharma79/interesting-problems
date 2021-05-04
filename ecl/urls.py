from django.urls import path

from . import views

app_name = 'ecl'
urlpatterns = [
    path('', views.IndexView.as_view(), name="entries"),
    path('<int:pk>/id/', views.EntryView.as_view(), name = 'entry'),
    path('add', views.add, name = 'add'),
    path('tag/<int:pk>/', views.EntriesByTag.as_view(), name='bytag'),
    path('about', views.about, name = 'about')
]