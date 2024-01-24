import datetime

from django.db import models

# modelos de dados da aplicação para SGBD relacional (Vide documentação)

class Pergunta( models.Model ):

    texto   = models.CharField( max_length=200 )
    date    = models.DateTimeField( "data da publicação" )

    def help(self):
        print('campos: {texto:str, date:datetime}')

    # Pergunta.objects.all() interactive prompt
    def __str__(self):
        return f'texto: {self.texto}, date: {self.date}'

    def perguntado_recentemente(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

class Escolha( models.Model ):

    pergunta    = models.ForeignKey( Pergunta, on_delete=models.CASCADE )
    texto       = models.CharField( max_length=200 )
    votes       = models.IntegerField( default=0 )

    def help(self):
        print('campos: {pergunta:FK, texto:str, votes:int}')

    def __str__(self):
        return f'pergunta: {self.pergunta}, texto: {self.texto}, votes: {self.votes}'
