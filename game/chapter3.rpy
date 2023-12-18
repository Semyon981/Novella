
define yasherov = Character('Ящеров', color="#00780e")
define student = Character('Неизвестный студент', color="#00baaa")
define audio.alarm = "music/alarm.wav"
define audio.yascherov = "music/yascherov.wav"


$infobez = False

$infobez = False

label startChapter3:
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА III “ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ”"

    play music alarm
    "{cps=45}{i}*звон будильника"

    scene room
    with fade

    menu: #поменял
<<<<<<< Updated upstream
        "Отложить на 5 минут?"
        "Да":
            "Как буд-то это вообще когда-то было хорошим решением..."
            call prospal from _call_prospal
        "Нет":
            "На первую пару опаздывать слишком опасно. "
=======
        "{cps=45}Отложить на 5 минут?"
        "Да":
            "{cps=45}{i}Как буд-то это вообще когда-то было хорошим решением..."
            stop music fadeout 1.0
            call prospal from _call_prospal
        "Нет":
            stop music fadeout 1.0
            "{cps=45}{i}На первую пару опаздывать слишком опасно. "
>>>>>>> Stashed changes
            scene auditoria_yascherov
            with fade
            show yasherov
            play music yascherov


    yasherov "{cps=45}Я раньше работал в другом институте, ещë во времена аспирантуры."
    yasherov "{cps=45}И был у нас один студент, который хорошо общался с преподавателями и многие вопросы решал 'на хороших отношениях'"
    yasherov "{cps=45}В те времена, интернет был только по трафику и его количество на объект было ограничено."
    yasherov "{cps=45}И вот этот студент, получив доступ к управлению сетью вуза, стал перепродавать часть вузовского трафика сторонним лицам." 
    yasherov "{cps=45}По итогу он украл у вуза таким способом много денег и самого трафика."
    yasherov "{cps=45}Дело замяли и завершили тем, что убедили его по собственному забрать документы из института, чтобы не создавать шума."
    yasherov "{cps=45}Потому что в ином случае пострадали и преподаватели, которые предоставили ему доступ к ресурсам вуза и никак не могли бы доказать свою непричастность."
    yasherov "{cps=45}Этот кейс хорошо иллюстрирует то, насколько внимательно нужно относиться к тому, кому предоставляете доступ к ресурсам предприятия."
    yasherov "{cps=45}Именно об этом и будет курс, в первую очередь не о программной защите, а о средствах корпоративной защиты доступа к ресурсам, финансам и данным компании или предприятия."
    yasherov "{cps=45}Вы должны понять ограничения при найме сотрудников, расположении помещений и выборе оборудования и подрядчиков, а также следить за своими сотрудниками во избежание корпоративного шпионажа."
    yasherov "{cps=45}У меня много статей на тему информационной безопасности, и книга, которую вы можете купить в специальных интернет магазинах с научной литературой в бумажном или электронном варианте."
    yasherov "{cps=45}А пока глянь те ка историю, которая идеально вписывается в нашу тему."

    hide yasherov

    hide yasherov

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    show comics11 with dissolve
    
    ""
    hide comics11
    show comics21 with dissolve
   
    ""
    hide comics21
    show comics31 with dissolve
    
    ""
    hide comics31
    show comics41 with dissolve
   
    ""
    hide comics41
    show comics51 with dissolve
    
    ""
    hide comics51
    show comics61 with dissolve
    
    ""
    hide comics61
    show comics71 with dissolve
    
    ""
    hide comics71
    show comics81 with dissolve
    
    ""
    hide comics81
<<<<<<< Updated upstream


    show yasherov with dissolve
=======
>>>>>>> Stashed changes


    show yasherov with dissolve

    yasherov "{cps=45}На сегодня закончим на этом. Уверен: вы и так всë поняли по моим примерам, проблем у ответственного студента возникнуть не должно."
    stop music fadeout 1.0

    return

label prospal:
    scene black
    with fade
    "{cps=15}{i}..."
    scene room
    with fade

<<<<<<< Updated upstream
    "Остаётся надеяться только на милость преподавателя в отношении опоздавших."
=======
    "{cps=45}{i}Остаётся надеяться только на милость преподавателя в отношении опоздавших."
>>>>>>> Stashed changes

    scene auditoria_yascherov
    play music yascherov
    with fade

    show yasherov
     
    #поменял
<<<<<<< Updated upstream
    yasherov "Добрый день, можете объяснить, прочему вы опаздываете на первое занятие??"
=======
    yasherov "{cps=45}Добрый день, можете объяснить, почему вы опаздываете на первое занятие??"
>>>>>>> Stashed changes
    menu:
        "Искренне прошу прощения, разобраться в сложной архитектуре этого здания и найти нужную аудиторию оказалось непростой задачей.":
            pass
        "Живот прихватило.":
            pass
        "Здание - настоящий лабиринт! А моё имя, вроде, в кубок огня не попадало.":
            pass
        "Надо было перевести бабушку через дорогу.":
            pass
<<<<<<< Updated upstream
    yasherov "Ладно, проходи."
=======
    yasherov "{cps=45}Ладно, проходи."
>>>>>>> Stashed changes

    return
