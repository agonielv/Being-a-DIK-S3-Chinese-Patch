init 1012:
    screen episode_title_screen:
        modal True
        tag episode_title_screen

        timer 5 action Hide("episode_title_screen")
        if currentEpisode == 0:
            $ episode_title_name = "乘风破浪"
        elif currentEpisode == 9:
            $ episode_title_name = "妖娆佳人"
        elif currentEpisode == 10:
            $ episode_title_name = "暴雪前的宁静"
        elif currentEpisode == 11:
            $ episode_title_name = "天翻地覆"
        elif currentEpisode == 12:
            $ episode_title_name = "烟与火"
        imagebutton at title_white_line_anim4 xoffset -2200 * persistent.scale_factor idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.28
        imagebutton at title_white_line_anim3 xoffset 2920 * persistent.scale_factor idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.32
        imagebutton at title_orange_line_anim xoffset -5030 * persistent.scale_factor idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.36
        imagebutton at title_orange_line_anim xoffset -1750 * persistent.scale_factor idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.36
        if currentEpisode >= 9:
            text "第 %d 章" % currentEpisode style "episode_number_title_style" at episode_number_anim xoffset -2000 * persistent.scale_factor yalign 0.35
        else:
            text "Interlude" style "episode_number_title_style" at episode_number_anim xoffset -2000 * persistent.scale_factor yalign 0.35
        if currentEpisode == 10:
            text "[episode_title_name]" style "episode_title_style2" at episode_title_anim xoffset 2000 * persistent.scale_factor yalign 0.45
        else:
            text "[episode_title_name]" style "episode_title_style" at episode_title_anim xoffset 2000 * persistent.scale_factor yalign 0.45
        imagebutton at title_orange_line_anim2 xoffset 2000 * persistent.scale_factor idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.57
        imagebutton at title_white_line_anim2 xoffset -4000 * persistent.scale_factor idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.61
        imagebutton at title_white_line_anim xoffset 1700 * persistent.scale_factor idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.65

    screen confirm(message, yes_action, no_action):
        modal True
        zorder 200
        style_prefix "confirm"

        add "[persistent.img_dir]/gui/overlay/confirm.png"
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45 * persistent.scale_factor
                label _s3_v12_prompt(message) text_style "custom_menu_style_text" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 150 * persistent.scale_factor
                    textbutton "确定" action yes_action text_style "custom_frame_style"
                    textbutton "取消" action no_action text_style "custom_frame_style"
        key "game_menu" action no_action
