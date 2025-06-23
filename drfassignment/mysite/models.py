from django.db import models




class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    telegram_id = models.BigIntegerField()








class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.username


