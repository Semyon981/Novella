
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

    "{cps=45}{i}Сентябрь. Знойное дыхание лета ещё не покинуло столицу."
    "{cps=45}{i}Утреннее солнце предвещает новые приключения."
    "{cps=45}{i}Что ждёт студента в его первый учебный день?"
    "{cps=45}{i}Корпус на улице Прянишникова (с некоторых пор здесь поселился факультет ИТ)."
    "{cps=45}{i}В народе это место известно как “Пряники”."
    "{cps=45}{i}Место спокойное и тихое. Находится около большого пруда, парка и садов Тимирязевской академии."
    
    scene university
    with fade
    
    play music arsenushkin

    show arsenushkin
    with dissolve
    
    arsenushkin "{cps=45}Я смотрю к нам прибыло пополнение."
    arsenushkin "{cps=45}Зовут меня Дмитрий Андреевич Арсенюшкин."
    arsenushkin "{cps=45}Я тут на кафедре информатики и ИТ вроде как не последний человек."
    
    hide arsenushkin
    with dissolve
    
    "{cps=45}{i}*перешёптывания в аудитории"
    "{cps=45}{i}Тот самый Арсенюшкин!" 
    "{cps=45}{i}Говорят, что он общается только сложными метафорами, шутками и оборванными фразами."
    "{cps=45}{i}Старшекурсники рассказывают, что у него есть уникальная способность появляться в нужный момент и предлагать сделать проект, за который можно получить зачёт."
    "{cps=45}{i}Ходят даже слухи что Арсенюшкин одолел кровожадность не менее легендарного Норникеля, что по половине группы валил."
    
    show arsenushkin
    with dissolve
    
    arsenushkin "{cps=45}Сегодня у нас будет первая пара по предмету “Введение в специальность”."
    arsenushkin "{cps=45}Вообще предмет будет проводится в дистанционном формате, так что напрягать вас с точки зрения передвижения не буду."
    arsenushkin "{cps=45}Итак… приступим! А то я уже устал так напрягать речевой аппарат."
    
    "{cps=45}Морально-волевые волевые возможности по поддержанию напряжённого монолога явно покинули Арсенюшкина, и он продолжил занятие в свойственном ему стиле."
    
    arsenushkin "{cps=45}Гениальный."
    arsenushkin "{cps=45}Алан."
    arsenushkin "{cps=45}Человек."
    arsenushkin "{cps=45}Прометей принёс нам огонь, а он эти ваши компухтеры запилил."
    arsenushkin "{cps=45}Немцам расшифровал."
    arsenushkin "{cps=45}Энигму."
    arsenushkin "{cps=45}Хорошая сегодня погодка."
    arsenushkin "{cps=45}Так о чём это я?"
    arsenushkin "{cps=45}Ах да..."
    arsenushkin "{cps=45}Не посрамите имя великого учёного своими нелепыми каракулями в коде!"
    arsenushkin "{cps=45}Поговорим о профилях."
    arsenushkin "{cps=45}Что у нас есть?"
    arsenushkin "{cps=45}Первый профиль."
    arsenushkin "{cps=45}Автоматизированные системы…"
    arsenushkin "{cps=45}…обработки информации и управления."
    arsenushkin "{cps=45}Ух ты!"
    arsenushkin "{cps=45}Запомнил"
    arsenushkin "{cps=45}Короче..."
    arsenushkin "{cps=45}Профиль для тех кто хочет программировать."
    arsenushkin "{cps=45}Что там дальше?"
    arsenushkin "{cps=45}Информационные технологии в медиаиндустрии и дизайне."
    arsenushkin "{cps=45}Ага... "
    arsenushkin "{cps=45}Туда у нас обычно все девочки сбегают."
    arsenushkin "{cps=45}И те, кто рисовать умеет."
    arsenushkin "{cps=45}Технологии дополненной и виртуальной реальности."
    arsenushkin "{cps=45}Вот это лютая тема!"
    arsenushkin "{cps=45}Современно."
    arsenushkin "{cps=45}Модно."
    arsenushkin "{cps=45}Молодёжно."
    arsenushkin "{cps=45}Дальше по списку наш флагман."
    arsenushkin "{cps=45}Программное обеспечение игровой компьютерной индустрии."
    arsenushkin "{cps=45}Готовим оккупантов стимов да плеймаркетов."
    arsenushkin "{cps=45}Ну и последний профиль…"
    arsenushkin "{cps=45}Информационные системы умных пространств."
    arsenushkin "{cps=45}Там мы настоящих волшебников учим."
    arsenushkin "{cps=45}Кричишь “да будет свет” и лампочка загорается."
    arsenushkin "{cps=45}Ладно."
    arsenushkin "{cps=45}Об этом вам ешё более подробно расскажут."
    arsenushkin "{cps=45}Тест на внимательность!"
    
    menu:
        "{cps=45}{i}Кто я?"
        "Дмитрий Алексеевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE
        "Дмитрий Андреевич":
            call ARSENTIEV_TRUE from _call_ARSENTIEV_TRUE
        "Андрей Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_1
        "Арсентий Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_2

    menu:
        arsenushkin "{cps=45}{i}Тьюринга хоть помните?"
        "Это гениальный человек.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY
        "Да, это из-за него у нас есть компьютеры.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_1
        "Шифр немецкий расшифровал.": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_2

    
    stop music fadeout 1.0

    
    return

label ARSENTIEV_TRUE:
    arsenushkin "{cps=45}Соколы!"
    return
    
label ARSENTIEV_FALSE:
    arsenushkin "{cps=45}Беда..."
    arsenushkin "{cps=45}Вы меня явно невнимательно слушали!"
    arsenushkin "{cps=45}Дмитрий Андреевич я!"
    return
    
label CONTINUE_STORY:
    arsenushkin "{cps=45}Вы чертовски правы!"
    arsenushkin "{cps=45}Ну ладно, гуляйте."
    return

