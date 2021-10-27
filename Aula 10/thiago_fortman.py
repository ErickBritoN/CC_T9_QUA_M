# -*- coding: utf-8 -*-
"""Exercicio_filas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qTxHKqH1atmcQLztYQgNaSJGHH9mWjx0
"""

#ex filas
ultimo = 10
vp = 3
pref = 1
fila=list(range(1,ultimo+1))
fpref=list(range(3,pref+3))
while( True):
  print('Fila Atual: ', fila)
  print('Fila Preferencial Atual: ', fpref)
  print('Digite <F> para adicionar \n<A> para atender \n<S> para sair \n<P> para preferencial')
  op = input('operação (F, A, S ou P): ')
  if op == 'A':
    if len(fila) > 0:
      if fpref[0]==fila[0]:
        atendido = fpref.pop(0)
        print("Cliente Atendido %d atendido" % atendido)
      else:  
        atendido = fila.pop(0)
        print("Cliente Atendido %d atendido" % atendido)
    else:
      print('Fila Vazia, ninguem para atender')
  elif op == 'F':
    ultimo += 1 #incrementando a fila
    fila.append(ultimo)
  elif op == 'P':
    vp += 3
    fpref.append(vp)
  elif op == 'S':
    break
  else:
    print('Operação invalida. Digite (F, A, P ou S)')