Верстка на джанго 
Функционал перед тем как запускать нужно ввести команды 
# Удалите старую базу данных 
rm db.sqlite3
# Новые миграции
python manage.py makemigrations
# Применение миграции
python manage.py migrate
# Создайте виртуальное окружение
python -m venv venv
# Введите команду
venv\Scripts\activate
# Запуск сервера
python manage.py runserver

Главная страница выглядят так:
<img width="1666" height="747" alt="image" src="https://github.com/user-attachments/assets/33a6a873-7cd6-40a9-aeff-ba28d0faceef" />
Функционал данной страницы это кнопка главная и распорядок который имеет переход на данную страницу 
<img width="174" height="146" alt="image" src="https://github.com/user-attachments/assets/c9372e21-989c-42fb-9a40-42d498c2a354" />
На главной страницы распологается информация о сотрудниках с кнопкой "новый сотрудник"
<img width="1239" height="362" alt="image" src="https://github.com/user-attachments/assets/9661ed25-8e3a-4cc5-854e-0d34eb0447c1" />
При нажатии на кнопку выполняется переход на заполнение формы добавления сотрудника которая имеет внешний вид 
<img width="1249" height="750" alt="image" src="https://github.com/user-attachments/assets/8c46b8b1-a8b8-47a1-922a-32016f094113" />
При нажатии на "Расписание"
<img width="1881" height="600" alt="image" src="https://github.com/user-attachments/assets/62fa03f3-b11c-4db5-93a3-7cf2b876ed22" />

  
