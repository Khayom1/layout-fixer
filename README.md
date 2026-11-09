# Layout Fixer 4.0


<p align="center">
  <img src="assets/layout-fixer-banner.gif"
       alt="NetScope Animated Banner"
       width="100%">
</p>


**Author:** Khayom  
**Version:** 4.0  
**Updated:** 2026-11-09

Layout Fixer corrects text typed with the wrong keyboard layout. It supports Russian, English, and Tajik keyboard mappings. It is not a translator: it changes characters according to keyboard-key positions.

## Features

- `AUTO` mode selected by default.
- Manual directions: RU → EN, EN → RU, TJ → EN, EN → TJ.
- English, Russian, and Tajik interface.
- Clear (`×`) input and Copy output controls.
- Swap, paste, `.txt` import, result download, and conversion history.
- Dark/light themes.
- Local processing; no external libraries or network service required after download.

## Installation and usage

### Android — Termux

1. Install and open Termux.
2. Allow shared-storage access:

   ```bash
   termux-setup-storage
   ```

3. Install Git and Python:

   ```bash
   pkg update
   pkg install git python
   ```

4. Clone the project:

   ```bash
   git clone https://github.com/Khayom1/layout-fixer.git
   cd layout-fixer
   ```

5. Start the local server:

   ```bash
   python -m http.server 8000 --bind 127.0.0.1
   ```

6. Open this address in your phone browser:

   **http://127.0.0.1:8000/**

Keep Termux and the server running while using the app. To stop the server, return to Termux and press `CTRL + C`.

### Computer

Download or clone the repository. Keep `index.html` and `README.md` in the same folder, then open `index.html` in a modern browser.

If local-file restrictions prevent it from working, run this command inside the project folder:

```bash
python -m http.server 8000
```

Then open **http://localhost:8000/**.

## Updating

If installed using Git, run:

```bash
cd ~/layout-fixer
git pull origin main
```

Refresh the browser page after updating. If installed manually, download the latest `index.html` and `README.md` from the GitHub repository and replace the old files.

## Project files

- `index.html` — complete application.
- `README.md` — installation guide, project information, and version history.

Keep both files in the same directory so the README link in the application footer works.

## Version history

### 4.0 — 2026-11-09
- Set `AUTO` as the initial conversion mode.
- Added a clear (`×`) button to the input panel.
- Moved Copy below the output.
- Added author, version, update information, and README link to the footer.
- Retained the three-language interface and offline single-page structure.

### 3.0 — 2026-11-09
- Added English, Russian, and Tajik interface languages.
- Added Tajik keyboard mapping and automatic text detection.

## Update policy

For every release, update the version in `index.html` and add a dated entry under **Version history** in this file.

---

# Тоҷикӣ

**Муаллиф:** Khayom  
**Версия:** 4.0  
**Навсозӣ:** 09.11.2026

Layout Fixer матнеро ислоҳ мекунад, ки бо раскладкаи нодурусти клавиатура чоп шудааст. Ин барнома тарҷумон нест: он аломатҳоро мувофиқи ҷойгиршавии тугмаҳои клавиатура иваз мекунад.

## Насб дар Android бо Termux

1. Termux-ро насб ва кушоед.
2. Иҷозати хотираро диҳед:

   ```bash
   termux-setup-storage
   ```

3. Git ва Python-ро насб кунед:

   ```bash
   pkg update
   pkg install git python
   ```

4. Лоиҳаро аз GitHub гиред:

   ```bash
   git clone https://github.com/Khayom1/layout-fixer.git
   cd layout-fixer
   ```

5. Серверро фаъол кунед:

   ```bash
   python -m http.server 8000 --bind 127.0.0.1
   ```

6. Дар браузери телефон кушоед:

   **http://127.0.0.1:8000/**

Ҳангоми истифода Termux ва сервер бояд фаъол бошанд. Барои қатъ кардани сервер `CTRL + C`-ро пахш кунед.

## Насб дар компютер

Репозиторийро зеркашӣ ё clone кунед. `index.html` ва `README.md`-ро дар як папка нигоҳ доред ва `index.html`-ро дар браузери муосир кушоед.

Агар кушодани мустақими файл маҳдуд бошад, дар папкаи лоиҳа иҷро кунед:

```bash
python -m http.server 8000
```

Баъд **http://localhost:8000/**-ро кушоед.

## Навсозӣ

Агар лоиҳаро бо Git гирифта бошед:

```bash
cd ~/layout-fixer
git pull origin main
```

Баъд саҳифаро дар браузер нав кунед. Агар файлҳоро дастӣ гирифта бошед, версияҳои охирини `index.html` ва `README.md`-ро аз GitHub зеркашӣ карда, файлҳои кӯҳнаро иваз кунед.

## Имкониятҳо

- Реҷаи `AUTO` ҳангоми кушодан.
- Самтҳои RU → EN, EN → RU, TJ → EN ва EN → TJ.
- Интерфейс бо тоҷикӣ, русӣ ва англисӣ.
- Тугмаи `×` барои поккунӣ ва `Copy` барои нусхабардорӣ.
- Иваз кардани самт, гузоштан, воридоти `.txt`, боргирии натиҷа ва таърихи табдилҳо.
- Реҷаи равшан ва торик.
- Баъд аз зеркашии файлҳо интернет лозим нест.

## Файлҳои лоиҳа

- `index.html` — барномаи асосӣ.
- `README.md` — дастури насб, маълумоти лоиҳа ва таърихи версияҳо.

Ҳар ду файлро дар як папка нигоҳ доред, то пайванди README дар поёни барнома дуруст кор кунад.

## Таърихи версияҳо

- **4.0 — 09.11.2026:** AUTO ҳамчун реҷаи ибтидоӣ; тугмаи поккунӣ; нусхабардорӣ дар қисми натиҷа; маълумоти муаллиф ва версия дар поёни саҳифа.
- **3.0 — 09.11.2026:** интерфейси тоҷикӣ, русӣ ва англисӣ; харитаи клавиатураи тоҷикӣ ва муайянкунии худкор.

---

# Русский

**Автор:** Khayom  
**Версия:** 4.0  
**Обновлено:** 09.11.2026

Layout Fixer исправляет текст, набранный при неверно выбранной раскладке клавиатуры. Это не переводчик: программа заменяет символы по расположению клавиш.

## Установка на Android — Termux

1. Установите и откройте Termux.
2. Разрешите доступ к общей памяти:

   ```bash
   termux-setup-storage
   ```

3. Установите Git и Python:

   ```bash
   pkg update
   pkg install git python
   ```

4. Скачайте проект:

   ```bash
   git clone https://github.com/Khayom1/layout-fixer.git
   cd layout-fixer
   ```

5. Запустите локальный сервер:

   ```bash
   python -m http.server 8000 --bind 127.0.0.1
   ```

6. Откройте в браузере телефона:

   **http://127.0.0.1:8000/**

Во время работы Termux и сервер должны оставаться запущенными. Для остановки нажмите `CTRL + C`.

## Установка на компьютер

Скачайте или клонируйте репозиторий. Поместите `index.html` и `README.md` в одну папку и откройте `index.html` в современном браузере.

Если браузер ограничивает работу локального файла, выполните в папке проекта:

```bash
python -m http.server 8000
```

Откройте **http://localhost:8000/**.

## Обновление

При установке через Git выполните:

```bash
cd ~/layout-fixer
git pull origin main
```

Затем обновите страницу в браузере. При ручной установке скачайте новые `index.html` и `README.md` с GitHub и замените старые файлы.

## Возможности

- Режим `AUTO` включён по умолчанию.
- Направления RU → EN, EN → RU, TJ → EN и EN → TJ.
- Интерфейс на русском, английском и таджикском языках.
- Очистка поля кнопкой `×`, копирование результата кнопкой `Copy`.
- Обмен полей, вставка, импорт `.txt`, скачивание результата и история.
- Светлая и тёмная темы.
- После загрузки файлов подключение к интернету не требуется.

## Файлы проекта

- `index.html` — приложение.
- `README.md` — инструкция по установке, информация о проекте и история версий.

Храните оба файла в одной папке, чтобы ссылка на README внизу приложения работала.

## История версий

- **4.0 — 09.11.2026:** AUTO по умолчанию; очистка ввода; копирование под результатом; сведения об авторе и версии внизу страницы.
- **3.0 — 09.11.2026:** английский, русский и таджикский интерфейс; таджикская раскладка и автоопределение.

## Правила обновления

При каждом выпуске обновляйте версию в `index.html` и добавляйте дату и список изменений в этот README.
