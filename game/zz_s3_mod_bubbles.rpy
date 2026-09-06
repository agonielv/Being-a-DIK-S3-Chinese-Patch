init 1101:
    screen zoey_choice_screen(choice1, x1, y1, choice2, x2, y2):
        modal True
        tag zoey_choice_screen

        hbox:
            xpos (x1 - 50) * persistent.scale_factor
            ypos (y1 - 60) * persistent.scale_factor
            imagebutton at z_choice_button_transform xalign 0.5 yalign 0.5 idle "z_choice_button1_idle" hover "z_choice_button1_hover" hovered Function(play_bubble_func) action (Function(play_select_choice_func),Call("choice_1_label"))
        hbox:
            xpos x1 * persistent.scale_factor
            ypos y1 * persistent.scale_factor
            xoffset 10 * persistent.scale_factor
            yoffset 55 * persistent.scale_factor
            xminimum 350 * persistent.scale_factor
            xmaximum 350 * persistent.scale_factor
            vbox:
                xsize 350 * persistent.scale_factor
                spacing 5 * persistent.scale_factor
                text sc_choice_text(choice1) style "zoey_choice_style" size sc_choice_size(choice1) xalign 0.5 text_align 0.5 xmaximum 340 * persistent.scale_factor
                if sc_choice_hint(choice1, choice2, 0):
                    text sc_choice_hint(choice1, choice2, 0) font "fonts/s3_cn.ttf" size 22 * persistent.scale_factor color "#176240" xalign 0.5 text_align 0.5 xmaximum 340 * persistent.scale_factor
        hbox:
            xpos (x2 - 50) * persistent.scale_factor
            ypos (y2 - 60) * persistent.scale_factor
            imagebutton at z_choice_button_transform xalign 0.5 yalign 0.5 idle "z_choice_button2_idle" hover "z_choice_button2_hover" hovered Function(play_bubble_func) action (Function(play_select_choice_func),Call("choice_2_label"))
        hbox:
            xpos x2 * persistent.scale_factor
            ypos y2 * persistent.scale_factor
            xoffset 10 * persistent.scale_factor
            yoffset 55 * persistent.scale_factor
            xminimum 350 * persistent.scale_factor
            xmaximum 350 * persistent.scale_factor
            vbox:
                xsize 350 * persistent.scale_factor
                spacing 5 * persistent.scale_factor
                text sc_choice_text(choice2) style "zoey_choice_style" size sc_choice_size(choice2) xalign 0.5 text_align 0.5 xmaximum 340 * persistent.scale_factor
                if sc_choice_hint(choice1, choice2, 1):
                    text sc_choice_hint(choice1, choice2, 1) font "fonts/s3_cn.ttf" size 22 * persistent.scale_factor color "#176240" xalign 0.5 text_align 0.5 xmaximum 340 * persistent.scale_factor
