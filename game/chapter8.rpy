define arsentiev = Character('Арсюшкин', color="#ffea00")
<<<<<<< Updated upstream
define student = Character('Я', color="#00baaa")
=======
define student = Character('Неизвестный студент', color="#00baaa")
>>>>>>> Stashed changes
define nastya = Character('Настя', color="#ff7a7a")
define valera = Character('Валера', color="#00baaa")
define sanek = Character('Саня', color="#8f8f8f")

<<<<<<< Updated upstream
label startChapter8:

    scene black
    with fade

    "{font=Gilroy-ExtraBold.otf}ГЛАВА XIII. СЕССИЯ"
=======
define audio.arsentiev = "music/arsentiev.mp3"

label startChapter8:
    
    stop music fadeout 1.0
    scene black
    with fade

    "{font=Gilroy-ExtraBold.otf}ГЛАВА VIII ”СЕССИЯ”"
>>>>>>> Stashed changes
    

    scene university
    with fade

<<<<<<< Updated upstream
    show arsentiev
    with dissolve
    
    arsentiev "{cps=25}О, давно не виделись!"
    arsentiev "{cps=25}Поговаривают, что у кого-то тут трудности с зачëтами появились"
    arsentiev "{cps=25}А я так и знал, что у некоторых проблемки возникнут!"
    arsentiev "{cps=25}Но на то они и проблемки, а не проблемы, значит поменьше и решать проще"
    arsentiev "{cps=25}Именно, чтобы помочь с этими проблемками, я и пришëл"
    arsentiev "{cps=25}У меня тут появилась пара этих ... Как его... Интересных инициатив!"
    arsentiev "{cps=25}Но они только для активных и ответственных. Поэтому полный вперëд!"
=======
    play music arsentiev

    show arsentiev
    with dissolve
    
    arsentiev "{cps=45}О, давно не виделись!"
    arsentiev "{cps=45}Поговаривают, что у кого-то тут трудности с зачëтами появились."
    arsentiev "{cps=45}А я так и знал, что у некоторых проблемки возникнут!"
    arsentiev "{cps=45}Но на то они и проблемки, а не проблемы, значит поменьше и решать проще."
    arsentiev "{cps=45}Именно, чтобы помочь с этими проблемками, я и пришëл."
    arsentiev "{cps=45}У меня тут появилась пара этих ... Как его... Интересных инициатив!"
    arsentiev "{cps=45}Но они только для активных и ответственных. Поэтому полный вперëд!"
>>>>>>> Stashed changes
    
    hide arsentiev
    with dissolve
    
<<<<<<< Updated upstream
    "{i}Все студенты столпились вокруг фигуры солнцеликого Арсенюшкина{i}"
    "{i}Каждый из них ждал, какой способ спасения души от первой заваленной сессии предложит всем известный не последний человек на кафедре{i}"
    "{i}Некоторые перешëптываются о каторжной работе на пользу университета{i}"
    
    student "{cps=25}Надеюсь, нас не превратят в уборщиков или строителей, я всë-таки не за этим сюда поступал..."
    
    "{i}Но тут всех успокоил вовремя вступивший с продолжением своей пламенной речи Арсенюшкин{i}"
=======
    "{cps=45}{i}Все студенты столпились вокруг фигуры солнцеликого Арсенюшкина.{i}"
    "{cps=45}{i}Каждый из них ждал, какой способ спасения души от первой заваленной сессии предложит всем известный не последний человек на кафедре.{i}"
    "{cps=45}{i}Некоторые перешëптываются о каторжной работе на пользу университета.{i}"
    
    show student
    student "{cps=45}Надеюсь, нас не превратят в уборщиков или строителей, я всë-таки не за этим сюда поступал..."
    hide student
    with dissolve

    "{cps=45}{i}Но тут всех успокоил вовремя вступивший с продолжением своей пламенной речи Арсенюшкин.{i}"
>>>>>>> Stashed changes
    
    show arsentiev
    with dissolve
    
<<<<<<< Updated upstream
    arsentiev "{cps=25}Тут есть вариант, который поможет всем вам одновременно"
    arsentiev "{cps=25}Вы же молодые программисты?"
    
    "{i}Все студенты утвердительно кивают{i}"
    
    arsentiev "{cps=25}Вот и я так думаю"
    arsentiev "{cps=25}Именно поэтому всплыл очень важный вопрос"
    arsentiev "{cps=25}А вы слышали о таком мероприятии, как хакатон?"   
    
    "{i}Большинство студентов одобрительно кивает, а некоторые смотрят удивлëнными глазами{i}"
    
    arsentiev "{cps=25}Для тех, кто вырос в лесу или специально игнорировал всех и вся в сфере IT, я поясню"
    arsentiev "{cps=25}Хакатон — это, понимаете ли, такое мероприятие, на котором программисты, дизайнеры, маркетологи и прочие заимствованные слова решают в одной команде какую-нибудь интересную задачу, соревнуясь с другими командами"
    arsentiev "{cps=25}Теперь, надеюсь, хотя бы этот вопрос отпал"
    arsentiev "{cps=25}Ладно, к чему я это всë..."
    arsentiev "{cps=25}Точно, я вас именно на этот хакатон пригласить и хотел!"
    arsentiev "{cps=25}Если удачно справитесь с задачей или просто покажете достойный результат..."
    arsentiev "{cps=25}Вы сами должны понимать, что тогда мне проще будет убедить других преподавателей, как говориться, по моим правилам сыграть"
    arsentiev "{cps=25}Ладно, слишком уж я начал растекаться мыслью по древу"
    arsentiev "{cps=25}К сути"
    arsentiev "{cps=25}На хакатоне вы будете писать компьютерную игру"
    arsentiev "{cps=25}Но вам ещë и очень повезло, ведь писать еë вы будете на C++"
    arsentiev "{cps=25}Думаю вы должны понимать, в чëм ваше везение"
    arsentiev "{cps=25}Ведь в этом языке одни плюсы, недаром они даже в названии есть"
    arsentiev "{cps=25}Тааак... В курс дела я вас ввëл..."
    arsentiev "{cps=25}Теперь ждите моей команды, как опытные солдаты"
      
    student "{cps=25}Яволь!"
    
    arsentiev "{cps=25}Хахаха, шучу я, шучу"
    arsentiev "{cps=25}Я же знаю, что в армию из вас никто не хочет, потому и ко мне пришли. Один незачёт я вам могу прикрыть"
    arsentiev "{cps=25}Но отмашку с моей стороны ждите, обговорю с преподавателями и вас в списки на хакатон подам"
    arsentiev "{cps=25}Задание будет позже. На выполнение у вас будет две недели"
=======
    arsentiev "{cps=45}Тут есть вариант, который поможет всем вам одновременно."
    arsentiev "{cps=45}Вы же молодые айтишники?"
    
    "{cps=45}{i}Все студенты утвердительно кивают.{i}"
    
    arsentiev "{cps=45}Вот и я так думаю"
    arsentiev "{cps=45}Именно поэтому всплыл очень важный вопрос."
    arsentiev "{cps=45}А вы слышали о таком мероприятии, как хакатон?"   
    
    "{cps=45}{i}Большинство студентов одобрительно кивает, а некоторые смотрят удивлëнными глазами.{i}"
    
    arsentiev "{cps=45}Для тех, кто вырос в лесу или специально игнорировал всех и вся в сфере IT, я поясню."
    arsentiev "{cps=45}Хакатон — это, понимаете ли, такое мероприятие, на котором программисты, дизайнеры, маркетологи и прочие заимствованные слова решают в одной команде какую-нибудь интересную задачу, соревнуясь с другими командами."
    arsentiev "{cps=45}Теперь, надеюсь, хотя бы этот вопрос отпал."
    arsentiev "{cps=45}Ладно, к чему я это всë..."
    arsentiev "{cps=45}Точно, я вас именно на этот хакатон пригласить и хотел!"
    arsentiev "{cps=45}Если удачно справитесь с задачей или просто покажете достойный результат..."
    arsentiev "{cps=45}Вы сами должны понимать, что тогда мне проще будет убедить других преподавателей, как говориться, по моим правилам сыграть."
    arsentiev "{cps=45}Ладно, слишком уж я начал растекаться мыслью по древу."
    arsentiev "{cps=45}К сути."
    arsentiev "{cps=45}На хакатоне вы будете писать компьютерную игру."
    arsentiev "{cps=45}Но вам ещë и очень повезло, ведь писать еë вы будете на C++."
    arsentiev "{cps=45}Думаю вы должны понимать, в чëм ваше везение."
    arsentiev "{cps=45}Ведь в этом языке одни плюсы, недаром они даже в названии есть."
    arsentiev "{cps=45}Тааак... В курс дела я вас ввëл..."
    arsentiev "{cps=45}Теперь ждите моей команды, как опытные солдаты."
    
    hide arsentiev
    with dissolve
    show student
    student "{cps=45}Яволь!"
    hide student
    with dissolve
    show arsentiev
    with dissolve
    
    arsentiev "{cps=45}Хахаха, шучу я, шучу!"
    arsentiev "{cps=45}Я же знаю, что в армию из вас никто не хочет, потому и ко мне пришли. Незачётик я вам запросто могу прикрыть."
    arsentiev "{cps=45}Но отмашку с моей стороны ждите, обговорю с преподавателями и вас в списки на хакатон подам."
    arsentiev "{cps=45}Задание будет позже. На выполнение у вас будет две недели."
>>>>>>> Stashed changes
    
    hide arsentiev
    with dissolve
    
<<<<<<< Updated upstream
    "{i}Через некоторое время настала пора познакомиться с командой и приступить к ковке победы{i}"
=======
    "{cps=45}{i}Через некоторое время настала пора познакомиться с командой и приступить к ковке победы.{i}"
>>>>>>> Stashed changes
    
    scene university
    with fade

    show nastya
    with dissolve
    
<<<<<<< Updated upstream
    nastya "{cps=25}Алоха! Меня Настя зовут!"
    nastya "{cps=25}Умею рисовать, делать 3D модели, анимировать. Художку закончила"
    nastya "{cps=25}Буду рада работать в команде!"
=======
    nastya "{cps=45}Алоха! Меня Настя зовут!"
    nastya "{cps=45}Умею рисовать, делать 3D модели, анимировать. Художку закончила."
    nastya "{cps=45}Буду рада работать в команде!"
>>>>>>> Stashed changes
    
    hide nastya
    with dissolve
    
    show valera
    with dissolve
    
<<<<<<< Updated upstream
    valera "{cps=25}Живите долго и процветайте, земляне!"
    valera "{cps=25}Я Валера. Я хороший человек, ведь код определяет человека"
    valera "{cps=25}Пока все писали на заборах, я писал код"
    valera "{cps=25}Мой родной язык Java Script"
    valera "{cps=25}Надеюсь, сработаемся..."
    valera "{cps=25}Пока все писали на заборах, я писал код"
=======
    valera "{cps=45}Живите долго и процветайте, земляне!"
    valera "{cps=45}Я Валера. Я хороший человек, ведь код определяет человека."
    valera "{cps=45}Пока все писали на заборах, я писал код."
    valera "{cps=45}Мой родной язык Java Script."
    valera "{cps=45}Надеюсь, сработаемся..."

>>>>>>> Stashed changes
    
    hide valera
    with dissolve
    
    show sanek
    with dissolve
    
<<<<<<< Updated upstream
    sanek "{cps=25}Я вас категорически приветствую!"
    sanek "{cps=25}Могу помочь со сценариям"
    sanek "{cps=25}Вообще я тестировщик, а писательство так… Для души"
    sanek "{cps=25}В свободное от основного творчества время пишу музыку"
=======
    sanek "{cps=45}Я вас категорически приветствую!"
    sanek "{cps=45}Могу помочь со сценариям."
    sanek "{cps=45}Вообще я тестировщик, а писательство так… Для души."
    sanek "{cps=45}В свободное от основного творчества время пишу музыку."
>>>>>>> Stashed changes
    
    hide sanek
    with dissolve
    
    show valera
    with dissolve
    
<<<<<<< Updated upstream
    valera "{cps=25}О! А не ты ли разрыдался после математики, когда узнал, что есть мнимая единица?"
=======
    valera "{cps=45}О! А не ты ли разрыдался после математики, когда узнал, что есть мнимая единица?"
>>>>>>> Stashed changes
    
    hide valera
    with dissolve
    
    show nastya
    with dissolve 
    
<<<<<<< Updated upstream
    nastya "{cps=25}Ха! Я тоже это помню! “Весь наш мир мнимый! Всё ненастоящее!"
=======
    nastya "{cps=45}Ха! Я тоже это помню! “Весь наш мир мнимый! Всё ненастоящее!"
>>>>>>> Stashed changes
    
    hide nastya
    with dissolve 
    
    menu:
        "Похохотать":
            jump Bad_choice
        "Попросить прекратить":
            jump Good_choice
    return
    
    
    
label Bad_choice:
    
    show sanek
    with dissolve
    
<<<<<<< Updated upstream
    sanek "{cps=25}Сволочи! Негодяи! Видеть вас не хочу!"
=======
    sanek "{cps=45}Сволочи! Негодяи! Видеть вас не хочу!"
>>>>>>> Stashed changes
    
    hide sanek
    with dissolve
    
<<<<<<< Updated upstream
    "{i}Александр отказался участвовать{i}"
    "{i}Без него вся команда осталась у разбитого корыта{i}"
    "{i}Арсюшкин расстроен, поэтому зачёты можно не ждать{i}"
=======
    "{cps=45}{i}Александр отказался участвовать.{i}"
    "{cps=45}{i}Без него вся команда осталась у разбитого корыта.{i}"
    "{cps=45}{i}Арсюшкин расстроен, поэтому зачёты можно не ждать.{i}"
>>>>>>> Stashed changes
    
    return
    
    
    
label Good_choice:
    
    show nastya
    with dissolve
    
<<<<<<< Updated upstream
    nastya "{cps=25}Окей, окей. Проехали"
=======
    nastya "{cps=45}Окей, окей. Проехали"
>>>>>>> Stashed changes
    
    hide nastya
    with dissolve
    
    scene comp
    with dissolve
    
    "ОБЩЕНИЕ В ЧАТЕ"
    scene comp_valera
    with dissolve
<<<<<<< Updated upstream
    valera "{cps=25}Давай движок состряпаю?"
=======
    valera "{cps=45}Давай движок состряпаю?"
>>>>>>> Stashed changes
    menu:
        "Давай":
            jump choice_davay
        "Все на Unity делаем":
            jump unity_do
    return
    
    
    
label choice_davay:
    scene comp_nastya
    with dissolve
    
<<<<<<< Updated upstream
    nastya "{cps=25}Хочу рейтрейсинг в движке!"
    menu:
        "Скажу Валере сделать":
            jump choice_valerado
        "Перехочешь":
            jump unity_do
=======
    nastya "{cps=45}Хочу рейтрейсинг в движке!"
    menu:
        "Перехочешь!":
            jump unity_do
        "ВАЛЕРА, ТВОЙ ВЫХОД!":
            jump choice_valerado
>>>>>>> Stashed changes
    return



label choice_valerado:
    scene comp_valera
    with dissolve
<<<<<<< Updated upstream
    valera "{cps=25}Ты чё!? Как я это сделаю? Я тебе миллиардная корпорация что ли?"
=======
    valera "{cps=45}Ты чё!? Как я это сделаю? Я тебе миллиардная корпорация что ли?"
>>>>>>> Stashed changes
    menu:
        "Сделаешь как-нибудь":
            jump choice_valerasdelaesh
        "Ладно, без трассировки обойдемся":
            jump unity_do
    return


label choice_valerasdelaesh:
<<<<<<< Updated upstream
    "{i}Валера не успел{i}"
    "{i}Из-за рейтрейсинга Валера вообще ничего не успел реализовать{i}"
    "{i}В итоге вся команда провалилась{i}"
    "{i}Арсюшкин расстроен, поэтому зачёты можно не ждать{i}"
=======
    "{cps=45}{i}Валера не успел.{i}"
    "{cps=45}{i}Из-за рейтрейсинга Валера вообще ничего не успел реализовать.{i}"
    "{cps=45}{i}В итоге вся команда провалилась.{i}"
    "{cps=45}{i}Арсюшкин расстроен, поэтому зачёты можно не ждать.{i}"
    jump end_scene
>>>>>>> Stashed changes
    return



label unity_do:
    scene comp_sanek
    with dissolve
<<<<<<< Updated upstream
    sanek "{cps=25}Предлагаю добавить сцену в потустороннем мире"
=======
    sanek "{cps=45}Предлагаю добавить сцену в потустороннем мире."
>>>>>>> Stashed changes
    menu:
        "Как хочешь":
            pass
        "Нет!":
            pass
    scene comp_valera
    with dissolve
<<<<<<< Updated upstream
    valera "{cps=25}Давай напишем продвинутый ИИ?"
=======
    valera "{cps=45}Давай напишем продвинутый ИИ?"
>>>>>>> Stashed changes
    menu:
        "А давайте!":
            pass
        "Давайте без davayte":
            pass
    scene comp_nastya
    with dissolve
<<<<<<< Updated upstream
    nastya "{cps=25}Предлагаю добавить кастомизацию снаряжения"
=======
    nastya "{cps=45}Предлагаю добавить кастомизацию снаряжения"
>>>>>>> Stashed changes
    menu:
        "Лишнее":
            pass
        "Почему бы и нет":
            pass
    scene comp_sanek
    with dissolve
<<<<<<< Updated upstream
    sanek "{cps=25}Слушай, может мы удвоим количество третьестепенных персонажей, а то мне кажется, что их по ходу повествования мало умирает?"
    menu:
        "Отличная идея!":
            jump sessia_successful
        "АСТАНАВИТЕСЬ!":
            jump sessia_successful


label sessia_successful:
    scene university
    with fade
    
    "{i}Шедевр геймдева готов!{i}"
    "{i}На хакатоне он не победил, но всем запомнился чрезвычайной жестокостью{i}"
    "{i}Арсюшкин остался доволен, поэтому сессия в кармане!{i}"
=======
    sanek "{cps=45}Слушай, может мы удвоим количество третьестепенных персонажей, а то мне кажется, что их по ходу повествования мало умирает?"
    menu:
        "Отличная идея!":
            jump sessia_successful1
        "АСТАНАВИТЕСЬ!":
            jump sessia_successful2


label sessia_successful1:
    scene university
    with fade
    
    "{cps=45}{i}Шедевр геймдева готов!{i}"
    "{cps=45}{i}На хакатоне он не победил, но всем запомнился чрезвычайной жестокостью.{i}"
    "{cps=45}{i}Арсюшкин остался доволен, поэтому сессия в кармане!{i}"
>>>>>>> Stashed changes
    
    show arsentiev
    with dissolve
    
<<<<<<< Updated upstream
    arsentiev "{cps=25}Ну что ж соколы... Поздравляю вас! Молодцы!"
    arsentiev "{cps=25}Долгов у вас больше нет! Все зачтено!"
    return
=======
    arsentiev "{cps=45}Ну что ж соколы... Поздравляю вас! Молодцы!"
    arsentiev "{cps=45}Долгов у вас больше нет! Все зачтено!"
    jump end_scene
    return

label sessia_successful2:
    scene university
    with fade
    
    "{cps=45}{i}Шедевр геймдева готов!{i}"
    "{cps=45}{i}Сие творение буквально переиграло и уничтожило всех конкурентов.{i}"
    "{cps=45}{i}Арсюшкин остался доволен, поэтому сессия в кармане!{i}"
    
    show arsentiev
    with dissolve
    
    arsentiev "{cps=45}Ну что ж соколы... Поздравляю вас! Молодцы!"
    arsentiev "{cps=45}Долгов у вас больше нет! Все зачтено!"
    jump end_scene
    return

label end_scene:
    scene end 
    with dissolve
    $ renpy.pause(3.0)
    scene black with fade
    return

>>>>>>> Stashed changes
