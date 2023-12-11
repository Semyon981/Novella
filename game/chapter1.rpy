
define arsenushkin = Character('Арсенюшкин', color="#ba0000")

define audio.street = "music/part.wav"
define audio.arsenushkin = "music/arsentiev.mp3"

label startChapter1:

    scene street
    with fade

    play music street

    "{font=Gilroy-ExtraBold.otf}ГЛАВА I “ВВЕДЕНИЕ В СПЕЦИАЛЬНОСТЬ”"
    "{cps=25}Сентябрь. Знойное дыхание лета ещё не покинуло столицу."
    "{cps=25}Утреннее солнце предвещает новые приключения."
    "{cps=25}Что ждёт студента в его первый учебный день?"
    "{cps=25}Корпус на улице Прянишникова (с некоторых пор здесь поселился факультет ИТ)."
    "{cps=25}В народе это место известно как “Пряники”."
    "{cps=25}Место спокойное и тихое. Находится около большого пруда, парка и садов Тимирязевской академии."
    
    scene university
    with fade

    play music arsenushkin
    
    "{font=Gilroy-ExtraBold.otf}КАФЕДРА ИНФОРМАТИКИ"
    
    show arsentiev
    with dissolve
    
    arsenushkin "{cps=25}Я смотрю к нам прибыло пополнение."
    arsenushkin "{cps=25}Зовут меня Дмитрий Андреевич Арсенюшкин."
    arsenushkin "{cps=25}Я тут на кафедре информатики и ИТ вроде как не последний человек."
    
    hide arsentiev
    with dissolve
    
    "*перешёптывания в аудитории"
    "{cps=25}Тот самый Арсенюшкин!" 
    "{cps=25}Говорят, что он общается только сложными метафорами, шутками и оборванными фразами."
    "{cps=25}Старшекурсники рассказывают, что у него есть уникальная способность появляться в нужный момент и предлагать сделать проект, за который можно получить зачёт."
    "{cps=25}Ходят даже слухи что Арсенюшкин одолел кровожадность не менее легендарного Норникеля, что по половине группы валил."
    
    show arsentiev
    with dissolve
    
    arsenushkin "{cps=25}Сегодня у нас будет первая пара по предмету “Введение в специальность”."
    arsenushkin "{cps=25}Вообще предмет будет проводится в дистанционном формате, так что напрягать вас с точки зрения передвижения не буду."
    arsenushkin "{cps=25}Итак… приступим! А то я уже устал так напрягать речевой аппарат."
    
    "{cps=25}Морально-волевые волевые возможности по поддержанию напряжённого монолога явно покинули Арсенюшкина, и он продолжил занятие в свойственном ему стиле."
    
    arsenushkin "{cps=25}Гениальный."
    arsenushkin "{cps=25}Алан."
    arsenushkin "{cps=25}Человек."
    arsenushkin "{cps=25}Прометей принёс нам огонь, а он эти ваши компухтеры запилил."
    arsenushkin "{cps=25}Немцам расшифровал."
    arsenushkin "{cps=25}Энигму."
    arsenushkin "{cps=25}Хорошая сегодня погодка."
    arsenushkin "{cps=25}Так о чём это я?"
    arsenushkin "{cps=25}Ах да..."
    arsenushkin "{cps=25}Не посрамите имя великого учёного своими нелепыми каракулями в коде!"
    arsenushkin "{cps=25}Поговорим о профилях."
    arsenushkin "{cps=25}Что у нас есть?"
    arsenushkin "{cps=25}Первый профиль."
    arsenushkin "{cps=25}Автоматизированные системы…"
    arsenushkin "{cps=25}…обработки информации и управления."
    arsenushkin "{cps=25}Ух ты!"
    arsenushkin "{cps=25}Запомнил"
    arsenushkin "{cps=25}Короче..."
    arsenushkin "{cps=25}Профиль для тех кто хочет программировать."
    arsenushkin "{cps=25}Что там дальше?"
    arsenushkin "{cps=25}Информационные технологии в медиаиндустрии и дизайне."
    arsenushkin "{cps=25}Ага... "
    arsenushkin "{cps=25}Туда у нас обычно все девочки сбегают."
    arsenushkin "{cps=25}И те, кто рисовать умеет."
    arsenushkin "{cps=25}Технологии дополненной и виртуальной реальности."
    arsenushkin "{cps=25}Вот это лютая тема!"
    arsenushkin "{cps=25}Современно."
    arsenushkin "{cps=25}Модно."
    arsenushkin "{cps=25}Молодёжно."
    arsenushkin "{cps=25}Дальше по списку наш флагман."
    arsenushkin "{cps=25}Программное обеспечение игровой компьютерной индустрии."
    arsenushkin "{cps=25}Готовим оккупантов стимов да плеймаркетов."
    arsenushkin "{cps=25}Ну и последний профиль…"
    arsenushkin "{cps=25}Информационные системы умных пространств."
    arsenushkin "{cps=25}Там мы настоящих волшебников учим."
    arsenushkin "{cps=25}Кричишь “да будет свет” и лампочка загорается."
    arsenushkin "{cps=25}Ладно."
    arsenushkin "{cps=25}Об этом вам ешё более подробно расскажут."
    arsenushkin "{cps=25}Тест на внимательность!"
    
    menu:
        "{cps=25}Кто я?"
        "Дмитрий Алексеевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE
        "Дмитрий Андреевич":
            call ARSENTIEV_TRUE from _call_ARSENTIEV_TRUE
        "Андрей Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_1
        "Арсентий Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_2

    menu:
        arsenushkin "{cps=25}Тьюринга хоть помните?"
        "Это гениальный человек.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY
        "Да, это из-за него у нас есть компьютеры.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_1
        "Шифр немецкий расшифровал.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_2

    
    stop music fadeout 1.0

    
    return

label ARSENTIEV_TRUE:
    arsenushkin "{cps=25}Соколы!"
    return
    
label ARSENTIEV_FALSE:
    arsenushkin "{cps=25}Беда..."
    arsenushkin "{cps=25}Вы меня явно невнимательно слушали!"
    arsenushkin "{cps=25}Дмитрий Андреевич я!"
    return
    
label CONTINUE_STORY:
    arsenushkin "{cps=25}Вы чертовски правы!"
    arsenushkin "{cps=25}Ну ладно, гуляйте."
    return

