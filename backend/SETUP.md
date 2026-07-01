## CHECK PREREQUISITES
| prerequisite | version |
| -------- | -------- |
| php |  8.2-8.4 |
| composer | any ¯\\_(ツ)_/¯ (latest is g i think) |
```
php --version
composer --version
```
## SETUP
this is basically all I used to setup the base server

```
composer create-project laravel/laravel <project-name>
```
or
```
composer global require laravel/installer
laravel new <project-name>
```
```
php artisan install:api

composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
```
#### docker
idk bro, just copy the config i made in ```docker-compose.yml``` and .```env.example```
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