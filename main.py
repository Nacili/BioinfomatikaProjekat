import DTree
import KNeighbors
import Gaussian
import MLP
import SVM
import CleanOriginal
import SeparateChromosomes
import DefineGenes
import MergeChromosomes
#import warnings

#def fxn():
#    warnings.warn("deprecated", DeprecationWarning)
#
#with warnings.catch_warnings():
#    warnings.simplefilter("ignore")
#    fxn()

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
        print('Odabrali ste analizu metodom potpornih vektora')
        SVM.SVM(data)
        
    metoda = input('Zelite li da isprobate drugu metodu? (y/n)')
    if metoda == 'n':
        break