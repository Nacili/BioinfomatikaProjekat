import DTree
import KNeighboors
import Gaussian
import MLP
import SVM

print ('Preprocesiranje podataka u toku...')
data = ''
print('Podaci nad kojima se vrsi istrazivanje:')
print(data)

while True:
    print('Odaberite zeljenu metodu:')
    print('\t1. Drvo odlucivanja')
    print('\t2. K najblizih suseda')
    print('\t3. Gausova raspodela')
    print('\t4. Neuronske mreze')
    print('\t5. Potporni vektori')
    while True:
        metoda = int(input(''))
        if metoda in (1, 2, 3, 4, 5):
            break
        else:
            print('Neispravna opcija')
            print('Odabrali ste metodu pod rednim brojem ' + str(metoda))
            print('--------------------------------------------------------')

    if metoda == 1:
        DTree(data)
    elif metoda == 2:
        KNeighboors(data)
    elif metoda == 3:
        Gaussian(data)
    elif metoda == 4:
        MLP(data)
    else:
        SVM(data)
        
    metoda = input('Zelite li da isprobate drugu metodu? (y/n)')
    if metoda == 'n':
        break