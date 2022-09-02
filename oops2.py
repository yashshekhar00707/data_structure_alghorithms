import csv
from oops import Item
class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # call to super function to have access to all the attributes/methods
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to 0"
        self.broken_phones = broken_phones

    @property
    def read_only_name(self):
        return "AAA"

phone1 = Item("jscPhonev10", 500, 5)
phone2 = Item("jscPhonev20", 700, 5)

Item.instantiate_from_csv()
print(Item.all)
