small=2
regular=5
big=6
user_budget=input('¿Cual es tu presupuesto? ')

user_budget=int(user_budget)
print('El monto disponible es ', user_budget, '$')

if user_budget > 0:
    if user_budget >= big:
        print('Puedes permitirte un buen café')
        if user_budget==big:
            print('Es todo')
        else:
            print('Tu cambio', user_budget-big, '$')
    elif user_budget==regular:
        print('Puedes pagar un cafe regular')
        print('Es todo')
    elif user_budget>=small:
        print('Puedes pagar un cafe pequeno')
        if user_budget==small:
            print('Es todo')
        else:
            print('Tu cambio', user_budget-small, '$')
            
