from IPython.display import clear_output
import random

def print_plansza(plansza):
    clear_output()

    print('        ||        ||        ')
    print(f'   {plansza[7]}    ||   {plansza[8]}    ||   {plansza[9]}     ')
    print('        ||        ||        ')
    print('||||||||||||||||||||||||||||')
    print('        ||        ||        ')
    print(f'   {plansza[4]}    ||   {plansza[5]}    ||   {plansza[6]}     ')
    print('        ||        ||        ')
    print('||||||||||||||||||||||||||||')
    print('        ||        ||        ')
    print(f'   {plansza[1]}    ||   {plansza[2]}    ||   {plansza[3]}     ')
    print('        ||        ||        ')


def znak():
    marker=''

    while marker!='X' and marker!='O':
        marker=input("Choose your mark, X or O ").upper()

    if marker=='X':
        return ('X','O')
    else:
        return('O','X')

def znak_plansza(plansza,pozycja,marker):
    plansza[pozycja]=marker


def wygrana(plansza,marker):
    return (plansza[1]==plansza[2]==plansza[3]==marker or plansza[4]==plansza[5]==plansza[6]==marker or
           plansza[7]==plansza[8]==plansza[9]==marker or plansza[1]==plansza[5]==plansza[9]==marker or
           plansza[3]==plansza[5]==plansza[7]==marker or plansza[1]==plansza[4]==plansza[7]==marker or
           plansza[2]==plansza[5]==plansza[8]==marker or plansza[3]==plansza[6]==plansza[9]==marker)


def wolne_miejsce(plansza,pozycja):
    return plansza[pozycja]==' '


def gracz_wybor(plansza):
    pozycja=0
    while pozycja not in [1,2,3,4,5,6,7,8,9] or not wolne_miejsce(plansza,pozycja):
        pozycja= int(input('Podaj pozycje, na której chcesz umieścić swój znak'))
    return pozycja


def cala_plansza(plansza):
    for i in range(1,10):
        if wolne_miejsce(plansza,i):
            return False
    return True


def replay():
    return input('Czy chcesz zagrac jeszcze raz? ' ).lower().startswith('y')


def pierwszy():
    if random.randint(0,1)==0:
        return 'Gracz 1'
    else:
        return 'Gracz 2'


print('Witaj w grze kółko i krzyżyk')
while True:
    plansza=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1,player2=znak()

    kolej=pierwszy()

    print( kolej + 'rozpocznie jako pierwszy.')

    rozgrywka=input('Chcesz rozpocząć grę? ')

    if rozgrywka.lower()[0]=='y':
        gra=True
    else:
        gra=False

    while gra:
        if kolej=='Gracz 1':

            #wyswietl plansze
            print_plansza(plansza)
            #wybierz pozycje na planszy
            pozycja=gracz_wybor(plansza)
            #umiesc znak na planszy według wyboru
            znak_plansza(plansza,pozycja,player1)

            if wygrana(plansza,player1):
                print_plansza(plansza)
                print('Gratulacje! Wygrałeś')
                gra= False
            else:
                if cala_plansza(plansza):
                    print_plansza(plansza)
                    print('Remis')
                    break
                else:
                    kolej='Gracz 2'


        else:
            #wyswietl plansze
            print_plansza(plansza)
            #wybierz pozycje na planszy
            pozycja=gracz_wybor(plansza)
            #umiesc znak na planszy według wyboru
            znak_plansza(plansza,pozycja,player2)

            if wygrana(plansza,player2):
                print_plansza(plansza)
                print('Gratulacje! Wygrałeś')
                gra= False
            else:
                if cala_plansza(plansza):
                    print_plansza(plansza)
                    print('Remis')
                    break
                else:
                    kolej='Gracz 1'

    if not replay():
        break
