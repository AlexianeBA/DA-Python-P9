from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    TicketForm,
    DeleteTicketForm,
    ReviewForm,
    NewReviewForm,
    DeleteReviewForm,
)
from .models import Ticket, Review
from manage_user.models import UserFollows
from itertools import chain
from operator import attrgetter
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
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
            return redirect("flux")
    else:
        form = TicketForm()
        context["form"] = form
        return render(request, "creation_ticket.html", context)


def ticket_list(request):
    if request.user.is_authenticated:
        user_tickets = Ticket.objects.filter(user=request.user)
        context = {"tickets": user_tickets}
        return render(request, "ticket_list.html", context)
    else:
        return render(request, "flux")


def flux(request):
    following_users = UserFollows.objects.filter(user=request.user).values_list(
        "followed_user", flat=True
    )
    tickets = Ticket.objects.filter(
        user__in=[request.user] + list(following_users)
    ).order_by("-created_at")
    reviews = Review.objects.filter(
        user__in=[request.user] + list(following_users)
    ).order_by("-time_created")

    return render(request, "flux.html", {"tickets": tickets, "reviews": reviews})


def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()
    if request.method == "POST":
        edit_form = TicketForm(request.POST, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("flux")
        if "delete_ticket" in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("flux")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "edit_ticket.html", context=context)


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    edit_form = ReviewForm(instance=review)
    delete_form = DeleteReviewForm()
    if request.method == "POST":
        edit_form = TicketForm(request.POST, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("")
        if "delete_review" in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect("login")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "edit_review.html", context=context)


def create_review(request, ticket_id=None):
    context = {}

    ticket = get_object_or_404(Ticket, id=ticket_id) if ticket_id else None

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_instance = form.save(commit=False)
            user = request.user
            review_instance.user = user
            if ticket:
                review_instance.ticket = ticket
            review_instance.save()
            context["username"] = user.username
            return redirect("flux")
    else:
        form_initial = {"ticket": ticket} if ticket else {}
        form = ReviewForm(initial=form_initial)

    form.fields["ticket"].queryset = Ticket.objects.all()

    context["form"] = form
    return render(request, "create_review.html", context)


def create_new_review(request):
    context = {}

    if request.method == "POST":
        form = NewReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_instance = form.save(commit=False)
            user = request.user
            review_instance.user = user
            review_instance.save()
            context["username"] = user.username
            return redirect("flux")
    else:
        form = NewReviewForm()

    context["form"] = form
    return render(request, "create_new_review.html", context)


def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")
    return render(request, "delete_ticket.html", {"ticket": ticket})


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        review.delete()
        return redirect("flux")
    return render(request, "delete_review.html", {"review": review})
