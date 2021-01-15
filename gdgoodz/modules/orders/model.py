class OrderModel():

    def __init__(self, supplier, products, quantities, skus, costs_per_unit, shipping_cost,
                 delivery_date, delivery_address, status, notes):
        self._id = None
        self._supplier = supplier
        self._products = products
        self._quantities = quantities
        self._skus = skus
        self._costs_per_unit = costs_per_unit
        self._shipping_cost = shipping_cost
        self._delivery_date = delivery_date
        self._delivery_address = delivery_address
        self._status = status
        self._notes = notes
        self._created_at = None
        self._updated_at = None

    ''' Properties and Setters '''

    # ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # Supplier
    @property
    def supplier(self):
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        self._supplier = supplier

    # Products
    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    # Quantities
    @property
    def quantities(self):
        return self._quantities

    @quantities.setter
    def quantities(self, quantities):
        self._quantities = quantities

    # SKUs
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, skus):
        self._skus = skus

    # Cost Per Unit
    @property
    def costs_per_unit(self):
        return self._costs_per_unit

    @costs_per_unit.setter
    def costs_per_unit(self, costs_per_unit):
        self._costs_per_unit = costs_per_unit

    # Shipping Cost
    @property
    def shipping_cost(self):
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        self._shipping_cost = shipping_cost

    # Delivery Date
    @property
    def delivery_date(self):
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        self._delivery_date = delivery_date

    # Delivery Address
    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self._delivery_address = delivery_address

    # Status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    # Notes
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    # Created At
    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    # Updated At
    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    ''' Helper Methods '''

    # To Dict
    def to_dict(self):
        order_dict = {
            'id': self._id,
            'supplier': self._supplier,
            'products': self._products,
            'quantities': self._quantities,
            'skus': self._skus,
            'costs_per_unit': self._costs_per_unit,
            'shipping_cost': self._shipping_cost,
            'delivery_date': self._delivery_date,
            'delivery_address': self._delivery_address,
            'status': self._status,
            'notes': self._notes,
            'created_at': self._created_at,
            'updated_at': self._updated_at
        }
        return order_dict
