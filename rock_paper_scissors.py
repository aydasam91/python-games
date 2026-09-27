rock_paper_scissors.py
import random

def get_computer_choice():
    return random.choice(["سنگ", "کاغذ", "قیچی"])

def check_winner(user, computer):
    if user == computer:
        return "مساوی"
    elif (user == "سنگ" and computer == "قیچی") or (user == "کاغذ" and computer == "سنگ") or (user == "قیچی" and computer == "کاغذ"):
        return "تو بردی"
    else:
        return "کامپیوتر برد"

user_score = 0
computer_score = 0

for i in range(3):
    print("--- دست", i + 1, "---")
    user = input("سنگ، کاغذ یا قیچی؟ ")
    computer = get_computer_choice()
    print("کامپیوتر:", computer)
    result = check_winner(user, computer)
    print(result)
    
    if result == "تو بردی":
        user_score = user_score + 1
    elif result == "کامپیوتر برد":
        computer_score = computer_score + 1

print("--- نتیجه نهایی ---")
print("امتیاز تو:", user_score)
print("امتیاز کامپیوتر:", computer_score)
