
define snegov = Character('Снегов', color="#003ea2")

define aperturova = Character('Апертурова', color="#f201ff")

define audio.jazz = "music/jazz.mp3"

define audio.street = "music/part.wav"

label startChapter4:

    scene black
    with fade

    "{font=Gilroy-ExtraBold.otf}ГЛАВА IV. ЭКОЛОГИЯ"

    play music street

    scene street with dissolve

    "{i}Новый день, а впереди неизвестность."
    "{i}Неизвестность заключается в новом предмете."
    "{i}Вообще он называется “Нормирование качества и методы обращения с материалами информационных систем”"
    "{i}Однако все зовут его Экологией."
    "{i}Также разведданные говорят о том что у нас сразу два преподавателя на этом предмете."
    "{i}Нечего думать. На паре всё станет ясно."


    scene ecolab2 with fade

    show aperturova:
        xpos 0.3
    with dissolve
    show snegov:
        xpos -0.3
    with dissolve

    play music jazz

    snegov "Я пожалуй начну."

    snegov "Моё имя Сергей Спиридонович Снегов. Профессор. Химик."
    snegov "Вы здесь для того, чтобы изучить науку синтезирования различных веществ. Очень точную и тонкую науку."
    snegov "Глупое глядение в монитор к этой науке не имеет никакого отношения, и потому многие из вас с трудом поверят, что мой предмет является важной составляющей учебного плана."
    snegov "Я постараюсь научить вас, как околдовать разум и обмануть чувства. Я расскажу вам, как разлить по бутылкам спирт, как заваривать эпоксидную смолу и даже как закупорить аргон."
    "{i}Часть про спирт явно заинтересовала студентов."

    aperturova "Вы уже закончили, Сергей Спиридонович?"
    aperturova "Прошу простить моего коллегу. Он совсем не понимает сути данной дисциплины."
    aperturova "Забудьте всё, что он вам сказал. Я начну сначала. Так, как правильно."
    aperturova "Добро пожаловать в компьютеризированный экспериментальный центр при лаборатории исследования природы."
    aperturova "Меня зовут Ирина Георгиевна Апертурова. Как наиболее квалифицированный специалист в этом помещении, я рекомендую не прибегать к помощи всяких зельеваров."
    snegov "Всякие, как вы выразились, зельевары, умеют преподавать дисциплину, в отличие от прочих инвалидов умственного труда."
    aperturova "Я пожалуй пропущу мимо ушей вашу грубость и продолжу выполнять свою работу."
    aperturova "В этом научном комплексе мы будем проводить различные эксперименты."
    aperturova "Экспериментальный центр гарантирует абсолютную безопасность условий каждого испытания."
    aperturova "А в опасных условиях экспериментальный центр предоставляет помощь в виде полезных советов"
    aperturova "В целях соблюдения безопасности проведения утвержденных программой опытов просим вас не уничтожать оборудование первостепенной важности."



    aperturova "Первое испытание: Тест на определение жёсткости воды."
    aperturova "Всё необходимое оборудование лежит перед вами."

    snegov "Ой, а вы, я вижу, совсем для умственно отсталых рассказываете."
    snegov "Студенты итак прекрасно видят приборы и, уверен, понимают что это за устройства."
    snegov "Лучше сразу переходит к рецепту успеха сегодняшнего предприятия."
    snegov "Рецепт следующий: в коническую колбу пипеткой поместить 50 кубических сантиметров воды, с помощью пипетки добавить 5 миллилитров буферного раствора. Далее следует добавить индикатор эриохрома черного Т.. Жидкость должна окраситься в сиреневый цвет."
    snegov "Самая интересная часть - это титрование. Нужно взять вторую пипетку и начать постепенно добавлять раствор трилона Б, пока цвет жидкости не сменится на синий потеряв красные тона. Спешить не следует, раствор меняет цвет только через несколько секунд. У некоторых особо торопливых жидкость не синеет, а чернеет. Количество капель нужно подсчитать и выяснить объём затраченного раствора трилона Б. Двадцать капель - один миллилитр."
    snegov "В итоге взяв эту цифру можно выяснить жёсткость воды."
    aperturova "Перед началом тестирования хотим вам напомнить, что хотя основным принципом экспериментального центра является обучение в игровой форме, мы не гарантируем отсутствие увечий и травм."
    aperturova "Можете приступать."

   

    
    
    call colbagame
    

    stop music fadeout 1.0
    return

label colbagame:
    hide aperturova
    hide snegov
    
    menu:
        "В колбу налить 50 миллилитров воды":
            pass
            
    
    show colba_voda with dissolve

    menu:
        "Добавить 5 мл буферного раствора":
            pass

    menu:
        "Добавить индикатор эриохрома черного Т":
            pass

    show colba_purple with dissolve
    hide colba_voda

    $trilon = 0
    $posinelo = False

    call addtrilon

    return



label addtrilon:

    menu:
        "Добавить 10 капель раствора трилона Б":
            $trilon += 10
        "Добавить 5 капель раствора трилона Б":
            $trilon += 5
        "Добавить 20 капель раствора трилона Б":
            $trilon += 20

    if trilon < 40:
        "{i}Цвет явно не синий. Надо продолжать."
        jump addtrilon
    elif trilon >= 40 and trilon <= 50:
        if posinelo == False:
            show colba_blue-purple with dissolve
            hide colba_purple
            $posinelo = True
        "{i}В колбе вещество сиреневого цвета, но уже чуть-чуть синеет"
        jump addtrilon
    elif trilon > 55:
        show colba_black with dissolve
        hide colba_blue-purple
        "Вещество в колбе стало чёрным, как душа сценаристов последнего сезона \"Икры Престолов\"."
        show snegov with dissolve
        snegov "Знаете, Мозг - сложный и многослойный орган - по крайней мере, у большинства людей, но, видимо, не у вас. Переделывайте."
        jump colbagame



    show colba_blue with dissolve
    hide colba_blue-purple
            
    "{i}Жижа посинела"
    "{i}Итого, затрачено было [trilon] капель трилона Б"
    $jest = trilon * 0.05
    "{i}Это значит, что жёсткость воды составляет [jest] градусов жёсткости."
    show aperturova with dissolve
    aperturova "Работа принята. Погрешность не превышена"



    
    return
       
    


