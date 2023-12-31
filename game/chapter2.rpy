
define olga = Character('Ольга', color="#ba00b7")

define student = Character('Неизвестный студент', color="#00baaa")

define audio.gostova = "music/gostova.mp3"

$tpr = False

define audio.gostova = "music/gostova.mp3"

$tpr = False

label startChapter2:
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА II “ТЕОРИЯ ПРИНЯТИЯ РЕШЕНИЙ”"
    scene university
    with fade
    
    "{cps=45}{i}Следующаяя пара - теория принятия решений."
    "{cps=45}{i}Звучит просто."
    "{cps=45}{i}Все студенты голову на плечах имеют, решения принимать умеют, да и предмет скорее всего разговорный будет."
    "{cps=45}{i}Хотя, чем проще предмет кажется, тем больше вероятность, что с ним возникнут неожиданные сложности."





    scene auditoriya_tpr
    with fade

    show olga
    with dissolve

    play music gostova



    olga "{cps=45}Здравствуйте студенты, меня зовут Гостова Ольга Владимировна."

    olga "{cps=45}Вам наверное интересно, о чём будет предмет - теория принятия решений?"
    olga "{cps=45}Начнём с простого. В теории принятия решений есть специальный термин – лицо, принимающее решение, сокращенно ЛПР."
    olga "{cps=45}Это тот, на ком лежит ответственность за принятое решение, тот, кто подписывает приказ или иной документ, в котором выражено решение."
    olga "{cps=45}Есть ещё много понятий важных в этой сфере, например, цели, регламент, риски, ресурсы и критерии оценивания, но пока мы поговорим о математической составляющей."

    olga "{cps=45}Математические модели и методы – необходимый элемент экономической теории на микро- и макроуровне. Их использование позволяет:"
    olga "{cps=45}Во-первых, выделить и формально описать наиболее важные, существенные связи переменных и объектов."
    olga "{cps=45}Во-вторых, из четко сформулированных исходных данных и соотношений методами дедукции можно получать выводы, адекватные изучаемому объекту в той же мере, что и сделанные предпосылки."

    hide olga 
    with dissolve
    show student
    student "{cps=45}Да я в лучшем случае только половину слов понимаю! Откуда терминов столько?! Я же не на физике или дискретке сижу."
    hide student 
    with dissolve
    show olga

    olga "{cps=45}Эй, на галёрке, не отвлекайтесь, это пока самые основы, не зная этого вы вообще у меня зачёт не получите."
    olga "{cps=45}Кстати, о зачёте, есть много правил, которые вам придётся соблюдать, если хотите, чтобы проблем не было."
    olga "{cps=45}Но одно из главных, это соблюдение всех ГОСТов. Они были придуманы не случайно, все вы должны их соблюдать при оформлении любых работ."
    olga "{cps=45}Так, сейчас не об этом. На чём я там остановилась? А точно.."

    olga "{cps=45}В-третьих, методы математики и статистики позволяют индуктивным путем получать новые знания об объекте: оценивать форму и параметры зависимостей его переменных, в наибольшей степени соответствующие имеющимся наблюдениям."
    olga "{cps=45}В-четвёртых, использование языка математики позволяет точно и компактно излагать положения теории, формулировать её понятия и выводы."

    olga "{cps=45}В общем, я думаю вы уже поняли, что пока мы сосредоточимся на математических методах, в такой науке, как принятие решений."
    
    olga "{cps=45}На этом закончим вводную часть лекции, теперь я хотела задать вам пару вопросов."
    olga "{cps=45}Как расшифровывается аббревиатура ЛПР?"

    $a = 0
    menu:
        "Лидер, принимающий решение.":
            pass
        "Лабораторно-практическая работа.":
            pass
        "Лицо, принимающее решение.":
            $a += 1
        "Личные параметры регламента.":
            pass


    olga "{cps=45}И ещё один вопрос, что можно получить из четко сформулированных исходных данных и соотношений методами дедукции?"

    menu:
        "Правильное решение":
            pass
        "Выводы, адекватные изучаемому объекту":
            $a += 1
        "Правильный ответ":
            pass
        "Объективный регламентированный способ решения задачи":
            pass
            
    if a == 0:
        olga "{cps=45}Это только первое занятие, а вы уже меня не слушаете, думаю нам трудно будет иметь с вами дело, поэтому сосредоточьтесь сейчас, чтобы не жалеть потом. С таким усердием зачёта вам не видать."
    elif a == 1:

        olga "{cps=45}Да, с памятью у вас, конечно, не очень, но суть вы улавливаете, поэтому приложите больше усилий и сдадите любой предмет без проблем."
        olga "{cps=45}Хоть и с долей скепсиса, но я признаю, что шансы не попасть на пересдачу у вас есть."
        $tpr = True
    else:
        olga "{cps=45}Вот, наконец умные ребята, которые умеют слушать преподавателя, у таких точно проблем не будет, ни с учёбой, ни с сессией, возможно далеко заглядываю, но понятно, что не просто так в ВУЗ поступали."
        olga "{cps=45}Вижу, вы претендуете на зачёт."
        $tpr = True
        

    olga "{cps=45}Ладно, на сегодня всё. Надеюсь, вы ответственно подойдёте к изучению моего предмеа. Уверена, это всё вам ещё ни раз пригодится. А пока отпускаю вас в свободное плавание, ещё увидимся."


    stop music fadeout 1.0


    stop music fadeout 1.0

    scene university
    with fade
    hide olga

    #поменял

    "{cps=45}{i}На сегодня пары закончились."

    "{cps=45}{i}Дома ждёт лучший друг студента - кровать."
    return