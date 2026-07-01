## STARTUP
#### setting up
```
cd <project-name>

composer install

# copy the .env.example to a .env file
# commands on Windows and Linux/Mac OS respectively
copy .env.example .env
cp .env.example .env

php artisan key:generate
php artisan db:seed
```
#### starting the project
```
docker compose up -d
php artisan serve
```