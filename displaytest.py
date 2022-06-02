import unittest
# import the display method
from display import display
# create a test class for display function
class DisplayTest(unittest.TestCase):
    # create a test method for display function
    def test_display(self):
        # ARRANGE
        # create a list of menu
        menu = ["ham", "butter", "tomato", "bread"]
        # create a name for menu
        name = 'Menu'
        expected = '=========Menu==========='
        # actual call a function to display menu
        # student work in progress, failing presently
        actual = ""
        # ASSERT
        # compare expected and actual
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()