def calculate_total(flavor, milk, boba):
    total = flavor_total(flavor) + milk_total(milk) + boba_total(boba)
    return f'${total:.2f}'


def flavor_total(flavor):
    flavor_cost = 0.00
    if flavor == 'oolong':
        flavor_cost = 4.50
    elif flavor == 'jasmine':
        flavor_cost = 4.50
    elif flavor == 'silver needle':
        flavor_cost = 5.00
    return flavor_cost
    
def milk_total(milk):
    milk_cost = 0.00
    if milk == 'none':
        milk_cost = 0.00
    elif milk == 'dairy':
        milk_cost = 0.50
    elif milk == 'oat':
        milk_cost = 0.75
    elif milk == 'soy':
        milk_cost = 0.50
    return milk_cost
    
def boba_total(boba):
    boba_cost = 0.00
    if boba == 'yes':
        boba_cost = 0.50
    elif boba == "no":
        boba_cost = 0.00
    return boba_cost

def drink_summary(flavor, milk, boba):
    total = calculate_total(flavor, milk, boba)

    print('*** Drink Summary ***')
    drink_display = flavor.capitalize()
    if milk != 'none' or boba != 'no':
        drink_display = drink_display + ' with '
    if milk != 'none':
        drink_display = drink_display + milk + ' milk'
    if milk != 'none' and boba != 'no':
        drink_display = drink_display + ' and '
    if boba != 'no':
        drink_display = drink_display + 'boba'
    
    print(drink_display)
    print(f'Drink total: {total}')

drink_summary('oolong', 'none', 'yes')
drink_summary('silver needle', 'oat', 'yes')