screen key_lock_buttons(cur_route):
    image "images/keys/lock_r[cur_route].png" xalign 0.5 yalign 0.5
    vbox xalign 0.1 yalign 0.0:
        imagebutton:
            if cur_route <= 1:
                idle Transform(Image('images/keys/key_r1 idle.png'), rotate=60, zoom=0.65)
            else:
                idle Transform(Image('images/keys/key_r1 disabled.png'), rotate=60, zoom=0.65)
            focus_mask Transform(Image('images/keys/key_r1 idle.png'), rotate=60, zoom=0.65)
            hover Transform(Image('images/keys/key_r1 hover.png'), rotate=60, zoom=0.65)
            if key_lock_active and cur_route <= 1:
                action Call("handle_key_lock_click", index=cur_route, expected=1)

    vbox xalign 0.1 yalign 1.0:
        imagebutton:
            if cur_route <= 3:
                idle Transform(Image('images/keys/key_r3 idle.png'), rotate=60, zoom=0.65)
            else:
                idle Transform(Image('images/keys/key_r3 disabled.png'), rotate=60, zoom=0.65)
            focus_mask Transform(Image('images/keys/key_r3 idle.png'), rotate=60, zoom=0.65)
            hover Transform(Image('images/keys/key_r3 hover.png'), rotate=60, zoom=0.65)
            if key_lock_active and cur_route <= 3:
                action Call("handle_key_lock_click", index=cur_route, expected=3)

    vbox xalign 0.9 yalign 0.0:
        imagebutton:
            if cur_route <= 4:
                idle Transform(Image('images/keys/key_r4 idle.png'), rotate=60, zoom=0.65)
            else:
                idle Transform(Image('images/keys/key_r4 disabled.png'), rotate=60, zoom=0.65)
            idle Transform(Image('images/keys/key_r4 idle.png'), rotate=60, zoom=0.65)
            focus_mask Transform(Image('images/keys/key_r4 idle.png'), rotate=60, zoom=0.65)
            hover Transform(Image('images/keys/key_r4 hover.png'), rotate=60, zoom=0.65)
            if key_lock_active and cur_route <= 4:
                action Call("handle_key_lock_click", index=cur_route, expected=4)

    vbox xalign 0.9 yalign 1.0:
        imagebutton:
            if cur_route <= 2:
                idle Transform(Image('images/keys/key_r2 idle.png'), rotate=60, zoom=0.65)
            else:
                idle Transform(Image('images/keys/key_r2 disabled.png'), rotate=60, zoom=0.65)
            focus_mask Transform(Image('images/keys/key_r2 idle.png'), rotate=60, zoom=0.65)
            hover Transform(Image('images/keys/key_r2 hover.png'), rotate=60, zoom=0.65)
            if key_lock_active and cur_route <= 2:
                action Call("handle_key_lock_click", index=cur_route, expected=2)

default key_lock_active = True

label true_end:
label end_4:
label end_14: # lazy and don't want to fix tl tags
    $ persistent.ed_unlocked_4 = True
    if _in_replay:
        play music room_bgm

    scene bg intersection day with dissolve

    "While heading to the park…"

    play sound phonecall loop
    pause 3.0

    "…my phone started to ring."

    stop sound channel 0
    play music hitona_theme fadein 1.0

    sn "Kohi~"

    p "Ah senpai, I’m on my way there now!"

    sn "Hmmm? I’m in front of your place though…"

    sn "I kept waiting but you didn’t come, so I decided to go to you instead."

    p "Eh? But it hasn’t even been 5 minutes…"

    p "Did we pass by each other somehow???"

    sn "Well, I’ll wait here then. You wanted to ask about the safe as well, right?"

    p "I…okay, I’ll head back now then."

    p "{i}I just left though…weird. How did I not see her??{/i}"

    scene bg intersection day with dissolve

    "When I returned, I found senpai standing outside my door waiting for me."

    sn "Hi Kohiii! It’s been a while, hasn’t it!"

    p "Ah senpaaai!"

    p "You should’ve told me you were coming!"

    sn "It’s because Kohi took so long!"

    p "But…I headed straight for the park right after you called!"

    sn "Eh…but I waited so long though…"

    p "{i}Weird…{/i}"

    "I opened the door, and the two of us went inside."

    scene bg room with dissolve

    sn "About the safe though, here is the last key. You left it in your room."

    p "Huh? What are you talking…about…?"

    p" {i}Come to think of it, I do remember having 3 pieces of paper and 3 keys…{/i}"

    "I took three keys and slips of paper out from my drawer."

    "4 keys, and three sheets of papers with 1, 0, and 7 written on them."

    sn "Try opening the safe!"

label true_end_combination:
    show screen lock_buttons with dissolve
    $ _skipping = False

    $ lock_active = True
    while True:
        window hide
        $ renpy.pause(hard=True)

    label combination_lock_wrong:
        $ lock_active = False
        p "{i}It’s not opening…probably the wrong code. Let’s try again.{/i}"
        $ lock_active = True
        while True:
            window hide
            $ renpy.pause(hard=True)

    label combination_lock_correct:
        $ lock_active = False
        p "Oh it opened!"
        hide screen lock_buttons with dissolve
        play music last_end fadein 1.0


label true_end_combination_unlocked:
    $ _skipping = True
    "There’s a letter inside and…another safe with a keyhole."

    nvl clear
    nvl_narrator "“Hitona!"
    nvl_narrator "This is our gift to you."
    nvl_narrator "Open each safe with each key!”"

    call handle_key_lock(1) from _call_handle_key_lock

    call show_cg("hitonadress", True) from _call_show_cg_3
    call show_cg("anniv", True) from _call_show_cg_4
    call show_cg("regret1", True) from _call_show_cg_5
    call show_cg("regret2", True) from _call_show_cg_6
    call show_cg("regret3", True) from _call_show_cg_7
    call show_cg("regret4", True) from _call_show_cg_8
    call show_cg("noregret1", True) from _call_show_cg_9
    call show_cg("noregret2", True) from _call_show_cg_10
    call show_cg("noregret3", True) from _call_show_cg_11
    call show_cg("noregret4", True) from _call_show_cg_12

    #^ Or show just one from regret CG and one from Not Regret CG

    nvl clear
    nvl_narrator "“First of all!"
    nvl_narrator "We want to tell you that your fans are always there behind you!"
    nvl_narrator "No matter when or where, across time and space, we will always be there for you!”"

    "There’s another locked safe inside, and there are three keys left."

    call handle_key_lock(2) from _call_handle_key_lock_1
    call show_cg("spreg1", True) from _call_show_cg_13
    call show_cg("spreg2", True) from _call_show_cg_14
    call show_cg("spreg3", True) from _call_show_cg_15
    call show_cg("grandspell", True) from _call_show_cg_16

    nvl_narrator "“Second!"
    nvl_narrator "Keep being yourself!"
    nvl_narrator "That is Hitona’s unique charm!"
    nvl_narrator "Let loose!”"

    "There’s another locked safe inside, and there are two keys left."

    call handle_key_lock(3) from _call_handle_key_lock_2
    call show_cg("artreel1", True) from _call_show_cg_17
    call show_cg("artreel2", True) from _call_show_cg_18
    call show_cg("artreel3", True) from _call_show_cg_19
    call show_cg("artreel4", True) from _call_show_cg_20
    call show_cg("artreel5", True) from _call_show_cg_21
    call show_cg("artreel6", True) from _call_show_cg_42
    call show_cg("hitonamemory", True) from _call_show_cg_22


    nvl_narrator "“Third!"
    nvl_narrator "The memories that you have made all this time are irreplaceable!"
    nvl_narrator "We want Hitona to keep on making wonderful memories!”"

    "There’s another locked safe inside, and there is one key left."

    call handle_key_lock(4) from _call_handle_key_lock_3
    call show_cg("truehitona", False) from _call_show_cg_23
    $ renpy.pause(10.0)

    call credits() from _call_credits

    window hide
    $ _skipping = False
    if _preferences.language == 'simplified_chinese':
        show image 'images/true_end_c.png' with dissolve
    else:
        show image 'images/true_end.png' with dissolve
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True

    return

label handle_key_lock(index):
    show screen key_lock_buttons(index) with dissolve

    window hide
    $ key_lock_active = True

    while key_lock_active:
        $ renpy.pause(hard=True)

    hide screen key_lock_buttons with dissolve
    return

label handle_key_lock_click(index, expected):
    if index == expected:
        $ key_lock_active = False
        play sound keyunlock
        p "{i}The key fits perfectly!{/i}"
    else:
        $ key_lock_active = True
        play sound keylock
        p "{i}The key doesn't fit...let's try another key.{/i}"
    return
