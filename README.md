# Тестовое задание

## Подготовка к тестовому заданию

Написать на FastAPI endpoint принимающий в get-запросе два параметра `x` и `y`.
`x` и `y` должны быть целыми числами.
`x` должен быть больше нуля.
Результатом get-запроса должен быть json следующего вида:

```json
{
  "x": 10,
  "y": 2,
  "result": 5
}
```

где `result` является результатом деления `x` на `y` и умноженном на случайное число в диапазоне от -10 до 10

Все ошибки, включая ошибки валидации, должны быть обработаны и возвращены из get-запроса в виде следующей json структуры:

```json
{
  "Error": "Тип ошибки",
  "ErrorMessage": "Что пошло не так",
  "RequestData": "x = ?; y = ?"
}
```

Запрос должен отрабатывать за рандомное время от 0 до 3 секунд.

## Примеры тестовых заданий

### Задание 1

- выполнить пять конкурентных запросов к тестовому API
- распечатать результаты выполнения в порядке следования запросов;
- все ошибки должны быть обработаны

### Задание 2

- выполнить пять конкурентных запросов к тестовому API
- распечатать результат второго по времени выполнения запроса а остальные запросы отменить;
- все ошибки должны быть обработаны

### Задание 3

- выполнить пять конкурентных запросов к тестовому API
- если третий выполнившийся по времени запрос вернул отрицательный результат распечатать результат выполнения первых двух а остальные запросы отменить иначе распечатать результат выполнения последних двух
- все ошибки должны быть обработаны


### Решение 1
```json
- Запрос 1: Ответ = {'x': 1, 'y': 2, 'result': 0.0}
- Запрос 2: Ответ = {'x': 3, 'y': 4, 'result': 0.75}
- Запрос 3: Ответ = {'x': 5, 'y': 1, 'result': 35.0}
- Запрос 4: Ответ = {'x': 2, 'y': 2, 'result': -1.0}
- Запрос 5: Ответ = {'x': 6, 'y': 3, 'result': -18.0}
```