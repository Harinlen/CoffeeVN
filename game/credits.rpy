define credits_names = {
    'rabbit': _('BlackRabbit13'),
    'kosa': _('Kosakyun'),
    'luttii': _('Luttii'),
    'wari': _('超エライひまわり'),
    'gabu': _('Gabuccino'),
    'cryo': _('Cryo83 (C83Ren)'),
    'pupu': _('miyo'),
    'nep': _('Nepelz_AR'),
    'lemon': _('ILLimN'),
    'lobster': _('Lobsteranian'),
    'xn': _('名前はなんだっけ'),
    'kimagure': _('きまぐれアフター'),

    'company': _('Black Rabbit Black Company'),

    'dova': _('DOVA-SYNDROME'),
    'zap': _('ZapSplat'),

    'kohi': _('Hitona Kohigashi'),

    'artist0': _('かくうさこ'),
    'artist1': _('ナッツ'),
    'artist2': _('omurice'),

    'message0': _('???'),
    'message1': _('???'),
    'message2': _('???'),
    'message3': _('???'),
    'message4': _('???'),
    'message5': _('???'),
    'message6': _('???'),
    'message7': _('???'),
    'message8': _('???'),
    'message9': _('???'),
    'message10': _('???'),
    'message11': _('???'),
    'message12': _('???'),
    'message13': _('???'),
    'message14': _('???'),
    'message15': _('???'),
    'message16': _('???'),
    'message17': _('???'),
}

define credits_font = 'tl/japanese/SourceHanSansLite.ttf'

screen credits_centered_text(t):
    text t xalign 0.5 color '#FFF' font credits_font

screen credits_space(space):
    fixed xsize 1920 ysize space

screen credits_entry(what, who, trailing_spaces=True):
    vbox:
        use credits_centered_text(what)
        use credits_space(75)
        $ first = True
        for person in who:
            if first:
                $ first = False
            else:
                use credits_space(15)
            use credits_centered_text(credits_names[person])
        if trailing_spaces:
            use credits_space(315)

screen credits_message(who, message, img):
    vbox:
        use credits_space(180)
        fixed xsize 1300 ysize 20
        if img:
            fixed xsize 1000 ysize 400 xalign 0.5:
                vbox xalign 0.5 yalign 0.5 xsize 1000:
                    text message xalign 0.5 yalign 0.5 xsize 1000 color '#FFF' font credits_font
                    fixed ysize 70
                    vbox xalign 1.0 yalign 0.5:
                        $ t = '———' + __(credits_names[who])
                        text t xalign 1.0 color '#FFF' font credits_font
            fixed xalign 0.5 ysize 400:
                image img xalign 0.5 yalign 0.0 xsize 350 ysize 350
        else:
            fixed xsize 1000 ysize 800 xalign 0.5:
                vbox xalign 0.5 yalign 0.5 xsize 1000:
                    text message xalign 0.5 yalign 0.5 xsize 1000 color '#FFF' font credits_font
                    fixed ysize 70
                    vbox xalign 1.0 yalign 0.5:
                        $ t = '———' + __(credits_names[who])
                        text t xalign 1.0 color '#FFF' font credits_font

screen credits_display():
    vbox:
        use credits_space(125)
        use credits_entry(_("Planning"), ["company"])
        use credits_entry(_("Scenario"), ["rabbit", "wari"])
        use credits_entry(_("Translation"), ["kosa", "xn"])
        use credits_entry(_("Editing"), ["rabbit", "xn"])
        use credits_entry(_("Illustration"), ["nep", "lobster", "lemon", "gabu", "wari", "rabbit", "kosa", "artist0", "artist1", "artist2", "kimagure"])
        use credits_entry(_("Music"), ["luttii", "dova"])
        use credits_entry(_("Sound"), ["zap"])
        use credits_entry(_("Programming"), ["rabbit", "cryo", "xn"])
        use credits_entry(_("Support"), ["pupu"])
        fixed xsize 1920 ysize 1080:
            vbox xalign 0.5 yalign 0.5:
                image Transform(Image('gui/title.png'), zoom=0.35) xalign 0.5 yalign 0.5
        frame xsize 1920 ysize 10 background '#f00' xpadding 0 ypadding 0

# for figuring out height
screen credits_offset(offset):
    fixed:
        use credits_display()
        ypos -offset+1080

screen credits_final():
    fixed xsize 1920 ysize 1080:
        vbox xalign 0.5 yalign 0.5:
            use credits_centered_text(_("Congratulations on your second anniversary!"))

define credits_messages = [
    ('wari', '60歳になるまで配信をやめちゃダメですよ！', 'images/credits/wari.png'),
    ('gabu', 'Dont forget to eat healthy food!\n\n健康的な食べ物もお忘れずに！', 'images/credits/gabu.png'),
    ('kosa', 'kohisuki', 'images/credits/kosa.png'),
    ('nep', 'Kohi is a good girl and always trying hard; I hope you\'re taking care of yourself and taking some rest whenever you feel tired.\n\nこっひーはいい子ですし、いつも頑張ってますね。お体お大事にして、疲れた時に休んでくださいね！', 'images/credits/nep.png'),
    ('lobster', 'Let\'s continue having fun together!\n\nこれからも一緒に楽しましょう！', 'images/credits/lobster.png'),
    ('lemon', 'I wanted to thank you for keeping us entertained and making our day brighter with your smile, best wishes for your future!\n\nいつも楽しませてくれて、笑顔で一日一日明るくしてくれて、ありがとうございます。これからもよろしくお願いします！', 'images/credits/lemon.png'),
    ('xn', '宇宙一可愛いひとなちゃんがずっと幸せでいられますように。', 'images/credits/xn.png'),
    ('cryo', 'Congratulations on your second anniversary! May all your works, your daily life, your health, and your gacha, always be blessed\n\n２週年おめでとうございます！これからのお仕事や日々の生活、健康、ガチャにも、永久に祝福がありますように。', None),
    ('luttii', 'G G A G C B\nG G A G D C', None),
    # ('pupu', 'kohisuki', None),
    ('rabbit', 'A selfish present that I hoped you\'d like.\n\nわがままなプレゼントなんでしたが、気に入っていただけたら嬉しいです。', None),
]

default credits_message_index = 0
screen credits_message_display():
    use credits_message(*credits_messages[credits_message_index])

define credits_scroll_time = 60.0
define credits_message_display_time = 7.5
# use show screen credits_offset(x) until the red bar is just not visible
define credits_height = 6383

transform credits_scroll:
    xalign 0.5
    ypos 1080

    linear credits_scroll_time ypos -credits_height + 1080

screen credits_scroll_screen():
    fixed at credits_scroll:
        use credits_display()

image credits_bg = 'images/credits/bg.png'

label credits:
    stop sound
    $ _skipping = False
    $ _game_menu_screen, _old_game_menu_screen = None, _game_menu_screen
    window hide

    scene credits_bg with dissolve

    show screen credits_scroll_screen
    $ renpy.pause(credits_scroll_time + 2, hard=True)
    pause
    hide screen credits_scroll_screen with dissolve

    $ credits_message_index = 0
    while credits_message_index < len(credits_messages):
        show screen credits_message_display with dissolve
        pause # credits_message_display_time
        hide screen credits_message_display with dissolve
        $ credits_message_index += 1
        
    show screen credits_final with dissolve
    pause
    hide screen credits_final with dissolve

    $ _game_menu_screen = _old_game_menu_screen
    $ _skipping = True

    return
