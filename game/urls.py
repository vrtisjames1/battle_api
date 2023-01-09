from django.urls import path
from . import views

urlpatterns = [
    path('api/games', views.GamesList.as_view(), name='games_list'), # api/games will be routed to the ContactList view for handling
    path('api/games/<int:pk>', views.GamesDetail.as_view(), name='games_detail'), # api/games will be routed to the ContactDetail view for handling
]