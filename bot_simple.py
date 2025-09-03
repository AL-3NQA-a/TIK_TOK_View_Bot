import os
import time
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import requests

# إعدادات التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# قائمة User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36"
]

async def start_command(update: Update, context: CallbackContext) -> None:
    welcome_text = '''
•••••••••••••••••••••Yusef•••••••••••••••••••••••••

⌯ 1 - Throw   Views  TikTok

⌯ 2 - Throw   Likes    TikTok

•••••••••••••••••••••Yusef•••••••••••••••••••••••••
    '''
    await update.message.reply_text(welcome_text)

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

async def process_views(update: Update, context: CallbackContext, link: str) -> None:
    await update.message.reply_text("جاري المعالجة... انتظر 60 ثانية 🕑")
    time.sleep(2)
    
    try:
        headers = {
            'authority': 'leofame.com',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://leofame.com',
            'referer': 'https://leofame.com/ar/free-tiktok-views',
            'user-agent': random.choice(USER_AGENTS),
        }
        
        data = {
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'timezone_offset': 'Asia/Baghdad',
            'free_link': link,
            'quantity': '200',
        }
        
        response = requests.post(
            'https://leofame.com/ar/free-tiktok-views',
            headers=headers,
            data=data,
            timeout=30
        )
        
        if '"success"' in response.text:
            await update.message.reply_text("✅ تم إرسال المشاهدات بنجاح")
        else:
            await update.message.reply_text("❌ فشل في إرسال المشاهدات")
            
    except Exception as e:
        logger.error(f"Error in process_views: {e}")
        await update.message.reply_text("❌ حدث خطأ أثناء المعالجة")
    
    context.user_data.clear()

async def process_likes(update: Update, context: CallbackContext, link: str) -> None:
    await update.message.reply_text("جاري المعالجة... انتظر 60 ثانية 🕑")
    time.sleep(2)
    
    try:
        headers = {
            'authority': 'leofame.com',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://leofame.com',
            'referer': 'https://leofame.com/ar/free-tiktok-likes',
            'user-agent': random.choice(USER_AGENTS),
        }
        
        data = {
            'token': 'ba32154da67cdd18110b5b5e8aa22f46',
            'timezone_offset': 'Asia/Baghdad',
            'free_link': link,
        }
        
        response = requests.post(
            'https://leofame.com/ar/free-tiktok-likes',
            headers=headers,
            data=data,
            timeout=30
        )
        
        if '"success"' in response.text:
            await update.message.reply_text("✅ تم إرسال 10 إعجابات بنجاح")
        else:
            await update.message.reply_text("❌ فشل في إرسال الإعجابات")
            
    except Exception as e:
        logger.error(f"Error in process_likes: {e}")
        await update.message.reply_text("❌ حدث خطأ أثناء المعالجة")
    
    context.user_data.clear()

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("❌ TELEGRAM_BOT_TOKEN not set in environment variables")
        return
    
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("🤖 Starting bot in polling mode...")
    application.run_polling()

if __name__ == '__main__':
    main()
