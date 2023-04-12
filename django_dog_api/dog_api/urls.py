from django.urls import path
from . import views

urlpatterns = [
    # api/contacts will be routed to the ContactList view for handling
    path('api/dog', views.dogList.as_view(), name='dog_list'),
    # api/dogs will be routed to the ContactDetail view for handling
    path('api/dog/<int:pk>', views.dogDetail.as_view(), name='dog_detail'),
    path('api/food', views.FoodList.as_view(), name='food_list'),
    path('api/food/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),
]
