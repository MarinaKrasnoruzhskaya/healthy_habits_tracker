from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ Класс для определения является ли авторизованный пользователь владельцем """

    def has_object_permission(self, request, view, obj):
        """ Метод для проверки является ли авторизованный пользователь владельцем """
        return obj.user == request.user
