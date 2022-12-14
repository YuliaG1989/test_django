from django.urls import path
from . import views

urlpatterns = [
    path('api/marvel', views.MarvelList.as_view(), name='marvel_list'), # api/marvel will be routed to the MarvelList view for handling
    path('api/marvel/<int:pk>', views.MarvelDetail.as_view(), name='marvel_detail'), # api/marvel will be routed to the ContactDetail view for handling
]
