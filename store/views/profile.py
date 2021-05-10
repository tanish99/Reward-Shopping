from django.shortcuts import render, redirect
from django.views import View
# from store.models.profile import Profile
from store.models.customer  import Customer

class ProfileView(View):
    def get(self, request):
        customerid = request.session.get('customer')
        custom= Customer.objects.get(pk=customerid)

        if custom.image == '':
            custom.image = 'uploads/customerimages/defaultimage.jpg'
        data={}
        data['customer']=custom
        return render(request, 'userprofile.html', data)

