EXPECTED_BAKE_TIME = 40


PREPARATION_TIME = 2

elapsed_bake_time=int(input('Cuanto tiempo lleva en el horno?:'))
number_of_layers=int(input('Cuantas capas tiene la lasaña?:'))

print('Tiempo de horno restante =', end = ' ')
print(EXPECTED_BAKE_TIME - elapsed_bake_time)

print('Tiempo de preparación de la lasaña =', end = ' ')
print(number_of_layers * PREPARATION_TIME)


print('Tiempo que llevo cocinando =', end = ' ')
print(elapsed_bake_time + number_of_layers * PREPARATION_TIME)