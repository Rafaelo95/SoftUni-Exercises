from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for r in self.rooms:
            result += r.cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        res = []
        for r in self.rooms:
            if r.budget >= r.cost:
                res.append(f"{r.family_name} paid {r.cost:.2f}$ and have {r.budget:.2f}$ left.")
                r.budget -= r.cost
            else:
                self.rooms.remove(r)
                res.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(res)

    def status(self):
        all_people_in_hotel = sum([r.members_count for r in self.rooms])
        return '\n'.join([f'Total population: {all_people_in_hotel}'] +
                         list(map(str, self.rooms)))


