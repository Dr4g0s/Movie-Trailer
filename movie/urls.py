from django.urls import path
from . import views



urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
    path('search/', views.MovieSearch.as_view(), name='list_search'),
    path('category/<str:category>/', views.MovieListByCategory.as_view(), name='list_by_category'),
    path('language/<str:language>/', views.MovieListByLanguage.as_view(), name='list_by_language'),
    path('year/<str:year>/', views.MovieListByYear.as_view(), name='list_by_year'),
    path('cast/<str:cast>/', views.MovieListByCast.as_view(), name='list_by_cast'),
    path('<slug:slug>', views.MovieDetailView.as_view(), name='detail'),
    path('contact/', views.MovieContactForm, name='contact'),
    path('terms/', views.MovieTerms, name='terms'),
]
