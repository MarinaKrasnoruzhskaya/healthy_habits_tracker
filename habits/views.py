from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import CustomPagination
from habits.permissions import IsOwner
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

    def get_object(self):
        """ Возвращает привычку в том случае, если она публичная или текущий пользователь является её владельцем,
        иначе сообщение об ошибке доступа """

        habit = super().get_object()
        user = self.request.user
        if habit.user == user or habit.is_publicity:
            return habit
        else:
            raise PermissionDenied("You don't have access to this habit.")


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения информации о привычке """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner,]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления привычки """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner,]


class HabitListAPIView(generics.ListAPIView):
    """ Контроллер для получения списка публичных привычек """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        """ Возвращает только публичные привычки """

        return super().get_queryset().filter(is_publicity=True)


class HabitOwnerListAPIView(generics.ListAPIView):
    """ Контроллер для получения списка привычек текущего пользователя"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        """ Возвращает привычки текущего пользователя"""

        user = self.request.user
        return super().get_queryset().filter(user=user)
