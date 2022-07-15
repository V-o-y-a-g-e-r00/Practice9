# Practice #9

**Социальная сеть по развитию внутреннего туризма в России.**
    
Бригада:
    - Frontend:
        - Сахаровский И.А. 
        - Киреев В.Т.
        - Морозов Н.Н.
    - Backend:
        - Telegarmm post parser:
            - Молошников Ф.А. @V-o-y-a-g-e-r00
        - Web server:
            - Борисов А.Э @ArtemBorisow и Молошников Ф.А. @V-o-y-a-g-e-r00
    - Web design:
        - Миронова П.
    - Descripiton/Docs:
        - Коклина Е.
    - Other
        - Артамонов Е.

Описание проекта: Сайт «Around Russia» с описанием всех 85 регионов России и их туристическими мощностями, для подробного знакомства с туризмом в России. Удобная анимированная карта с названиями регионов и кратким описанием для детального знакомства с каждой точкой страны, выбор региона по списку, приятный дизайн и удобный функционал никого не оставит равнодушным.  

## Frontend:
В данном репозитории присутствует папка проекта 
  Что бы запусть данный сайт у вас на компьютере вы должны скачать данный архив
  -Далее для запуска главной страницы сайта внутри этого архива нажмите на файл index.html
  -В файле Map.html представлена интерактивная карта России с разграничеными регионами , при наведении на который вы получаете информацию о данном субъекте и его герб
  
  -Если хотите поменять стиль сайта , то вы должны будете работать с файлом style.css , там представлены все стили дня данного сайта 
## Backend:
Сервер реализован на cpprestsdk. Он принимает GET запросы. Если в запросе tag, то он выдает координаты всех мест из этого региона. Если в запросе id, то он выдает всю информацию по этому месту, т.е. всю запись из базы данных. Сборка осуществляется через CMake. Управление CMakeLists.txt осуществляется вручную. Для работы нужен установленный MySQL Connector/C++ и C++ REST SDK. Работа над сервером велась на debian 11.
