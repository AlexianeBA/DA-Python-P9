from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket

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
            return render(request, "login.html", context)
    else:
        form = TicketForm()
        context["form"] = form
        return render(request, "creation_ticket.html", context)


def ticket_list(request):
    ticket = Ticket.objects.all()
    context = {"tickets": ticket}
    return render(request, "ticket_list.html", context)


def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")

    return render(request, "delete_ticket.html", {"ticket": ticket})
