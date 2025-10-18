class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        if self.disponibile:
            return f'{self.codice} | Cabina Classica: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € | Disponibile'
        else:
            return f'{self.codice} | Cabina Classica: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € | Occupata'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Prezzo: {self.prezzo}'

class Cabina_Animali(Cabina):
    def __init__(self, codice, letti, ponte, animali_max, prezzo):
        super().__init__(codice, letti, ponte, prezzo=None)
        self.animali_max = animali_max
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        if self.disponibile:
            return f'{self.codice} | Cabina per Animali: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € - {self.animali_max} Animali | Disponibile'
        else:
            return f'{self.codice} | Cabina per Animali: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € - {self.animali_max} Animali | Occupata'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, AnimaliM: {self.animali_max}, prezzo: {self.prezzo}'

class Cabina_Deluxe(Cabina):
    def __init__(self, codice, letti, ponte, stile, prezzo):
        super().__init__(codice, letti, ponte, prezzo=None)
        self.stile = stile
        self.prezzo = prezzo
        self.disponibile = True

    def __str__(self):
        if self.disponibile:
            return f'{self.codice} | Cabina Deluxe: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € - Stile {self.stile} | Disponibile'
        else:
            return f'{self.codice} | Cabina Deluxe: {self.letti} Letti - Ponte {self.ponte} - Costo {self.prezzo:.2f} € - Stile {self.stile} | Occupata'

    def __repr__(self):
        return f'CodC: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Stile: {self.stile}, Prezzo: {self.prezzo}'