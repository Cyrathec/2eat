class Basket():

    # Create the basket
    def __init__(self, id, restaurant, client, address):
        self.id = id
        self.restaurant = restaurant                        # ForeignKey to the Restaurant id
        self.client = client                                # ForeignKey to the client id
        self.address = address                              # Shipment address
        self.products = []                                  # List of the products that will be shipped
        self.price = 0                                      # Total price of the order

    # Add a product to the basket
    def addProduct(self, product: dict):
        self.products.append(product)
        self.price += product['price']
    
    # Delete a product from the basket
    def delProduct(self, product: dict):
        for p in products:
            if p == product:
                self.products.pop(p)
        self.price -= product['price']

    def toDict():
        return {
            "restaurant": self.restaurant,
            "client": self.client,
            "address": self.address,
            "products": self.products,
            "price": self.price
        }