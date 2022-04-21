from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from contact.models import Contact, PhoneNumber
from .constant import NumberType


def contact_list(request):
    contacts = Contact.objects.all()
    p = Paginator(contacts, 2)
    page = request.GET.get('page', 1)
    page_obj = p.page(page)
    return render(request, 'contact_list.html', {"page_obj": page_obj})


def create_page(request):
    type_number = NumberType.choice()
    return render(request, 'create.html', {'types': type_number})


def create(request):
    name = request.POST.get('contact_name')
    try:
        contact = Contact.objects.get(name=name)
        if not contact:
            raise Exception
    except Exception:
        contact = Contact(name=name)
        contact.save()
    phone_numbur = PhoneNumber(number=request.POST.get('phone_number'), contact=contact, type=request.POST.get('type'))
    phone_numbur.save()
    return redirect('contact:list')


def get(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, "detail.html", {"contact": contact})


def delete_page(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'delete.html', {'contact': contact})


def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact:list')


def add_page(request, contact_id):
    types = NumberType.choice()
    return render(request, 'add.html', {"types": types, "contact_id": contact_id})


def add(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    phone_numbur = PhoneNumber(number=request.POST.get('phone_number'), contact=contact, type=request.POST.get('type'))
    phone_numbur.save()
    return redirect('contact:list')
