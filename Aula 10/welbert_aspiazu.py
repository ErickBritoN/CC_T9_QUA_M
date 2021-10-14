# Simulação de fila de banco
ultimo = 10
fila = list(range(1, ultimo+1))
filap = list(range(1, ultimo+1))
while(True):
  print("\nExixtem %d clientes na fila " % len(fila))
  print('Fila atual: ', fila)
  print("\nExistem %d clientes na fila preferencial " % len(filap))
  print('Fila atual: ', filap)
  print('\nDigite \n<F> para adicionar \n<P> adicionar preferencial \n<A> para atender \n<S> para sair')
  op = input('Operação (F,A,S): ')
  if op == 'A': # Atendimento 
    if len(fila) > 0: 
      atendido = fila.pop(0) # Remove o primeiro
      
      print("\nCliente  %d atendido" % atendido)
    else:
      print('Fila vazia, ninguém para atender')  
    if len(filap) > 0:
      atendidop = filap.pop(0) # Remove o primeiro prefirencial
      atendidop = filap.pop(0)
    else:
       print('Fila Preferencial vazia, ninguém para atender') 
  elif op == 'F':
      ultimo += 1 # incrementando a fila (ticket)
      fila.append(ultimo)
  elif op == 'P':
      ultimo += 1 # Incremento a fila preferencial
      filap.append(ultimo)  
  elif op == 'S':
      break
  else:
      print('Operação Inválida. Digite (F, A ou S)')

# O que fazer
# 1 - implementar atendimentos especiais
# 2 - definir alguma regra de atendimento, de forma que não haja prejuízo
# preferencial é uma faixa 100 ->
# [479, 480, 481, 101, 102, 103, 482, 104, 485]