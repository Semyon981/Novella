
define arsenushkin = Character('Арсенюшкин', color="#ba0000")

define audio.street = "music/part.wav"
define audio.arsenushkin = "music/arsenushkin.mp3"

$ renpy.force_autosave()


label startChapter1:
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА I. ВВЕДЕНИЕ В СПЕЦИАЛЬНОСТЬ"

    scene street
    with fade

    play music street

    "{i}Сентябрь. Знойное дыхание лета ещё не покинуло столицу."
    "{i}Утреннее солнце предвещает новые приключения."
    "{i}Что ждёт студента в его первый учебный день?"
    "{i}Корпус на улице Прянишникова (с некоторых пор здесь поселился факультет ИТ)."
    "{i}В народе это место известно как “Пряники”."
    "{i}Место спокойное и тихое. Находится около большого пруда, парка и садов Тимирязевской академии."
    
    scene university
    with fade
    
    play music arsenushkin

    show arsenushkin
    with dissolve
    
    arsenushkin "Я смотрю к нам прибыло пополнение."
    arsenushkin "Зовут меня Дмитрий Андреевич Арсенюшкин."
    arsenushkin "Я тут на кафедре информатики и ИТ вроде как не последний человек."
    
    hide arsenushkin
    with dissolve
    
    "{i}*перешёптывания в аудитории"
    "{i}Тот самый Арсенюшкин!" 
    "{i}Говорят, что он общается только сложными метафорами, шутками и оборванными фразами."
    "{i}Старшекурсники рассказывают, что у него есть уникальная способность появляться в нужный момент и предлагать сделать проект, за который можно получить зачёт."
    "{i}Ходят даже слухи что Арсенюшкин одолел кровожадность не менее легендарного Норникеля, что по половине группы валил."
    
    show arsenushkin
    with dissolve
    
    arsenushkin "Сегодня у нас будет первая пара по предмету “Введение в специальность”."
    arsenushkin "Вообще предмет будет проводится в дистанционном формате, так что напрягать вас с точки зрения передвижения не буду."
    arsenushkin "Итак… приступим! А то я уже устал так напрягать речевой аппарат."
    
    "Морально-волевые волевые возможности по поддержанию напряжённого монолога явно покинули Арсенюшкина, и он продолжил занятие в свойственном ему стиле."
    
    arsenushkin "Гениальный."
    arsenushkin "Алан."
    arsenushkin "Человек."
    arsenushkin "Прометей принёс нам огонь, а он эти ваши компухтеры запилил."
    arsenushkin "Немцам расшифровал."
    arsenushkin "Энигму."
    arsenushkin "Хорошая сегодня погодка."
    arsenushkin "Так о чём это я?"
    arsenushkin "Ах да..."
    arsenushkin "Не посрамите имя великого учёного своими нелепыми каракулями в коде!"
    arsenushkin "Поговорим о профилях."
    arsenushkin "Что у нас есть?"
    arsenushkin "Первый профиль."
    arsenushkin "Автоматизированные системы…"
    arsenushkin "…обработки информации и управления."
    arsenushkin "Ух ты!"
    arsenushkin "Запомнил"
    arsenushkin "Короче..."
    arsenushkin "Профиль для тех кто хочет программировать."
    arsenushkin "Что там дальше?"
    arsenushkin "Информационные технологии в медиаиндустрии и дизайне."
    arsenushkin "Ага... "
    arsenushkin "Туда у нас обычно все девочки сбегают."
    arsenushkin "И те, кто рисовать умеет."
    arsenushkin "Технологии дополненной и виртуальной реальности."
    arsenushkin "Вот это лютая тема!"
    arsenushkin "Современно."
    arsenushkin "Модно."
    arsenushkin "Молодёжно."
    arsenushkin "Дальше по списку наш флагман."
    arsenushkin "Программное обеспечение игровой компьютерной индустрии."
    arsenushkin "Готовим оккупантов стимов да плеймаркетов."
    arsenushkin "Ну и последний профиль…"
    arsenushkin "Информационные системы умных пространств."
    arsenushkin "Там мы настоящих волшебников учим."
    arsenushkin "Кричишь “да будет свет” и лампочка загорается."
    arsenushkin "Ладно."
    arsenushkin "Об этом вам ешё более подробно расскажут."
    arsenushkin "Тест на внимательность!"
    
    menu:
        "{i}Кто я?"
        "Дмитрий Алексеевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE
        "Дмитрий Андреевич":
            call ARSENTIEV_TRUE from _call_ARSENTIEV_TRUE
        "Андрей Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_1
        "Арсентий Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_2

    menu:
        arsenushkin "{i}Тьюринга хоть помните?"
        "Это гениальный человек.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY
        "Да, это из-за него у нас есть компьютеры.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_1
        "Шифр немецкий расшифровал.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_2

    
    stop music fadeout 1.0

    
    return

label ARSENTIEV_TRUE:
    arsenushkin "Соколы!"
    return
    
label ARSENTIEV_FALSE:
    arsenushkin "Беда..."
    arsenushkin "Вы меня явно невнимательно слушали!"
    arsenushkin "Дмитрий Андреевич я!"
    return
    
label CONTINUE_STORY:
    arsenushkin "Вы чертовски правы!"
    arsenushkin "Ну ладно, гуляйте."
    return

