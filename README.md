# 🤖 بوت تليجرام لزيادة المشاهدات والإعجابات على تيك توك

هذا البوت معدل للعمل على منصة Render بدون مشاكل التوافق.

## ✨ التغييرات التي تم إجراؤها:

1. إزالة dependency `user-agent` واستبدالها بقائمة ثابتة من User-Agents
2. تغيير إصدار Python إلى 3.11.0 للتأكد من التوافق
3. إضافة دعم لـ Flask وGunicorn للعمل على Render
4. تحسين معالجة الأخطاء وإضافة logging

## 🚀 طريقة النشر على Render:

1. انسخ هذه الملفات إلى مستودع GitHub
2. سجل الدخول إلى [Render](https://render.com/)
3. انقر على "New +" واختر "Web Service"
4. صلح مع حساب GitHub واختر المستودع
5. في إعدادات النشر:
   - **Name**: `tiktok-throw-bot`
   - **Environment**: Python 3
   - **Region**: اختر الأقرب لك
   - **Branch**: main
   - **Root Directory**: اتركه فارغاً
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn bot:app -b 0.0.0.0:$PORT --timeout 600`
6. في Environment Variables:
   - أضف `TELEGRAM_BOT_TOKEN` مع توكن البوت من BotFather
7. انقر على "Create Web Service"

## 📋 ملاحظات:

- البوت الآن يعمل بنمط Polling ولا يحتاج إلى webhook
- تمت إضافة timeouts لطلبات HTTP لمنع التجميد
- السكريبت سيعمل تلقائياً عند النشر

## 📞 الدعم:

لأي استفسارات: [@XRR60](https://t.me/xrr60)
