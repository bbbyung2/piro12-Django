from django.db import models

# Create your models here.
from mysite import settings


class Item(models.Model):
    name = models.CharField(max_length=100, validators=[])
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return '<{}> {}'.format(self.pk, self.name)
        return f'<{self.pk}> {self.name}'
