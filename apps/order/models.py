import uuid
from django.db import models


class Weight_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Volume_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Type_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Mode_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=65)
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE, null=True)
    car = models.ForeignKey('autopark.Car', on_delete=models.CASCADE, null=True)
    from_here = models.CharField(max_length=50)
    to_here = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    weight_cargo = models.ForeignKey(Weight_cargo, on_delete=models.CASCADE, null=True)
    volume_cargo = models.ForeignKey(Volume_cargo, on_delete=models.CASCADE, null=True)
    type_cargo = models.ForeignKey(Type_cargo, on_delete=models.CASCADE, null=True)
    mode_cargo = models.ForeignKey(Mode_cargo, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image_1 = models.ImageField(upload_to='OrderImages/', null=True)
    image_2 = models.ImageField(upload_to='OrderImages/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='OrderImages/', null=True, blank=True)

    def __str__(self):
        return self.title
