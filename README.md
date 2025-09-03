# 🤖 بوت تليجرام لزيادة المشاهدات والإعجابات على تيك توك

هذا البوت معدل للعمل على منصة Render كـ Worker.

## 🚀 طريقة النشر على Render:

1. **أنشئ Worker Service**:
   - في Render، انقر على "New +"
   - اختر "Worker" (ليس Web Service)
   - اربط بمستودع GitHub

2. **الإعدادات**:
   - **Name**: `tiktok-throw-bot`
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot_simple.py`

3. **Environment Variables**:
   - `TELEGRAM_BOT_TOKEN`: توكن البوت من BotFather

## 📋 ملاحظات:

- البوت يعمل بنمط Polling ولا يحتاج إلى webhook
- تمت إزالة dependency `user-agent` واستبدالها بقائمة ثابتة
- تم تحسين معالجة الأخطاء وإضافة logging

## 🔧 إذا لم يعمل:

1. تحقق من logs في Render
2. تأكد من صحة توكن البوت
3. تأكد أن البوت ليس في "Privacy Mode"

## 📞 الدعم:

لأي استفسارات: [@XRR60](https://t.me/xrr60)
