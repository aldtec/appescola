from django import forms

import pendulum
pendulum.set_locale('pt-br')

STATES = [
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
]

LISTAGEM = []
today = pendulum.today('America/Sao_Paulo')
mes = today.month
ano = today.year
#vai = str(mes)+","+str(ano)
today = pendulum.today('America/Sao_Paulo').subtract(months=1)
vai = str(today.month)+","+str(today.year)
foi = today.format('MMMM').capitalize()+" - "+str(ano)
#date = pendulum.date(ano, mes, dia)
mes_passado = pendulum.today('America/Sao_Paulo').subtract(months=1)
LISTAGEM.append([vai, foi])
x = 0
while x <= 2:
	today = pendulum.today('America/Sao_Paulo').add(months=x)
	LISTAGEM.append([
 		str(today.month)+","+str(today.year), #vai
		today.format('MMMM').capitalize()+" - "+str(today.year) #foi
	])
	x += 1

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	periodo = forms.ChoiceField(choices=LISTAGEM)

	def __init__(self, *args, **kwargs):
		super(NameForm, self).__init__(*args, **kwargs)
		self.initial['periodo'] = LISTAGEM[2]


class PeriodoForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	periodo = forms.ChoiceField(choices=LISTAGEM)

	def __init__(self, *args, **kwargs):
		super(NameForm, self).__init__(*args, **kwargs)
		self.initial['periodo'] = LISTAGEM[2]