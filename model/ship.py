class Ship:
    def __init__(self,data, id:int):
        if 'name' in data and 'num_places' in data:
            self.name = data ['name']
            self.name_places = data['num_places']
            self.id = id
        else:
            raise Exception ("Los atributos no son validos para el barco")
