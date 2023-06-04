from django.db import models
from django.urls import reverse

USAGE = (
    ('W', 'Walk'),
    ('S', 'Sport'),
    ('O', 'Office'),
)

# Create your models here.
class Sock(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('socks_details', kwargs={'pk': self.id})


class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    # Changing this instance method
    # does not impact the database, therefore
    # no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})
    
class Worn(models.Model):
    date = models.DateField('date worn')
    usage = models.CharField(
        max_length=1,
        choices=USAGE,
        default=USAGE[0][0]
    )
    # Create a sneaker_id FK
    sneaker = models.ForeignKey(
        Sneaker,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_usage_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

