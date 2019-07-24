from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DataForm, NodeForm
from .models import Block, Blockchain, Node
import json
from hashlib import sha256
import requests
from django.views.decorators.csrf import csrf_exempt
from .serializers import Blockserializer


# Create your views here.
def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


def index(request):
    return render(request, "bchain/admin_option.html")


def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            r = Block()
            r.amount = request.POST['amount']
            r.location = request.POST['location']
            r.buyer = request.POST['buyer']
            r.seller = request.POST['seller']
            x = Blockchain.objects.all()
            # #y = x[-1]
            # #print(y)
            if Enquiry(x) == 1:
                temp_size = len(x)
                # x = Blockchain.objects.get().reverse()[0]
                # y = x.reverse()[0]
                # y =x.objects.get(pk=temp_size)
                y = Blockchain.objects.last()
                print(y.hash)
                r.prev_hash = y.hash

            st = r.__dict__
            state = st['_state']
            del st['_state']
            # print(r.__dict__)
            rec = json.dumps(st, sort_keys=True)
            r.hash = sha256(rec.encode()).hexdigest()
            r._state = state
            r.save()
            b = Blockchain()
            # print(r.id)
            b.amount = r.amount
            b.location = r.location
            b.buyer = r.buyer
            b.seller = r.seller
            b.prev_hash = r.prev_hash
            b.hash = r.hash
            # b.id = 1
            b.save()
            announce_block( b)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:


            return render(request, 'bchain/option.html')
            # return render(request, 'bchain/announce.html')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()
        return render(request, 'bchain/data.html', {'form': form})


def show_data(request):
    # records = Block['record'][:-1]
    # Need to make sure that the dictionary is ordered. Otherwise we'll get a different hash
    # block_elements = ['amount', 'location', 'buyer','seller']
    # records = [OrderedDict((k, record[k]) for k in block_elements) for record in records]


    '''if request.method == 'GET':

        z = Block.objects.all()
        # print(Block.objects.all()[1])
        while Block.objects.all()[i] is not None:

            serializer = Blockserializer(z, many=True)
            i+=1
            print(serializer.data)
        return HttpResponse(serializer.data)'''
    # form = DataForm(request.GET)
    z = Blockchain.objects.all()
    # y=z.objects.all()
    context = {"blocks": z}
    print(len(z))
    # i in z:
    # print("amount",i.block.amount)
    # print(y.prev_hash)
    print(type(z))
    return render(request, 'bchain/view_record.html', {'z': z})
    ##z=Blockchain.objects.all()
    # serializer=Blockserializer(z,many=True)
    # return HttpResponse(serializer.data)


def show_nodes(request):
    k = Node.objects.all()
    if Enquiry(k) == 0:
        return HttpResponse("No a single node")

    return render(request, 'bchain/view_node.html', {'k': k})


def announce_block(block):
    nodes = Node.objects.all()
    st = block.__dict__
    state = st['_state']
    del st['_state']
    for node in nodes:
        if node.url != '127.0.0.1:8000':
            URL = "http://{}/bchain/receiveblock/".format(node.url)
            r = requests.post(url=URL, data=json.dumps(st, sort_keys=True))
        # requests.post(URL, data={'345': '678'})
        # return HttpResponse("Data announced")


@csrf_exempt
def receive_block(request):
    if request.method == 'POST':
        print('hello')
        # block_data=request.POST["Block"]
        # block_data = json.loads(request.POST.get('prev_hash'))
        block_unicode = request.body.decode('utf-8')
        body = json.loads(block_unicode)
        block_data = body
        print("Check", block_data)
        print(block_data['prev_hash'])
        # return HttpResponse(block_data)
        # block = Block(block_data["amount"],block_data["location"],block_data["buyer"],block_data["seller"],
        #            block_data["prev_hash"],block_data["hash"])
        blkch = Blockchain()
        l = Blockchain.objects.all()
        if Enquiry(l) == 1:
            b_last = Blockchain.objects.last()
            if block_data['prev_hash'] != b_last.hash:
                return HttpResponse("Not a valid block.Check the previous hash")
            blkch.amount = block_data['amount']
            blkch.location = block_data['location']
            blkch.buyer = block_data['buyer']
            blkch.seller = block_data['seller']
            blkch.prev_hash = block_data['prev_hash']
            blkch.hash = block_data['hash']
            blkch.save()
            return render(request, 'bchain/receive.html')
        else:
            if block_data != '00':
                return HttpResponse("Not a valid block.Check the previous hash")
            blkch.amount = block_data['amount']
            blkch.location = block_data['location']
            blkch.buyer = block_data['buyer']
            blkch.seller = block_data['seller']
            blkch.prev_hash = block_data['prev_hash']
            blkch.hash = block_data['hash']
            blkch.save()
            return render(request, 'bchain/receive.html')
    return render(request, 'bchain/receive.html')

        # if request.method=='POST':


def register_nodes(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)

        if form.is_valid():
            n = Node()
            n.url = request.POST['url']
            n.save()
            return render(request, 'bchain/nodeoption.html')


    else:
        form = NodeForm()
        return render(request, 'bchain/node.html', {'form': form})
