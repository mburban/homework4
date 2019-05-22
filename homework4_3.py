# Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.
# Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.

train1V = int(input('Enter the speed of the first train: '))
train2V = int(input('Enter the speed of the second train: '))
timeForTrain1 = 4 / train1V
timeForTrain2 = 6 / train2V
if timeForTrain1 < timeForTrain2:
    print('Trains did not clash')
else:
    print('Trains are clashed')
