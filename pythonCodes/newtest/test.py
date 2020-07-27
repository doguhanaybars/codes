import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = main.mailpushing('Doğuhan Aybars Ay','doguhanaybars71@gmail.com','Aybars1071.','doguhanaybars71@gmail.com','class deneme','içerik',2)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()