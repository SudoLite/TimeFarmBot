
[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/SudoLite)

![img1](.github/images/demo.png)

## عملکرد
| عملکرد                                                        | پشتیبانی شده |
|---------------------------------------------------------------|:------------:|
| چند نخی                                                          |      ✅      |
| اتصال پروکسی به جلسه                                            |      ✅      |
| دریافت خودکار تمام وظایف به جز وظایف تلگرام                   |      ✅      |
| ارتقاء خودکار سطح برای سرعت بیشتر در جمع آوری                 |      ✅      |
| تکرار درخواست در هر دریافت                                      |      ✅      |
| پشتیبانی از tdata / pyrogram .session / telethon .session        |      ✅      |

## [تنظیمات](https://github.com/SudoLite/TimeFarmBot/blob/main/.env-example)
| تنظیمات                    | توضیحات                                                                     |
|----------------------------|------------------------------------------------------------------------------|
| **API_ID / API_HASH**      | داده‌های پلتفرم برای شروع یک جلسه تلگرام (پیش‌فرض - اندروید)               |
| **CLAIM_RETRY**            | تعداد تلاش‌ها در صورت ناموفق بودن **دریافت ها** _(مثال: 3)_                  |
| **SLEEP_BETWEEN_CLAIM**    | تأخیر بین **دریافت ها** به دقیقه _(مثال: 180)_                              |
| **AUTO_UPGRADE_FARM**      | باید افزایش سطح را انجام بدهم _(True / False)_                               |
| **MAX_UPGRADE_LEVEL**      | سظح آخر شما _(up to 4)_                                         |
| **USE_PROXY_FROM_FILE**    | آیا از پروکسی از فایل `bot/config/proxies.txt` استفاده شود (True / False)  |

## نصب
می‌توانید [**مخزن**](https://github.com/SudoLite/TimeFarmBot) را با کلون کردن به سیستم خود دانلود کرده و وابستگی‌های لازم را نصب کنید:
```shell
~ >>> git clone https://github.com/SudoLite/TimeFarmBot.git
~ >>> cd TimeFarmBot

# اگر از جلسات Telethon استفاده می‌کنید، شاخه "converter" را کلون کنید
~ >>> git clone https://github.com/SudoLite/TimeFarmBot.git -b converter
~ >>> cd TimeFarmBot

#لینوکس
~/TimeFarmBot >>> python3 -m venv venv
~/TimeFarmBot >>> source venv/bin/activate
~/TimeFarmBot >>> pip3 install -r requirements.txt
~/TimeFarmBot >>> cp .env-example .env
~/TimeFarmBot >>> nano .env # در اینجا باید API_ID و API_HASH خود را مشخص کنید، بقیه به طور پیش‌فرض گرفته می‌شوند
~/TimeFarmBot >>> python3 main.py

#ویندوز
~/TimeFarmBot >>> python -m venv venv
~/TimeFarmBot >>> venv\Scripts\activate
~/TimeFarmBot >>> pip install -r requirements.txt
~/TimeFarmBot >>> copy .env-example .env
~/TimeFarmBot >>> # API_ID و API_HASH خود را مشخص کنید، بقیه به طور پیش‌فرض گرفته می‌شوند
~/TimeFarmBot >>> python main.py
```

همچنین برای راه‌اندازی سریع می‌توانید از آرگومان‌ها استفاده کنید، به عنوان مثال:
```shell
~/TimeFarmBot >>> python3 main.py --action (1/2)
# یا
~/TimeFarmBot >>> python3 main.py -a (1/2)

#1 - ایجاد جلسه
#2 - اجرای کلیکر
```
