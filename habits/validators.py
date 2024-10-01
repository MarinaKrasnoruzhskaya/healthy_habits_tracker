from rest_framework.exceptions import ValidationError


class UsefulHabitValidator:
    """ Валидация для полезной привычки """

    def __init__(self, associated_habit, reward, is_pleasant_habit):
        self.associated_habit = associated_habit
        self.reward = reward
        self.is_pleasant_habit = is_pleasant_habit

    def __call__(self, value):
        associated_habit = dict(value).get(self.associated_habit)
        reward = dict(value).get(self.reward)
        is_pleasant_habit = dict(value).get(self.is_pleasant_habit)

        if not is_pleasant_habit:
            if associated_habit and reward:
                raise ValidationError('Нельзя одновременно выбирать связанную привычку и указывать вознаграждение')
            if not associated_habit and not reward:
                raise ValidationError('Полезная привычка должна содержать приятную привычку или вознаграждение')

            if associated_habit:
                if not associated_habit.is_pleasant_habit:
                    raise ValidationError('Cвязанной привычкой может быть только привычка с признаком приятной привычки')


class PleasantHabitValidator:
    """ Валидация для приятной привычки """

    def __init__(self, is_pleasant_habit, associated_habit, reward):
        self.is_pleasant_habit = is_pleasant_habit
        self.associated_habit = associated_habit
        self.reward = reward

    def __call__(self, value):
        is_pleasant_habit = dict(value).get(self.is_pleasant_habit)
        associated_habit = dict(value).get(self.associated_habit)
        reward = dict(value).get(self.reward)

        if is_pleasant_habit:
            if associated_habit:
                raise ValidationError('У приятной привычки не может быть связанной привычки')
            if reward:
                raise ValidationError('У приятной привычки не может быть указано вознаграждение')


class LeadTime:
    """ Валидация для времени выполнения привычки """

    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        time_to_complete = dict(value).get(self.time_to_complete)

        if time_to_complete:
            if time_to_complete < 1:
                raise ValidationError('Время выполнения привычки должно быть положительным числом')
            elif time_to_complete > 120:
                raise ValidationError('Время выполнения привычки не может превышать 120 минут')
