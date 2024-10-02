from datetime import timedelta, datetime

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """ Класс для тестирования работы CRUD привычек """

    def setUp(self):
        self.user = User.objects.create(email='test_user@hht.com')
        self.owner = User.objects.create(email='test_user_owner@hht.com')

        self.pleasant_habit = Habit.objects.create(
            user=self.owner,
            place="place test 1",
            time=datetime.strptime('12:00', '%H:%M').time(),
            action="action test 1",
            periodicity="1 time in 1 days",
            time_to_complete=60,
            is_pleasant_habit=True
        )
        self.useful_habit = Habit.objects.create(
            user=self.owner,
            place="place test 2",
            time=datetime.strptime('12:00', '%H:%M').time(),
            action="action test 2",
            periodicity="1 time in 1 days",
            time_to_complete=60,
            associated_habit=self.pleasant_habit,
            is_publicity=True,
        )
        self.useful_habit_with_reward = Habit.objects.create(
            user=self.owner,
            place="place test 3",
            time=datetime.strptime('12:00', '%H:%M').time(),
            action="action test 3",
            periodicity="1 time in 1 days",
            time_to_complete=60,
            reward="reward test 3",
            is_publicity=True,
        )
        self.useful_habit_non_publicity = Habit.objects.create(
            user=self.owner,
            place="place test 4",
            time=datetime.strptime('12:00', '%H:%M').time(),
            action="action test 4",
            periodicity="1 time in 1 days",
            time_to_complete=60,
            associated_habit=self.pleasant_habit,
            is_publicity=False,
        )
        self.useful_habit_user = Habit.objects.create(
            user=self.user,
            place="place test 5",
            time=datetime.strptime('14:00', '%H:%M').time(),
            action="action test 5",
            periodicity="1 time in 2 days",
            time_to_complete=30,
            associated_habit=self.pleasant_habit,
            is_publicity=False,
        )
        self.client.force_authenticate(user=self.owner)

    def test_habit_create_unauthorized(self):
        """ Тестирование создания привычки неавторизованным пользователем """

        self.client.force_authenticate(user=None)
        url = reverse("habits:create")
        data = {
            "place": "place test 1",
            "time": timedelta(minutes=12),
            "action": "action test 1",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_habit_create(self):
        """ Тестирование создания приятной привычки авторизованным пользователем """

        url = reverse("habits:create")
        data = {
            "place": "place test 2",
            "time": timedelta(minutes=12),
            "action": "action test 2",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            6
        )

    def test_useful_habit_create(self):
        """ Тестирование создания полезной привычки со связанной приятной привычкой """

        url = reverse("habits:create")
        data = {
            "place": "place test 3",
            "time": timedelta(minutes=12),
            "action": "action test 3",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "associated_habit": self.pleasant_habit.pk,
            "is_publicity": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            6
        )

    def test_useful_habit_reward_with_create(self):
        """ Тестирование создания полезной привычки с вознаграждением """

        url = reverse("habits:create")
        data = {
            "place": "place test 3",
            "time": timedelta(minutes=12),
            "action": "action test 3",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "reward": "reward test 3",
            "is_publicity": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            6
        )

    def test_habit_create_not_valid_time_to_complete(self):
        """ Тестирование создания привычки с невалидным временем на выполнение """

        url = reverse("habits:create")
        data = {
            "place": "place test 2",
            "time": timedelta(minutes=12),
            "action": "action test 2",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 121,
            "is_pleasant_habit": "True"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        data = {
            "place": "place test 2",
            "time": timedelta(minutes=12),
            "action": "action test 2",
            "periodicity": "1 time in 1 days",
            "time_to_complete": -1,
            "is_pleasant_habit": "True"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            Habit.objects.all().count(),
            5
        )

    def test_create_not_valid_pleasant_habit(self):
        """ Тестирование создания невалидной приятной привычки с вознаграждением """

        url = reverse("habits:create")
        data = {
            "place": "place test 4",
            "time": timedelta(minutes=12),
            "action": "action test 4",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True",
            "reward": "reward test 4",
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            Habit.objects.all().count(),
            5
        )

    def test_create_not_valid_pleasant_habit_with_a_related_habit(self):
        """ Тестирование создания невалидной приятной привычки со связанной привычкой"""

        url = reverse("habits:create")
        data = {
            "place": "place test 4",
            "time": timedelta(minutes=12),
            "action": "action test 4",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True",
            "associated_habit": self.pleasant_habit,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            Habit.objects.all().count(),
            5
        )

    def test_create_not_valid_associated_habit(self):
        """ Тестирование создания невалидной связанной привычки без признака приятной привычки"""

        url = reverse("habits:create")
        data = {
            "place": "place test 4",
            "time": timedelta(minutes=12),
            "action": "action test 4",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True",
            "associated_habit": self.useful_habit,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            Habit.objects.all().count(),
            5
        )

    def test_create_not_valid_habit(self):
        """ Тестирование создания невалидной привычки при одновременном выборе и связанной привычки,
         и указания вознаграждения"""

        url = reverse("habits:create")
        data = {
            "place": "place test 4",
            "time": timedelta(minutes=12),
            "action": "action test 4",
            "periodicity": "1 time in 1 days",
            "time_to_complete": 60,
            "is_pleasant_habit": "True",
            "associated_habit": self.pleasant_habit,
            "reward": "reward test 4",
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            Habit.objects.all().count(),
            5
        )

    def test_habit_retrieve(self):
        """ Тестирование просмотра привычки владельцем"""

        url = reverse("habits:detail", args=(self.useful_habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('place'),
            self.useful_habit.place
        )

    def test_public_habit_retrieve(self):
        """ Тестирование просмотра публичной привычки не владельцем"""

        self.client.force_authenticate(user=self.user)
        url = reverse("habits:detail", args=(self.useful_habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('place'),
            self.useful_habit.place
        )

    def test_non_publicity_habit_retrieve(self):
        """ Тестирование просмотра непубличной привычки не владельцем"""

        self.client.force_authenticate(user=self.user)
        url = reverse("habits:detail", args=(self.useful_habit_non_publicity.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_habit_update(self):
        """ Тестирование редактирования привычки владельцем"""

        url = reverse("habits:update", args=(self.pleasant_habit.pk,))
        data = {
            "time": timedelta(minutes=13),
            "is_pleasant_habit": True
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('time'),
            '00:13:00'
        )

    def test_habit_update_non_owner(self):
        """ Тестирование редактирования привычки не владельцем"""

        self.client.force_authenticate(user=self.user)
        url = reverse("habits:update", args=(self.pleasant_habit.pk,))
        data = {
            "time": timedelta(minutes=13),
            "is_pleasant_habit": True
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_habit_update_unauthorized(self):
        """ Тестирование редактирования привычки неавторизованным пользователем"""

        self.client.force_authenticate(user=None)
        url = reverse("habits:update", args=(self.pleasant_habit.pk,))
        data = {
            "time": timedelta(minutes=13),
            "is_pleasant_habit": True
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_habit_destroy(self):
        """ Тестирование удаления привычки владельцем"""

        url = reverse("habits:delete", args=(self.pleasant_habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Habit.objects.all().count(),4)

    def test_habit_destroy_non_owner(self):
        """ Тестирование удаления привычки не владельцем"""

        self.client.force_authenticate(user=self.user)
        url = reverse("habits:delete", args=(self.pleasant_habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_habit_destroy_unauthorized(self):
        """ Тестирование удаления привычки неавторизованным пользователем """

        self.client.force_authenticate(user=None)
        url = reverse("habits:delete", args=(self.pleasant_habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_habit_owner_list(self):
        """ Тестирование просмотра списка привычек владельца """

        url = reverse('habits:list-owner')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(data),4)

        self.client.force_authenticate(user=self.user)
        url = reverse('habits:list-owner')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(data),1)

    def test_habit_owner_list_unauthorized(self):
        """ Тестирование просмотра списка привычек неавторизованным пользователем """

        self.client.force_authenticate(user=None)
        url = reverse('habits:list-owner')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_habit_list(self):
        """ Тестирование просмотра списка публичных привычек """

        url = reverse('habits:list')
        response = self.client.get(url)
        data = response.json()
        # print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 2)
        self.assertEqual(data['count'], 2)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
