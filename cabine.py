class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        return f'Cabina {self.codice}: {self.letti} letti, ponte {self.ponte}, costo {self.prezzo} €.'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Prezzo: {self.prezzo}'

class Cabina_Animali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, animali_max):
        super().__init__(codice, letti, ponte, prezzo=None)
        self.animali_max = animali_max
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        return f'Cabina {self.codice}: {self.letti} letti, ponte {self.ponte}, costo {self.prezzo} €.'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, AnimaliM: {self.animali_max}, prezzo: {self.prezzo}'

class Cabina_Deluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo=None)
        self.stile = stile
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        return f'Cabina {self.codice}: {self.letti} letti, ponte {self.ponte}, costo {self.prezzo_finale} €.'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Stile: {self.stile}, Prezzo: {self.prezzo}'
