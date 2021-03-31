class Child:
    def __init__(self, food_cost: int, *args):
        result = food_cost + sum(args)
        self.cost = result

    def get_monthly_expense(self):
        return self.cost * 30