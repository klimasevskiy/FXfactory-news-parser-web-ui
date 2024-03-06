<p align="center">
   <img src="imgs/Logo-Full.png?raw=true "/>
</p>

# NOTIONfactory

## Зміст

- [Про проект](#про-проект)
- [Початок роботи](#початок-роботи)
- [Додаткова інформація](#додаткова-інформація)
- [Внесок](../CONTRIBUTING.md)

## Про проект <a name = "про-проект"></a>

NOTIONfactory допомагає вам розбирати дані з [FXfactory](https://www.forexfactory.com/calendar) у вашу таблицю на Notion за допомогою зручного веб-інтерфейсу.

## Початок роботи <a name = "початок-роботи"></a>

- склонуйте проект на ваш комп'ютер
- встановіть всі залежності: `pip install -r requirements.txt`
- запустіть програму за допомогою Streamlit: `streamlit run webui.py`
- або просто скористайтеся готовою версією за посиланням: [ТУТ](https://notionfactrory-by-klimasevskiy.streamlit.app/)

[![YT-video](imgs/Video.png?raw=true)](https://youtu.be/6Fr4sdUvYPs)

### Вимоги

- streamlit
- beautifulsoup4
- notion_client
- pytz
- requests
- tabulate

```
pip install streamlit
pip install beautifulsoup4
pip install notion_client
pip install pytz
pip install requests
pip install tabulate
```

## Додаткова інформація <a name = "додаткова-інформація"></a>

- Не підтримує таблиці з іншими назвами стовпців, крім моїх.
- Використовуйте зсув часу для відображення правильного часу у вашій таблиці.
- Якщо ви зіткнетеся з проблемами у роботі, напишіть мені в [Telegram](https://t.me/klimasevskiy)
