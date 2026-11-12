
import unittest
from film import Film


class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film = Film("Titanic", "James Cameron", 1997, 9.5)

    def test_creation(self):
        self.assertEqual(self.film.titre, "Titanic")
        self.assertEqual(self.film.realisateur, "James Cameron")
        self.assertEqual(self.film.annee, 1997)
        self.assertEqual(self.film.note, 9.5)

    def test_est_classique(self):
        self.assertTrue(self.film.est_classique())

        film_recent = Film("Avatar", "James Cameron", 2009, 8.5)
        self.assertFalse(film_recent.est_classique())

    def test_to_json(self):
        resultat = self.film.to_json()
        self.assertIn('"titre": "Titanic"', resultat)

    def test_from_json(self):
        texte = self.film.to_json()
        film_charge = Film.from_json(texte)

        self.assertEqual(film_charge, self.film)

    def test_comparaison(self):
        film2 = Film("Avatar", "James Cameron", 2009, 8.5)
        self.assertFalse(self.film < film2)

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Realisateur", 2020, 12)

    def test_note_negative(self):
        with self.assertRaises(ValueError):
            Film("Film", "Realisateur", 2020, -2)

    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Realisateur", 2020, 8)

    def test_titre_none(self):
        with self.assertRaises(ValueError):
            Film(None, "Realisateur", 2020, 8)

    def test_annee_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Realisateur", "2020", 8)

    def test_note_type_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Realisateur", 2020, "excellent")

    def test_immutabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 8.0


if __name__ == "__main__":
    unittest.main()
