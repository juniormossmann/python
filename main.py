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











