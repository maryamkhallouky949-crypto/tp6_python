
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
       
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre est obligatoire.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur est obligatoire.")

    
        if isinstance(self.annee, bool) or not isinstance(self.annee, int):
            raise TypeError("L'année doit être un entier.")

        if self.annee <= 0:
            raise ValueError("L'année doit être positive.")

      
        if isinstance(self.note, bool) or not isinstance(self.note, (int, float)):
            raise TypeError("La note doit être un nombre.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être comprise entre 0 et 10.")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @classmethod
    def from_json(cls, chaine_json):
        donnees = json.loads(chaine_json)
        return cls(**donnees)

    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note


if __name__ == "__main__":

    film1 = Film("Titanic", "James Cameron", 1997, 10.5)
    film2 = Film("Avatar", "James Cameron", 2009, 9.5)

    print("Film 1 :", film1.to_json())
    print("Film 2 :", film2.to_json())

    print("Titanic est un classique :", film1.est_classique())
    print("Avatar est un classique :", film2.est_classique())

    if film1 < film2:
        print("Titanic a une note inférieure à Avatar.")
    else:
        print("Titanic a une note supérieure ou égale à Avatar.")

   
    film3 = Film.from_json(film1.to_json())
    print("Film chargé :", film3)

    
    favoris = [film1, film2]

    json_favoris = json.dumps(
        [asdict(film) for film in favoris],
        ensure_ascii=False
    )

    print("Liste des favoris :")
    print(json_favoris)
