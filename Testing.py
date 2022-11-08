# Introduction to Testing

# Individual units of source code (such as functions) are tested to make sure they are working properly
# Typically you have a test file that accompanies each module
# Tests are only for development and the customer never sees this file

import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'ssdvbnsdj'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')



if __name__ == '__main__':
    unittest.main()






