# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg_room1 = "images/room1.jpg"
image keys = "images/key.png"
image computer = "images/Laptop.png"
image receipt = "images/receipt.png"
image cookie = "images/cookie.png"
image diary = "images/diary_open.png"
image diary_closed = "images/diary_closed.png"
image book4 = "images/book4.png"
image lock = "images/lock.png"
image victory_img = "images/victory.png"

init python:
    def label_callback(name, abnormal):
        if name.startswith("_"): return
        store.current_label = name
    config.label_callback = label_callback
    store._rollback = False
    store._skipping = False
    _game_menu_screen = None
    store._history = False

# The game starts here.
label start:
    # Cookie painting
    $ phase1 = True

    $ phase2 = False
    $ phase2_done = False

    # Computer
    $ phase3 = True

    $ phase4 = False
    $ phase4_done = False

    $ phase5 = False

    $ trigger_room1 = False
    $ trigger_computer = False
    $ trigger_lock = False
    $ active_item = None

    jump l_room1

label l_room1:
    scene bg_room1
    if not trigger_room1:
        "I've successfully infiltrated the room. \nI've been locked in though!"
        "Maybe if I look around, I can find something that'll get me out of here."
        $ trigger_room1 = True
    call screen s_room1

label l_phase1:
    show cookie
    "It's a stunning piece of art depicting...big cookies. \nThe painting's bulging in the center. I think there's something behind it?"
    show keys
    "* Got a key!"
    $ phase1 = False
    $ phase2 = True
    jump l_room1

label l_phase2:
    show diary_closed
    "This book's got a lock on it. I have a key now though..."
    show diary
    "What's this...?"
    $ phase2 = False
    $ phase2_done = True
    jump l_room1

label l_phase3:
    # Computer
    $ pw = ""
    show computer
    if not trigger_computer:
        "I think I need to put in a password here."
        $ trigger_computer = True
    else:
        "Let's give this password another go."
    call screen s_inputtext("Input password")
    if isinstance(_return, basestring):
        $ pw = (_return).strip()
    if pw == "1320":
        "I think that was right!"
        show receipt
        "There's something highlighted on here...?"
        $ phase3 = False
        $ phase4 = True
        jump l_room1
    elif pw == "":
        jump l_room1
    else:
        "Guess that wasn't right :("
        jump l_phase3

label l_phase4:
    "This book's titled, \"Art of Moana\""
    "I'm pretty sure this is the book we found from that receipt."
    "Let's see here... \nHey, one of these pages is thicker than the others."
    show book4
    "What the...? Looks like I found a clue."
    "What can I say except, \"You're welcome\"?"
    $ phase4 = False
    $ phase4_done = True
    $ phase5 = True
    jump l_room1

label l_final:
    # Computer
    $ pw2 = ""
    show lock
    if not trigger_lock:
        "Nuts, it's a keypad. \nGuess I can't pick it..."
        "The doorframe looks pretty sturdy too. \nI'll probably just break my foot if I kick it down."
        "I wonder if I've got what I need to guess the password?"
        $ trigger_lock = True
    else:
        "Let's give this another try."
    call screen s_inputtext("Input keycode")
    if isinstance(_return, basestring):
        $ pw2 = (_return).strip()
    if pw2 == "703":
        "I think that was right!"
        "It's unlocked! I can escape!"
        
    elif pw2 == "":
        jump l_room1
    else:
        "Nuts, doesn't seem to have worked."
        jump l_final

label victory:
    scene victory_img
    "Thanks for playing!"
    $ MainMenu(confirm=False)()

label r_displaytext(content=[], last_label, img=None):
    if img:
        show expression img
    python:
        for c in content:
            renpy.say(None, c)
    jump expression last_label


screen s_room1:
    on "hide" action Hide("s_hovertext")
    imagebutton:
        # Paintbrushes
        xanchor 0.5
        yanchor 0.5
        xpos 1100
        ypos 405
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Jar of brushes") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["Just some paintbrushes."], current_label)
    imagebutton:
        # Hanging plant
        xanchor 0.5
        yanchor 0.5
        xpos 458
        ypos 223
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Hanging plant") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["A hanging plant. Nothing special."], current_label)

    imagebutton:
        # Plants
        xanchor 0.5
        yanchor 0.5
        xpos 571
        ypos 508
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Plants") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["Some plants on a windowsill."], current_label)

    imagebutton:
        # Thresh
        xanchor 0.5
        yanchor 0.5
        xpos 947
        ypos 308
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Poster") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["A poster of some strange skeletal figure with a fishing hook."], current_label)

    imagebutton:
        # LemonNa
        xanchor 0.5
        yanchor 0.5
        xpos 1344
        ypos 254
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Painting") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["A painting of some cute lemons. \nI think this guy has some weird taste in art..."], current_label)

    imagebutton:
        # Catsukidon
        xanchor 0.5
        yanchor 0.5
        xpos 1419
        ypos 378
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Painting") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["A painting of a cat... eating fried pork? \n That doesn't look healthy..."], current_label)

    imagebutton:
        # Chair
        xanchor 0.5
        yanchor 0.5
        xpos 1283
        ypos 738
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Chair") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["This chair looks very comfortable."], current_label)

    imagebutton:
        # Trash
        xanchor 0.5
        yanchor 0.5
        xpos 989
        ypos 803
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Trashcan") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a trash bin. I'm not sure what I was expecting.", "Why are there so many tissues in it...?"], current_label)

    imagebutton:
        # Dinosaur
        xanchor 0.5
        yanchor 0.5
        xpos 1614
        ypos 924
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Stuffed animal") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a cute, small dinosaur plushie."], current_label)

    imagebutton:
        # Tablet
        xanchor 0.5
        yanchor 0.5
        xpos 1453
        ypos 520
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Tablet") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a very expensive Wacom tablet. Should I steal this, too...?"], current_label)

    imagebutton:
        # Window
        xanchor 0.5
        yanchor 0.5
        xpos 1656
        ypos 302
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Window") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["Moonlight is flowing through the window."], current_label)

    imagebutton:
        # Book-Death of the boy
        xanchor 0.5
        yanchor 0.5
        xpos 481
        ypos 613
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a book titled, \"Death of the Boy.\"", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)

    imagebutton:
        # Jocking May
        xanchor 0.5
        yanchor 0.5
        xpos 619
        ypos 683
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's \"Jocking May\", a famous battle royale novel.", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)    

    imagebutton:
        # That's How Mafia Works
        xanchor 0.5
        yanchor 0.5
        xpos 1888
        ypos 187
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a book titled, \"That's How Mafia Works.\"", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)    

    imagebutton:
        # Memeology of the 21st Century
        xanchor 0.5
        yanchor 0.5
        xpos 1840
        ypos 543
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["\"Memeology of the 21st Century,\"" , "It's a enlightening research paper on memes.", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)

    imagebutton:
        # Fantastic Breasts and Where to Find them
        xanchor 0.5
        yanchor 0.5
        xpos 1845
        ypos 734
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a book titled, \"Fantastic Breasts and Where to Find them.\"", "It's book on all man's dream", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)

    imagebutton:
        # Introduction to Blinker Fluids
        xanchor 0.5
        yanchor 0.5
        xpos 231
        ypos 1005
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Book") 
        unhovered Hide("s_hovertext")
        action Call("r_displaytext", ["It's a book titled, \"Introduction to Blinker Fluids.\"", "It's the first book to read in order to understand cars.", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)

    # Cookie painting
    if phase1:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1115
            ypos 260
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Painting") 
            unhovered Hide("s_hovertext")
            action Jump("l_phase1")
    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1115
            ypos 260
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Painting") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["Just a painting of big cookies. \n I don't think there's anything else to see here."], current_label)

    # Diary
    if phase2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 417
            ypos 941
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Jump("l_phase2")
    elif phase2_done:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 417
            ypos 941
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["Here's the inside of the diary again."], current_label, "images/diary_open.png")
    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 417
            ypos 941
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["It's a dusty old book. \nThere seems to be a lock on this one. I wonder if I can't find the key?"], current_label, "images/diary_closed.png")

    # Computer monitor
    if phase3:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1104
            ypos 453
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Computer") 
            unhovered Hide("s_hovertext")
            action Jump("l_phase3")
    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1104
            ypos 453
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Computer") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["Here's that receipt again.", "There's something highlighted on here...?"], current_label, "images/receipt.png")

    # Art of Moana
    if phase4:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1832
            ypos 936
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Jump("l_phase4")
    elif phase4_done:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1832
            ypos 936
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["Here's that page I found in the book again."], current_label, "images/book4.png")
    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1832
            ypos 936
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Book") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["It's a book titled, \"Art of Moana\".", "There's so many books here. \nI don't think I'm going to find anything quick enough if I flip through them at random."], current_label)
    if phase5:
        # Gem
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1639
            ypos 733
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Gem") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["A shiny gemstone. It sparkles in the moonlight.", "Hey, isn't there a strange shape shining in the gem?"], current_label, "images/gem.png")
        # Coat
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 312
            ypos 437
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Gem") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["It's a coat...\n Wait, isn't there something inside the pocket??"], current_label, "images/coat.png")
        # Figurine
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 941
            ypos 525
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Figurine") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["A sculpture used for drawing figures. \nWait a second, I think there's something etched on the base...?"], current_label, "images/figure.png")
    else:
        # Gem
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1639
            ypos 733
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Gem") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["A shiny gemstone. It sparkles in the moonlight."], current_label, "images/gem.png")
        # Coat
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 312
            ypos 437
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Coat") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["It's a coat. \nI'm not particularly cold right now, thanks..."], current_label)
        # Figurine
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 941
            ypos 525
            idle "images/gui/empty.png"
            hover "images/gui/hover.png"
            hovered Show("s_hovertext", content = "Figurine") 
            unhovered Hide("s_hovertext")
            action Call("r_displaytext", ["A sculpture used for drawing figures. \nMan, if I didn't sleep through art class, would I be this loaded?"], current_label)

    # Final lock
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 146
        ypos 551
        idle "images/gui/empty.png"
        hover "images/gui/hover.png"
        hovered Show("s_hovertext", content = "Door handle") 
        unhovered Hide("s_hovertext")
        action Jump("l_final")


screen s_hovertext:
    default content = ""
    vbox:
        spacing 10
        xalign 0.5
        yalign 0.8
        frame:
            text content

screen s_inputtext(content=""):
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 200
        vbox:
            label "[content] and hit enter"
            input 
            textbutton _("Cancel") action Return()
