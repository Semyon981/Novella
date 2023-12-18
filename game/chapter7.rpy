

define poderevyanov = Character('Подеревянов', color="#ffa601")

define student = Character('Неизвестный студент', color="#00baaa")

define audio.japan = "music/japan.mp3"
define audio.jazz = "music/jazz.mp3"

define rnd1 = renpy.random.randint(-10, 10)
define rnd2 = renpy.random.randint(-10, 10)

define audio.japan = "music/japan.mp3"

define rnd = renpy.random.randint(-10, 10)

label startChapter7:
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА VII ”ПРОЕКТНАЯ ДЕЯТЕЛЬНОСТЬ”"    

    stop music fadeout 1.0
    play music jazz
    scene computer
    with fade

    "{cps=45}{i}На этот раз, приключения начинаются задолго до первого занятия по предмету."
    "{cps=45}{i}Проектная деятельность. Священная корова всея политеха."
    "{cps=45}{i}Самое главное на проектной деятельности - не прогадать с выбором проекта."
    "{cps=45}{i}И что не менее важно - успеть заползти на понравившийся проект, пока есть свободные места."
    "{cps=45}{i}И желательно друзей прихватить."
    "{cps=45}{i}Чтобы записаться на некоторые, проекты нужно пройти собеседование. Но это редкость."
    "{cps=45}{i}В любом случае сегодня последний день записи, расспрашивать о проектах некогда, надо уже что-то выбирать, иначе это сделает рандомайзер."
    "{cps=45}{i}А из доброй сотни вариантов уже осталось всего несколько."
    "{cps=45}{i}Проект “Солнечная галера”. Судя по описанию, будем делать лодку, использующую для передвижения силу солнышка нашего. И разумеется гоняться с другими изобретателями."
    "{cps=45}{i}Проект “Веломобиль от политеха”. Похоже нужно будет сделать веломобиль."
    "{cps=45}{i}Проект “Мониторинг состояния газовых труб”. Кажется надо будет спроектировать аппаратную и программную часть системы мониторинга состояния газовых труб."
    "{cps=45}{i}Проект ”Mospolyhelper”. Тут всё понятно. Большинство студентов политеха, имеющих в своём распоряжении android-смартфон, пользуются этим приложением как заменой личного кабинета студента. Приложить руку к данному творению - великая честь."
    "{cps=45}{i}”Группа проектов из сферы геймдева”. На направлении ИСиТ есть профиль, связанный с геймдевом. Так что почему бы и не попробовать поделать видеоигры."
    "{cps=45}{i}”Стратегический проект: предпрофессиональная образовательная среда” - Непонятно, что значит “стратегический”, но выглядит очень важно. Из описания ничего не понятно."
    "{cps=45}{i}Choose your fighter!"
    "{cps=45}{i}В смысле нужно наконец выбрать проект."

    menu:
        "Солнечная галера":
            call Solar from _call_Solar

        "Веломобиль от политеха":
            call Velomobil from _call_Velomobil

        "Мониторинг состояния газовых труб":
            call GasPipes from _call_GasPipes

        "Mospolyhelper":
            call Mospolyhelper from _call_Mospolyhelper

        "Группа проектов из сферы геймдева":
            call GameDev from _call_GameDev

        "Стратегический проект: предпрофессиональная образовательная среда":
            call PredProf from _call_PredProf

            
    return


label Solar:
    scene back_pd_regata
    "{cps=45}{i}Ну на самом деле айтишникам надо привыкать работать на галере."
    "{cps=45}{i}Несмотря на совершенно рабские условия работы на импровизированной верфи, результаты восхищают."
    "{cps=45}{i}За пару месяцев на воду был спущен целый флот."
    "{cps=45}{i}Все оппоненты были биты в пух и прах во всех соревнованиях."
    show petr1 with dissolve
    "{cps=45}{i}Пётр:" "Горжусь!"


    return

label Velomobil:
    scene back_pd_velomobile with fade
    "{cps=45}{i}Было категорически непонятно, каким образом в данном проекте айтишнику  можно применить свои знания."
    "{cps=45}{i}Поэтому, пока ребята с транспортного факультета что-то там чертили и изготавливали, одна заблудшая душа подавала гайки и шуруповёрт."
    "{cps=45}{i}Всё бы ничего, но после окончания производства этой тарантайки, команда разругалась, выясняя кому в пользование достанется сия карета."

    return

label GasPipes:
    "{cps=45}{i}Невозможно было пройти мимо актуальности данного проекта. Ведь нефтегазовая отрасль приносит немало золотишка в карман, а значит нужно максимально глубоко погрузиться в этот бизнес."
    "{cps=45}{i}Навыки программиста пригодились создании программной части системы. Если точнее - в подсистеме распределения электропитания датчиков."
    "{cps=45}{i}На самом деле работка показалась чересчур сложной и нудной."
    "{cps=45}{i}Ну хотя бы проект был успешно сдан в срок."
    "{cps=45}{i}Тоску развеяла лента новостей. Твердили о взрыве на международном газопроводе"
    "{cps=45}{i}“Северное течение”. Огромный скандал, перекрёстные обвинения, миллиардные убытки."

    "{cps=45}{i}Совещание с командой выявило баг в той самой подсистеме распределения электропитания. Он с большой вероятностью приводил к сгоранию датчиков и взрыву внутри трубы."
    "{cps=45}{i}Было решено промолчать об этой проблеме. А у руководителя проекта явно прибавилось седых волос."
    "{cps=45}{i}Как говорит японская мудрость: Путь самурая - дебага путь."

    

    return

label Mospolyhelper:
    "{cps=45}{i}Проект, откровенно говоря, сложный. Над ним уже несколько команд пару лет тужатся."
    "{cps=45}{i}В этот раз за половину семестра удалось в десятый раз переворотить пользовательский интерфейс, добавить журнал посещений по физ-ре и починить электронную зачётную книжку."
    "{cps=45}{i}Настоящая засада ждала на промежуточной защите проекта. Члены комиссии явно ожидали более значимых успехов, о чём представитель комиссии по фамилии Подервянов и намекнул."
    
    scene back_pd_samurai with fade
    show samurai with dissolve
    play music japan

    poderevyanov "{cps=45}Медленно ползёт улитка на гору Фудзи. Ничего не обещая. Дао её совершенно. "
    poderevyanov "{cps=45}Вы же, товарищи, про успехи проекта только говорите."
    poderevyanov "{cps=45}Ваша некомпетентность в данном вопросе всем очевидна. Восемь недель вы кормите нас обещаниями!"
    poderevyanov "{cps=45}И я говорю вам - хватит!"
    poderevyanov "{cps=45}Или покажите завершенный проект, или все пойдут на пересдачу!"
    "{cps=45}{i}Сильная речь дала огромный заряд мотивации."
    "{cps=45}{i}Mospolyhelper был допилен в считанные недели."
    "{cps=45}{i}Хотя сколько же кофеина было затрачено."

    stop music fadeout 1.0

    return

label GameDev:
   
    scene black with fade
    "{cps=45}{i}Тетрис, Сталкер, Киберпанк…"
    "{cps=45}{i}Шедевры славянского геймдева!"
    scene back_pd_gamedev with fade
    "{cps=45}{i}Но в мире этих титанов восходит новая звезда “Погибель ящера”!"
    "{cps=45}{i}Начинать производство шедевра нужно с написания сценария."
    
    $res = 0
    menu:
        "{cps=45}{i}Для начала определиться с выбором имени ГГ."
        "Святослав":
            pass
        "Доброжир":
            $res += 1
        "Богдана":
            $res += 2
    
    menu:
        "{cps=45}{i}Нужно придумать для ГГ конечную цель."
        "Истребление ящеров":
            pass
        "Мир во всём мире":
            $res += 1
        "Всемирное равенство":
            $res += 2
    
    menu:
        "{cps=45}{i}История должна содержать главного антагониста."
        "Самый сильный ящер":
            pass
        "Злой волшебник":
            $res += 1
        "Ящерица-цундере":
            $res += 2

    menu:
        "{cps=45}{i}Дальше по списку оружие, которое будет использовать ГГ."
        "Топор":
            pass
        "Двуручный меч":
            $res += 1
        "Протез с крюком":
            $res += 2

    menu:
        "{cps=45}{i}Ну и куда же без доспеха…"
        "Кольчужный панцирь":
            pass
        "Лёгкая бригантина":
            $res += 1
        "Розовый кожаный жилет":
            $res += 2

    menu:
        "{cps=45}{i}У ГГ должен быть дом"
        "Острог":
            pass
        "Каменный замоrк":
            $res += 1
        "Домик на дереве":
            $res += 2

    menu:
        "{cps=45}{i}Надо выбрать божество, которому поклоняется ГГ."
        "Перун":
            pass
        "Зевс":
            $res += 1
        "Не будет божества":
            $res += 2

    menu:
        "{cps=45}{i}Напоследок нужно решить вопрос монетизации."
        "Платно":
            pass
        "Условно бесплатно":
            $res += 1
        "Платно и с микротранзакциями":
            $res += 2

    $p = 90 - res * 5 + rnd1
    $k = 10 + res * 5 + rnd2


    "{cps=45}{i}Вот он знаменательный день релиза! Вся команда очень взволнована."
    "{cps=45}{i}И вот шедевр уже покоряет просторы steam"
    "{cps=45}{i}Через некоторое время можно узнать реакцию игроков"
    "{cps=45}{i}А сделать это можно на портале Metacritic"
    "{cps=45}{i}Ну честно говоря оценки средненькие. Оценка пользователей: [p]; Оценка критиков: [k]"
    "{cps=45}{i}Впрочем этого вполне достаточно чтобы проект засчитали"


    return

label PredProf:
    "{cps=45}{i}Не проект, а загадка"
    "{cps=45}{i}Почему “стратегический”?"
    "{cps=45}{i}Почему “среда”, а не “пятница”?”"
    "{cps=45}{i}Непонятно…"
    "{cps=45}{i}И вообще именно понедельник является днём проектной деятельности."
    "{cps=45}{i}Как выяснилось на первом собрании, суть проекта в продвижении политеха в довузовских учреждениях и в отлове талантливой молодёжи."
    "{cps=45}{i}В качестве основного занятия предлагаются поездки в школы и выступления перед учениками, а также организация мастер-классов."
    

    menu:
        "{cps=45}{i}Но можно в качестве альтернативы предложить какую-нибудь отсебятину."
        "Испытать удачу в общении со школьниками.":
            pass
        "Делать визуальную новеллу про направление ИСиТ.":
            "{cps=45}{i}Идея конечно хорошая, только эту новеллу уже сделали."
            "{cps=45}{i}Придётся ходить по школам."
    

    scene back_pd_school_outside with dissolve

    "{cps=45}{i}Здравствуй школа!"
    "{cps=45}{i}Как вообще айтишнику могли поставить задачу где-то выступать?"
    "{cps=45}{i}Как вообще разговаривать с детьми?"
    "{cps=45}{i}Что если класс будет представлять из себя стаю велоцирапторов в человеческом обличии?"
    "{cps=45}{i}Нельзя допускать такие мысли. Дети уже ждут."


    $respect = 0
    $promotion = 0

    menu:
        "Зайти со стуком":
            $respect += -3
            $promotion += 3
            scene back_pd_school_inside with dissolve
            "{cps=45}{i}Дети, похоже, совершенно не обратили внимание на появление ещё одного гуманоида в помещении."
            "{cps=45}{i}Нужно привлечь их внимание."
            call PredProfStuk from _call_PredProfStuk

        "Зайти, пнув дверь ногой":
            "{cps=45}{i}Ну такой жест точно привлёк внимание."
            scene back_pd_school_inside with dissolve
            call PredProfNoStuk from _call_PredProfNoStuk
            

    
    "{cps=45}{i}Какими-то чудесными и нечеловеческими усилиями удалось закрыть этот предмет."
    "{cps=45}{i}А впереди, словно туча, надвигается сессия."
    hide poderevyanov
    with dissolve
    return

label PredProfStuk:
    menu:
        "Минуточку внимания, пожалуйста.":
            $respect += -3
            $promotion += 1
            "{cps=45}{i}Было наивно полагать, что призыв хоть кто-то услышит."

            menu:
                "Расплакаться и убежать":
                    $respect += -100
                    $promotion += -100
                    call PredProfProval from _call_PredProfProval
                   
                "А ну ка заткнулись все!!":
                    $respect += -3
                    $promotion += 1
                    "{cps=45}{i}Класс быстро пришёл в чувство."
                    call PredProfDelo from _call_PredProfDelo
                "Если слушать не будете, на обед не успеете":
                    $respect += -3
                    $promotion += 1
                    "{cps=45}{i}Класс быстро пришёл в чувство."
                    call PredProfDelo from _call_PredProfDelo_1

        "Тишина в классе!!1":
            "{cps=45}{i}Сработало, остальные гуманоиды притихли и смотрят в правильном направлении."
            call PredProfDelo from _call_PredProfDelo_2


    return


label PredProfProval:
    $respect += 3
    $promotion += -7
    scene computer with fade
    "{cps=45}{i}Полный провал"
    "{cps=45}{i}Хотя и этого достаточно, чтобы зачёт кое-как поставили."
    return


label PredProfNoStuk:
    menu:
        "Вежливо представиться":
            $respect += 5
            $promotion += 5
        "Запомните моё имя, твари...":
            $respect += -5
            $promotion += -10
        "Салют, пацаны и девчата!":
            $respect += 5
            $promotion += 5

    
    call PredProfDelo from _call_PredProfDelo_3

    return


label PredProfDelo:
    "{cps=45}{i}Надо переходить к делу."

    menu:
        "Я учусь в московском политехе, сегодня расскажу вам о нём":
            $respect += -2
            $promotion += 5
        "У меня для вас презентация":
            $respect += -3
            $promotion += -1

    "{cps=45}{i}По середине выступления от велоцираптора на задней парте летит ластик."

    menu:
        "Попросить прекратить":
            $respect += -5
            $promotion += 1
        "Ловко отбить в сторону":
            $respect += 5
            $promotion += 3
        "Ловко отбить обратно":
            $respect += 5
            $promotion += -5

    "{cps=45}{i}После инцидента с ластиком, возникла другая проблема: люди массово залипают в телефоны."

    menu:
        "Занимательный факт: держание телефона в руках значительно повышает риск этого телефона лишиться.":
            $respect += 2
            $promotion += -4
        "Правильно, подписываемся на наш телеграмм.":
            $respect += 5
            $promotion += 5
        "Ребят, ну хорош в телефоны пялиться!":
            $respect += -3
            $promotion += 1

    "{cps=45}{i}Выступление подходит к концу."
    "{cps=45}{i}По ощущениям оно продолжалось вечность"
    scene computer
    with fade

    if respect <= 0 and promotion > 0:
        "{cps=45}{i}Результат выступления неутешительный: Не удалось удержать внимание детей."
        "{cps=45}{i}Ну за саму попытку как-нибудь зачёт поставят."
    elif respect > 0 and promotion <= 0:
        "{cps=45}{i}Результат выступления неутешительный. Теперь в этой школе политех считают за обителей зла."
        "{cps=45}{i}Ну за саму попытку как-нибудь зачёт поставят"
    elif respect <= 0 and promotion <= 0:
        "{cps=45}{i}Результат выступления неутешительный. Мероприятие полностью провалилось. Полностью."
        "{cps=45}{i}Ну за саму попытку как-нибудь зачёт поставят."
    elif respect > 0 and promotion > 0:
        "{cps=45}{i}Результат отличный! Мероприятие прошло успешно!"
        "{cps=45}{i}Зачёт точно будет получен!"

    return