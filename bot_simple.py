import os
import time
import logging
import random
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import requests

# إصلاح مشكلة encoding
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# إعدادات التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# قائمة User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
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
    try:
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
    except Exception as e:
        logger.error(f"Error in handle_message: {e}")

# ... [بقية الدوال كما هي] ...

def main():
    try:
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not token:
            logger.error("❌ TELEGRAM_BOT_TOKEN not set")
            return
        
        application = Application.builder().token(token).build()
        
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("🤖 Starting bot in polling mode...")
        application.run_polling()
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")

if __name__ == '__main__':
    main()
