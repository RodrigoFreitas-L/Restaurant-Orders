class TrackOrders:
    def __init__(self):
        self.customer_order = {}
        self.days = {}
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_days(self, day):
        if day not in self.days:
            self.days[day] = 1
        self.days[day] += 1

    def add_order(self, order):
        self.orders.add(order)

    def add_customer_order(self, customer, order, day):
        if customer not in self.customer_order:
            self.customer_order[customer] = [[order, day]]
        self.customer_order[customer].append([order, day])

    def add_new_order(self, customer, order, day):
        self.add_days(day)
        self.add_order(order)
        self.add_customer_order(customer, order, day)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = self.customer_order[customer]
        orders = {}
        for order in customer_orders:
            if order[0] not in orders:
                orders[order[0]] = 1
            orders[order[0]] += 1
        return max(orders, key=orders.get)

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set()
        for order in self.customer_order[customer][0]:
            customer_orders.add(order)
        orders = self.orders
        return orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_days = {day[1] for day in self.customer_order[customer]}
        days = self.days.keys()
        return days - customer_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
