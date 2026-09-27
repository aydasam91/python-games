import random

def get_response(user_input):
    user_input = user_input.lower()
    
    if "سلام" in user_input:
        return random.choice(["سلام!", "سلام به روی ماهت!", "چه خبر؟"])
    
    elif "اسمت چیه" in user_input or "اسمت" in user_input:
        return "من یه رباتم. اسمم «چت‌بات»ه!"
    
    elif "چطوری" in user_input or "حالت" in user_input:
        return random.choice(["خوبم، مرسی!", "عالی! تو چطوری؟", "به خوبی تو!"])
    
    elif "سن" in user_input:
        return "من تازه متولد شدم! چند دقیقه‌ای بیشتر سن ندارم."
    
    elif "خداحافظ" in user_input or "بای" in user_input:
        return "خداحافظ! مراقب خودت باش."
    
    elif "کمک" in user_input:
        return "چیکار می‌تونم برات بکنم؟"
    
    elif "برنامه‌نویسی" in user_input:
        return "برنامه‌نویسی عالیه! من هم با پایتون ساخته شدم."
    
    else:
        return random.choice([
            "متوجه نشدم! یه چیز دیگه بگو.",
            "جالبه! ادامه بده.",
            "می‌تونی واضح‌تر بگی؟"
        ])

def chat():
    print("=== ربات چت ===")
    print("سلام! من یه رباتم. باهات حرف می‌زنم.")
    print("برای خروج بنویس: خداحافظ")
    print()
    
    while True:
        user = input("تو: ")
        
        if "خداحافظ" in user or "بای" in user:
            print("ربات:", get_response(user))
            break
        
        response = get_response(user)
        print("ربات:", response)

chat()
