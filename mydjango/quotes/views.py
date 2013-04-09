# Create your views here.
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from quotes.models import Quotes

class QuotesForm(forms.Form):
	quotes = forms.CharField(widget = forms.Textarea(attrs={'size': 20, 'title': 'Your name','cols':70}))



def index(request):
	
	model_obj = Quotes()
	if request.method == 'POST':

		form = QuotesForm(request.POST)
		if form.is_valid():
                        quote_text = form.cleaned_data['quotes']
                        model_obj.quote = quote_text
                        model_obj.save()
			print "OK"

		return HttpResponse("thanks")
	else:
		form = QuotesForm()


	return render(request, 'home_page.html', {'form': form,})
	
