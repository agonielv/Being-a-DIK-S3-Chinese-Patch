init 1203:
    screen mphone_chat_screen(arg, idx):
        modal True
        tag mphone_chat_screen

        add "mphone_contacts_app_bg"
        if persistent.golden_phone and persistent.golden_phone_skin_enabled:
            add "mphone_shell_gold"
        else:
            add "mphone_shell"
        key "mousedown_4" action NullAction()
        key "mousedown_5" action NullAction()
        $ renpy.block_rollback()
        hbox:
            xalign 0.5
            yalign 0.06
            spacing 300 * persistent.scale_factor
            add "mphone_top_cakenet"
            add "mphone_top_icons"
        if "ep11_zoey_joy_label" in event_list:
            imagebutton at mphone_off_transform idle "mphone_off_circle_idle" hover "mphone_off_circle_hover" action (Function(mphone_count_notifications),SetVariable("mphone_text_frame",["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]),Hide("mphone_chat_reply_screen"),Hide("mphone_chat_screen"), Hide("mphone_contacts_app_screen"), SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"),Jump(currentFreeRoamLabel)) xalign 0.5 yalign mphone_off_yalign
            key "mouseup_2" action (Function(mphone_count_notifications),SetVariable("mphone_text_frame",["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]),Hide("mphone_chat_reply_screen"),Hide("mphone_chat_screen"), Hide("mphone_contacts_app_screen"), SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"),Jump(currentFreeRoamLabel))
        else:
            imagebutton at mphone_off_transform idle "mphone_off_circle_idle" hover "mphone_off_circle_hover" action (Function(mphone_count_notifications),SetVariable("mphone_text_frame",["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]),Hide("mphone_chat_reply_screen"),Hide("mphone_chat_screen")) xalign 0.5 yalign mphone_off_yalign
            key "mouseup_2" action (Function(mphone_count_notifications),SetVariable("mphone_text_frame",["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]),Hide("mphone_chat_reply_screen"),Hide("mphone_chat_screen"))
        imagebutton idle "contacts_chat_hover" hover "contacts_chat_hover" action NullAction() xalign 0.405 yalign 0.1
        hbox:
            xalign 0.5
            yalign 0.08
            spacing 100 * persistent.scale_factor
            imagebutton idle "mphone_avatar_"+arg[0].lower().replace(" ","")+"_idle" hover "mphone_avatar_"+arg[0].lower().replace(" ","")+"_idle" action NullAction() yoffset -5 * persistent.scale_factor
        imagebutton:
            action NullAction()
            xalign 0.518
            yalign 0.135
            yoffset -5 * persistent.scale_factor
            if arg[2]:
                idle "mphone_contacts_online"
                hover "mphone_contacts_online"
            else:
                idle "mphone_contacts_offline"
                hover "mphone_contacts_offline"
        text "%s" % arg[0] style "mphone_contacts_header_style" xalign 0.5 yalign 0.17
        vpgrid:
            draggable True
            mousewheel True
            cols 1
            xminimum 470 * persistent.scale_factor
            xmaximum 470 * persistent.scale_factor
            yminimum 773 * persistent.scale_factor
            ymaximum 773 * persistent.scale_factor
            xalign 0.50
            yalign 0.685
            xoffset 1 * persistent.scale_factor
            spacing 5 * persistent.scale_factor
            yinitial 1.0
            vbox:
                xalign 0.5
                yalign 0.05
                spacing 5 * persistent.scale_factor
                xoffset 5 * persistent.scale_factor
                yoffset 5 * persistent.scale_factor
                for x in range (0,len(mphone_chat_history_list[idx][2])):
                    if x > 0 and x == mphone_chat_history_list[idx][1]:
                        hbox:
                            frame:
                                xoffset 25 * persistent.scale_factor
                                xmaximum 420 * persistent.scale_factor
                                xminimum 420 * persistent.scale_factor
                                yminimum 40 * persistent.scale_factor
                                background Frame("chat_new_msg_frame",10 * persistent.scale_factor,10 * persistent.scale_factor)
                                text "New messages" style "mphone_chat_text_style" xoffset 115 * persistent.scale_factor
                    hbox:
                        yoffset 5 * persistent.scale_factor
                        yalign 1
                        spacing -5 * persistent.scale_factor
                        xminimum 420 * persistent.scale_factor
                        xmaximum 420 * persistent.scale_factor
                        if mphone_chat_history_list[idx][3][x]:
                            vbox:
                                yalign 0.5
                                xalign 0.0
                                frame background "mphone_mini_avatar_"+arg[0].lower().replace(" ","")+"_idle" xmaximum 48 * persistent.scale_factor ymaximum 48 * persistent.scale_factor yalign 0.5
                        frame:
                            if mphone_chat_history_list[idx][3][x]:
                                xoffset 15 * persistent.scale_factor
                                yalign 0.5
                                xalign 0.0
                                xmaximum 280 * persistent.scale_factor
                                background Frame("mphone_chat_them_box",10 * persistent.scale_factor,10 * persistent.scale_factor)
                            else:
                                xoffset 35 * persistent.scale_factor
                                xalign 1.0
                                yalign 0.5
                                xmaximum 280 * persistent.scale_factor
                                background Frame("chat_mc_box",10 * persistent.scale_factor,10 * persistent.scale_factor)
                            if mphone_chat_history_list[idx][2][x][0:5] != "chat_":
                                vbox:
                                    if mphone_get_chat_str(mphone_chat_history_list[idx][2][x]).strip() != "":
                                        text "%s" % mphone_get_chat_str(mphone_chat_history_list[idx][2][x]) style "mphone_chat_text_style" text_align 0.0
                                    hbox:
                                        for i in mphones_emotes:
                                            if i[1]:
                                                imagebutton idle i[0] hover i[0] yminimum 24 * persistent.scale_factor ymaximum 24 * persistent.scale_factor action NullAction()
                            else:
                                imagebutton idle mphone_chat_history_list[idx][2][x] hover mphone_chat_history_list[idx][2][x]+"_hover" action (Show(mphone_chat_history_list[idx][2][x].split("_thumb")[0]+"_screen"))
                        if mphone_chat_history_list[idx][3][x]:
                            hbox xfill True
                text "\n\n\n\n" style "mphone_chat_text_style"
        add "mphone_fg"
        vbox:
            xalign 0.78
            yalign 0.75
            spacing 5 * persistent.scale_factor
            xoffset -25 * persistent.scale_factor
            yoffset 5 * persistent.scale_factor
            for i in range(0,len(mphone_replies)):
                if mphone_replies[i] != "":
                    hbox:
                        vbox:
                            yalign 0.5
                            frame background "mphone_mini_avatar_mc%d" % mphone_mc_avatar + "_idle" xmaximum 50 * persistent.scale_factor ymaximum 50 * persistent.scale_factor
                        if mphone_replies[i][0:5] != "chat_":
                            frame:
                                yalign 0.5
                                xalign 1.0
                                xmaximum 285 * persistent.scale_factor
                                xminimum 285 * persistent.scale_factor
                                background Frame(mphone_text_frame[i],10 * persistent.scale_factor,10 * persistent.scale_factor)
                                vbox:
                                    textbutton "%s" % scw_phone(mphone_replies[i]) action (Function(mphone_mc_replies,idx,i),Function(mphone_chat_handle_replies,idx)) text_style "mphone_chat_text_style" yalign 0.5 hovered SetDict(mphone_text_frame,i,"mphone_chat_selection_box") unhovered SetDict(mphone_text_frame,i,"chat_mc_box") xmaximum 280 * persistent.scale_factor xminimum 280 * persistent.scale_factor
                                    hbox:
                                        for j in mphones_emotes:
                                            if j[1]:
                                                imagebutton idle j[0] hover j[0] hovered SetDict(mphone_text_frame,i,"mphone_chat_selection_box") unhovered SetDict(mphone_text_frame,i,"chat_mc_box") yminimum 24 * persistent.scale_factor ymaximum 24 * persistent.scale_factor action (Function(mphone_mc_replies,idx,i),Function(mphone_chat_handle_replies,idx))
                        else:
                            imagebutton idle mphone_replies[i] hover mphone_replies[i]+"_hover" yalign 0.5 background Frame(mphone_text_frame[i],10 * persistent.scale_factor,10 * persistent.scale_factor) hovered SetDict(mphone_text_frame,i,"mphone_chat_selection_box") unhovered SetDict(mphone_text_frame,i,"chat_mc_box") action (Function(mphone_mc_replies,idx,i),Function(mphone_chat_handle_replies,idx)) xmaximum 120 * persistent.scale_factor xminimum 120 * persistent.scale_factor
                            textbutton " " action NullAction() yalign 0.5 xalign 1.0 xmaximum 160 * persistent.scale_factor xminimum 160 * persistent.scale_factor

    screen major_choice_screen:
        modal True
        tag major_choice_screen

        add "major_choices_blur"
        imagebutton at show_hide_dissolve idle "bg_toprightmsg_short" xalign 0.9825 yalign -0.01 action NullAction()
        text "Affinity: {font=fonts/collegiate.ttf}[affinity]{/font}" style "score_new_style" at show_hide_dissolve xalign 0.97 yalign 0.01
        hbox:
            xalign 0.5
            yalign 0.868
            spacing 50 * persistent.scale_factor
            imagebutton:
                at show_hide_dissolve
                if affinity == "DIK" or (affinity == "NEUTRAL" and mc_info[6]):
                    idle "mc_dik_idle"
                    hover "mc_dik_hover"
                    action (Function(addCPenalty),Hide("major_choice_screen"),Jump(mc_info[1]))
                else:
                    idle "mc_dik_disabled"
                    hover "mc_dik_disabled"
                    action NullAction()
            imagebutton at show_hide_dissolve idle "mc_neutral_idle" hover "mc_neutral_hover" action (Function(addNPenalty),Hide("major_choice_screen"),Jump(mc_info[3]))
            imagebutton:
                at show_hide_dissolve
                if affinity == "CHICK" or (affinity == "NEUTRAL" and not mc_info[6]):
                    idle "mc_chick_idle"
                    hover "mc_chick_hover"
                    action (Function(addDPenalty),Hide("major_choice_screen"),Jump(mc_info[5]))
                else:
                    idle "mc_chick_disabled"
                    hover "mc_chick_disabled"
                    action NullAction()
        hbox:
            xalign 0.5
            yalign 0.868
            spacing 50 * persistent.scale_factor
            xoffset 110 * persistent.scale_factor
            yoffset 35 * persistent.scale_factor
            hbox:
                xminimum 598 * persistent.scale_factor
                xmaximum 598 * persistent.scale_factor
                yminimum 127 * persistent.scale_factor
                ymaximum 220 * persistent.scale_factor
                if affinity == "DIK" or (affinity == "NEUTRAL" and mc_info[6]):
                    text scw_major(mc_info[0]) style "mc_choice_dik_style" size 30 * persistent.scale_factor xmaximum 550 * persistent.scale_factor at show_hide_dissolve
                else:
                    text scw_major(mc_info[0]) style "mc_choice_disabled_style" size 30 * persistent.scale_factor xmaximum 550 * persistent.scale_factor at show_hide_dissolve
            hbox:
                xminimum 598 * persistent.scale_factor
                xmaximum 598 * persistent.scale_factor
                yminimum 127 * persistent.scale_factor
                ymaximum 220 * persistent.scale_factor
                text scw_major(mc_info[2]) style "mc_choice_neutral_style" size 30 * persistent.scale_factor xmaximum 550 * persistent.scale_factor at show_hide_dissolve
            hbox:
                xminimum 598 * persistent.scale_factor
                xmaximum 598 * persistent.scale_factor
                yminimum 127 * persistent.scale_factor
                ymaximum 220 * persistent.scale_factor
                if affinity == "CHICK" or (affinity == "NEUTRAL" and not mc_info[6]):
                    text scw_major(mc_info[4]) style "mc_choice_chick_style" size 30 * persistent.scale_factor xmaximum 550 * persistent.scale_factor at show_hide_dissolve
                else:
                    text scw_major(mc_info[4]) style "mc_choice_disabled_style" size 30 * persistent.scale_factor xmaximum 550 * persistent.scale_factor at show_hide_dissolve

    screen epi_camera_screen(x):
        modal True
        tag epi_camera_screen

        for i in range(0,len(x)):
            imagebutton idle "camera_icon_idle" hover "camera_icon_hover" hovered SetVariable("tmpInt",i+1) unhovered SetVariable("tmpInt",0) action (SetVariable("tmpInt",i+1), Return()) xpos x[i][1] * persistent.scale_factor ypos x[i][2] * persistent.scale_factor
            if tmpInt == i+1:
                text scw_camera(x, i) style "camera_text_style" xpos x[i][3] * persistent.scale_factor ypos x[i][4] * persistent.scale_factor
