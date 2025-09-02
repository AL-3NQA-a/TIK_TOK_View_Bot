import os
import time
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import requests
from user_agent import generate_user_agent

# إعدادات التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# تعريف الألوان للنصوص (للتنسيق في التيرمينال)
R = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
RESET = '\033[0m'

# وظيفة البداية
async def start(update: Update, context: CallbackContext) -> None:
    welcome_text = '''
•••••••••••••••••••••Yusef•••••••••••••••••••••••••

⌯ 1 - Throw   Views  TikTok

⌯ 2 - Throw   Likes    TikTok

•••••••••••••••••••••Yusef•••••••••••••••••••••••••
    '''
    await update.message.reply_text(welcome_text)

# وظيفة معالجة الرسائل النصية
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.strip()
    
    if user_input == '1':
        await update.message.reply_text("أدخل رابط الفيديو لزيادة المشاهدات:")
        context.user_data['action'] = 'views'
    elif user_input == '2':
        await update.message.reply_text("أدخل رابط الفيديو لزيادة الإعجابات:")
        context.user_data['action'] = 'likes'
    elif 'action' in context.user_data:
        if context.user_data['action'] == 'views':
            await process_views(update, context, user_input)
        elif context.user_data['action'] == 'likes':
            await process_likes(update, context, user_input)
    else:
        await update.message.reply_text("يرجى اختيار 1 للمشاهدات أو 2 للإعجابات")

# معالجة طلبات زيادة المشاهدات
async def process_views(update: Update, context: CallbackContext, link: str) -> None:
    await update.message.reply_text("جاري المعالجة... انتظر 60 ثانية 🕑")
    
    # محاكاة الانتظار (يمكن إزالته في الإصدار النهائي)
    time.sleep(2)
    
    try:
        cookies = {
            'trsdb': '1',
            'ci_session': 'd8181db98c74ba288005e95b60781a7d6bbacb9c',
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D',
            'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1786780560357%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1755244560776%2C%22e%22%3A1786780562216%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2297%22%2C%22e%22%3A1786780560357%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%2212%22%2C%22e%22%3A1786780560357%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%221cc48343-de36-40d8-aff4-b84c5c6b5deb%22%2C%22e%22%3A1786780560357%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221755244560357%22%2C%22e%22%3A1786780560357%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22936743970%22%2C%22e%22%3A1755246360357%7D%7D',
        }
        
        headers = {
            'authority': 'leofame.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar-AE;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://leofame.com',
            'referer': 'https://leofame.com/ar/free-tiktok-views',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
        }
        
        params = {'api': '1'}
        
        data = {
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'timezone_offset': 'Asia/Baghdad',
            'free_link': link,
            'quantity': '200',
        }
        
        response = requests.post(
            'https://leofame.com/ar/free-tiktok-views',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        
        if '"success"' in response.text:
            await update.message.reply_text("تم إرسال المشاهدات بنجاح ✅")
        else:
            await update.message.reply_text("فشل في إرسال المشاهدات ❌")
            
    except Exception as e:
        logger.error(f"Error in process_views: {e}")
        await update.message.reply_text("حدث خطأ أثناء المعالجة ❌")
    
    # مسح حالة المستخدم
    context.user_data.clear()

# معالجة طلبات زيادة الإعجابات
async def process_likes(update: Update, context: CallbackContext, link: str) -> None:
    await update.message.reply_text("جاري المعالجة... انتظر 60 ثانية 🕑")
    
    # محاكاة الانتظار (يمكن إزالته في الإصدار النهائي)
    time.sleep(2)
    
    try:
        cookies = {
            'trsdb': '1',
            'ci_session': 'd8181db98c74ba288005e95b60781a7d6bbacb9c',
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%224%22%7D%7D',
            'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%223729%22%2C%22e%22%3A1786782091115%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1755246091398%2C%22e%22%3A1786782092966%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%22106%22%2C%22e%22%3A1786782081691%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%2212%22%2C%22e%22%3A1786782081691%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%221cc48343-de36-40d8-aff4-b84c5c6b5deb%22%2C%22e%22%3A1786782081691%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221755246081691%22%2C%22e%22%3A1786782081691%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22936743970%22%2C%22e%22%3A1755247881691%7D%7D',
        }
        
        headers = {
            'authority': 'leofame.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar-AE;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://leofame.com',
            'referer': 'https://leofame.com/ar/free-tiktok-likes',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
        }
        
        params = {'api': '1'}
        
        data = {
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'timezone_offset': 'Asia/Baghdad',
            'free_link': link,
        }
        
        response = requests.post(
            'https://leofame.com/ar/free-tiktok-likes',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        
        if '"success"' in response.text:
            await update.message.reply_text("تم إرسال 10 إعجابات بنجاح ✅")
        else:
            await update.message.reply_text("فشل في إرسال الإعجابات ❌")
            
    except Exception as e:
        logger.error(f"Error in process_likes: {e}")
        await update.message.reply_text("حدث خطأ أثناء المعالجة ❌")
    
    # مسح حالة المستخدم
    context.user_data.clear()

# وظيفة الرئيسية
def main() -> None:
    # الحصول على توكن البوت من متغير البيئة
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("لم يتم تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة")
        return
    
    # إنشاء التطبيق
    application = Application.builder().token(token).build()
    
    # إضافة معالجات الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # بدء البوت
    application.run_polling()

if __name__ == '__main__':
    main()
