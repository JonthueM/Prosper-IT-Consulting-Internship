from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game'),                                                 #home page
    path('addEvent/', views.addEvent, name='addEvent'),
    path('add/', views.addEvent, name="viewAdd"),
    path('Event/', views.index, name='listEvent'),
    path('Event/<int:pk>/Details/', views.details_Event, name='eventDetails'),        #get details for a single game event item
    path('Event/<int:pk>/Edit/', views.edit_Event, name='edit_Event'),  # edit workout
    path('Event/<int:pk>/Edit/Delete', views.delete_Event, name='deleteEdit'),
    path('News', views.game_News, name='latestNews'),
   # path('API/',)


]