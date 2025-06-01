# Локальный Сканер Умных Устройств (mDNS)

Простой Python-скрипт для обнаружения умных колонок и других устройств в вашей локальной сети, которые анонсируют свои сервисы с использованием протокола mDNS (также известного как Bonjour или Zeroconf). Скрипт помогает идентифицировать IP-адреса, порты и другую доступную информацию об этих устройствах.

## Возможности

* Обнаружение устройств по различным типам mDNS-сервисов (например, `_yandexio._tcp.local.`, `_googlecast._tcp.local.`, `_spotify-connect._tcp.local.` и другие).
* Отображение IP-адресов, портов и доступных свойств (properties) для каждого обнаруженного устройства.
* Вывод общего количества найденных устройств по завершении сканирования.
* Настраиваемая продолжительность сканирования (по умолчанию 10 секунд).
* Понятный вывод информации в консоль во время и после сканирования.

## Требования

* Python 3.6+
* Библиотека `zeroconf`

## Установка

1.  Клонируйте репозиторий (или скачайте скрипт `multiroom_scanner.py`):
    ```bash
    git clone https://github.com/Iversat/alice-multiroom.git
    cd alice-multiroom
    ```

2.  Установите необходимые зависимости:
    ```bash
    pip install zeroconf
    ```


## Использование

Запустите скрипт из командной строки:

```bash
python multiroom_scanner.py
 ```

## Пример вывода

 ```bash
Начинаем сканирование на 10 секунд...
Ищем типы сервисов: _yandexio._tcp.local., _yandexstation._tcp.local., _googlecast._tcp.local., _spotify-connect._tcp.local.
------------------------------
Устройство: yandexmicro-LP00XXXXXXXXX (192.168.1.57)
------------------------------
Устройство: yandex-hub-SXXXXXXXXXXXXX (192.168.1.11)
------------------------------

==============================
Завершение сканирования.

Найдено устройств: 2

Список обнаруженных устройств:

  1. Устройство: yandexmicro-LP00XXXXXXXXX
     Сервисное имя: YandexIOReceiver-LP00XXXXXXXXX._yandexio._tcp.local.
     Тип: _yandexio._tcp.local.
     IP: ['192.168.1.57']
     Порт: 1961
     Свойства: {'deviceId': 'LP00XXXXXXXXX', 'platform': 'yandexmicro', 'cluster': 'yes'}

  2. Устройство: yandex-hub-SXXXXXXXXXXXXX
     Сервисное имя: YandexIOReceiver-SXXXXXXXXXXXXX._yandexio._tcp.local.
     Тип: _yandexio._tcp.local.
     IP: ['192.168.1.11']
     Порт: 1961
     Свойства: {'deviceId': 'SXXXXXXXXXXXXX', 'platform': 'saturn', 'cluster': 'yes'}
 ```
