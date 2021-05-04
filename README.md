# D9.11 Домашнее задание: добавляем категории в API
## блог

### Зависимости
* python = "^3.8"
* Django = "^3.2"
* djangorestframework = "^3.12.4"
* drf-yasg = "^1.20.0"

### DEV зависимости
* black = "^20.8b1"
* pylint = "^2.7.4"
* pytest-django = "^4.2.0"


### Установка 
`activate your virtualenv`

`pip install -r requirements.txt`


### Тестирование 
`pytest -v`


### Проверка 
`http :8001/categories/`

`http POST :8001/categories/ < blog/fixture/test.json`

### URls:
* /swagger/
* https://infinite-ridge-47412.herokuapp.com/swagger/