def contaRegressivaRecursao(n):
    if n > 0:
        print(n)
        contaRegressivaRecursao(n - 1)
        
contaRegressivaRecursao(10)