from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current sesion key if it exists
        cart = self.session.get('session_key')

        # If the user is ne, no session key! Create One!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # Make sure cart is available on all page of site
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def cart_total(self):
        # Get product_ids
        product_ids = self.cart.keys()
        # lookup those keys in our product database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            # covert key string into int
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # delte from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]
        # save our session after we modified it
        self.session.modified = True