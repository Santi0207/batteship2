from .type_user import Type_User
from .user_dto import UserDTO

class User:
    def __init__(self,data, id:int, type_user:Type_User):
        if 'email' in data and 'password' in data:
            self.email = data['email']
            self.password = data['password']
            self.type_user = type_user
            self.id = id
        else:
            raise Exception ('los datos ingresados no son validos para crear el usuario')

    def toUserDTO(self):
        return UserDTO(self.email,self.type_user.description)