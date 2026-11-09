# Layout Fixer 4.0

**Author:** Khayom  
**Version:** 4.0  
**Updated:** 2026-11-09  
**Type:** Offline, single-page keyboard-layout correction tool

## Overview

Layout Fixer corrects text typed with the wrong keyboard layout. It supports Russian, English, and Tajik keyboard mappings. It is a layout converter, not a language translator: it changes characters according to keyboard-key positions and does not translate meaning.

## Features

- Automatic mode (`AUTO`) is selected by default when the page opens.
- Manual conversion directions: RU → EN, EN → RU, TJ → EN, and EN → TJ.
- Interface languages: English, Russian, and Tajik.
- One-tap clear (`×`) control in the input panel.
- Copy control located below the output text.
- Swap, paste, import `.txt`, download result, and recent conversion history.
- Dark/light appearance.
- Local processing; no external libraries or network service required.

## Files

- `index.html` — the complete application.
- `README.md` — project information and version history.

Keep both files in the same directory so the README link in the application footer works.

## Run locally on Android (Termux)

```bash
cd ~/layout-fixer
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/` in the phone browser. Keep the Termux server process running while using the page.

## Version history

### 4.0 — 2026-11-09

- Set `AUTO` as the initial conversion mode.
- Added a dedicated clear (`×`) button to the input panel.
- Moved the copy action into the output panel footer.
- Added author, version, update information, and a README link to the page footer.
- Retained the three-language interface and offline single-file application structure.

### 3.0 — 2026-11-09

- Added English, Russian, and Tajik interface languages.
- Added Tajik keyboard mapping and automatic text detection.

## Update policy

For every release, update the version shown in `index.html` and add a dated entry under **Version history** in this file. Keep `index.html` and `README.md` together in the project directory.

---

# Тоҷикӣ

**Муаллиф:** Khayom  
**Версия:** 4.0  
**Навсозӣ:** 09.11.2026

Layout Fixer матнеро ислоҳ мекунад, ки бо раскладкаи нодурусти клавиатура чоп шудааст. Барнома забонро тарҷума намекунад; он танҳо аломатҳоро мувофиқи ҷойгиршавии тугмаҳои клавиатура иваз мекунад. Забонҳои дастгиришаванда: тоҷикӣ, русӣ ва англисӣ.

### Имкониятҳо

- Ҳангоми кушодан реҷаи `AUTO` фаъол аст.
- Самтҳои дастӣ: RU → EN, EN → RU, TJ → EN ва EN → TJ.
- Интерфейс бо се забон: тоҷикӣ, русӣ ва англисӣ.
- Тугмаи `×` барои пок кардани матни воридотӣ.
- Тугмаи нусхабардорӣ дар поёни натиҷа.
- Иваз кардани самт, гузоштан, воридоти `.txt`, боргирии натиҷа ва таърихи табдилҳо.
- Реҷаи равшан ва торик.
- Коркард дар худи дастгоҳ, бе китобхонаҳои беруна ва бе интернет.

### Таърихи версияҳо

- **4.0 — 09.11.2026:** AUTO ҳамчун реҷаи ибтидоӣ; тугмаи поккунӣ; нусхабардорӣ дар қисми натиҷа; маълумоти муаллиф ва версия дар поёни саҳифа.
- **3.0 — 09.11.2026:** иловаи интерфейси тоҷикӣ, русӣ ва англисӣ; харитаи клавиатураи тоҷикӣ ва муайянкунии худкор.

### Тартиби навсозӣ

Ҳангоми ҳар навсозӣ рақами версияро дар `index.html` тағйир диҳед ва дар ҳамин файл, дар бахши таърихи версияҳо, сана ва тағйиротро илова кунед. Файлҳои `index.html` ва `README.md` бояд дар як папка бошанд.

---

# Русский

**Автор:** Khayom  
**Версия:** 4.0  
**Обновлено:** 09.11.2026

Layout Fixer исправляет текст, набранный при неверно выбранной раскладке клавиатуры. Это не переводчик: программа заменяет символы по расположению клавиш. Поддерживаются русский, английский и таджикский варианты раскладки.

### Возможности

- При запуске по умолчанию включён режим `AUTO`.
- Ручные направления: RU → EN, EN → RU, TJ → EN и EN → TJ.
- Интерфейс на русском, английском и таджикском языках.
- Кнопка `×` для очистки поля ввода.
- Кнопка копирования под полем результата.
- Обмен полей, вставка, импорт `.txt`, скачивание результата и история.
- Светлая и тёмная темы.
- Локальная обработка без внешних библиотек и подключения к интернету.

### История версий

- **4.0 — 09.11.2026:** AUTO по умолчанию; очистка поля ввода; копирование под результатом; информация об авторе и версии внизу страницы.
- **3.0 — 09.11.2026:** английский, русский и таджикский интерфейс; таджикская раскладка и автоматическое определение.

### Правила обновления

При каждом выпуске обновляйте номер версии в `index.html` и добавляйте дату и список изменений в этот README. Храните оба файла в одной папке.
