import random
import time

def show_dice(number):
    if number == 1:
        print("┌─────┐")
        print("│     │")
        print("│  ●  │")
        print("│     │")
        print("└─────┘")
    elif number == 2:
        print("┌─────┐")
        print("│ ●   │")
        print("│     │")
        print("│   ● │")
        print("└─────┘")
    elif number == 3:
        print("┌─────┐")
        print("│ ●   │")
        print("│  ●  │")
        print("│   ● │")
        print("└─────┘")
    elif number == 4:
        print("┌─────┐")
        print("│ ● ● │")
        print("│     │")
        print("│ ● ● │")
        print("└─────┘")
    elif number == 5:
        print("┌─────┐")
        print("│ ● ● │")
        print("│  ●  │")
        print("│ ● ● │")
        print("└─────┘")
    else:
        print("┌─────┐")
        print("│ ● ● │")
        print("│ ● ● │")
        print("│ ● ● │")
        print("└─────┘")

def play_game():
    user_score = 0
    computer_score = 0
    
    print("=== بازی تاس ===")
    print("هر کی تاس بزرگ‌تر بیاره، برنده‌ست!")
    print()
    
    for i in range(3):
        print("--- دست", i + 1, "---")
        input("برای انداختن تاس، اینتر بزن...")
        
        print("در حال انداختن تاس...")
        time.sleep(1)
        
        user_dice = random.randint(1, 6)
        computer_dice = random.randint(1, 6)
        
        print()
        print("تاس تو:")
        show_dice(user_dice)
        print("عدد:", user_dice)
        
        print()
        print("تاس کامپیوتر:")
        show_dice(computer_dice)
        print("عدد:", computer_dice)
        
        print()
        if user_dice > computer_dice:
            print("🎉 تو بردی این دست رو!")
            user_score = user_score + 1
        elif computer_dice > user_dice:
            print("😢 کامپیوتر برد این دست رو!")
            computer_score = computer_score + 1
        else:
            print("🤝 مساوی!")
        
        print()
        print("=" * 30)
    
    print()
    print("--- نتیجه نهایی ---")
    print("امتیاز تو:", user_score)
    print("امتیاز کامپیوتر:", computer_score)
    
    if user_score > computer_score:
        print("🏆 تو برنده بازی شدی!")
    elif computer_score > user_score:
        print("😢 کامپیوتر برنده شد!")
    else:
        print("🤝 مساوی شد!")

play_game()
