from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
import json

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/contact_list.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        else:
            errors_json = json.dumps(form.errors.get_json_data())
            return render(request, 'myapp/contact_form.html', {'form': form, 'errors_json': errors_json})
    else:
        form = ContactForm()
    return render(request, 'myapp/contact_form.html', {'form': form})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'myapp/contact_detail.html', {'contact': contact})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
        else:
            errors_json = json.dumps(form.errors.get_json_data())
            return render(request, 'myapp/update_contact_form.html', {'form': form, 'errors_json': errors_json})
    else:
        form = ContactForm(instance=contact)
    return render(request, 'myapp/update_contact_form.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'myapp/contact_confirm_delete.html', {'contact': contact})
