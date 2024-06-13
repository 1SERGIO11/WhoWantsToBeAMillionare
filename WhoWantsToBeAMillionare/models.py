from django.db import models


class Questions(models.Model):
    question = models.TextField(blank=True)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    right_answer = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"Вопрос: {self.question}. Правильный ответ: {self.right_answer}"


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_level = models.IntegerField(default=1)
    max_level_reached = models.IntegerField(default=1)
    stopped_question = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True, blank=True)
    prize_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Hint(models.Model):
    user = models.ForeignKey(User, related_name='used_hints', on_delete=models.CASCADE)
    hint_type = models.CharField(max_length=100, choices=[
        ('audience', 'Помощь зала'),
        ('fifty_fifty', '50 на 50'),
        ('call_a_friend', 'Звонок другу'),
        ('second_chance', 'Право на ошибку'),
        ('change_question', 'Замена вопроса')
    ])
    used = models.BooleanField(default=False)
    question_level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.hint_type} (Used: {'Yes' if self.used else 'No'})"
