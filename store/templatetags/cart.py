from django import template
from store.models.reward import Reward,RewardTable


register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_quantity(product , cart)



@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum=0
    for p in products:
        sum += price_total(p , cart)

    return sum

@register.filter(name='total_reward_used')
def total_reward_used(products , cart):
    max_per_discount = 0
    max_discount = 0
    discount = 0
    balance =0
    r_balance=Reward.objects.all()
    for total in r_balance:
        balance = int(balance) + int(str(total))
    if balance > 0:
        tcp=total_cart_price(products,cart)
        print(tcp)
        table=RewardTable.objects.all()

        for i in table:
            print(i.minimum_amount," - ",tcp)
            if(i.minimum_amount>tcp):

                max_per_discount =  i.percentage_discount
                max_discount =i.max_discount
                break

        try:
            discount=(tcp*max_per_discount)/100
        except:
            print("hello")
        if(discount>max_discount):
            discount=max_discount


    return max_per_discount,discount

@register.filter(name='final_price')
def final_price(products,cart):
    tcp = total_cart_price(products, cart)
    max_per_discount,discount=total_reward_used(products, cart)
    print(tcp-discount)
    return tcp-discount


