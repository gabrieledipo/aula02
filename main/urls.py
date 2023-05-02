    # def somar(x,y,z):
    #     soma = x+y+z
    #     print(soma)
    
    # somar(5,10,15) #isso é uma chamada de função

from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
]