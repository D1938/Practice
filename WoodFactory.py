class Furniture:
    sn = 1
    list_furniture = []
    def __init__(self, price= None, sn=None):
        self.price = price + 10
        self.sn = Furniture.sn
        Furniture.list_furniture.append(self)
        Furniture.sn +=1
    @classmethod
    def get_list(cls):
        for i in Furniture.list_furniture:
            i.price = i.price+10
            print(vars(i))



class Table(Furniture):
    def __init__(self, size=None, geometry=None, price= None, sn=None):
        super().__init__(price,sn)


        self.size = size
        self.geometry = geometry
    def __str__(self):
        return str(vars(self))


class Chair(Furniture):
    def __init__(self, color = None, price=None, sn=None):
        super().__init__(price, sn)
        self.color = color

    def __str__(self):
        return str(vars(self))





if __name__ == "__main__":
    table_1 = Table(size=2, geometry="round", price=10)
    chair_1 = Chair(color="Black", price=20)
    print(table_1)
    print(chair_1)
    Furniture.get_list()