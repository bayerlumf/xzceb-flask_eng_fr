import unittest

from translator import english2french, french2english

class test_englishtofrench(unittest.Testcase):
    def teste2f(self):
        self.assertEqual(english2french(""), "")
        self.assertEqual(english2french("Hello"), "Bonjour")
        self.assertNotEqual(english2french("Hello"),"Hello")

class test_frenchtoenglish(unittest.Testcase):
    def testf2e(self):
        self.assertEqual(french2english(""), "")
        self.assertEqual(french2english("Bonjour"), "Hello")
        self.assertNotEqual(french2english("Bonjour"),"Bonjour")

unittest.main()