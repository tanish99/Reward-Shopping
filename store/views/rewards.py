from django.shortcuts import render, redirect
from django.views import View
from store.models.reward import Reward,RewardTable
from store.models.customer import Customer
class RewardView(View):
    def get(self, request):
        data={}
        customer = request.session.get('customer')
        print(customer)
        reward_point = Reward.objects.filter(customer_id=customer)
        balance = 0
        for total in reward_point:
            balance = int(balance) + int(str(total))

        print("bal" ,balance)
        reward_table=RewardTable.objects.all()

        data={}
        data['balance'] = balance
        print(data['balance'])
        data['table'] = reward_table
        print(data['table'])
        lis=[]

        len1=len(reward_point)

        for i in range(len1):
            lis.append(reward_point[i].reward_balance)
        print(lis)
        data['reward_log']=lis
        print(data['reward_log'])

        return render(request, 'rewards.html',data)


