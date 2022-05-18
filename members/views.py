from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member


def index(request):
    members = Member.objects.all().values()
    template = loader.get_template("index.html")
    context = {"members": members}

    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))


def add_record(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    member = Member(first_name=first_name, last_name=last_name)
    member.save()

    return HttpResponseRedirect(reverse("index"))


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse("index"))


def update(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        "member": member,
    }
    return HttpResponse(template.render(context, request))


def update_record(request, id):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    member = Member.objects.get(id=id)
    member.first_name = first_name
    member.last_name = last_name
    member.save()
    return HttpResponseRedirect(reverse("index"))


def testing(request):
    members = Member.objects.all()
    template = loader.get_template("template.html")
    context = {
        "members": members,
    }

    return HttpResponse(template.render(context, request))
