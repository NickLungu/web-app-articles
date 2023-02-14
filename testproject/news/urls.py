from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_home'),
    path('add_article', views.add_article, name='add_article'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='details_view'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_view'),
]
