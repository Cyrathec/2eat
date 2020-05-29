class Basket():

    # Create the basket
    def __init__(self, restaurant, client, address):
        self.restaurant = restaurant                        # ForeignKey to the Restaurant id
        self.client = client                                # ForeignKey to the client id
        self.address = address                              # Shipment address
        self.products = []                                  # List of the products that will be shipped
        self.price = 0                                      # Total price of the order

    # Add a product to the basket
    def addProduct(self, product):
        self.products.append(product)
        self.price += product.price
    
    # Delete a product from the basket
    def delProduct(self, product):
        self.products.append(product)
        self.price -= product.price