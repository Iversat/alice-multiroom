import time
from zeroconf import ServiceBrowser, Zeroconf, ServiceListener
import socket
import logging


# Включаем логирование для отладки, если нужно
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('zeroconf').setLevel(logging.DEBUG)

class MyListener(ServiceListener):
    def __init__(self):
        self.found_devices = {}

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        # Эта функция вызывается, когда информация о сервисе обновляется,
        # но для простого обнаружения мы обработаем это в add_service
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Сервис удален: {name} ({type_})")
        if name in self.found_devices:  # Проверяем по ключу, который мог быть info.server или info.name
            del self.found_devices[name]
        # Также проверим, нет ли его по другому возможному ключу, если логика ключей изменится
        elif name.replace("." + type_, "") in self.found_devices:
            del self.found_devices[name.replace("." + type_, "")]

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        if info:
            device_name_candidate = info.server.split('.')[0] if info.server else name.replace("." + type_, "")
            addresses = [socket.inet_ntoa(addr) for addr in info.addresses]

            key_to_store = info.server if info.server else info.name
            if key_to_store not in self.found_devices:
                self.found_devices[key_to_store] = {
                    "name": device_name_candidate,
                    "service_name": info.name,
                    "type": info.type,
                    "addresses": addresses,
                    "port": info.port,
                    "properties": {k.decode('utf-8'): v.decode('utf-8') if isinstance(v, bytes) else v
                                   for k, v in info.properties.items()} if info.properties else {}
                }
                # Изменение 1: "Добавлено устройство:" -> "Устройство:"
                print(f"Устройство: {device_name_candidate} ({', '.join(addresses)})")
                print("-" * 30)
        else:
            pass


def scan_local_network_for_speakers(scan_duration_seconds=10):
    """
    Сканирует локальную сеть на наличие умных колонок, анонсирующих себя через mDNS.
    """
    zeroconf = Zeroconf()
    listener = MyListener()

    service_types_to_scan = [
        "_yandexio._tcp.local.",
        "_yandexstation._tcp.local.",
        "_googlecast._tcp.local.",
        "_spotify-connect._tcp.local.",
        # "_http._tcp.local.",
        # "_airplay._tcp.local.",
    ]

    print(f"Начинаем сканирование на {scan_duration_seconds} секунд...")
    # Изменение 2: "Ищем сервисы типов:" -> "Ищем типы сервисов:"
    print(f"Ищем типы сервисов: {', '.join(service_types_to_scan)}")
    print("-" * 30)

    browser = ServiceBrowser(zeroconf, service_types_to_scan, listener)

    try:
        time.sleep(scan_duration_seconds)
    except KeyboardInterrupt:
        print("\nСканирование прервано пользователем.")
    finally:
        print("\n" + "=" * 30)
        print("Завершение сканирования.")

        num_found_devices = len(listener.found_devices)

        if num_found_devices > 0:
            print(f"\nНайдено устройств: {num_found_devices}")
            print("\nСписок обнаруженных устройств:")
            device_counter = 1
            for device_key, device_info in listener.found_devices.items():
                print(f"\n  {device_counter}. Устройство: {device_info.get('name', device_key.split('.')[0])}")
                print(f"     Сервисное имя: {device_info.get('service_name')}")
                print(f"     Тип: {device_info.get('type')}")
                print(f"     IP: {device_info.get('addresses')}")
                print(f"     Порт: {device_info.get('port')}")
                props_to_show = {}
                if device_info.get('properties'):
                    for prop_key, prop_val in device_info['properties'].items():
                        if prop_key in ['fn', 'md', 'rm', 've', 'id', 'ca', 'ic', 'st', 'bs', 'rs']:
                            props_to_show[prop_key] = prop_val
                if props_to_show:
                    print(f"     Свойства: {props_to_show}")
                else:
                    print(f"     Свойства: {device_info.get('properties') if device_info.get('properties') else '{}'}")
                device_counter += 1
        else:
            print("\nУстройства не найдены (или не анонсируют себя через выбранные типы сервисов mDNS).")

        zeroconf.close()


if __name__ == "__main__":
    scan_local_network_for_speakers(scan_duration_seconds=10)