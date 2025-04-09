class Postman():
    def __init__(self):
        self.delivery_data = list()

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        if self.delivery_data:
            temp_list = [data[1] for data in self.delivery_data if data[0] == street]
            if temp_list:
                out_list = []
                for i in temp_list:
                    if i not in out_list:
                        out_list.append(i)
                return out_list
        return []

    def get_flats_for_house(self, street, house):
        if self.delivery_data:
            temp_list = [data[2] for data in self.delivery_data if data[0] == street and data[1] == house and data[2]]
            if temp_list:
                out_list = []
                for i in temp_list:
                    if i not in out_list:
                        out_list.append(i)
                return out_list
        return []


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))