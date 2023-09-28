INFO
============================

Тестовое задание для **Mayak.travel**

Версия интерпретатора Python 3.10.3

Порядок установки и запуск на своей машине
===========
**Linux**

    git clone https://github.com/rzge/mayak_travel_task.git
    cd mayak_travel_task
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    touch config.ini
    nano config.ini

        [Telegram]
        api_token = YOUR_TOKEN

    python main.py

