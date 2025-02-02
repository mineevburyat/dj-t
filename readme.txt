часть один

1. Создание виртуального окружения
2. .gitignore
3. Установка django
    - freeze
4. Создание проекта, описание какая лучшая практика
 - продемонстировать удаление проекта и снова создание 
 в текущей папки и название как conf
 - структура проекта
 - запустить проект
 - назначение параметров и их изменение и как влияет на проект
 - ключ в отдельном файле переменных окружения
 - сразу выполнить это
5. Просмотр файла sqlite с помощью вьювера
6. Админка
 - показать что админка не доступна
 - миграцию выполнить
 - зайти под админом - не получится
 - создать суперадмина
 - зайти
7. Продемонстрировать работу клиента и сервера
 - тайминг
 - методы запроса
 - пост запрос с помощью создания еще одного пользователя
8. Разница между дебагсервером и продакт сервером
 - логирование
 - траблшутинг
9. Вывод
 - требования к бэкэндеру на данном этапе (OSI - отсылка)
 - краткий разбор библиотеки django
 

часть два

1. Создание приложение
2. еще раз разбираем логику работы сервера
3. маршрутизатор глобальный проекта и локальный приложения
4. представление - контекст и шаблон
5. модель и ORM

xfcnm nhb
"file_picker_callback": """function (cb, value, meta) {
        var input = document.createElement("input");
        input.setAttribute("type", "file");
        if (meta.filetype == "image") {
            input.setAttribute("accept", "image/*");
        }
        if (meta.filetype == "media") {
            input.setAttribute("accept", "video/*");
        }

        input.onchange = function () {
            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function () {
                var id = "blobid" + (new Date()).getTime();
                var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                var base64 = reader.result.split(",")[1];
                var blobInfo = blobCache.create(id, file, base64);
                blobCache.add(blobInfo);
                cb(blobInfo.blobUri(), { title: file.name });
            };
            reader.readAsDataURL(file);
        };
        input.click();
    }""",


аутентификация и регистрация
форма создания поста
редактирование поста
сообщения
