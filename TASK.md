# Необходимо создать REST API для проведения аукционов:

- Должен быть реализован механизм регистрации пользователя, получения токена и дальнейшей авторизации запросов по токену.
- Пользователь может получить список всех аукционов, зарегистрированных в системе. Используя фильтр в запросе, можно получить все, только активные или только завершенные аукционы.
- Пользователь может создать новый аукцион установив описание товара, начальную цену, шаг цены и время окончания аукциона.
- В момент, когда новый аукцион создан, всем зарегистрированным пользователям системы должно отправляться сообщение по электронной почте о том, что у них есть возможность присоединится к торгам.
- Обновлять поля аукциона, указанные при создании, нельзя. Удалять созданные аукционы нельзя.
- Если пользователь не является хозяином аукциона, то должна иметься возможность сделать ставку, если аукцион активен. При этом её размер должен быть свалидирован, исходя из предыдущей цены и шага. Изменять или удалять ставки нельзя.
- Если пользователь сделал на конкретном аукционе хотя бы одну ставку, то информация о изменении цены этого аукциона должна доставляться на электронную почту пользователя при каждой новой ставке от других пользователей.
- При получении детальной информации об аукционе необходимо вернуть поля, указанные при его создании + список сделанных на него ставок с именами пользователей, которые их сделали.
[Не сделано] - В момент, когда время аукциона подошло к концу, система должна прекратить прием новых ставок, автоматически определить победителя и разослать всем, кто участвовал в торгах, уведомления по почте об их прекращении.
- При разработке можно использовать фреймворки и библиотеки по желанию.