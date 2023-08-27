import unittest

# Define the Cart class
class Cart:
    # Initialize the Cart instance
    def __init__(self):
        self.items = []

    # add an item to Cart
    def new_item(self, name, amount):
        self.items.append({"name": name, "price": amount})

    # get the total amount of the items in the Cart
    def sum_total(self):
        total = sum(item["price"] for item in self.items)
        return total
    
    # discount is applied when the condition is met
    def discounted_price(self, discount):
        total = self.sum_total()

        # check if conditions are met
        if len(self.items) >= 5 and total >= 200:
            total -= discount

        return total
    
# The fucntion that demonstrate the Cart class
def main():
    # create an instance for the Cart class
    cart = Cart()

    # Add items to the cart
    cart.new_item("toy_truck", 60)
    cart.new_item("teddy_bear", 25)
    cart.new_item("barbie_doll", 35)
    cart.new_item("lego", 100)
    cart.new_item("hot_wheels", 20)

    # get the total and display before discount
    total_before_discountedprice = cart.sum_total()
    print("Total before discount is applied: $", total_before_discountedprice)

    # apply discount and display the total after discount is applied
    discount = 50
    total_after_discountedprice = cart.discounted_price(discount)
    print("Total after discount is applied: $", total_after_discountedprice)
    
    # Run the main function
if __name__ == "__main__":
    main()

# unit tests
class TestCart(unittest.TestCase):
    # Test the calculation of the total price of the items
    def test_total_calc(self):
        cart = Cart()
        cart.new_item("toy_truck", 60)
        cart.new_item("teddy_bear", 25)
        cart.new_item("barbie_doll", 35)
        cart.new_item("lego", 100)
        cart.new_item("hot_wheels", 20)

        total = cart.sum_total()
        self.assertEqual(total,240)

# test if the application of discount is properly applied

def test_application_of_discount(self):
     cart = Cart()
     cart.new_item("toy_truck", 60)
     cart.new_item("teddy_bear", 25)
     cart.new_item("barbie_doll", 35)
     cart.new_item("lego", 100)
     cart.new_item("hot_wheels", 20)

     total_discount_applied = cart.discount(50)
     self.assertEqual(total_discount_applied, 190)

# run the unit test
if __name__ == "__main__":
   unittest.main()