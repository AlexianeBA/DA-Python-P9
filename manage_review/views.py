from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, DeleteTicketForm, ReviewForm
from .models import Ticket, Review
from itertools import chain
from operator import attrgetter


# Create your views here.


def creation_ticket(request):
    context = {}
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket_instance = form.save(commit=False)
            user = request.user
            ticket_instance.user = user
            ticket_instance.uploader = user
            ticket_instance.save()
            context["username"] = user.username
            return redirect('flux')
    else:
        form = TicketForm()
        context["form"] = form
        return render(request, "creation_ticket.html", context)


def ticket_list(request):
    ticket = Ticket.objects.all()
    context = {"tickets": ticket}
    return render(request, "ticket_list.html", context)

def flux(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    reviews = Review.objects.all().order_by('-time_created')
    return render(request, "flux.html", {'tickets': tickets, 'reviews': reviews})

def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()
    if request.method == 'POST':
        edit_form = TicketForm(request.POST, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('')
        if 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('login')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'edit_ticket.html', context=context)
    

    
def create_review(request):
    context = {}
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            review_instance = review_form.save(commit=False)
            user = request.user
            ticket_id = ticket_form.cleaned_data['ticket_id']
            ticket_instance = Ticket.objects.get(pk=ticket_id)
            review_instance.ticket = ticket_instance
            review_instance.user = user
            review_instance.save()
            context["username"] = user.username
            return redirect('flux')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    context["ticket_form"] = ticket_form
    context["review_form"] = review_form
    return render(request, "create_review.html", context)
