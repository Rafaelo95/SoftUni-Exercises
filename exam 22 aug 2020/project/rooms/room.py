class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, val):
        if val < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = val

    def calculate_expenses(self, *args):
        for item in args:
            for i in item:
                self.expenses += i.get_monthly_expense()

    @property
    def cost(self):
        return self.expenses

    def __str__(self):
        return '\n'.join(
            [f'{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$']
            +
            [f'--- Child {i + 1} monthly cost: {c.get_monthly_expense():.2f}$' for i, c in enumerate(self.children)]
            +
            [f'--- Appliances monthly cost: {sum(seq.get_monthly_expense() for seq in self.appliances):.2f}$'])