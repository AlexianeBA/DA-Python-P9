from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
# Create your views here.

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.uploader = request.user
            new_ticket.save()
            return redirect('posts')  
    return render(request, 'create_ticket.html', content={'form': form})

def posts(request):
    ticket = Ticket.objects.all()
    print(f"Number of tickets: {ticket.count()}")
    return render(request, 'posts.html', context={'tickets': ticket})

