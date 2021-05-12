from django.db import models
from .customer import Customer

class Reward(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    reward_balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.reward_balance)

    @staticmethod
    def get_reward_balance(customer_id):
        return Reward.objects.filter(customer=customer_id)

class RewardTable(models.Model):
    minimum_amount = models.IntegerField(null=True,blank=True)
    percentage_discount = models.IntegerField(null=True,blank=True)
    max_discount = models.IntegerField(null=True,blank=True)




