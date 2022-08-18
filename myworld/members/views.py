from re import template
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members


def index(request):
    template = loader.get_template('members.html')
    my_members = Members.objects.all().values()

    context = {
        "members": my_members
    }

    return HttpResponse(template.render(context, request))


def add_member(request):
    template = loader.get_template('add-member.html')

    return HttpResponse(template.render({}, request))


def create_member(request):
    first_name = request.POST['first']
    last_name = request.POST['last']

    member = Members(first_name=first_name, last_name=last_name)
    member.save()

    return HttpResponseRedirect(reverse('index'))

def delete_member(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    
    return HttpResponseRedirect(reverse('index'))
def update_member(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('update-member.html')
    context = {
        "member" : member
    }
    
    return HttpResponse(template.render(context, request))

def save_member(request, id):
    first_name = request.POST["first"]
    last_name = request.POST["last"]
    
    member = Members.objects.get(id=id)
    member.first_name = first_name
    member.last_name = last_name
    member.save()
    
    return HttpResponseRedirect(reverse("index"))