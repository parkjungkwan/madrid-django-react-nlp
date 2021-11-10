from django.db import models

class Customer(models.Model):
    use_in_migrations = True
    id = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    city = models.TextField()
    state = models.TextField()
    address = models.TextField()
    date_of_birth = models.DateField()

    class Meta:
        db_table = "customers"

    def __str__(self):
        return f'[{self.pk}] {self.id}'