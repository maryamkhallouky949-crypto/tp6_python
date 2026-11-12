
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit):
        if prix_reduit <= 0 or prix_reduit >= self.prix:
            raise ValueError("Le prix réduit doit être positif et inférieur au prix original.")

        return Livre(self.titre, self.auteur, self.annee, prix_reduit)

    @classmethod
    def from_json(cls, chaine_json):
        donnees = json.loads(chaine_json)
        return cls(**donnees)

    def __lt__(self, autre):
        return self.prix < autre.prix


if __name__ == "__main__":

    livre1 = Livre("1984", "George Orwell", 1949, 10.90)

    print("Livre original :")
    print(livre1.to_json())

    livre2 = livre1.promo(8.50)

    print("Livre après promotion :")
    print(livre2.to_json())

    print("Prix original :", livre1.prix)

    livre3 = Livre.from_json(livre1.to_json())
    print("Livre chargé :", livre3)

 
    livre4 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 13.0)

    if livre1 < livre4:
        print("1984 est moins cher que Le Petit Prince.")
