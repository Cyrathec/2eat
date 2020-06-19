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
    def addProduct(self, product):
        self.products.append(product)
        self.price += product['price']
    
    # Delete a product from the basket
    def delProduct(self, product: dict):
        i = 0
        for p in self.products:
            if p == product:
                self.products.pop(i)
                self.price -= product['price']
                return
            i += 1

    def delProductAtIndex(self, index):
        self.price -= self.products[index]['price']
        self.products.pop(index)

    # Update the restaurant id
    def updateRestaurant(self, restaurant: str):
        self.restaurant = restaurant
        self.products.clear()
        self.price = 0

    # Update the shipment address
    def updateAddress(self, address: str):
        self.address = address

    def toDict(self):
        return {
            "id": self.id,
            "restaurant": self.restaurant,
            "client": self.client,
            "address": self.address,
            "products": self.products,
            "price": self.price
        }