
define snegov = Character('Снегов', color="#003ea2")

define aperturova = Character('Апертурова', color="#f201ff")

define student = Character('Я', color="#00baaa")

define audio.jazz = "music/jazz.mp3"

define audio.street = "music/part.wav"

label startChapter4:

    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА IV “ЭКОЛОГИЯ”"    
    play music street
    scene street with dissolve

    "{cps=45}{i}Новый день, а впереди неизвестность."
    "{cps=45}{i}Неизвестность заключается в новом предмете."
    "{cps=45}{i}Вообще он называется “Нормирование качества и методы обращения с материалами информационных систем”."
    "{cps=45}{i}Однако все зовут его Экологией."
    "{cps=45}{i}Также разведданные говорят о том что у нас сразу два преподавателя на этом предмете."
    "{cps=45}{i}Нечего думать. На паре всё станет ясно."


    scene ecolab2 with fade

    show aperturova:
        xpos 0.3
    with dissolve
    show snegov:
        xpos -0.3
    with dissolve

    play music jazz

    snegov "{cps=45}Я пожалуй начну."
    snegov "{cps=45}Моё имя Сергей Спиридонович Снегов. Профессор. Химик."
    snegov "{cps=45}Вы здесь для того, чтобы изучить науку синтезирования различных веществ. Очень точную и тонкую науку."
    snegov "{cps=45}Глупое глядение в монитор к этой науке не имеет никакого отношения, и потому многие из вас с трудом поверят, что мой предмет является важной составляющей учебного плана."
    snegov "{cps=45}Я постараюсь научить вас, как околдовать разум и обмануть чувства. Я расскажу вам, как разлить по бутылкам спирт, как заваривать эпоксидную смолу и даже как закупорить аргон."
    "{cps=45}{i}Часть про спирт явно заинтересовала студентов."

    aperturova "{cps=45}Вы уже закончили, Сергей Спиридонович?"
    aperturova "{cps=45}Прошу простить моего коллегу. Он совсем не понимает сути данной дисциплины."
    aperturova "{cps=45}Забудьте всё, что он вам сказал. Я начну сначала. Так, как правильно."
    aperturova "{cps=45}Добро пожаловать в компьютеризированный экспериментальный центр при лаборатории исследования природы."
    aperturova "{cps=45}Меня зовут Ирина Георгиевна Апертурова. Как наиболее квалифицированный специалист в этом помещении, я рекомендую не прибегать к помощи всяких зельеваров."
    snegov "{cps=45}Всякие, как вы выразились, зельевары, умеют преподавать дисциплину, в отличие от прочих инвалидов умственного труда."
    aperturova "{cps=45}Я пожалуй пропущу мимо ушей вашу грубость и продолжу выполнять свою работу."
    aperturova "{cps=45}В этом научном комплексе мы будем проводить различные эксперименты."
    aperturova "{cps=45}Экспериментальный центр гарантирует абсолютную безопасность условий каждого испытания."
    aperturova "{cps=45}А в опасных условиях экспериментальный центр предоставляет помощь в виде полезных советов"
    aperturova "{cps=45}В целях соблюдения безопасности проведения утвержденных программой опытов просим вас не уничтожать оборудование первостепенной важности."



    aperturova "{cps=45}Первое испытание: Тест на определение жёсткости воды."
    aperturova "{cps=45}Всё необходимое оборудование лежит перед вами."

    snegov "{cps=45}Ой, а вы, я вижу, совсем для умственно отсталых рассказываете."
    snegov "{cps=45}Студенты итак прекрасно видят приборы и, уверен, понимают что это за устройства."
    snegov "{cps=45}Лучше сразу переходить к рецепту успеха сегодняшнего предприятия."
    snegov "{cps=45}Рецепт следующий: в коническую колбу пипеткой поместить 50 кубических сантиметров воды, с помощью пипетки добавить 5 миллилитров буферного раствора. Далее следует добавить индикатор эриохрома черного Т."
    snegov "{cps=45}Жидкость должна окраситься в сиреневый цвет."
    snegov "{cps=45}Самая интересная часть - это титрование. Нужно взять вторую пипетку и начать постепенно добавлять раствор трилона Б, пока цвет жидкости не сменится на синий потеряв красные тона."
    snegov "{cps=45}Спешить не следует, раствор меняет цвет только через несколько секунд. У некоторых особо торопливых жидкость не синеет, а чернеет."
    snegov "{cps=45}Количество капель нужно подсчитать и выяснить объём затраченного раствора трилона Б. Двадцать капель - один миллилитр."
    snegov "{cps=45}В итоге взяв эту цифру можно выяснить жёсткость воды."
    aperturova "{cps=45}Перед началом тестирования хотим вам напомнить, что хотя основным принципом экспериментального центра является обучение в игровой форме, мы не гарантируем отсутствие увечий и травм."
    aperturova "{cps=45}Можете приступать."

    
    call colbagame from _call_colbagame
    

    stop music fadeout 1.0
    return

label colbagame:
    hide aperturova
    hide snegov

    menu:
        "В колбу налить 50 миллилитров воды":
            show colba_voda with dissolve
               


    menu:
        "Добавить 5 мл буферного раствора":
            $trilon = 0
    menu:
        "Добавить индикатор эриохрома черного Т":
            $trilon = 0

    show colba_purple with dissolve
    hide colba_voda

    $trilon = 0
    $posinelo = False

    call addtrilon from _call_addtrilon

    return



label addtrilon:

    menu:
        "Добавить 5 капель раствора трилона Б":
            $trilon += 5
        "Добавить 10 капель раствора трилона Б":
            $trilon += 10
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
        "{cps=45}{i}В колбе вещество сиреневого цвета, но уже чуть-чуть синеет"
        jump addtrilon
    elif trilon > 55:
        show colba_black with dissolve
        hide colba_blue-purple
        "{cps=45}{i}Вещество в колбе стало чёрным, как душа сценаристов последнего сезона \"Икры Престолов\"."
        show snegov with dissolve
        snegov "Знаете, Мозг - сложный и многослойный орган - по крайней мере, у большинства людей, но, видимо, не у вас. Переделывайте."
        jump colbagame



    show colba_blue with dissolve
    hide colba_blue-purple

    "{cps=45}{i}Жижа посинела"
    "{cps=45}{i}Итого, затрачено было [trilon] капель трилона Б"
    $jest = trilon * 0.05
    "{cps=45}{i}Это значит, что жёсткость воды составляет [jest] градусов жёсткости."
    show aperturova with dissolve
    aperturova "{cps=45}Работа принята. Погрешность не превышена"

    
    return
       
    


