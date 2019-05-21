# Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.
# Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.

Train1V = int(input('Enter the speed of the first train: '))
Train2V = int(input('Enter the speed of the second train: '))
TimeForTrain1 = 4 / Train1V
TimeForTrain2 = 6 / Train2V
if TimeForTrain1 < TimeForTrain2:
    print('Trains did not clash')
else:
    print('Trains are clashed')
