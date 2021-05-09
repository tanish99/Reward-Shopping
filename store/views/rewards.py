from django.shortcuts import render, redirect
from django.views import View
from store.models.reward import Reward
from store.models.customer import Customer
class RewardView(View):
    def get(self, request):
        customer = request.session.get('customer')
        print(customer)
        reward_point = Reward.objects.filter(customer_id=customer)
        for balance in reward_point:
            print("reward view ",balance)
        return render(request, 'rewards.html',{'points':0})