# social_auth_mymapa

<h1>Описание проекта:</h1>

У сайта есть две страницы:
<ul>
    <li>Главная страница</li>
    <li>Страница для создания учетной записи <i>/login</i></li>
</ul>



<h3>Запуск проекта (через docker-compose):</h3>
Клонируем репозиторий
```
git clone https://github.com/metro6/social_auth_mymapa.git
cd social_auth_mymapa
```
Создаем файл с настройками Django

```
cp social_auth_mymapa/src/custom_settings/custom_settings.py.example social_auth_mymapa/src/custom_settings/custom_settings.py
```
В файле конфигурации нужно указать: 
<ul>
    <li>Настройки facebook</li>
    <li>Настройки google</li>
</ul>


Запускаем проект
```
(sudo) make build
(sudo) make up
```
Или остановите его
```
(sudo) make down
```

После запуска, проект будет доступен по адресу "http://you_domain_or_ip:8001"

<h3>В проекте используется:</h3>
<ul>
    <li>django</li>
    <li>DRF</li>
    <li>social-auth-app-django</li>
    <li>postgresql + django-ORM</li>
    <li>Препроцессор PUG для верстки и Stilus для CSS</li>
    <li>jQuery</li>
    <li>docker-compose</li>
    <li>nginx</li>
    <li>gunicorn</li>
    <li>swagger</li>
</ul>


<h3>P.S.:</h3>

Можно так же запустить проект как мы обычно привыкли при работе с Docker
```bash
(sudo) docker-compose build
(sudo) docker-compose up
(sudo) docker-compose down
```
Если нужно запустить проект без docker, вы знаете как это сделать :)