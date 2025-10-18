from cabine import *
from passeggeri import *

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.cabine=list()
        self.passeggeri=list()
        """Inizializza gli attributi e le strutture dati"""

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        return f'Hai cambiato il nome della crociera in: {nome}'

    def carica_file_dati(self, file_path):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line=line.strip().split(',')
                    if line[0].startswith('C') and len(line)==4:
                        cabina=Cabina(line[0], int(line[1]), int(line[2]), float(line[3]))
                        self.cabine.append(cabina)
                    elif line[0].startswith('C') and line[4].isdigit():
                        prezzo=(float(line[3]))*(1+(0.1*int(line[4])))
                        cabina = Cabina_Animali(line[0], int(line[1]), int(line[2]), int(line[4]), prezzo)
                        self.cabine.append(cabina)
                    elif line[0].startswith('C') and line[4].isalnum():
                        prezzo=(float(line[3]))*(1.2)
                        cabina = Cabina_Deluxe(line[0], int(line[1]), int(line[2]), line[4], prezzo)
                        self.cabine.append(cabina)
                    else:
                        passeggero=Passeggero(line[0], line[1], line[2])
                        self.passeggeri.append(passeggero)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")
        """Carica i dati (cabine e passeggeri) dal file"""

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        c=None
        p=None
        for cab in self.cabine:
            if cab.codice == codice_cabina:
                if cab.disponibile==True:
                    c=codice_cabina
                    for pas in self.passeggeri:
                        if pas.codice == codice_passeggero:
                            if pas.libero==True:
                                p=codice_passeggero
                                pas.cabina=cab.codice
                                cab.disponibile=False
                                pas.libero=False
                            else:
                                raise Exception(f'Passeggero {pas.codice} già assegnato ad una cabina.')
                else:
                    raise Exception(f'Cabina {cab.codice} già assegnata ad un passeggero.')
        if p is None or c is None:
            raise Exception(f'Cabina o Passeggero non trovati.')
        """Associa una cabina a un passeggero"""

    def cabine_ordinate_per_prezzo(self):
        return sorted(self.cabine, key=lambda c: c.prezzo)
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

    def elenca_passeggeri(self):
        for el in self.passeggeri:
            print (el)
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """

if __name__ == '__main__':
    print()