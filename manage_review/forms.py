from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ["title", "content", "image"]
        labels = {"title": "Titre du ticket", "content": "Description"}


class EditTicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ["title", "content"]
        labels = {"title": "Titre du ticket", "content": "Description"}


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    title = forms.CharField(label="Titre de la critique")
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    headline = forms.CharField(label="Titre")
    rating = forms.IntegerField(label="Note", min_value=1, max_value=5)
    commentary = forms.CharField(label="Commentaire")
    ticket = forms.ModelChoiceField(
        queryset=Ticket.objects.all(),
        label="Ticket",
        required=False,
        widget=forms.HiddenInput(attrs={"disabled": "disabled"}),
    )
    image = forms.ImageField(label="Image de la critique", required=False)
    content = forms.CharField(label="Description")

    class Meta:
        model = Review
        fields = [
            "ticket",
            "headline",
            "rating",
            "commentary",
            "title",
            "image",
            "content",
        ]


# class NewReviewForm(forms.ModelForm):
#     title = forms.CharField(label="Titre du ticket")
#     content = forms.CharField(label="Description")
#     image = forms.ImageField(label="Image du ticket", required=False)
#     headline = forms.CharField(label="Titre")
#     rating = forms.IntegerField(label="Note", min_value=1, max_value=5)
#     body = forms.CharField(label="Commentaire")

#     class Meta:
#         model = Review
#         fields = ["title", "content", "image", "headline", "rating", "body"]
