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
    git clone [https://github.com/Iversat/alice-multiroom.git](https://github.com/Iversat/alice-multiroom.git)
    cd alice-multiroom
    ```

2.  Установите необходимые зависимости:
    ```bash
    pip install zeroconf
    ```
    Если вы используете `requirements.txt`, можно также:
    ```bash
    pip install -r requirements.txt
    ```
    (В этом случае создайте файл `requirements.txt` с содержимым `zeroconf`)

## Использование

Запустите скрипт из командной строки:

```bash
python multiroom_scanner.py

## Пример вывода
 
Начинаем сканирование на 10 секунд...
Ищем типы сервисов: _yandexio._tcp.local., _yandexstation._tcp.local., _googlecast._tcp.local., _spotify-connect._tcp.local.
------------------------------
Устройство: Yandex-Station-Mini-E4A5 (192.168.1.15)
------------------------------
Устройство: Google-Home-Mini-A1B2 (192.168.1.12)
------------------------------

==============================
Завершение сканирования.

Найдено устройств: 2

Список обнаруженных устройств:

  1. Устройство: Yandex-Station-Mini-E4A5
     Сервисное имя: Yandex Station Mini E4A5._yandexio._tcp.local.
     Тип: _yandexio._tcp.local.
     IP: ['192.168.1.15']
     Порт: 8030
     Свойства: {'fn': 'Yandex Station Mini E4A5', 'md': 'yandexstation_2', 'rm': '', 've': '1.0.0.2', 'id': '012345abcdef6789', 'ca': '4100', 'st': '1', 'bs': 'AA:BB:CC:DD:EE:FF', 'rs': ''}

  2. Устройство: Google-Home-Mini-A1B2
     Сервисное имя: Google Home Mini A1B2._googlecast._tcp.local.
     Тип: _googlecast._tcp.local.
     IP: ['192.168.1.12']
     Порт: 8009
     Свойства: {'id': 'aabbccddeeff001122334455', 've': '05', 'md': 'Google Home Mini', 'fn': 'Living Room Speaker', 'ca': '4101', 'st': '0', 'ic': '/setup/icon.png', 'rm': '', 'rs': ''}
