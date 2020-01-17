import re

while True:
    arg = input('Entrer votre argent: ')
    while not re.match(r'^[0-9_]+$', arg):
        arg = input('(error) Entrer votre argent: ')
    arg = str(int(arg))
    

    unite =  ['', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix',
                'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf']

    dizaine = [None, None, 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante-dix', 'quatre-vingt', 'quatre-vingt-dix']

    # autre = ['cent', 'mille', 'millions', 'milliards']

    def prints(arg): print(" ".join(arg.split()))


    def func_unite(arg): return unite[int(arg)]


    def func_dizaine(arg):
        if int(arg[0]) == 0: return func_unite(arg[1])

        if int(arg) < 20:
            return unite[int(arg)]
        else:
            if int(arg[1]) == 0: return dizaine[int(arg[0])]
            else:
                if int(arg[0]) == 7 or int(arg[0]) == 9:
                    unit_new = int(arg) - int(arg[0]+'0') + 10
                    return dizaine[int(arg[0]) - 1] + ' ' + unite[unit_new]

                else: return dizaine[int(arg[0])] + ' ' + unite[int(arg[1])]


    def func_centaine(arg):
        if int(arg[0]) == 0: return main(arg[1:])
        
        if int(arg[0]) == 1: return 'cent ' + func_dizaine(arg[1:])
        else: return unite[int(arg[0])] + ' cents ' + func_dizaine(arg[1:])


    def func_millieme(arg):
        if int(arg[0]) == 0: return main((arg[1:]))

        if len(arg) == 4:
            if int(arg[0]) == 0: return func_centaine(arg[1:])

            if int(arg[0]) == 1: 
                return 'mille ' + func_centaine(arg[1:])
            else: 
                return unite[int(arg[0])] + ' milles ' + func_centaine(arg[1:])

        elif len(arg) == 5:
            # if int(arg[0]) == 0: return func_centaine(arg[2:])
            return func_dizaine(arg[:2]) + ' milles ' + func_centaine(arg[2:])
        
        elif len(arg) == 6:
            # if int(arg[0]) == 0: return func_centaine(arg[3:])
            return func_centaine(arg[:3]) + ' milles ' + func_centaine(arg[3:])
    

    def func_million(arg):
        if int(arg[0]) == 0: return main(arg[1:])

        if len(arg) == 7:
            # if int(arg[0]) == 0: return func_millieme(arg[1:])

            if int(arg[0]) == 1: 
                return 'un million ' + func_millieme(arg[1:])
            else: 
                return unite[int(arg[0])] + ' millions ' + func_millieme(arg[1:])

        elif len(arg) == 8:
            # if int(arg[0]) == 0: return func_millieme(arg[2:])
            return func_dizaine(arg[:2]) + ' millions ' + func_millieme(arg[2:])
        
        elif len(arg) == 9:
            # if int(arg[0]) == 0: return func_millieme(arg[3:])
            return func_centaine(arg[:3]) + ' millions ' + func_millieme(arg[3:])


    def func_milliard(arg):
        if int(arg[0]) == 0: return main(arg[1:])
        
        if len(arg) == 10:
            if int(arg[0]) == 1: 
                return 'un milliard' + func_million(arg[1:])
            else: 
                return unite[int(arg[0])] + ' milliards ' + func_million(arg[1:])

        elif len(arg) == 11:
                return func_dizaine(arg[:2]) + ' milliards ' + func_million(arg[2:])
        
        elif len(arg) == 12:
                return func_centaine(arg[:3]) + ' milliards ' + func_million(arg[3:])
        
        else:
            return main(arg[:len(arg)-9]) + ' milliards ' + func_million(arg[len(arg)-9:])



    def main(arg):
        if len(arg) == 1: return func_unite(arg)

        elif len(arg) == 2: return func_dizaine(arg)

        elif len(arg) == 3: return func_centaine(arg)

        elif len(arg) in [4, 5, 6]: return func_millieme(arg)

        elif len(arg) in [7, 8, 9]: return func_million(arg)

        elif len(arg) > 9 : return func_milliard(arg)


    if int(arg) == 0:
        print("zero")
    
    
    prints(main(arg))
    
        

    



