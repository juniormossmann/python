saldo = 0
nConta = 1234
transacoes = []

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

print(saldo)
saldo = deposito(100, saldo, transacoes)    
saldo = deposito(-100, saldo, transacoes)    
saldo = saque(50, saldo, transacoes)    
saldo = saque(-50, saldo, transacoes)   
saldo = saque(200, saldo, transacoes) 
print(saldo)

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









