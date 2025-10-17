class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.libero = True

    def __str__(self):
        return f'Passeggero {self.codice}: {self.nome} {self.cognome}'

    def __repr__(self):
        return f'CodP: {self.codice}, NomP: {self.nome}, CogP: {self.cognome}'