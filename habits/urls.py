from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitListAPIView, HabitOwnerListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='detail'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='delete'),
    path('', HabitListAPIView.as_view(), name="list"),
    path('habits/', HabitOwnerListAPIView.as_view(), name="list-owner"),
]
