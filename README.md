# Who Wants To Be A Millionaire

**Who Wants To Be A Millionaire** - это веб-приложение, созданное на Django, которое имитирует популярное телевизионное шоу. Пользователи могут регистрироваться, отвечать на вопросы, использовать подсказки и соревноваться за главный приз.

## Особенности
- Регистрация пользователей
- Система уровней вопросов
- Поддержка подсказок: 50/50, звонок другу, помощь зала и другие
- Топ-10 победителей

## Установка
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/1SERGIO11/WhoWantsToBeAMillionare.git` 

2.  Перейдите в каталог проекта:

   `git clone cd WhoWantsToBeAMillionare`

3. Установите зависимости:  
    
    `pip install -r requirements.txt` 
    
4.  Примените миграции:
    
    `python manage.py migrate` 
    
5.  Запустите сервер разработки:
    
    `python manage.py runserver` 
    

## Использование

Перейдите в браузере по адресу `http://127.0.0.1:8000/` и зарегистрируйтесь для участия в игре.

## API Endpoints

-   `GET /`: домашняя страница
-   `POST /submit-answer/`: отправка ответа на вопрос
-   `GET /get-question/<int:level>/`: получение вопроса для указанного уровня

## Модели

-   **User**: модель пользователя, содержащая информацию о текущем уровне, максимальном достигнутом уровне и сумме приза.
-   **Questions**: модель вопросов, включающая текст вопроса, варианты ответов и правильный ответ.
-   **Hint**: модель подсказок, привязанная к пользователю и уровню вопроса.

## Скриншоты
![image](https://github.com/1SERGIO11/WhoWantsToBeAMillionare/assets/114675359/6b45eb3a-3793-409b-8747-8e0330dee85a)
![WWTBAM](https://github.com/1SERGIO11/WhoWantsToBeAMillionare/assets/114675359/0cd178a3-06fb-4504-8e56-7bf5f9c027e8)
![image](https://github.com/1SERGIO11/WhoWantsToBeAMillionare/assets/114675359/eedf87b4-9b6a-496e-8bab-d77cc2fcb5d7)
