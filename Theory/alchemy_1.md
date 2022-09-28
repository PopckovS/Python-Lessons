Примеры запросов SQLalchemy  
---

Задача: есть 3 таблицы, требуется сгруппировать данные и одним запросом получить,
email, ресурс принадлежащий ему, и в одну строку перечисление всех объектов 
этого ресурса.

Запрос в SQLalchemy

```python
    from sqlalchemy import func, delete, distinct, update

    data = session.query(
            Subscribe.resource_id.label('resource'),
            Email.email.label('email'),
            func.array_agg(Subscribe.feature_id).label('features'))\
        .filter(
            SubscribeEmail.notification_email_id == Email.id)\
        .filter(
            SubscribeEmail.notification_subscribe_id == Subscribe.id).\
        group_by(
            Subscribe.resource_id, Email.email).\
        all()
```

Эквивалент sql запроса:

```sql
SELECT 
	ne.email AS email, 
	ns.resource_id AS resource,
	array_agg(ns.feature_id)
FROM public.subscribe_email AS nse
INNER JOIN public.email AS ne ON  nse.email_id = ne.id 
INNER JOIN public.subscribe AS ns ON nse.subscribe_id = ns.id
GROUP BY 
	email, 
	resource
;
```
