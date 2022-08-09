from django.shortcuts import render, redirect
from . models import StorePass

import rsa


# Create your views here.



def index(request):

   
    
    al = StorePass.objects.all()



  
    context = {
        'all': al
        ,

    }

    return render(request, 'index.html', context)


def entry(request):

    publicKey, privateKey = rsa.newkeys(512)


    if request.method == 'POST':
        user = request.POST['user']
        website = request.POST['website']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        if password == conf_password :

            encrypt_pass = rsa.encrypt(password.encode(),
                         publicKey)
            StorePass.objects.create(
                user=user,
                website=website,
                gmail= email,
                password=encrypt_pass
            )
            return redirect('index')
            
    # decMessage = rsa.decrypt(encMessage, privateKey).decode()dir

    return render(request,'entry.html')