# HomeWork 24.1 Django DRF
Задание 1

Создайте новый Django-проект, подключите DRF в настройках проекта.
Задание 2

Создайте следующие модели:
Пользователь:
Курс:
Урок:

Модель курса и урока разместите в отдельном приложении.

Задание 3
Опишите CRUD для моделей курса и урока. 
Для реализации CRUD для курса используйте Viewsets,
а для урока - Generic-классы.
Для работы контроллеров опишите простейшие сериализаторы.



# HomeWork 24.2 Сериализаторы
Задание 1

Для модели курса добавьте в сериализатор поле вывода количества уроков. 
Поле реализуйте с помощью SerializerMethodField()

Задание 2

Добавьте новую модель в приложение users:
Платежи

Поля пользователь, оплаченный курс и отдельно оплаченный урок
должны быть ссылками на соответствующие модели.

Задание 3

Для сериализатора для модели курса реализуйте поле вывода уроков. 
Вывод реализуйте с помощью сериализатора для связанной модели.

Задание 4

Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

    менять порядок сортировки по дате оплаты,
    фильтровать по курсу или уроку,
    фильтровать по способу оплаты.

# HomeWork 25.1 Права доступа в DRF

Задание 1

Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, 
настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

Задание 2

Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, 
но без возможности их удалять и создавать новые. 
Заложите функционал такой проверки в контроллеры.

Задание 3

Опишите права доступа для объектов таким образом, чтобы пользователи, 
которые не входят в группу модераторов, могли видеть, 
редактировать и удалять только свои курсы и уроки.


    Дополнительное задание

Для профиля пользователя введите ограничения, 
чтобы авторизованный пользователь мог просматривать любой профиль, 
но редактировать только свой. 
При этом для просмотра чужого профиля должна быть доступна только общая информация, 
в которую не входят: пароль, фамилия, история платежей.

# HomeWork 25.2 Валидаторы, пагинация и тесты

Задание 1

Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах 
ссылок на сторонние ресурсы, кроме youtube.com. То есть ссылки на видео можно прикреплять в материалы, 
а ссылки на сторонние образовательные платформы или личные сайты — нельзя.

Задание 2

Добавьте модель подписки на обновления курса для пользователя. 
Вам необходимо реализовать эндпоинт для установки подписки пользователя 
и на удаление подписки у пользователя.

Задание 3

Реализуйте пагинацию для вывода всех уроков и курсов.

Задание 4

Напишите тесты, которые будут проверять корректность работы CRUD уроков 
и функционал работы подписки на обновления курса.
Сохраните результат проверки покрытия тестами.


Дополнительное задание

Напишите тесты на все имеющиеся эндпоинты в проекте.

