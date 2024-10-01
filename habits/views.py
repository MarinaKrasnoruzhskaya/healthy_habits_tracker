from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания привычки """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """ Автоматическая привязка создаваемой привычки к текущему пользователю """
        serializer.save(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для получения информации о привычке """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения информации о привычке """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления привычки """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """ Контроллер для получения списка всех привычек """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
