# BakeCake

## Взаимодействие с базой данных

### Установка

Скачайте содержимое репозитория на ПК.

Установите зависимости командой

    pip install -r requirements.txt
    
База данных находится в файле `database.sqlite3`
    
### Функции взаимодействия с БД

Находятся в файле `functions.py`

Для тестирования в терминале запустите в терминале скрипт `manage.py` с параметром `shell`

    manage.py shell
    
Далее импортируйте файл командой

    import functions

Запускайте имеющиеся функции (в тестовой БД есть пользователь с `telegram_id = 'Michalbl4'`, можно запросить его)

Для добавления в код просто импортируйте в него `functions`

### get_user_data(telegram_id)

Возвращает данные о пользователе и список его заказов по telegram_id в следующем формате

Если пользователя с указанным id в базе нет, возвращает None

		{'user':
			{'id': 'Michalbl4',
			 'phone_number': '56789',
			 'last_name': 'Миронов',
			 'first_name': 'Михаил',
			 'registration_date': datetime.date(2022, 5, 5),
			 'last_address': 'Москва, Кремль'},
		 'orders':
			[
				{
					'number': 1,
					'date': datetime.datetime(2022, 5, 5, 5, 56, 51, tzinfo=datetime.timezone.utc),
					'price': 2000.0,
					'delivery': datetime.datetime(2022, 5, 7, 5, 57, 18, tzinfo=datetime.timezone.utc),
					'delivery_adress':
					'Москва, Кремль',
					'levels': 2,
					'form': 'Квадрат',
					'topping': 'Кленовый сироп',
					'berries': '',
					'decor': '',
					'comment': '',
					'inscription': ''
				},
				{
					'number': 2,
					'date': datetime.datetime(2022, 5, 5, 5, 59, 31, tzinfo=datetime.timezone.utc),
					'price': 1200.0,
					'delivery': datetime.datetime(2022, 5, 7, 6, 0, 8, tzinfo=datetime.timezone.utc),
					'delivery_adress': 'Москва, Кремль',
					'levels': 2,
					'form': '2',
					'topping': '',
					'berries': '',
					'decor': '',
					'comment': '',
					'inscription': ''
				}
			]
		}



### create_or_update_user(user_data)

Создает нового пользователя либо обновляет данные уже имеющегося (в случае совпадения `telegram_id` с имеющимся в базе).

Данные следует передавать в следующем формате

		user_data = {
			'id': 'Michalbl4',
			'phone_number': '56789',
			'last_name': 'Миронов',
			'first_name': 'Михаил'
		}
Возвращает `id` нового либо обновленного пользователя.
 

### create_order(telegram_id, order_data)

Создает новый заказ. Следует передать `id` и данные о заказе в формате словаря

		{
			'price': 1200.0,
			'delivery': datetime.datetime(2022, 5, 7, 6, 0, 8, tzinfo=datetime.timezone.utc),
			'delivery_adress': 'Москва, Кремль',
			'levels': 2,
			'form': '2',
			'topping': '',
			'berries': '',
			'decor': '',
			'comment': '',
			'inscription': ''
		}

Возвращает порядковый номер нового заказа.


