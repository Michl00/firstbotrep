from dataclasses import dataclass

@dataclass
class User:
    uid: int
    name: str
    age: int

user1 = User(1, "Miles", 23)
user2 = User(2, "Jane", 19)

def info(user: User) -> str:
    return f"Имя: {user.name} \t Возраст: {user.age} \n"

print(info(user1), info(user2))