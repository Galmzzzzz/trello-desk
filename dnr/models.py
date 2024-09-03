from django.db import models

from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процессе'),
        ('ready_for_delivery', 'Готов для доставки'),
        ('in_transit', 'В пути'),
        ('completed', 'Завершен'),
    ]

    client = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='in_progress')

    class Meta:
        ordering = ['time']
        indexes = [
            models.Index(fields=['time']),
        ]

    def __str__(self):
        return f'Order {self.id}'
