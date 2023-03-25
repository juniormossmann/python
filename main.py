saldo = 0
nConta = 1234
transacoes = []
ext = 0

def registrarTransacoes(valor, historico):
    historico.append(valor)
    print(historico)

def deposito(valor, saldo, historico):
    if valor > 0:  
        registrarTransacoes(valor, historico)   
        saldo += valor        
    else:
        print("Valor Inválido")    
    return saldo

def saque(valor, saldo, historico):
    if valor > 0: 
        if saldo >= valor:
            registrarTransacoes(valor * -1, historico)
            saldo -= valor  
        else:
            print("Saldo Insuficiente")      
    else:
        print("Valor Inválido")
    return saldo   

def extrato(historico):
    for i in range(len(historico)):
        print("Transação ",i+1,":",historico[i])

def menu():    
    print("Escolha a Opção: ")
    print("1 = Depósito")
    print("2 = Saque")
    print("3 = Extrato")
    print("4 = Sair")
    opcao = input()
    while opcao != 4:
        if opcao == 1:
            print("Valor do Depósito:")
            valor = float(input())
        elif opcao == 2:
            print("Valor do Depósito:")
            valor = float(input())    
        elif opcao == 3:
            extrato(transacoes)
        else:
            print("Valor inválido!")
        return valor

print(saldo)
saldo = deposito(100, saldo, transacoes)    
saldo = deposito(-100, saldo, transacoes)    
saldo = saque(50, saldo, transacoes)    
saldo = saque(-50, saldo, transacoes)   
saldo = saque(200, saldo, transacoes) 
print(saldo)
print(transacoes)
ext = extrato(transacoes)
menu()

# desafio
'''
    Adicionar uma função (Extrato) para mostrar o histórico linha por linha.
        Exemplo:
            Transação 1: 100
            Transação 2: -50
            ...

    Alterar o código para que sejam possível o usuário escolher
        as ações: deposito, saque e "extrato".
'''









