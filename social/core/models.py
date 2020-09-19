from django.db import models


class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=40)
	senha = models.CharField(max_length=40)
	data_nascimento = models.DateField()


class Perfil(models.Model):
	nome = models.CharField(max_length=60)
	usuario = models.ForeignKey('Usuario', 
		related_name = 'perfil', 
		on_delete=models.CASCADE)
	contatos = models.ManyToManyField('self')


class Postagem(models.Model):
	texto = models.CharField(max_length=140)
	data_hora_postagem = models.DateTimeField(auto_now_add=True)
	perfil = models.ForeignKey('Perfil', 
		related_name = 'postagem', 
		on_delete=models.CASCADE)


class Comentario(models.Model):
	texto = models.CharField(max_length=60)
	data_hora_comentario = models.DateTimeField(auto_now_add=True)
	postagem = models.ForeignKey('Postagem', 
		related_name = 'comentario', 
		on_delete=models.CASCADE)


class TipoReacao(models.Model):
	tipo = models.CharField(max_length=20)


class Reacao(models.Model):
	data_hora_reacao = models.DateTimeField(auto_now_add=True)
	peso = models.IntegerField(default=1)
	perfil = models.ForeignKey('Perfil', 
		related_name = 'reacao', 
		on_delete=models.CASCADE)
	tipo = models.ForeignKey('TipoReacao', 
		related_name = 'reacao',
		on_delete=models.CASCADE)
	postagem = models.ForeignKey('Postagem', 
		related_name = 'reacao', 
		on_delete=models.CASCADE)
