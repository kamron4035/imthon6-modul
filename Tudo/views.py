from django.shortcuts import render
from forms import TudoForm


def create_view(request):
	context = {}
	form = TudoForm(request.POST or None)
	if form.is_valid():
		form.save()
	context['form'] = form
	return render(request, "home.html", context)