from django.shortcuts import render

# Usando no examplo
from django.http import HttpResponseRedirect
from .forms import NameForm

# Usado nos testes
from django.http import HttpResponse
import pendulum
pendulum.set_locale('pt-br')

def come(request):
	listagem = []
	today = pendulum.today('America/Sao_Paulo')
	mes = today.month
	ano = today.year
	#vai = str(mes)+","+str(ano)
	today = pendulum.today('America/Sao_Paulo').subtract(months=1)
	vai = str(today.month)+","+str(today.year)
	foi = today.format('MMMM').capitalize()+" - "+str(ano)
	#date = pendulum.date(ano, mes, dia)
	mes_passado = pendulum.today('America/Sao_Paulo').add(months=12)
	listagem.append([vai, foi])
	x = 0
	while x <= 2:
		today = pendulum.today('America/Sao_Paulo').add(months=x)
		listagem.append([
	 		str(today.month)+","+str(today.year), #vai
			today.format('MMMM').capitalize()+" - "+str(today.year) #foi
		])
		x += 1
	return HttpResponse(mes_passado)


def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
	return render(request, 'name.html', {'form': form})
