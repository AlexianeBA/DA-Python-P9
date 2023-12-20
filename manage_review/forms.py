from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'image']
        
class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    
class ReviewForm(forms.ModelForm):
    headline = forms.CharField(label="Titre")
    rating = forms.TypedChoiceField(choices=zip(range(1,6), range(1,6)), coerce=int, widget=forms.CheckboxSelectMultiple, label="Note")
    body = forms.CharField(label="Commentaire")
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body' ]