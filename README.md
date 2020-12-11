# nosql2h20-arxiv

# Запуск проекта
Перед запуском убедитесь, что порты 5000,3000,7687,7474 не заняты.
```
docker-compose build --no-cache
docker-compose up
```
или
```
docker-compose up --build
```
После сборки и запуска проекта БД будет пустая.
Проект запустится на 3000 порту
# Имопрт даных в БД
Для демонстрации импорта даных в БД есть файл import.zip, который надо залить на страце home и нажать кнопку import.(P.s. импорт принимает только архив с 3 файлами: articles.csv, authors.csv и wrote.csv.)(P.p.s максимальное время импорта в бд 5 минут дольше выкидывается exception)

# Экспорт данных из БД
Запрос по кнопке скачивает архив export.zip с 50 вершинами для авторов и статей, а так же 50 связей.(Сделали 50, чтобы можно было быстро протетстить экспорт, так как весь датасет весит более 2 гб и ждать пршлось бы дольше)
