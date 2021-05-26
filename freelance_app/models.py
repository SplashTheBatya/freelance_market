from django.db import models
from django.conf import settings
from django.db.models import CASCADE


class Offer(models.Model):
    STATUSES = (
        ("NEW", "Новый"),
        ("IN_PROGRESS", "В процессе"),
        ("DONE", "Выполнен")
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        choices=STATUSES,
        default="NEW",
        max_length=255
    )
    payment = models.PositiveIntegerField()


class Response(models.Model):
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE
    )
    commentary = models.TextField()


class ResponseImage(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)

