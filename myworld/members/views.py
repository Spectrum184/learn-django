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

    print(f"first name {first_name}, last name {last_name}")

    member = Members(first_name=first_name, last_name=last_name)
    member.save()

    return HttpResponseRedirect(reverse('index'))
