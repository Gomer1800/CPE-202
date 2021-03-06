import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex_2(self):
        """
        Testing defaults from prompt
        """ 
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex_3(self):
        """
        Testing defaults from prompt
        """ 
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])

    def test_perm_gen_lex_empty_string(self):
        """
        Empty string should return [] & None argument raises ValueError
        """
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
        with self.assertRaises(ValueError):
            perm_lex.perm_gen_lex()

if __name__ == "__main__":
        unittest.main()
