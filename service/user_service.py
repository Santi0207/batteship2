from model.user import User,Type_User

class UserService:
    def __init__(self):
        self.userList=[]
        self.userList.append(User({"email": "slope92755@umanizales.edu.co",
                                   "password": "10293847"}, 1, Type_User("1", "Administrador")))

    def get_users(self):
        list = []
        for user in self.userList:
            list.append(user.toUserDTO())
        return list

    def valide_user(self, email: str, administrador: bool, cantidad: int):
        cont = 0
        for user in self.userList:
            if user.email == email:
                return True
            if administrador and user.type_user.code == 1:
                return True
            if user.type_user.code == 2:
                cont += 1
        if administrador == False and cantidad == cont:
            return True
        return False

    def create_user(self,data):
        administrador = False
        if data['type_user']['code'] == 1:
            administrador = True
        if self.valide_user(data['email'],administrador,2):
            raise Exception('Las condiciones no son aptas para adiccionar al usuario')

    def login(self, data):
        for user in self.userList:
            if data['email'] == user.email and data['password'] == user.password:
                return user
        return None


