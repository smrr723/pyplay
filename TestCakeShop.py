import unittest

from CakeShop import CakeShop
from Cake import Cake


class TestCakeShop(unittest.TestCase):

    def setUp(self):
        ingredients = ["Sugar", "Spam", "Banana"]
        self.cake = Cake("Banana Bread", ingredients, 5)
        self.cake1 = Cake("Banana Bread", ingredients, 5)
        self.cake2 = Cake("Chocolate Cake", ingredients, 5)
        self.cake3 = Cake("Shortbread Cake", ingredients, 5)
        self.cake4 = Cake("Victoria Sponge", ingredients, 5)
        self.CakeShop = CakeShop("Tontine Cakes", [self.cake1, self.cake2, self.cake3, self.cake4])


    def test_cakeshop_has_name(self):
        # assertEquals is a unittest method so needs to be this name and also needs to use self.
        self.assertEquals("Tontine Cakes", self.CakeShop.name)
    #
    def test_gets_average(self):
        self.assertEquals(5, self.CakeShop.average_rating())
    # def test_cake_has_ingredients(self):
    #     self.assertEquals(3,
    #         len(self.cake.ingredients))
    # def test_cake_can_bake(self):
    #     self.assertEquals("The cake is baking", self.cake.bake())


unittest.main()
