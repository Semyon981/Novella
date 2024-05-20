define african = Character('Африканец', color="#632c00")
define englishman = Character('Англичанин', color="#00ff80")
define american = Character('Американец', color="#1100ff")

define canadian = Character('Канадец', color="#fa0000")

define australian = Character('Австралиец', color="#f6fa00")

define indian  = Character('Индиец', color="#00fa15")

define audio.menujet = "music/menujet.mp3"


transform base:
    xanchor 0.5

transform pos_left:
    base
    linear 0.1 xpos 0.2

transform pos_left_init:
    base
    xpos 0.2

transform pos_center:
    base
    linear 0.1 xpos 0.5

transform pos_center_init:
    base
    xpos 0.5

transform pos_right:
    base
    linear 0.1 xpos 0.8

transform pos_right_init:
    base
    xpos 0.8

transform speak:
    base
    linear 0.1 ypos -0.05 zoom 1.05

transform speak_init:
    base
    ypos -0.05 
    zoom 1.05

transform normal:
    base
    linear 0.1 ypos 0.0 zoom 1.0

transform normal_init:
    base
    ypos 0 
    zoom 1.0



label startChapterEnglish:

    stop music fadeout 1.0
    scene black with fade

    "{i}Начиная с этого момента, в ход идут специфические языковые формы, которые могут вызвать приступы острой лингвистической боли, кровоточивость глазных яблок и открытый перелом языка."

    play music street fadein 2.0

    scene university with fade

    "В этот погожий день ничего не предвещало беды..."
    "Но коварный враг поджидал студентов..."
    "Языком своим заморским, да латиницей клятой решила учащимся зачётки испортить кафедра иностранных языков!."
    "Да собралась рать народная оценки свои силою богатырской оборонять, да в кабинете под номером -данные удалены- сочинения свои защищать."
    "И беды бы не было, да рать народная из дюжины групп собрана была, да в субботу перед сессией последнюю…"
    "Поговаривают, что сдавать иноземные языки раньше дня зимнего солнцестояния - дурная примета."
    "И очередь на сдачу раскинулась от лесов Тимерязевских до морей северных."
    "Да стояла та очередь с первых утренних лучей до заката кроваво красного, беду предвещающего. И конца и края не было видно ей."
    "Хитёр был план подлецов иноземных. Задумали они измором победить."
    "Провиант был на исходе. В шаббат буфеты все закрыли."
    "Одно отделяло в тот день Политех от голодного бунта…"
    "Нерушимая вера в главный козырь доблестных витязей - студента угандийского, в совершенстве языками владеющего."


    show african with dissolve
    
    african "Не волнуйтесь, братья мои, не будет нечисть поганая на святой земле православной бесчинства учинять."
    african "Задумали они нас хитростью одолеть, да мы хитрее. Клин клином вышибают!"
    african "Не знают ироды ни братства ни стойкости. Нет единства в их рядах."
    african "Рассорим подлецов, тогда духу им не хватит продолжать экзекуцию."

    stop music fadeout 1.0

    "Перекрестившись и испив воды “Пресвятого источника”, отправился угандийский богатырь в самое логово бесов."


    play music menujet fadein 2.0
    scene english_lab with fade

    show english_prepod at pos_center_init, speak_init with dissolve
    englishman "Well, i am listening to you." # 1 ---------------------
    show english_prepod at pos_right, normal
    show african at pos_left, speak

    african "Yes, sir. Кстати, а вы видели какая там очередь?" # 2 ---------------------
    show english_prepod at pos_right, speak
    show african at normal
    englishman "Yes, of course, this queue is incredibly huge, but what can I do?"
    show english_prepod at pos_center, normal
    show american:
        xpos 1.14
    show american at speak_init, pos_right zorder 2
    american "Вот дид ю сэй? ‘Кьюю’? Оф корз зыс ыс ‘Лайн’!" # 3 ---------------------
    show english_prepod at speak
    show american at normal, pos_right
    englishman "Yankee. go home!"

    show english_prepod at normal zorder 1
    show african:
        linear 0.1 xpos -0.14
    show indian at speak_init, pos_left

    indian "Chello gaij. Time kya hua hai?" # 4 ---------------------
    show indian at normal, pos_left
    show english_prepod at speak, pos_center
    englishman "???"
    show english_prepod at normal, pos_center
    show american at speak, pos_right
    american "Хи аскс зе тайм, росбиф!"
    show english_prepod at speak, pos_center
    show american at normal, pos_right
    englishman "It’ quarter to eight, my indian friend."
    show english_prepod at normal, pos_center
    show american at speak, pos_right
    american "Индианс хэв ред скин! Хи ис хинду! Энд итс найнтин фотифайв!"
    
    show australian:
        xanchor 0.5
        xpos 0.1
    with MoveTransition(0.1,enter=offscreenleft)
    australian ".gninrom eht ni kcolc'o eerht tsomla s'ti syas hctaw yM" # 5 ---------------------
    hide australian with MoveTransition(0.1,leave=offscreenleft)
    show american:
        linear 0.1 xpos 1.18
    show canadian:
        xpos 1.14
    show canadian at speak, pos_right
    canadian "im so sry, not gotcha this." # 6 ---------------------
    show indian at speak, pos_left
    show canadian at normal, pos_right
    indian "jhagda N karein, bhaee!"
    show indian at normal, pos_left
    show canadian at speak, pos_right
    canadian "U2, sry."
    show english_prepod at speak, pos_center
    show canadian at normal, pos_right
    englishman "Are you experiencing such difficult times in Canada that there is a shortage of letters?"
    show english_prepod at normal, pos_center
    show indian at speak, pos_left
    indian "Hindoo aap sabhi se behatr jante hain ki \"shortage\" shabd ka matlab kya hai!"
    show indian at normal, pos_left
    show australian:
        xanchor 0.5
        xpos 0.1
    with MoveTransition(0.1,enter=offscreenleft)
    australian "¿¿¿"
    hide australian with MoveTransition(0.1,leave=offscreenleft)
    show canadian at speak, pos_right
    canadian "Pardon?"
    show canadian:
        linear 0.1 xpos 1.18
    show african:
        xpos 1.14
    show african at speak, pos_right
    african" Раз не можем мы друг-друга понять, давайте же на местном наречии молвить."
    show african at normal, pos_right
    show english_prepod at speak, pos_center
    englishman "Правильно! Давайте без ваших заморских диалектов. Переходим на нормальный европейский язык."
    show english_prepod at normal, pos_center
    show indian at speak, pos_left
    indian "Кто бы про “заморских” говорил, я тут единственный с этого материка, а вас сюда по воле Стхана Девата занесло."
    show english_prepod at speak, pos_center
    show indian at normal, pos_left
    englishman "Вообще-то тут важнее близость относительно культуры, а не геолакации, что как раз отличает меня или хотя б того высокомерного янки. Поэтому мне проще будет общаться с этими юными умами."
    show american:
        xpos 1.18
    show american at speak_init, pos_right
    show african:
        linear 0.1 xpos 1.18
    show english_prepod at normal, pos_center
    american "Хахаха, если о культуре говорить, то нашу давно с фильмами впитали, так что я им поинтереснее буду."
    show american at normal, pos_right
    show english_prepod at speak, pos_center
    englishman "Да что мы тут выясняем? Важно только то, кто лучше научит студентов английскому, я прав?"
    show english_prepod at normal, pos_center
    show australian:
        xanchor 0.5
        xpos 0.1
    with MoveTransition(0.1,enter=offscreenleft)
    australian "!варП"
    hide australian with MoveTransition(0.1,leave=offscreenleft)
    show english_prepod at speak, pos_center
    englishman "Тогда следующий вопрос, кому как не чистокровному englishmanУ, с детства жившему в восточном Бирмингеме, учить других АНГЛИЙСКОМУ языку?"
    show american at speak, pos_right
    show english_prepod at normal, pos_center
    american "Вообще-то американский английский распространëн сейчас больше, чем британский."
    show american at normal, pos_right
    show english_prepod at speak, pos_center
    englishman "Вы, янки, заменили некоторые слова, забросили произношение с фонетикой и назвали это “американским английским”. Опять на лицо лишний пафос, который вы пытаетесь выпячивать!"
    show american at speak, pos_right
    show english_prepod at normal, pos_center
    american "Мне про пафос будет говорить человек, который разоделся как джентльмен из 19 века?"
    show canadian:
        xpos 1.14

    show canadian zorder 2:
        ypos 0
        xanchor 0.5
        xpos 0.85
    with MoveTransition(0.2,enter=offscreenright)

    show american at normal, pos_right
    canadian "Простите, но что-то вы многовато спорите, давайте лучше пойдём Баннок с беконом схомячим."
    hide canadian with MoveTransition(0.2,leave=offscreenright)
    show indian at speak, pos_left
    indian "Давайте лучше насытимся горячим и сочным Карри."
    show indian at normal, pos_left
    show australian:
        xanchor 0.5
        xpos 0.1
    with MoveTransition(0.1,enter=offscreenleft)
    australian ".юагалдерп ен воноипрокс хынераЖ"
    hide australian with MoveTransition(0.1,leave=offscreenleft)
    show american at speak, pos_right
    american "Хахаха в споре о еде нас точно никто не уделает, наши рестораны давно по всему миру."
    
    show african:
        xpos 1.14

    show african zorder 3:
        ypos 0
        xanchor 0.5
        xpos 0.85
    with MoveTransition(0.2,enter=offscreenright)
    show american at normal, pos_right

    african "Кстати, а вы знали что около Петровско-Разумовской “Теремъ” открылся?"
    hide african with MoveTransition(0.2,leave=offscreenright)
    show australian:
        xanchor 0.5
        xpos 0.1
    with MoveTransition(0.1,enter=offscreenleft)
    australian ".тюадапвос ысукв ишан тут ,юагалоП !О"
    hide australian with MoveTransition(0.1,leave=offscreenleft)
    show american at speak, pos_right
    american "Внатуре! Может сгоняем?"
    show american at normal, pos_right
    show english_prepod at speak, pos_center
    englishman "В кой-то веке вынужден с вами согласиться!"
    show indian at speak, pos_left
    show english_prepod at normal, pos_center
    indian "Тогда идём?"
    show canadian:
        xpos 1.14

    show canadian zorder 4:
        ypos 0
        xanchor 0.5
        xpos 0.5
    with MoveTransition(0.2,enter=offscreenright)
    canadian "Го!"
    show australian zorder 5:
        xanchor 0.5
        xpos 0.8
    with MoveTransition(0.1,enter=offscreenright)
    australian ".ко"
    hide indian with MoveTransition(0.2,leave=offscreenleft)
    hide canadian with MoveTransition(0.2,leave=offscreenleft)
    hide australian with MoveTransition(0.2,leave=offscreenleft)
    show african:
        xanchor 0.5
        xpos 0.2
    with MoveTransition(0.2,enter=offscreenleft)
    african "А как же зачёт?"
    show american at speak, pos_right
    american "Damn it…"
    show american at normal, pos_right
    show english_prepod at speak, pos_center
    englishman "Да бес с ним! Проставь им всем оценки и пошли ужинать."
    hide african with MoveTransition(0.2,leave=offscreenleft)
    hide english_prepod with MoveTransition(0.2,leave=offscreenleft)
    hide american with MoveTransition(0.2,leave=offscreenleft)

    "Так отечественная пищевая индустрия и дружба с африканским континентом уберегла наше студенчество от басурман проклятых, да от зачёта непосильного"

