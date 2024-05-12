define udmurtov = Character('Удмуртов Владимир Святозарович', color="#000000")
define audio.riff = "music/soundscrate-repetitive-riff.mp3"


label startChapterOOP:
    scene black with fade

    play music riff fadein 2.0
    "{font=Gilroy-ExtraBold.otf}ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ"

    scene oop with fade
    show udmurtov

    udmurtov "Приветствую, товарищи будущие программисты."
    udmurtov "Хотяяя, какие вы мне товарищи..."
    udmurtov "Вам ведь и до будущих программистов, как до Китая ..., ну вы сами поняли."
    udmurtov "Ладно, не буду сильно запугивать, жизнь напугать успеет."
    udmurtov "Перейдëм к сути. На этом курсе мы с вами будем изучать такую методологию, как объектно-ориентированное программирование."
    udmurtov "Точнее вы будете пытаться нормально понять базу, которую я буду вам выдавать."
    udmurtov "Не волнуйтесь, говорить буду медленно, чтобы ваши неокрепшие мозги не начали закипать."
    udmurtov "Мы будем рассматривать принципы ООП в языке C++."
    udmurtov "В первую очередь вы должны узнать об основе основ ООП – объектах и классах."
    udmurtov "Классы являются основой С++. Для того чтобы определить объект, нужно сначала определить его форму с помощью ключевого слова class."
    udmurtov "Чтобы было понятнее, объект находится в таком же отношении к своему классу, в каком переменная находится по отношению к своему типу."
    udmurtov "Если говорить максимально просто, объект является экземпляром класса, так же, как и автомобиль — колесного средства передвижения. "
    udmurtov "Я сам учился довольно давно, несколько лет уже отработал в разных компаниях."
    udmurtov "По сути, уже почти ничего не помню из своей институтской программы, но когда применяешь свои навыки на практике, всë запоминается и нарабатывается намного лучше, чем от простых рассказов."
    udmurtov "Но это никак не отменяет того факта, что база закладывается именно сейчас, а без неë вас и не возьмут никуда."
    udmurtov "Класс может содержать приватную часть (private ) и общую (public). Приватные элементы не могут использоваться никакими функциями, не являющимися членами класса. "
    udmurtov "Также можно определить и приватные функции, которые могут вызываться только другими функциями — членами класса. Это — один из путей реализации принципа инкапсуляции. "
    udmurtov "По умолчанию все элементы класса приватные, поэтому ключевое слово private можно опустить. Поле класса — это данные, содержащиеся внутри класса. Методы класса — это функции, входящие в состав класса."
    udmurtov "Раз самые основные понятия прояснили то можем дальше двигаться?"
    udmurtov "Кстати, как я всегда говорил, чтобы быть солидным программистом вы обязаны соблюдать принципы SOLID."
    udmurtov "Хахахаха каждый раз смешно."
    udmurtov "А вы как я вижу не особо смеяться настроены?"
    udmurtov "Тогда возникает сомнения на счëт того, поняли ли вы в чëм смысл этой шутки?"
    udmurtov "Вы вообще знаете, что такое SOLID?"
    udmurtov "Ладно, по глазам вижу, что некоторые понимают, о чëм идëт речь."

    menu:
        udmurtov "А вот ты знаешь, что такое SOLID?"
        "Простите, впервые слышу.":
            udmurtov "Дааа, ладно, я понимаю, что вы как раз и пришли учиться, но серьëзно?"
            udmurtov "Тогда навострите уши и постарайтесь запомнить, без этого нет смысла даже думать об ООП."
            call solidLecture
        "Раньше слышал, но не смогу нормально объяснить.":
            udmurtov "Что, слышал звон, да не знает где он, так в таких ситуациях говорят обычно?"
            udmurtov "Я, конечно, понимаю, что у молодëжи клиповое мышление и вы больше пары дней не храните информацию в голове, но не запоминать то, что связано непосредственно с вашей будущей профессией, даже звучит безответственно."
            udmurtov "Ладно, думаю тогда только и остаëтся, что рассказать вам ещë раз и надеяться, что хоть в этот раз что-то отложится."
            call solidLecture
        "Да, конечно, я же не зря на IT специальность решил пойти.":
            udmurtov "Тогда расскажи мне и своим товарищам по группе, о чëм же речь идëт?"
            call solidTest
            if solid_test_score < 3:
                udmurtov "Ну откуда столько уверенности?"
                udmurtov "Вы не назвали правильно и половины, а пытались эксперта строить, слушайте меня с остальными."
                call solidLecture
            elif solid_test_score >= 3 and solid_test_score < 5:
                udmurtov "Есть некоторые ошибки, но по большей части верно."
                udmurtov "Ладно, тогда я расскажу всем, а вы тоже запомните, особенно места, в которых ошиблись."
                call solidLecture
            else:
                udmurtov "Надо же, всë верно, может вы даже вместо меня сможете ваших товарищей подтянуть."
                udmurtov "Особенно тех, кто впервые об этом услышал только сейчас."


    udmurtov "Тааак, думаю, стоит подводить к концу наше вводное занятие."
    udmurtov "Думаю, вы уже поняли, что для любого крупного проекта необходимо чëткое понимание и соблюдение принципов ООП."
    udmurtov "Для простой проверки, ответьте на парочку моих вопросов."
    
    $oop_test_score = 0
    menu:
        udmurtov "Что такое поле класса?"
        "Ячейки, на которые распределëн класс":
            pass
        "Данные, содержащиеся внутри класса":
            $oop_test_score += 1
        "Данные, содержащиеся вне класса":
            pass
    
    menu:
        udmurtov "Что такое методы класса?"
        "Функции, входящие в состав класса":
            $oop_test_score += 1
        "Средства создания класса":
            pass
        "Способы восстановления класса":
            pass

    menu:
        udmurtov "Какие элементы не могут использоваться никакими функциями, не являющимися членами класса?"
        "Общие":
            pass
        "Все":
            pass
        "Приватные":
            $oop_test_score += 1
    
    if oop_test_score <= 1:
        udmurtov "Фуух, да уж, даже половины вспомнить не можете, хотя услышали несколько минут назад."
        udmurtov "Теперь я однозначно переживаю о подрастающем поколении, которое нас заменять будет."
        udmurtov "Катитесь-ка отсюда и попробуйте дома подучиться."
    elif oop_test_score == 2:
        udmurtov "Ооо запомнили большую часть из рассказанного."
        udmurtov "Хотя всë равно странно, что уже успели что-то забыть."
        udmurtov "Ладно, можете идти, не забудьте всë повторить, чтобы точно улеглось."
    else:
        udmurtov "Ничего себе, реально остались те, у кого память не как у рыбки. Так и на сушу выйти можно.."
        udmurtov "Вы молодец, думаю если продолжите в том же духе, то проблем у нас не возникнет."
        udmurtov "Тогда, на этом и попрощаемся, до скорых встречь."

        stop music fadeout 3.0
    return

        


label solidLecture:
    udmurtov "На самом деле всë очень просто."
    udmurtov "В SOLID: S - Принцип единственной ответственности (Single Responsibility Principle, SRP)"
    udmurtov "O - Принцип открытости/закрытости (Open/Closed Principle, OCP)"
    udmurtov "L - Принцип подстановки Лисков (Liskov Substitution Principle, LSP)"
    udmurtov "I - Принцип разделения интерфейса (Interface Segregation Principle, ISP)"
    udmurtov "D - Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)"
    return


label solidTest:
    $solid_test_score = 0
    menu:
        "В SOLID, S это:"
        "S - Принцип упрощëнной ответственности (Simplified Responsibility Principle, SRP)":
            pass
        "S - Принцип единственной ответственности (Single Responsibility Principle, SRP)":
            $solid_test_score += 1

    menu:
        "В SOLID, O это:"
        "O - Принцип открытости/закрытости (Open/Closed Principle, OCP)":
            $solid_test_score += 1
        "O - Принцип частого повторения (Often Closed Repeat, OCR)":
            pass
    
    menu:
        "В SOLID, L это:"
        "L - Принцип подстановки Лисков (Liskov Substitution Principle, LSP)":
            $solid_test_score += 1
        "L - Принцип подстановки списков (Lists Substitution Principle, LSP)":
            pass

    menu:
        "В SOLID, I это:"
        "I - Принцип объединения интерфейса (Interface Associations Principle, IAP)":
            pass
        "I - Принцип разделения интерфейса (Interface Segregation Principle, ISP)":
            $solid_test_score += 1

    menu:
        "В SOLID, D это:"
        "D - Принцип интерпретации зависимостей (Dependency Interpretations Principle, DIP)":
            pass
        "D - Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)":
            $solid_test_score += 1
    
    return