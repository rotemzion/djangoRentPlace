from django.contrib.auth.models import User
from django.db import models


class UserP(models.Model):
    first_name = models.CharField(null=True, max_length=30, blank=True)
    last_name = models.CharField(null=True, max_length=30, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.RESTRICT, related_name='user_name')
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(null=True, max_length=30, blank=True)
    type = models.CharField(choices=[('Private', 'private'), ('Public', 'public')], max_length=20)

    class Meta:
        db_table = 'UserP'

    def __str__(self):
        return f'{self.user.username, self.first_name,self.last_name}'


class ItemLocation(models.Model):
    item_name = models.CharField(null=False, max_length=50, blank=True)
    num_people = models.IntegerField(null=False, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.RESTRICT, blank=True)
    city = models.CharField(null=False, max_length=60, blank=True)
    picture_location = models.FileField(upload_to='img/', null=True, blank=True)

    class Meta:
        db_table = 'ItemLocation'

    def __str__(self):
        return f'{self.item_name, self.num_people,self.city}'


class Renters(models.Model):
    id_User = models.ForeignKey(UserP, on_delete=models.RESTRICT)
    id_Place = models.ForeignKey(ItemLocation, on_delete=models.RESTRICT)
    start_date = models.DateTimeField(null=False, blank=True)
    end_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        db_table = 'Renters'

    def __str__(self):
        return f'{self.start_date, self.end_date}'
