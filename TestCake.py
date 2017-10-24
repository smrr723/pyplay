import unittest

from Cake import Cake
# from CakeShop import CakeShop


class TestCake(unittest.TestCase):

    def setUp(self):
        ingredients = ["Sugar", "Spam", "Banana"]
# self.cake same as Ruby instance variable
        self.cake = Cake("Banana Bread", ingredients, 5)

    def test_cake_has_name(self):
        # assertEquals is a unittest method so needs to be this name and also needs to use self.
        self.assertEquals("Banana Bread", self.cake.name)

    def test_cake_has_ingredients(self):
        self.assertEquals(3,
            len(self.cake.ingredients))
    def test_cake_can_bake(self):
        self.assertEquals("The cake is baking", self.cake.bake())


unittest.main()
