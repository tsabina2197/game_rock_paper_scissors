---

# Tosh-Qaychi-Qog'oz O'yini (Rock-Paper-Scissors Game)

## Ta'rif

Bu dastur **Tosh-Qaychi-Qog'oz** o'yini (rock-paper-scissors) bo'lib, unda foydalanuvchi kompyuterga qarshi o'ynaydi. O'yin oddiy: Tosh qaychini yutadi, qaychi qog'ozni yutadi, va qog'oz toshni yutadi. Har bir raqamni tanlash orqali o'yin davomida kim yutganini bilib olishingiz mumkin.

## Boshlash

### Talablar

* Python 3.6+ versiyasi

### O'rnatish

1. Kodni nusxalash va o'z kompyuteringizga saqlash.
2. Terminal yoki konsolda `main.py` faylini ishga tushiring:

   ```bash
   python main.py
   ```

### Foydalanish

O'yin boshlanishi bilan sizdan quyidagi tanlovlar so'raladi:

* **t** - Tosh
* **q** - Qaychi
* **g** - Qog'oz
* **x** yoki **exit** - O'yindan chiqish

### Qoidalar

* Tosh qaychini yutadi
* Qaychi qog'ozni yutadi
* Qog'oz toshni yutadi
* Agar foydalanuvchi va kompyuter bir xil tanlovni qilsa, bu **durrang** deb ataladi.

### O'yin Jarayoni

1. Foydalanuvchi biror tanlovni qiladi.
2. Kompyuter tasodifiy tanlov qiladi.
3. Natija aniqlanadi va hisob yangilanadi.
4. O'yin davom etadi, foydalanuvchi **x** yoki **exit** deb kiritsa, o'yin yakunlanadi.

### Misol

```bash
Tanlov (t=tosh, q=qaychi, g=qog'oz, qutish uchun 'x'): t
Siz: tosh | Kompyuter: qaychi -> Yutdingiz
Hisob: Siz 1 : 0 Kompyuter (raundlar: 1)
```

## Kod Tavsifi

* **`CHOICES`**: Foydalanuvchining tanlovlari va ularning nomlari ro'yxati.
* **`decide_winner()`**: Foydalanuvchi va kompyuterning tanlovlariga qarab kim yutganini aniqlaydi.
* **`prompt_choice()`**: Foydalanuvchidan tanlovni olish va noto'g'ri kiritilgan qiymatlarni qayta so'rash.
* **`game_loop()`**: O'yinning asosiy tsikli, foydalanuvchi va kompyuter o'rtasida raqobatni davom ettiradi.

## O'yin Yutish

* Har bir to'g'ri tanlovda foydalanuvchi yoki kompyuter ball olishadi.
* O'yin davomida **hisob** yangilanib boradi.

## O'yindan Chiqish

O'yindan chiqish uchun quyidagi buyruqlardan birini kiriting:

* **x**
* **exit**
* **q**


