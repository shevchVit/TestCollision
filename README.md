# Задание на коллизию

## server.py

Сервер для обработки сообщений от клиента и выявления коллизий.


Чтобы запустить, необходимо при запуске передать на вход количество объектов:
```
python server.py --n=10
```

Чтобы увидеть визуализацию столкновений клиента с объектами можно перейти по адресу http://127.0.0.1:9000.

## client.py

На вход программе необходимо подать размер дрона в метрах. После запуска программы дрон будет симулировать полет в зоне 10 на 10 метров

```
python client.py --d=1
```