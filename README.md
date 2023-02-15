# Job-shop

Gyárakban általánosan előforduló igény a gyártás optimazálása, mivel a folyamatok idejének redukálásával képesek vagyunk a termelés növelésére vagy adott termelési szint mellett a gyártási idő csökkentésére.

A feladat megoldása során a cél, hogy minél rövidebb gyártási időt érjünk el.

## Leírás

Gyártósori feladatot látunk el, ahol ahhoz, hogy elérjük a kész eredményt elég volna mindent sorban végrehajtanunk. Viszont tudjuk, hogy az egyes feladatok nem feltétlenül egymásra épülnek, így párhuzamosan is tudjuk végezni azokat. Gépekből meghatározott számú áll rendelkezésre, amelyek egy időben pedig csak egy feladaton tudnak dolgozni.
Emellett nem minden gép tud minden feladatot ellátni, így külön oda kell figyelni arra, hogy elvégezhető feladatot kapjanak a gépek.

## Megvalósítás

A feladat elvégzése során [GLPK](https://www.gnu.org/software/glpk/ 'GNU Linear Programming Toolkit')-t használtam, illetve a kapott eredményt JSON file-ba írtam, amit Python-nal feldolgozva jelenítek meg egy gannt diagrammon.

### Felhasznált eszközök és verzióik

A munka során a GLPK [Windows-os változat](https://winglpk.sourceforge.net/#download 'GLPK for Windows') változatát használtam.

- Python
  - [Python 3.11.2](https://www.python.org/downloads/release/python-3112/ 'Python')
  - [Matplotlib 3.6.2](https://matplotlib.org/stable/users/release_notes.html#version-3-6 'Matplotlib')
- GLPK
  - [GLPK 4.65](https://sourceforge.net/projects/winglpk/ 'GLPK')
