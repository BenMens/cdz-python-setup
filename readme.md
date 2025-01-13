# CoderDojo Python setup

Het doel van deze instructie is om het gebruik van Python voor onze Ninjas eenvoudiger te maken door ervoor te zorgen dat
alle libraries vooraf zijn geinstalleerd en dat ze werken in Thonny en in VS Code. Hierdoor kunnen we Python aanbieden aan
beginnende en gevorderde Ninjas.

Uitgangspunten:

- Ninjas moeten kunnen werken in Thonny
- Ninjas moeten kunnen werken in VS Code
- Libraries moeten vooraf geinstalleerd zijn zodat Ninjas direct kunnen beginnen met een opdracht.
- P5 moet worden ondersteund.

## Samenvatting installatie

De installatie bestaat uit het installeren van Thonny, het instaleren van Python versie 3.10.11 en het installeren van de benodigde 
plugins in VS Code. 

In de opties van Thonny wordt aangegeven dat deze de globale pyton installatie moet gebruiken.

Tenslotte worden de libraries die zijn opgelijst in het bestand requirements.txt geinstalleerd.

Het is de bedoeling dat wij als mentoren het bestand requirements.txt up-to-date houden met wat nodig is voor de opdrachten.
Dit kan bijvoorbeeld door requirements.txt op een gedeelde locatie te zetten. Bijvoorbeeld GIT.

Op dit moment wordt deze instructie beheerd in GIT [cdz-python-setup](https://github.com/BenMens/cdz-python-setup)

## Install cdz-python-setup op een laptop

Creeer de folder C:\Users\Ninja\Documents\Python

Open een command shell en start het commando:

```cmd
  git clone https://github.com/BenMens/cdz-python-setup
```

## Install python 3.10.11

Thonny gebruikt Python 3.10.11. Deze versie ondersteund ook P5. Door Pyhton 3.10.11 ook los te installeren wordt deze door VS Code
opgepikt en zullen script geschreven binnen Thonny ook in VS Code werken en vise versa.

Download [Python 3.10.11](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

Start de installer

- Kies Add python.exe to PATH
- Install
- .....
- Close

## VS Code python plug-ins

Install plugins

- Pylance
- Python
- Python debugger
- Black Formatter

## Installatie Thonny

Zie [Thonny](https://thonny.org/)

Installer with 64-bit Python 3.10, requires 64-bit Windows 8.1 / 10 / 11
thonny-4.1.7.exe (21 MB) ⇐ recommended for you

- Install
  - Only for me
  - next next finish

Zorg ervoor dat Thonny dezelfde Python installatie gebruikt als VS Code:

- Open Thonny
- Menu -> Hulpmiddelen -> opties -> Interpreter

  C:\Users\Ninja\AppData\Local\Programs\Python\Python310\python.exe

## Installing requirements.txt

De libraries die zijn opgelijst in requirements.txt moeten worden geinstalleerd met het onderstaande commando.
Dit commando haalt eerst de laaste versie op uit het GIT project en installeerd de libraries.

```cmd
  C:\Users\Ninja\Documents\Python\cdz-python-setup> install_libraries.cmd
```

## Achtegrond informatie

### Installing requirements.txt

Het bestand requirements.txt bevat een lijst van alle libraries die onze Ninjas nodig hebben voor het maken van opdrachten.
Deze libraries kunnen met één commando worden geinstalleerd.

Open een command shell en run:

```cmd
    pip install -r <path naar requirements>\requirements.txt 
```

### Updating requirements.txt

Als er voor nieuwe opdrachten aanvullende libraries nodig zijn, dan moet requirements.txt worden bijgewerkt.
Dit kan door eerst de benodigde libraries te toe te voegen aan requirements.txt. Daarna kan update worden geinstalleerd
met het commando:

```cmd
    pip install -r <path naar requirements>\requirements.txt 
```
