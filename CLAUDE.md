# telegram-eslatma-bot

Maqsudxon uchun shaxsiy Telegram eslatma boti: har kuni belgilangan vaqtlarda
(05:30 dan 22:00 gacha) kun tartibi bo'yicha motivatsion eslatmalar yuboradi.

## Muloqot qoidalari
- Egasi bilan **o'zbek tilida** gaplash.
- Bot xabarlari ham o'zbek tilida, emoji bilan, iliq va rag'batlantiruvchi ohangda.

## Tuzilishi
- `bot_eslatma.py` — butun bot (bitta fayl):
  - `/start`, `/test` buyruqlari (python-telegram-bot 22.1, async).
  - `schedule_tasks` ro'yxati — `("HH:MM", "matn")` juftliklari. Eslatma qo'shish/o'zgartirish shu yerda.
  - `schedule` kutubxonasi alohida thread'da ishlaydi va xabarni
    `asyncio.run_coroutine_threadsafe` orqali asosiy loop'ga yuboradi.
- `requirements.txt` — aniq versiyalar bilan bog'liqliklar (UTF-8).

## Ishga tushirish
```bash
export TOKEN="<BotFather tokeni>"
python bot_eslatma.py
```
- `TOKEN` — majburiy muhit o'zgaruvchisi. **Tokenni hech qachon kodga yoki gitga yozma.**
- `CHAT_ID` — xabarlar yuboriladigan chat (hozircha kodda qattiq yozilgan).
- Vaqtlar server vaqt zonasida ishlaydi. Render serveri UTC'da bo'lsa, eslatmalar
  Toshkent vaqtidan 5 soat farq qiladi — vaqt bilan bog'liq o'zgarishda buni hisobga ol.
- Joylash: Render (TOKEN Render → Environment bo'limida saqlanadi).

## Tekshirish
- Lint: `python -m pyflakes bot_eslatma.py`
- Testlar hozircha yo'q.
- Bulut sessiyasida `.claude/hooks/session-start.sh` bog'liqliklarni `.venv` ga o'rnatadi
  (tizimdagi `cryptography` buzilgan, shuning uchun venv ishlatiladi).
- Bulut konteyneri `api.telegram.org` ga ulanolmaydi — botni bu yerda to'liq ishga
  tushirib bo'lmaydi; `403 Forbidden` proksi xatosi kutilgan holat.
