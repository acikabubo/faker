# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = ('{{street_name}}', )
    street_address_formats = ('{{street_name}} {{building_number}}', )
    address_formats = ('{{street_address}}\n{{postcode}} {{city}}', )

    building_number_formats = (
        '###', '##', '#', '#a', '#b', '#c', '#a/#', '#b/#', '#c/#')

    postcode_formats = ('####', )

    street_suffixes_long = (
        '', 'улица', 'булевар', 'пат',
    )

    street_suffixes_short = (
        '', 'ул.', 'бул.'
    )

    cities = (
        'Велес', 'Демир Капија', 'Кавадарци', 'Неготино', 'Свети Николе',
        'Берово', 'Виница', 'Делчево', 'Кочани', 'Македонска Каменица',
        'Пехчево ', 'Пробиштип', 'Штип', 'Дебар', 'Кичево', 'Македонски Брод',
        'Охрид', 'Струга', 'Богданци', 'Валандово', 'Гевгелија', 'Дојран',
        'Радовиш', 'Струмица', 'Битола', 'Демир Хисар', 'Крушево', 'Прилеп',
        'Ресен', 'Гостивар', 'Тетово', 'Кратово', 'Крива Паланка',
        'Куманово', 'Скопје'
    )

    states = (
        'Арачиново', 'Берово', 'Битола', 'Богданци', 'Боговиње', 'Босилово',
        'Брвеница', 'Валандово', 'Василево', 'Вевчани', 'Велес', 'Виница',
        'Вранештица', 'Врапчиште', 'Гевгелија', 'Гостивар', 'Градско',
        'Дебар', 'Дебарца', 'Делчево', 'Демир Капија', 'Демир Хисар',
        'Дојран', 'Долнени', 'Другово', 'Желино', 'Зајас', 'Зелениково',
        'Зрновци', 'Илинден', 'Јегуновце', 'Кавадарци', 'Карбинци',
        'Кичево', 'Конче', 'Кочани', 'Кратово', 'Крива Паланка',
        'Кривогаштани', 'Крушево', 'Куманово', 'Липково', 'Лозово',
        'Маврово и Ростуше', 'Македонски Брод', 'Македонска Каменица',
        'Могила', 'Неготино', 'Новаци', 'Ново Село', 'Осломеј', 'Охрид',
        'Петровец', 'Пехчево', 'Пласница', 'Прилеп', 'Пробиштип', 'Радовиш',
        'Ранковце', 'Ресен', 'Росоман', 'Старо Нагоричане', 'Свети Николе',
        'Сопиште', 'Струга', 'Струмица', 'Студеничани', 'Теарце', 'Тетово',
        'Центар Жупа', 'Чашка'
    )

    streets = (
        'Арачиново', 'Берово', 'Битола', 'Богданци', 'Боговиње', 'Босилово',
        'Брвеница', 'Валандово', 'Василево', 'Вевчани', 'Велес', 'Виница',
        'Вранештица', 'Врапчиште', 'Гевгелија', 'Гостивар', 'Градско',
        'Дебар', 'Дебарца', 'Делчево', 'Демир Капија', 'Демир Хисар',
        'Дојран', 'Долнени', 'Другово', 'Желино', 'Зајас', 'Зелениково',
        'Зрновци', 'Илинден', 'Јегуновце', 'Кавадарци', 'Карбинци',
        'Кичево', 'Конче', 'Кочани', 'Кратово', 'Крива Паланка',
        'Кривогаштани', 'Крушево', 'Куманово', 'Липково', 'Лозово',
        'Маврово и Ростуше', 'Македонски Брод', 'Македонска Каменица',
        'Могила', 'Неготино', 'Новаци', 'Ново Село', 'Осломеј', 'Охрид',
        'Петровец', 'Пехчево', 'Пласница', 'Прилеп', 'Пробиштип', 'Радовиш',
        'Ранковце', 'Ресен', 'Росоман', 'Старо Нагоричане', 'Свети Николе',
        'Сопиште', 'Струга', 'Струмица', 'Студеничани', 'Теарце', 'Тетово',
        'Центар Жупа', 'Чашка'
    )

    regions = (
        'Вардарски регион', 'Источен регион', 'Југозападен регион',
        'Југоисточен регион', 'Пелагониски регион', 'Полошки регион',
        'Североисточен регион', 'Скопски регион'
    )

    countries = (
        'Обединети Арапски Емирати', 'Јордан', 'Турција', 'Туркменистан',
        'Казахстан', 'Ирак', 'Азербејџан', 'Брунеј', 'Тајланд', 'Кина',
        'Либан', 'Киргистан', 'Лаос', 'Сирија', 'Бангладеш', 'Источен Тимор',
        'Катар', 'Таџикистан', 'Ерменија', 'Израел', 'Пакистан', 'Авганистан',
        'Непал', 'Малезија', 'Кувајт', 'Малдиви', 'Бахреин', 'Филипини',
        'Русија', 'Оман', 'Бурма', 'Кипар', 'Индија', 'Камбоџа',
        'Северна Кореја', 'Саудиска Арабија', 'Јемен', 'Јужна Кореја',
        'Сингапур', 'Шри Ланка', 'Узбекистан', 'Грузија', 'Иран', 'Бутан',
        'Јапонија', 'Либија', 'Монголија', 'Виетнам', 'Индонезија', 'Нигерија',
        'Гана', 'Етиопија', 'Алжир', 'Мадагаскар', 'Еритреја', 'Мали',
        'Централноафриканска Република', 'Гамбија', 'Гвинеја Бисао',
        'Република Конго', 'Бурунди', 'Сејшели', 'Намибија', 'Боцвана',
        'Сенегал', 'Танзанија', 'Брег на Слоновата Коска БСК', 'Камерун',
        'Египет', 'Гвинеја', 'Уганда', 'Судан', 'Руанда', 'Мавританија',
        'Демократска Република Конго', 'Габон', 'Малави', 'Того', 'Ангола',
        'Замбија', 'Екваторска Гвинеја', 'Мозамбик', 'Лесото', 'Свазиленд',
        'Сомалија', 'Либерија', 'Комори', 'Кенија', 'Чад', 'Нигер',
        'Маврициус', 'Бенин', 'Зелен Рт', 'Јужна Африка ЈАР', 'Мароко',
        'Сао Томе и Принципе', 'Либија', 'Тунис', 'Буркина Фасо', 'Сиера Леоне',
        'Зимбабве', 'Џибути', 'Холандија', 'Андора', 'Турција', 'Грција',
        'Азербејџан', 'Србија', 'Германија', 'Швајцарија', 'Словачка',
        'Белгија', 'Романија', 'Унгарија', 'Лихтенштајн', 'Малта', 'Ватикан',
        'Австрија', 'Литванија', 'Полска', 'Ирска', 'Ерменија', 'Хрватска',
        'Молдавија', 'Данска', 'Украина', 'Португалија', 'Обединето Кралство',
        'Луксембург', 'Словенија', 'Шпанија', 'Белорусија', 'Монако', 'Русија',
        'Никозија', 'Норвешка', 'Франција', 'Црна Гора', 'Чешка', 'Исланд',
        'Латвија', 'Италија', 'Сан Марино', 'Босна и Херцеговина', 'Македонија',
        'Бугарија', 'Шведска', 'Естонија', 'Грузија', 'Албанија', 'Финска',
        'Парагвај', 'Колумбија', 'Бразил', 'Аргентина', 'Венецуела', 'Еквадор',
        'Перу', 'Уругвај', 'Суринам', 'Чиле', 'Боливија', 'Гвајана', 'Самоа',
        'Нов Зеланд', 'Источен Тимор', 'Науру', 'Австралија',
        'Маршалски Острови', 'Палау', 'Тонга', 'Микронезија',
        'Папуа Нова Гвинеја', 'Вануату', 'Кирибати', 'Фиџи', 'Тувалу',
        'Соломонски Острови', 'Индонезија', 'Свети Китс и Невис', 'Белизе',
        'Барбадос', 'САД', 'Гватемала', 'Света Луција', 'Јамајка',
        'Свети Винсент и Гренадини', 'Никарагва', 'Мексико', 'Бахами', 'Канада',
        'Панама', 'Хаити', 'Тринидад и Тобаго', 'Доминика', 'Костарика',
        'Ел Салвадор', 'Доминиканска Република', 'Гренада', 'Антигва и Барбуда',
        'Хондурас', 'Куба'
    )

    @classmethod
    def city_name(cls):
        return cls.random_element(cls.cities)

    @classmethod
    def street_name(cls):
        return cls.random_element(cls.streets)

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
