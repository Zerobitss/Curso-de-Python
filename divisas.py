def foreign_exchange_calculator(ammount):
    change_mex_to_col = 145.97
    return change_mex_to_col * ammount
def run():
    print('Calculadora de divisas')
    print('Convierte en pesos mexicanos a pesos colombianos')
    print('')
    ammount = float(input("Ingresa la cantidad de pesos mexicanos: "))
    result = foreign_exchange_calculator(ammount)
    print(f'{ammount} pesos mexicanos son igual a {result} pesos colombianos')
if __name__ == '__main__':
    run()