from django.shortcuts import render,redirect
from .models import customer,transfer_history
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request ,'indexnew.html')


def cust(request):
    custinfo = customer.objects.all()
    return render(request ,'viewcust.html',{'custinfo':custinfo})


def trans(request):
    alltransaction = transfer_history.objects.all()
    return render(request ,'transaction.html',{'tran':alltransaction})




def profile(request,id):
    if request.method == "POST":
        sender = request.POST['sender']
        senderaccno = request.POST['senderaccno']
        receiver = request.POST['receiver']
        receiveraccno= request.POST['receiveraccno']
        amountdep = request.POST['amount']


        real=customer.objects.filter(Q(name=receiver) & Q(accno=receiveraccno))
        if real.exists():
            send=customer.objects.filter(accno=senderaccno)
            for i in send:
                sendbal=i.accbal
            for j in real:
                recbal=j.accbal
            if(sender==receiver and int(senderaccno)==int(receiveraccno)):
                messages.add_message(request, messages.ERROR, 'Account no is same for both sender and receiver..Try Different Account!!')
                post = customer.objects.filter(id=id)
                return render(request, 'profilenew.html', {'prof': post})


            if(sendbal>=int(amountdep)):
                a = customer.objects.get(accno=senderaccno)
                a.accbal = sendbal-int(amountdep)
                a.save()

                b = customer.objects.get(accno=receiveraccno)
                b.accbal = recbal+int(amountdep)

                b.save()

                tranfer=transfer_history(sender=sender,receiver=receiver,amount=amountdep,senderaccno=senderaccno,receiveraccno=receiveraccno)
                tranfer.save()
                messages.success(request, "Money has been Sent !!")


            else:
                messages.add_message(request, messages.ERROR, 'Insufficient Balance!!')









        else:
            messages.add_message(request, messages.ERROR, 'Please Check Receiver Name and Account No')










    post = customer.objects.filter(id=id)
    return render(request ,'profilenew.html',{'prof':post})



