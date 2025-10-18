class Passeggero:
    def __init__(self, codice, nome, cognome, cabina=None):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = cabina
        self.libero = True

    def __str__(self):
        if self.cabina:
            return f'{self.codice} | {self.nome} {self.cognome} | Cabina: {self.cabina}'
        else:
            return f'{self.codice} | {self.nome} {self.cognome}'

    def __repr__(self):
        return f'CodP: {self.codice}, NomP: {self.nome}, CogP: {self.cognome}'