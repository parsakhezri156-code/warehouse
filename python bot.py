import telebot
import datetime
import random

# توکن بات رو اینجا بذار (از @BotFather بگیر)
BOT_TOKEN = "8124768100:AAH-k0b0SHHNwOeti1I7a8D0VcXkQzC3HvI"

# ساخت بات
bot = telebot.TeleBot(BOT_TOKEN)

# پیام خوش‌آمدگویی
@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.first_name
    welcome_text = f"""سلام {user_name}! 🤖
    
خوش اومدی به ربات هوشمند من!

دستورات موجود:
/help - راهنما
/time - زمان فعلی  
/joke - جوک بگو
/weather - آب و هوا
/about - درباره من

یا می‌تونی مستقیم با من چت کنی! 😊"""
    
    bot.reply_to(message, welcome_text)

# راهنما
@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = """📋 راهنمای کامل:

🤖 دستورات:
/start - شروع مجدد
/help - نمایش راهنما
/time - زمان و تاریخ فعلی
/joke - یک جوک تعریف کن
/weather - نمایش آب و هوا (نمونه)
/about - اطلاعات درباره بات

💬 چت آزاد:
می‌تونی هر چیزی بنویسی و من جواب میدم!
مثلاً: سلام، چطوری، اسمت چیه و ...

ساخته شده با ❤️"""
    
    bot.reply_to(message, help_text)

# زمان فعلی
@bot.message_handler(commands=['time'])
def time_message(message):
    now = datetime.datetime.now()
    persian_months = [
        'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 
        'مرداد', 'شهریور', 'مهر', 'آبان', 
        'آذر', 'دی', 'بهمن', 'اسفند'
    ]
    
    time_text = f"""🕐 زمان فعلی:
    
📅 تاریخ میلادی: {now.strftime('%Y/%m/%d')}
⏰ ساعت: {now.strftime('%H:%M:%S')}
📆 روز هفته: {now.strftime('%A')}
🌅 {now.strftime('%p')}"""
    
    bot.reply_to(message, time_text)

# جوک
@bot.message_handler(commands=['joke'])
def joke_message(message):
    jokes = [
        "چرا برنامه‌نویس‌ها قهوه دوست دارن؟ 🤔\nچون بدون کافئین کد نمی‌نویسن! ☕😄",
        
        "معلم: HTML چیه؟ 👩‍🏫\nدانش‌آموز: How To Meet Ladies! 😂",
        
        "چرا بات‌ها هیچوقت خسته نمی‌شن؟ 🤖\nچون اونا while True دارن! 🔄",
        
        "فرق برنامه‌نویس و جادوگر چیه? 🧙‍♂️\nجادوگر از راه دور کار می‌کنه! 😂",
        
        "چرا کامپیوتر سرد میشه؟ 🥶\nچون پنجره‌هاش همیشه بازه! 🪟",
        
        "بهترین زبان برنامه‌نویسی کدومه؟ 🤔\nزبان مادری! 😄",
        
        "Bug چیه؟ 🐛\nوقتی کدت کار می‌کنه ولی نمی‌دونی چرا! 🤷‍♂️"
    ]
    
    selected_joke = random.choice(jokes)
    bot.reply_to(message, selected_joke)

# آب و هوا (نمونه)
@bot.message_handler(commands=['weather'])
def weather_message(message):
    weather_text = """🌤️ آب و هوا امروز:

🏙️ تهران: آفتابی، ۲۳°C
🏔️ اصفهان: ابری، ۱۸°C  
🌊 بندرعباس: مرطوب، ۳۲°C
❄️ تبریز: سرد، ۱۰°C

⚠️ نکته: این فقط نمونه است
برای اطلاعات واقعی از API آب‌وهوا استفاده کنید"""
    
    bot.reply_to(message, weather_text)

# درباره بات
@bot.message_handler(commands=['about'])
def about_message(message):
    about_text = """ℹ️ درباره من:

🤖 نام: ربات هوشمند
📝 نسخه: 1.0
👨‍💻 سازنده: برنامه‌نویس عزیز شما
🐍 زبان: Python
📚 کتابخانه: pyTelegramBotAPI

قابلیت‌ها:
✅ پاسخ هوشمند به پیام‌ها
✅ دستورات کاربردی
✅ چت طبیعی
✅ شوخ‌طبعی و دوستانه

ساخته شده با عشق و Python! ❤️🐍"""
    
    bot.reply_to(message, about_text)

# پاسخ به پیام‌های عادی
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    user_name = message.from_user.first_name
    
    # پاسخ‌های هوشمند
    if any(word in text for word in ['سلام', 'hello', 'hi', 'درود']):
        responses = [
            f"سلام {user_name}! 👋 چطوری عزیزم؟",
            f"سلام و احوال {user_name}! 😊 حالت چطوره؟",
            f"هی {user_name}! 🤗 خوشحالم که اومدی"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in text for word in ['چطوری', 'حالت', 'خوبی']):
        responses = [
            "من که بات هستم، همیشه عالی‌ام! 😄 تو چطوری؟",
            "سالم و سلامت! 🤖 امیدوارم تو هم خوب باشی",
            "بات‌ها که خسته نمی‌شن! 😊 تو خوبی؟"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in text for word in ['اسمت', 'نام', 'کی هستی']):
        bot.reply_to(message, f"اسم من ربات هوشمنده! 🤖\nیک دستیار دیجیتال هستم که اینجا هستم تا کمکت کنم {user_name}!")
    
    elif any(word in text for word in ['ممنون', 'مرسی', 'تشکر']):
        responses = [
            f"خواهش می‌کنم {user_name}! 😊 کمک کردن وظیفه‌مه",
            "قابلی نداشت! 🤗 هر وقت کمک خواستی اینجام",
            "خوشحالم که مفید بودم! 😄"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in text for word in ['بای', 'خداحافظ', 'فعلا']):
        responses = [
            f"خداحافظ {user_name}! 👋 امیدوارم زودتر ببینمت",
            "بای بای! 😊 مراقب خودت باش",
            "تا دیدار دوباره! 🤗"
        ]
        bot.reply_to(message, random.choice(responses))
    
    elif any(word in text for word in ['عاشقتم', 'دوست دارم']):
        bot.reply_to(message, "ای بابا! 😅 منم دوستت دارم ولی من فقط یه بات هستم! 🤖❤️")
    
    elif 'چند سالته' in text or 'سنت' in text:
        bot.reply_to(message, "بات‌ها سن ندارن! 😄 ولی از لحاظ کد، تازه متولد شدم! 👶🤖")
    
    else:
        # پاسخ پیش‌فرض
        responses = [
            f"جالب بود {user_name}! 🤔 بیشتر توضیح بده",
            f"پیامت رو دریافت کردم: '{message.text}'\n/help رو بزن تا ببینی چی کار می‌تونم کنم! 📝",
            f"حرف جالبی زدی {user_name}! 😊 چیز دیگه‌ای می‌خوای بدونی؟",
            "هوم... 🤔 می‌تونی سوال واضح‌تری بپرسی؟"
        ]
        bot.reply_to(message, random.choice(responses))

# اجرای بات
if __name__ == "__main__":
    print("🤖 بات شروع شد...")
    print("برای توقف Ctrl+C بزنید")
    
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ ابتدا توکن بات رو از @BotFather بگیر و توی کد بذار!")
    else:
        print("✅ درحال اتصال...")
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"❌ خطا: {e}")
