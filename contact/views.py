import time

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact, PhoneNumber
from .constant import NumberType
from django.contrib.auth.decorators import login_required, permission_required
from mi.settings import MEDIA_ROOT, join_path


@login_required(redirect_field_name='keyingi')
def contact_list(request):
    contacts = Contact.objects.filter(created_by=request.user)
    p = Paginator(contacts, 2)
    page = request.GET.get('page', 1)
    page_obj = p.page(page)
    return render(request, 'contact_list.html', {"page_obj": page_obj})


@login_required()
def create_page(request):
    type_number = NumberType.choice()
    return render(request, 'create.html', {'types': type_number})


@login_required()
def create(request):
    name = request.POST.get('contact_name')
    try:
        contact = Contact.objects.get(name=name, created_by=request.user)
        if not contact:
            raise Exception
    except Exception:
        contact = Contact(name=name, created_by=request.user)
        contact.save()
    phone_numbur = PhoneNumber(number=request.POST.get('phone_number'), type=request.POST.get('type'), contact=contact)
    phone_numbur.save()
    return redirect('contact:list')


@login_required()
def get(request, contact_id):
    # first idea

    # try:
    #     contact = Contact.objects.get(id=contact_id)
    #     return render(request, "detail.html", {"contact": contact})
    # except Exception as e:
    #     messages.error(request, f"Not Found: {e}", extra_tags='danger')
    #     return redirect('contact:list')

    # second idea

    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, "detail.html", {"contact": contact})


@login_required()
def delete_page(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'delete.html', {'contact': contact})


@login_required()
def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact:list')


@login_required()
def add_page(request, contact_id):
    types = NumberType.choice()
    return render(request, 'add.html', {"types": types, "contact_id": contact_id})


@login_required()
def add(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    phone_numbur = PhoneNumber(number=request.POST.get('phone_number'), contact=contact, type=request.POST.get('type'))
    phone_numbur.save()
    return redirect('contact:list')


@login_required
@permission_required('contact.view_phonenumber', raise_exception=True)
def admin(request):
    # user_current = request.user
    # if not user_current.has_perm(perm='contact.view_phonenumber', obj=PhoneNumber):
    #     return HttpResponseForbidden('mumkin emas')
    return HttpResponse('This is admin page')


def upload_page(request):
    return render(request, 'upload.html', {})


def upload(request):
    file = request.FILES['file_name']
    write_file(file)
    return redirect('home')


def write_file(f):
    new_name = gen_new_name(f.name)
    for chunk in f.chunks():
        with open(join_path(MEDIA_ROOT, "uploads", new_name), mode='wb+') as file:
            file.write(chunk)


def gen_new_name(name: str):
    ext = name.split('.')[-1]
    return '%s,%s' % (time.time_ns(), ext)
