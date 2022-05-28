from model.user import User,Type_User
import random

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

    def game(self):
        opcion1 = ['Piedra', 'Papel', 'Tijeras', 'SPOCK', 'Lagarto']
        opcion2 = ['Piedra', 'Papel', 'Tijeras', 'SPOCK', 'Lagarto']
        player1 = random.choice(opcion1)
        player2 = random.choice(opcion2)
# Output for rock
        res =""
        if player1 == "Piedra" and player2 == "Tijeras":
            res ="Rock crushes scissors, the Player wins!"
        if player1 == "Tijeras" and player2 == "Piedra":
            res="Rock crushes scissors, the Computer wins!"
        if player1 == "Piedra" and player2 == "Papel":
            res="Paper covers rock, the Computer wins!"
        if player1 == "Papel" and player2 == "Piedra":
            res="Paper covers rock, the Player wins!"
        if player1 == "Piedra" and player2 == "SPOCK":
            res="Spock vaporizes rock, the Computer wins!"
        if player1 == "SPOCK" and player2 == "Piedra":
            res="Spock vaporizes rock, the Player wins!"
        if player1 == "Piedra" and player2 == "Lagarto":
            res="Rock crushes lizard, the Player wins!"
        if player1 == "Lagarto" and player2 == "Piedra":
            res="Rock crushes lizard, the Computer wins!"
# Output for paper
        if player1 == "Papel" and player2 == "Lagarto":
            res="Lizard eats paper, the Computer wins!"
        if player1 == "Lagartp" and player2 == "Papel":
            res="Lizard eats paper, the Player wins!"
        if player1 == "Papel" and player2 == "Tijeras":
            res="Scissors cuts paper, the Computer wins!"
        if player1 == "Tijeras" and player2 == "Papeles":
            res="Scissors cuts paper, the Player wins!"
        if player1 == "Papel" and player2 == "SPOCK":
            res="Paper disproves spock, the Player wins!"
        if player1 == "SPOCK" and player2 == "Papel":
            res="Paper disproves spock, the Computer wins!"
# Output for scissors
        if player1 == "Tijeras" and player2 == "SPOCK":
            res="Spock smashes scissors, the Computer wins!"
        if player1 == "SPOCK" and player2 == "Tijeras":
            res="Spock smashes scissors, the Computer wins!"
        if player1 == "Tijeras" and player2 == "Lagarto":
            res="Scissors decapitates lizard, the Player wins!"
        if player1 == "Lagarto" and player2 == "Tijeras":
            res="Scissors decapitates lizard, the Computer wins!"
        # Output for spock
        if player1 == "SPOCK" and player2 == "Lagarto":
            res="Lizard poisons spock, the Computer wins!"
        if player1 == "Lagarto" and player2 == "SPOCK":
            res="Lizard poisons spock, the Player wins!"
        if player1 == player2:
            res="It's a tie!"

        return {"player1":player1,"player2":player2,"result":res}