
# Grand Autograph Hotel Bar inventory management

## установка

нужно:

- python 3.12
- django
- pip


1. клонируем

  
2. создаем виртуальную среду (пишу в venv PyCharm, должно работать везде :D)


3. БД и супер-пользователь должны быть из коробки в БД которую прислал
- login: magaz | pass: superuser
4. если нет, то в терминале пишем:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser


4. запускаем сервер:
- python manage.py runserver
- хостится на 127.0.0.1:8000, в терминале должна быть ссылка


5. работает! (дай бог)
6. также в каталоге есть bash скрипт и докер чтобы в будущем запускать на линукс-сервере, но еще не работает)