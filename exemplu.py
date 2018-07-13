class Caine:
    def __init__(self, name, color, personality):
        self.name = name
        self.color = color
        self.personality = personality

    def do_trick(self):
        if self.personality == 'aggressive':
            print("BARK BARK BARK")
        elif self.personality == 'friendly':
            print("bow wow affectively")
        else:
            print('woof woof')

caine_rau = Caine('LABUSH', 'black', 'aggressive') #instante

caine_bun = Caine('Rexi', 'white', 'friendly') #instante

caine_neutru = Caine('Ursu', 'brown', 'random') #instante

caine_rau.do_trick()

caine_bun.do_trick() #apelatul metodei do_trick pe instanta caine_bun

caine_neutru.do_trick()


#Cand am creat obiectul caine rau am instantiat clasa caine cu 3 argumente ('LABUSH', 'black', 'aggressive')


#self - ii referinta la obiectul curent

#functia def __init__(constructor-o functie care consutruieste obiectul; celelatle functii definec comportamentul) - este o functie speciala care creaza obiectul; fiecare clasa

#unitatea de baza a unui program este functia; in OOP am niste functii create implicit


#metodele sunt functii, legate de un anumit obiect(clasa); sunt comportamente ale unor anumite clase.


# Intelenge ce ii un obiect si o clasa.