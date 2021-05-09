from django.db import models
from .customer import Customer

class Reward(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    reward_balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.reward_balance)
