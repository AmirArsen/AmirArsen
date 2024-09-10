import telebot
from telebot import types

# توکن ربات خود را اینجا قرار دهید
TOKEN = '7357770137:AAFkxR7wPnGyfoM-Y2aEncUdSv8Xmom7_do'
bot = telebot.TeleBot(TOKEN)

# متغیر برای ذخیره اطلاعات کاربر
user_data = {}

# دستور /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # ساختن کیبورد چسبیده (ReplyKeyboardMarkup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # افزودن دکمه‌ها به کیبورد
    btn_info = types.KeyboardButton("اطلاعات کاربر")
    btn_ads = types.KeyboardButton("تبلیغات")
    btn_help = types.KeyboardButton("آموزش کار با ربات")
    btn_support = types.KeyboardButton("پشتیبانی")

    markup.add(btn_info, btn_ads)
    markup.add(btn_help, btn_support)
    
    bot.send_message(message.chat.id, "به ربات خوش آمدید! یک گزینه را انتخاب کنید:", reply_markup=markup)

# مدیریت پیام‌ها برای دکمه‌های کیبورد
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "اطلاعات کاربر":
        ask_for_fullname(message)
    elif message.text == "تبلیغات":
        send_ads(message)
    elif message.text == "آموزش کار با ربات":
        send_help_video(message)
    elif message.text == "پشتیبانی":
        send_support_video(message)

# دریافت اطلاعات کاربر
def ask_for_fullname(message):
    bot.send_message(message.chat.id, "لطفاً نام کامل خود را وارد کنید:")
    bot.register_next_step_handler(message, get_fullname)

def get_fullname(message):
    user_data[message.chat.id] = {'name': message.text}
    bot.send_message(message.chat.id, "لطفاً شماره تماس خود را وارد کنید:")
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    user_data[message.chat.id]['phone'] = message.text
    bot.send_message(message.chat.id, "لطفاً ایمیل خود را وارد کنید:")
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    user_data[message.chat.id]['email'] = message.text
    bot.send_message(message.chat.id, f"اطلاعات شما ثبت شد:\n"
                                      f"نام: {user_data[message.chat.id]['name']}\n"
                                      f"شماره تماس: {user_data[message.chat.id]['phone']}\n"
                                      f"ایمیل: {user_data[message.chat.id]['email']}")

# ارسال تبلیغات و بررسی عضویت کاربر در کانال
def send_ads(message):
    bot.send_message(message.chat.id, "تبلیغات به زودی افزوده خواهد شد.")

# ارسال ویدیوی آموزش
def send_help_video(message):
    video_path = 'path_to_help_video.mp4'  # مسیر فایل ویدیو
    with open(video_path, 'rb') as video:
        bot.send_video(message.chat.id, video)

# ارسال ویدیوی پشتیبانی
def send_support_video(message):
    video_path = 'path_to_support_video.mp4'  # مسیر فایل ویدیو
    with open(video_path, 'rb') as video:
        bot.send_video(message.chat.id, video)

# اجرای ربات
bot.infinity_polling()
