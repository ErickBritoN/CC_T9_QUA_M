class Farol:
    def __init__(self, proportion: int):
        self.count = 0
        self.proportion = proportion

    def select(self, fn: list, fv: list):
        if ((len(fv) == 0) or (self.count // self.proportion) >= 1) and (len(fn) != 0):
            self.count = 0
            return fn

        self.count += 1
        return fv


# Simulação de fila de banco
ultimo = 10
fila_normal = []
fila_vip = []
farol = Farol(2)

while True:
    print(f"\nFila normal: {len(fila_normal)}\nFila V.I.P.: {len(fila_vip)}\nTotal: {len(fila_normal) + len(fila_vip)}")
    print('Digite\n<FN> para adicionar cliente normal\n<FV> para adicionar cliente V.I.P.\n<A> para atender\n<S> para sair')

    op = input('Operação (FN, FV, A, S): ').upper()

    if op == 'A': # atendimento
        selected_queue = farol.select(fila_normal, fila_vip)
        if len(selected_queue) > 0:
            atendido = selected_queue.pop(0) # remove o primeiro
            print("Cliente atendido %d atendido" % atendido)
        else:
            print('Fila vazia, ninguém para atender')
    elif op == 'FN':
        ultimo += 1 # incrementando a fila (ticket)
        fila_normal.append(ultimo) # <-
    elif op == "FV":
        ultimo += 1 # incrementando a fila (ticket)
        fila_vip.append(ultimo)
    elif op == 'S':
        break
    else:
        print('Operação inválida. Digite (FN, FV, A ou S')
