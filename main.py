import DTree
import KNeighbors
import Gaussian
import MLP
import CleanOriginal
import SeparateChromosomes
import DefineGenes
import MergeChromosomes

print('Da li želite da preskočite preprocesiranje? (y/n)\nProcenjeno vreme trajanja: 2h')
odg = input('')
if odg == 'y':
    print ('Preprocesiranje podataka u toku...')

    print('\t* Odstranjivanje suvisnih klasa')
    CleanOriginal.Clean()
    print('\t* Razvrstavanje hromozoma')
    SeparateChromosomes.SeparateChromosomes()
    print('\t* Definisanje gena')
    DefineGenes.DefineGenes()
    print('\t Grupisanje hromozoma')
    MergeChromosomes.MergeChromosomes()
    
    print('Preporocesiranje zavrseno. Podaci se nalaze u "preprocessed.xlsx".')


# ////////////////////////////////////////////////////

data = 'preprocessed.xlsx'

while True:
    print('Odaberite zeljenu metodu:')
    print('\t1. Drvo odlucivanja')
    print('\t2. K najblizih suseda')
    print('\t3. Gausova raspodela')
    print('\t4. Neuronske mreze')
    while True:
        metoda = int(input(''))
        if metoda in (1, 2, 3, 4):
            break
        else:
            print('Neispravna opcija')
            print('Odabrali ste metodu pod rednim brojem ' + str(metoda))
            print('--------------------------------------------------------')

    if metoda == 1:
        print('Odabrali ste analizu metodom drveta odlučivanja')
        DTree.DTree(data)
    elif metoda == 2:
        print('Odabrali ste analizu metodom k najbližih suseda')
        KNeighbors.KNeighboors(data)
    elif metoda == 3:
        print('Odabrali ste analizu Gausovom metodom')
        Gaussian.Gaussian(data)
    elif metoda == 4:
        print('Odabrali ste analizu metodom neuronskih mreža')
        MLP.MLP(data)
    else:
        print('Neispravna opcija')
        
    metoda = input('Zelite li da isprobate drugu metodu? (y/n)')
    if metoda == 'n':
        break