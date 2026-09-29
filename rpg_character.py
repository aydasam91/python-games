import random
import time

def create_character():
    races = {
        "انسان": {"قدرت": 5, "هوش": 7, "سرعت": 6},
        "الف": {"قدرت": 4, "هوش": 9, "سرعت": 8},
        "اورک": {"قدرت": 9, "هوش": 3, "سرعت": 4},
        "کوتوله": {"قدرت": 7, "هوش": 5, "سرعت": 3},
        "اژدها": {"قدرت": 10, "هوش": 6, "سرعت": 5}
    }
    
    classes = {
        "جنگجو": {"قدرت": 3, "هوش": 0, "سرعت": 1},
        "جادوگر": {"قدرت": 0, "هوش": 3, "سرعت": 1},
        "دزد": {"قدرت": 1, "هوش": 1, "سرعت": 3},
        "شفادهنده": {"قدرت": 0, "هوش": 2, "سرعت": 2},
        "شکارچی": {"قدرت": 2, "هوش": 1, "سرعت": 2}
    }
    
    titles = [
        "شکست‌ناپذیر", "سایه", "آتشین", "یخی", "طوفان", 
        "تاریک", "نورانی", "افسانه‌ای", "کشنده", "جاودان"
    ]
    
    race = random.choice(list(races.keys()))
    char_class = random.choice(list(classes.keys()))
    title = random.choice(titles)
    
    name = input("اسم کاراکترت چیه؟ ")
    
    print()
    print("در حال ساخت کاراکتر...")
    time.sleep(1)
    print()
    
    race_stats = races[race]
    class_stats = classes[char_class]
    
    power = race_stats["قدرت"] + class_stats["قدرت"]
    intelligence = race_stats["هوش"] + class_stats["هوش"]
    speed = race_stats["سرعت"] + class_stats["سرعت"]
    
    hp = power * 10 + 50
    mana = intelligence * 10 + 30
    
    print("╔══════════════════════════════╗")
    print("║      کاراکتر تو ساخته شد!      ║")
    print("╚══════════════════════════════╝")
    print()
    print("📛 اسم:", name, "the", title)
    print("🧬 نژاد:", race)
    print("⚔️  کلاس:", char_class)
    print()
    print("--- آمار ---")
    print("💪 قدرت:", power)
    print("🧠 هوش:", intelligence)
    print("⚡ سرعت:", speed)
    print()
    print("❤️  سلامتی:", hp)
    print("🔮 مانا:", mana)
    print()
    
    if power > 10:
        print("🔥 قدرتت فوق‌العاده‌ست!")
    if intelligence > 10:
        print("🎓 هوشت خیره‌کننده‌ست!")
    if speed > 10:
        print("💨 سرعتت باورنکردنیه!")

create_character()
