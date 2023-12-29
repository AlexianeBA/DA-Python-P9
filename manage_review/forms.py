from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ["title", "content", "image"]
        labels = {
            "title": "Titre du ticket",
        }


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    headline = forms.CharField(label="Titre")
    rating = forms.IntegerField(label="Note", min_value=1, max_value=5)
    body = forms.CharField(label="Commentaire")
    ticket = forms.ModelChoiceField(
        queryset=Ticket.objects.all(), label="Ticket", required=False
    )
    image = forms.ImageField(label="Image", required=False)

    class Meta:
        model = Review
        fields = ["ticket", "headline", "rating", "body", "image"]


class NewReviewForm(forms.ModelForm):
    headline = forms.CharField(label="Titre")
    rating = forms.IntegerField(label="Note", min_value=1, max_value=5)
    body = forms.CharField(label="Commentaire")
    image = forms.ImageField(label="Image", required=False)

    class Meta:
        model = Review
        fields = ["headline", "rating", "body", "image"]
