from django.shortcuts import render

# Usando no examplo
from django.http import HttpResponseRedirect
from .forms import PeriodoForm, NameForm

# Usado nos testes
from django.http import HttpResponse
import pendulum
pendulum.set_locale('pt-br')
from tempfile import NamedTemporaryFile
from openpyxl import Workbook

def excel(request):
	wb = Workbook()
	with NamedTemporaryFile() as tmp:
		wb.save(tmp.name)
		tmp.seek(0)
		stream = tmp.read()
	return HttpResponse()

def get_name(request):
	lista = []
	today = pendulum.today('America/Sao_Paulo')
	mes = today.month
	ano = today.year
	#vai = str(mes)+","+str(ano)
	today = pendulum.today('America/Sao_Paulo').subtract(months=1)
	vai = str(today.month)+","+str(today.year)
	foi = today.format('MMMM').capitalize()+" - "+str(ano)
	#date = pendulum.date(ano, mes, dia)
	mes_passado = pendulum.today('America/Sao_Paulo').subtract(months=1)
	lista.append([vai, foi])
	x = 0
	while x <= 2:
		today = pendulum.today('America/Sao_Paulo').add(months=x)
		lista.append([
	 		str(today.month)+","+str(today.year), #vai
			today.format('MMMM').capitalize()+" - "+str(today.year) #foi
		])
		x += 1
	context = {
		
		"vum" : lista[0][0],
		"tum" : lista[0][1],
		"vdois": lista[1][0],
		"tdois": lista[1][1],
		"vtres": lista[2][0],
		"ttres": lista[2][1],
		"vquatro": lista[3][0],
		"tquatro": lista[3][1]
	}
	#vum = lista[0][0]
	#tum = lista[0][1]

	return render(request, "name.html", context)

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


# def login_view(request):
#     if(request.POST):
#         login_data = request.POST.dict()
#         username = login_data.get("username")
#         password = login_data.get("password")
#         user_type = login_data.get("user_type")
#         print(user_type, username, password)
#         return HttpResponse("This is a post request")
#     else:
#         return render(request, "base.html")


# def detail(request, question_id):
# try:
# question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
# raise Http404("Question does not exist")
# return render(request, 'polls/detail.html', {'question': question})