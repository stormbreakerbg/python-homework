import unittest
import solution


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.adam = solution.Person(name='Adam', gender='M', birth_year=0)
        self.eva = solution.Person(name='Eva', gender='F', birth_year=0)
        self.first_son = solution.Person(name='Kain', gender='M',
                                         birth_year=20, father=self.adam,
                                         mother=self.eva)
        self.first_daughter = solution.Person(name='Pepa', gender='F',
                                              birth_year=22, father=self.adam,
                                              mother=self.eva)
        self.evas_secret_son = solution.Person(name='Ali Raza', gender='M',
                                               birth_year=25, mother=self.eva)
        self.third_daughter = solution.Person(name='Ferhunde', gender='F',
                                              birth_year=45,
                                              father=self.evas_secret_son)

    def tearDown(self):
        del self.adam
        del self.eva
        del self.first_son
        del self.first_daughter
        del self.evas_secret_son
        del self.third_daughter

    def test_attributes(self):
        self.assertIn('name', dir(self.adam))
        self.assertIn('gender', dir(self.adam))
        self.assertIn('birth_year', dir(self.adam))

    def test_has_sister(self):
        self.assertEqual(self.first_son.get_sisters(), [self.first_daughter])

    def test_has_brother(self):
        self.assertEqual(self.first_son.get_brothers(), [self.evas_secret_son])

    def test_common_mother_sisters(self):
        self.assertEqual(self.evas_secret_son.get_sisters(), [
            self.first_daughter
        ])

    def test_common_mother_brothers(self):
        self.assertEqual(self.evas_secret_son.get_brothers(), [
            self.first_son
        ])

    def test_has_no_sisters(self):
        self.assertEqual(self.adam.get_sisters(), [])
        self.assertEqual(self.first_daughter.get_sisters(), [])

    def test_has_no_brothers(self):
        self.assertEqual(self.adam.get_brothers(), [])

    def test_has_no_self_in_sisters(self):
        self.assertNotIn(self.first_daughter,
                         self.first_daughter.get_sisters())

    def test_has_no_self_in_brothers(self):
        self.assertNotIn(self.first_son,
                         self.first_son.get_brothers())

    def test_father_has_son(self):
        self.assertEqual(self.adam.children(gender='M'), [self.first_son])

    def test_father_has_daughter(self):
        self.assertEqual(self.adam.children(gender='F'), [self.first_daughter])

    def test_direct_successor(self):
        self.assertTrue(self.adam.is_direct_successor(self.first_son))
        self.assertFalse(self.adam.is_direct_successor(self.adam))
        self.assertTrue(self.eva.is_direct_successor(self.evas_secret_son))
        self.assertFalse(self.adam.is_direct_successor(self.evas_secret_son))
        self.assertFalse(self.adam.is_direct_successor(self.third_daughter))

if __name__ == '__main__':
    unittest.main()
