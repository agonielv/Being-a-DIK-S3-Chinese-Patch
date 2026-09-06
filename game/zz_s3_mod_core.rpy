# Scrappy-derived rules; independent Chinese core adapter.
init 1099 python:
    sc_flags = {'branchAlone': '独行分支', 'branchIsabella': '伊莎贝拉分支', 'branchJill': '吉尔分支', 'branchMayaJosy': '玛雅与乔西分支', 'branchSage': '赛琪分支', 'branchZoey': '佐伊分支', 'pathIsabella': '伊莎贝拉路线', 'pathJill': '吉尔路线', 'pathMayaJosy': '玛雅与乔西路线', 'pathSage': '赛琪路线', 'roadZoey': '佐伊路线', 'envyLikesYou': '恩薇喜欢主角', 'quinnLikesYou': '奎恩喜欢主角', 'number_quinn': '获得奎恩号码', 'ep10_cathy_lewd': '第10章：与凯茜亲密', 'ep10_date_nicole': '第10章：与妮可约会', 'ep10_dating_nora': '第10章：与诺拉交往', 'ep10_nora_encourage': '第10章：鼓励诺拉', 'ep10_nora_kids': '第10章：诺拉的孩子话题', 'ep10_quinn_help': '第10章：帮助奎恩', 'ep10_riona_lewd': '第10章：与里奥娜亲密', 'ep10_rolling': '第10章：与莉莉一起嗨', 'ep11_bianca_path': '第11章：碧安卡路线', 'ep11_elena_lewd': '第11章：与埃琳娜亲密', 'ep11_jade_lewd': '第11章：与杰德亲密', 'ep11_lily_want_more': '第11章：莉莉想进一步发展', 'ep11_mel_lewd': '第11章：与梅兰妮亲密', 'ep11_nicole_dating': '第11章：与妮可交往', 'ep11_rolling': '第11章：与莉莉一起嗨', 'ep11_sally_kiss': '第11章：亲吻莎莉', 'ep11_sarah_lewd': '第11章：与莎拉亲密', 'ep12_nicole_path': '第12章：妮可路线', 'ep12_zoey_friend': '第12章：与佐伊保持朋友关系', 'ep1_accepted_quinn_offer': '第1章：接受奎恩的提议', 'ep1_beat_up_troy': '第1章：与特洛伊打架', 'ep1_beat_up_troy_won': '第1章：打赢特洛伊', 'ep1_insulted_cafeteria_worker': '第1章：辱骂食堂员工', 'ep1_lewd_camila_quinn': '第1章：卡米拉与奎恩亲密事件', 'ep2SageGuitarTeacher': '第2章：教赛琪吉他', 'ep2_TriedToKissMaya': '第2章：尝试亲吻玛雅', 'ep2_cafeteriaWorkerInsulted': '第2章：辱骂食堂员工', 'ep2_dawe_fight_won': '第2章：打赢道威', 'ep2_flirtedJade': '第2章：与杰德调情', 'ep2_fuckHOT': '第2章：HOT亲密事件', 'ep2_fuckedJosy': '第2章：与乔西亲密', 'ep2_kissedSage': '第2章：亲吻赛琪', 'ep2_wonCumpetition': '第2章：赢得亲密竞赛', 'ep3_BellaLewd': '第3章：与伊莎贝拉亲密', 'ep3_bella_came_around': '第3章：伊莎贝拉改变心意', 'ep3_choseBella': '第3章：选择伊莎贝拉', 'ep3_choseDerek': '第3章：选择德里克', 'ep3_choseSage': '第3章：选择赛琪', 'ep3_fuckedCamilaAndMona': '第3章：与卡米拉、莫娜亲密', 'ep3_fuckedRionaQuinn': '第3章：与里奥娜、奎恩亲密', 'ep3_helpedCamilaAndMona': '第3章：帮助卡米拉与莫娜', 'ep3_mayaLewd': '第3章：与玛雅亲密', 'ep3_mayaOfferedHelp': '第3章：向玛雅提供帮助', 'ep3_sclubParty': '第3章：俱乐部派对标记', 'ep4_bella_lewd': '第4章：与伊莎贝拉亲密', 'ep4_camilaOffer': '第4章：卡米拉的提议', 'ep4_fuckedJade': '第4章：与杰德亲密', 'ep4_fuckedMelanie': '第4章：与梅兰妮亲密', 'ep4_jadeOffer': '第4章：杰德的提议', 'ep4_kissedJill': '第4章：亲吻吉尔', 'ep4_kissedRiona': '第4章：亲吻里奥娜', 'ep4_quinn_lewd': '第4章：与奎恩亲密', 'ep4_rejectedJade': '第4章：拒绝杰德', 'ep4_toldDerekAboutJade': '第4章：向德里克提及杰德', 'ep5_bella_lewd': '第5章：与伊莎贝拉亲密', 'ep5_cathy_lewd': '第5章：与凯茜亲密', 'ep5_dikWinner': '第5章：DIK竞赛获胜', 'ep5_feelingsForJosy': '第5章：对乔西有感情', 'ep5_feelingsForMaya': '第5章：对玛雅有感情', 'ep5_fuckedCamila': '第5章：与卡米拉亲密', 'ep5_fuckedRiona': '第5章：与里奥娜亲密', 'ep5_hot_lewd': '第5章：HOT亲密事件', 'ep5_kissed_jill': '第5章：亲吻吉尔', 'ep6_envy_lewd': '第6章：与恩薇亲密', 'ep6_jill_lewd': '第6章：与吉尔亲密', 'ep6_nora_lewd': '第6章：与诺拉亲密', 'ep6_quinn_lewd': '第6章：与奎恩亲密', 'ep6_reject_jade': '第6章：拒绝杰德', 'ep6_vipPass': '第6章：VIP通行证', 'ep7_accept_madame': '第7章：接受罗丝夫人', 'ep7_bella_lewd': '第7章：与伊莎贝拉亲密', 'ep7_bella_rejected_you': '第7章：被伊莎贝拉拒绝', 'ep7_camila_lewd': '第7章：与卡米拉亲密', 'ep7_jill_lewd': '第7章：与吉尔亲密', 'ep7_lily_lewd': '第7章：与莉莉亲密', 'ep7_rejected_cathy': '第7章：拒绝凯茜', 'ep7_rica_lewd': '第7章：里卡亲密事件', 'ep7_riona_lewd': '第7章：与里奥娜亲密', 'ep8_quinn_lewd': '第8章：与奎恩亲密', 'ep8_recital_failed': '第8章：演奏失败', 'ep9_b_kissed_jill': '第9章：亲吻吉尔', 'ep9_jm_sad': '第9章：玛雅与乔西失落', 'ep9_sage_vanilla': '第9章：赛琪的温柔亲密事件', 'ep9_told_jill': '第9章：告诉吉尔碧安卡男友的事', 'minigames': '启用小游戏', 'tutorials': '启用教程', 'permanent_affinity': '锁定倾向'}
    sc_flag_order = ['branchAlone', 'branchIsabella', 'branchJill', 'branchMayaJosy', 'branchSage', 'branchZoey', 'pathIsabella', 'pathJill', 'pathMayaJosy', 'pathSage', 'roadZoey', 'envyLikesYou', 'quinnLikesYou', 'number_quinn', 'ep10_cathy_lewd', 'ep10_date_nicole', 'ep10_dating_nora', 'ep10_nora_encourage', 'ep10_nora_kids', 'ep10_quinn_help', 'ep10_riona_lewd', 'ep10_rolling', 'ep11_bianca_path', 'ep11_elena_lewd', 'ep11_jade_lewd', 'ep11_lily_want_more', 'ep11_mel_lewd', 'ep11_nicole_dating', 'ep11_rolling', 'ep11_sally_kiss', 'ep11_sarah_lewd', 'ep12_nicole_path', 'ep12_zoey_friend', 'ep1_accepted_quinn_offer', 'ep1_beat_up_troy', 'ep1_beat_up_troy_won', 'ep1_insulted_cafeteria_worker', 'ep1_lewd_camila_quinn', 'ep2SageGuitarTeacher', 'ep2_TriedToKissMaya', 'ep2_cafeteriaWorkerInsulted', 'ep2_dawe_fight_won', 'ep2_flirtedJade', 'ep2_fuckHOT', 'ep2_fuckedJosy', 'ep2_kissedSage', 'ep2_wonCumpetition', 'ep3_BellaLewd', 'ep3_bella_came_around', 'ep3_choseBella', 'ep3_choseDerek', 'ep3_choseSage', 'ep3_fuckedCamilaAndMona', 'ep3_fuckedRionaQuinn', 'ep3_helpedCamilaAndMona', 'ep3_mayaLewd', 'ep3_mayaOfferedHelp', 'ep3_sclubParty', 'ep4_bella_lewd', 'ep4_camilaOffer', 'ep4_fuckedJade', 'ep4_fuckedMelanie', 'ep4_jadeOffer', 'ep4_kissedJill', 'ep4_kissedRiona', 'ep4_quinn_lewd', 'ep4_rejectedJade', 'ep4_toldDerekAboutJade', 'ep5_bella_lewd', 'ep5_cathy_lewd', 'ep5_dikWinner', 'ep5_feelingsForJosy', 'ep5_feelingsForMaya', 'ep5_fuckedCamila', 'ep5_fuckedRiona', 'ep5_hot_lewd', 'ep5_kissed_jill', 'ep6_envy_lewd', 'ep6_jill_lewd', 'ep6_nora_lewd', 'ep6_quinn_lewd', 'ep6_reject_jade', 'ep6_vipPass', 'ep7_accept_madame', 'ep7_bella_lewd', 'ep7_bella_rejected_you', 'ep7_camila_lewd', 'ep7_jill_lewd', 'ep7_lily_lewd', 'ep7_rejected_cathy', 'ep7_rica_lewd', 'ep7_riona_lewd', 'ep8_quinn_lewd', 'ep8_recital_failed', 'ep9_b_kissed_jill', 'ep9_jm_sad', 'ep9_sage_vanilla', 'ep9_told_jill', 'minigames', 'tutorials', 'permanent_affinity']
    sc_numbers = {'dik': ('性格分数（−20 至 20）', -20, 20), 'money': ('随身现金（受钱包等级限制）', 0, 10), 'pp_money': ('派对筹备资金', 0, 99999), 'tc': ('出轨点数', 0, 999), 'RPmaya': ('玛雅', -5, 50), 'RPjosy': ('乔西', -2, 46), 'RPsage': ('赛琪', -7, 37), 'RPisabella': ('伊莎贝拉', -9, 31), 'RPjill': ('吉尔', -5, 40), 'RPderek': ('德里克', -2, 16), 'RPdiks': ('DIK兄弟会', -2, 23), 'RPjocks': ('体育生', -3, 0), 'RPnerds': ('书呆子', -1, 1), 'RPpreps': ('富家子弟', -2, 0)}
    sc_number_order = ['dik', 'money', 'pp_money', 'tc', 'RPmaya', 'RPjosy', 'RPsage', 'RPisabella', 'RPjill', 'RPderek', 'RPdiks', 'RPjocks', 'RPnerds', 'RPpreps']
    sc_scenes = ['persistent.ep10_lewd_cathy', 'persistent.ep10_lewd_isabella', 'persistent.ep10_lewd_jill', 'persistent.ep10_lewd_jm', 'persistent.ep10_lewd_josy', 'persistent.ep10_lewd_lily', 'persistent.ep10_lewd_madame1', 'persistent.ep10_lewd_madame2', 'persistent.ep10_lewd_madame3', 'persistent.ep10_lewd_maya', 'persistent.ep10_lewd_nicole', 'persistent.ep10_lewd_nora', 'persistent.ep10_lewd_quinn', 'persistent.ep10_lewd_riona', 'persistent.ep10_lewd_sage', 'persistent.ep10_lewd_sage2', 'persistent.ep11_lewd_becky', 'persistent.ep11_lewd_bella', 'persistent.ep11_lewd_bella2', 'persistent.ep11_lewd_camila', 'persistent.ep11_lewd_elena', 'persistent.ep11_lewd_jade', 'persistent.ep11_lewd_jill', 'persistent.ep11_lewd_jill2', 'persistent.ep11_lewd_jm', 'persistent.ep11_lewd_lily', 'persistent.ep11_lewd_lynette', 'persistent.ep11_lewd_madame', 'persistent.ep11_lewd_melanie', 'persistent.ep11_lewd_sage', 'persistent.ep11_lewd_sage2', 'persistent.ep11_lewd_sarah', 'persistent.ep11_lewd_tara', 'persistent.ep11_lewd_tiffani', 'persistent.ep12_lewd_bianca', 'persistent.ep12_lewd_cathy', 'persistent.ep12_lewd_elena', 'persistent.ep12_lewd_isabella', 'persistent.ep12_lewd_jade', 'persistent.ep12_lewd_jill', 'persistent.ep12_lewd_josy', 'persistent.ep12_lewd_maya', 'persistent.ep12_lewd_nicole', 'persistent.ep12_lewd_nora', 'persistent.ep12_lewd_quinn', 'persistent.ep12_lewd_quinn2', 'persistent.ep12_lewd_sage', 'persistent.ep12_lewd_sally', 'persistent.ep12_lewd_ts', 'persistent.ep12_lewd_zoey', 'persistent.ep9_lewd_camila', 'persistent.ep9_lewd_cumpetition', 'persistent.ep9_lewd_heather', 'persistent.ep9_lewd_isabella', 'persistent.ep9_lewd_isabella2', 'persistent.ep9_lewd_jade', 'persistent.ep9_lewd_jill', 'persistent.ep9_lewd_jill2', 'persistent.ep9_lewd_jm', 'persistent.ep9_lewd_jm2', 'persistent.ep9_lewd_lily', 'persistent.ep9_lewd_ln', 'persistent.ep9_lewd_maya', 'persistent.ep9_lewd_quinn', 'persistent.ep9_lewd_sage1', 'persistent.ep9_lewd_sage2', 'persistent.ep9_lewd_sage3', 'persistent.ep9_lewd_sm', 'persistent.epi_lewd_eb', 'persistent.epi_lewd_zoey']
    sc_rewards = ['persistent.ep10_card1', 'persistent.ep10_card10', 'persistent.ep10_card11', 'persistent.ep10_card12', 'persistent.ep10_card13', 'persistent.ep10_card14', 'persistent.ep10_card15', 'persistent.ep10_card16', 'persistent.ep10_card2', 'persistent.ep10_card3', 'persistent.ep10_card4', 'persistent.ep10_card5', 'persistent.ep10_card6', 'persistent.ep10_card7', 'persistent.ep10_card8', 'persistent.ep10_card9', 'persistent.ep10_cardsa1', 'persistent.ep10_cardsa10', 'persistent.ep10_cardsa11', 'persistent.ep10_cardsa12', 'persistent.ep10_cardsa13', 'persistent.ep10_cardsa14', 'persistent.ep10_cardsa15', 'persistent.ep10_cardsa16', 'persistent.ep10_cardsa17', 'persistent.ep10_cardsa18', 'persistent.ep10_cardsa19', 'persistent.ep10_cardsa2', 'persistent.ep10_cardsa20', 'persistent.ep10_cardsa3', 'persistent.ep10_cardsa4', 'persistent.ep10_cardsa5', 'persistent.ep10_cardsa6', 'persistent.ep10_cardsa7', 'persistent.ep10_cardsa8', 'persistent.ep10_cardsa9', 'persistent.ep10_cardzo1', 'persistent.ep10_cardzo10', 'persistent.ep10_cardzo11', 'persistent.ep10_cardzo12', 'persistent.ep10_cardzo13', 'persistent.ep10_cardzo14', 'persistent.ep10_cardzo15', 'persistent.ep10_cardzo16', 'persistent.ep10_cardzo17', 'persistent.ep10_cardzo18', 'persistent.ep10_cardzo19', 'persistent.ep10_cardzo2', 'persistent.ep10_cardzo20', 'persistent.ep10_cardzo3', 'persistent.ep10_cardzo4', 'persistent.ep10_cardzo5', 'persistent.ep10_cardzo6', 'persistent.ep10_cardzo7', 'persistent.ep10_cardzo8', 'persistent.ep10_cardzo9', 'persistent.ep11_card1', 'persistent.ep11_card10', 'persistent.ep11_card10b', 'persistent.ep11_card11', 'persistent.ep11_card11b', 'persistent.ep11_card12', 'persistent.ep11_card12b', 'persistent.ep11_card2', 'persistent.ep11_card3', 'persistent.ep11_card4', 'persistent.ep11_card5', 'persistent.ep11_card6', 'persistent.ep11_card7', 'persistent.ep11_card8', 'persistent.ep11_card9', 'persistent.ep11_card9b', 'persistent.ep11_cardly1', 'persistent.ep11_cardly10', 'persistent.ep11_cardly11', 'persistent.ep11_cardly12', 'persistent.ep11_cardly13', 'persistent.ep11_cardly14', 'persistent.ep11_cardly15', 'persistent.ep11_cardly16', 'persistent.ep11_cardly17', 'persistent.ep11_cardly18', 'persistent.ep11_cardly19', 'persistent.ep11_cardly2', 'persistent.ep11_cardly20', 'persistent.ep11_cardly3', 'persistent.ep11_cardly4', 'persistent.ep11_cardly5', 'persistent.ep11_cardly6', 'persistent.ep11_cardly7', 'persistent.ep11_cardly8', 'persistent.ep11_cardly9', 'persistent.ep11_cardmy1', 'persistent.ep11_cardmy10', 'persistent.ep11_cardmy11', 'persistent.ep11_cardmy12', 'persistent.ep11_cardmy13', 'persistent.ep11_cardmy14', 'persistent.ep11_cardmy15', 'persistent.ep11_cardmy16', 'persistent.ep11_cardmy17', 'persistent.ep11_cardmy18', 'persistent.ep11_cardmy19', 'persistent.ep11_cardmy2', 'persistent.ep11_cardmy20', 'persistent.ep11_cardmy3', 'persistent.ep11_cardmy4', 'persistent.ep11_cardmy5', 'persistent.ep11_cardmy6', 'persistent.ep11_cardmy7', 'persistent.ep11_cardmy8', 'persistent.ep11_cardmy9', 'persistent.ep12_card1', 'persistent.ep12_card10', 'persistent.ep12_card11', 'persistent.ep12_card12', 'persistent.ep12_card13', 'persistent.ep12_card14', 'persistent.ep12_card15', 'persistent.ep12_card16', 'persistent.ep12_card17', 'persistent.ep12_card18', 'persistent.ep12_card19', 'persistent.ep12_card2', 'persistent.ep12_card3', 'persistent.ep12_card4', 'persistent.ep12_card5', 'persistent.ep12_card6', 'persistent.ep12_card7', 'persistent.ep12_card8', 'persistent.ep12_card9', 'persistent.ep12_cardcam1', 'persistent.ep12_cardcam10', 'persistent.ep12_cardcam11', 'persistent.ep12_cardcam12', 'persistent.ep12_cardcam13', 'persistent.ep12_cardcam14', 'persistent.ep12_cardcam15', 'persistent.ep12_cardcam16', 'persistent.ep12_cardcam17', 'persistent.ep12_cardcam18', 'persistent.ep12_cardcam19', 'persistent.ep12_cardcam2', 'persistent.ep12_cardcam20', 'persistent.ep12_cardcam3', 'persistent.ep12_cardcam4', 'persistent.ep12_cardcam5', 'persistent.ep12_cardcam6', 'persistent.ep12_cardcam7', 'persistent.ep12_cardcam8', 'persistent.ep12_cardcam9', 'persistent.ep12_cardisa1', 'persistent.ep12_cardisa10', 'persistent.ep12_cardisa11', 'persistent.ep12_cardisa12', 'persistent.ep12_cardisa13', 'persistent.ep12_cardisa14', 'persistent.ep12_cardisa15', 'persistent.ep12_cardisa16', 'persistent.ep12_cardisa17', 'persistent.ep12_cardisa18', 'persistent.ep12_cardisa19', 'persistent.ep12_cardisa2', 'persistent.ep12_cardisa20', 'persistent.ep12_cardisa3', 'persistent.ep12_cardisa4', 'persistent.ep12_cardisa5', 'persistent.ep12_cardisa6', 'persistent.ep12_cardisa7', 'persistent.ep12_cardisa8', 'persistent.ep12_cardisa9', 'persistent.ep7_wpi1', 'persistent.ep7_wpi2', 'persistent.ep7_wpj1', 'persistent.ep7_wpj2', 'persistent.ep7_wpjo1', 'persistent.ep7_wpjo2', 'persistent.ep7_wpm1', 'persistent.ep7_wpm2', 'persistent.ep7_wps1', 'persistent.ep7_wps2', 'persistent.ep8_wpe1', 'persistent.ep8_wpi1', 'persistent.ep8_wpj1', 'persistent.ep8_wpjade1', 'persistent.ep8_wpjo1', 'persistent.ep8_wpm1', 'persistent.ep8_wpmad1', 'persistent.ep8_wpq1', 'persistent.ep8_wps1', 'persistent.ep9_card1', 'persistent.ep9_card10', 'persistent.ep9_card11', 'persistent.ep9_card12', 'persistent.ep9_card13', 'persistent.ep9_card14', 'persistent.ep9_card15', 'persistent.ep9_card16', 'persistent.ep9_card17', 'persistent.ep9_card18', 'persistent.ep9_card19', 'persistent.ep9_card2', 'persistent.ep9_card20', 'persistent.ep9_card3', 'persistent.ep9_card4', 'persistent.ep9_card5', 'persistent.ep9_card6', 'persistent.ep9_card7', 'persistent.ep9_card8', 'persistent.ep9_card9', 'persistent.ep9_cardji1', 'persistent.ep9_cardji10', 'persistent.ep9_cardji11', 'persistent.ep9_cardji12', 'persistent.ep9_cardji13', 'persistent.ep9_cardji14', 'persistent.ep9_cardji15', 'persistent.ep9_cardji16', 'persistent.ep9_cardji17', 'persistent.ep9_cardji18', 'persistent.ep9_cardji19', 'persistent.ep9_cardji2', 'persistent.ep9_cardji20', 'persistent.ep9_cardji3', 'persistent.ep9_cardji4', 'persistent.ep9_cardji5', 'persistent.ep9_cardji6', 'persistent.ep9_cardji7', 'persistent.ep9_cardji8', 'persistent.ep9_cardji9', 'persistent.ep9_cardjo1', 'persistent.ep9_cardjo10', 'persistent.ep9_cardjo11', 'persistent.ep9_cardjo12', 'persistent.ep9_cardjo13', 'persistent.ep9_cardjo14', 'persistent.ep9_cardjo15', 'persistent.ep9_cardjo16', 'persistent.ep9_cardjo17', 'persistent.ep9_cardjo18', 'persistent.ep9_cardjo19', 'persistent.ep9_cardjo2', 'persistent.ep9_cardjo20', 'persistent.ep9_cardjo3', 'persistent.ep9_cardjo4', 'persistent.ep9_cardjo5', 'persistent.ep9_cardjo6', 'persistent.ep9_cardjo7', 'persistent.ep9_cardjo8', 'persistent.ep9_cardjo9', 'persistent.epi_card1', 'persistent.epi_card10', 'persistent.epi_card11', 'persistent.epi_card12', 'persistent.epi_card13', 'persistent.epi_card14', 'persistent.epi_card15', 'persistent.epi_card16', 'persistent.epi_card2', 'persistent.epi_card3', 'persistent.epi_card4', 'persistent.epi_card5', 'persistent.epi_card6', 'persistent.epi_card7', 'persistent.epi_card8', 'persistent.epi_card9']
    sc_art_indices = {'art_unlocked_lvl1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'art_unlocked_lvl2': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'art_unlocked_lvl3': [0, 2, 7, 9, 14]}
    sc_choice_hints = {('Encourage him', 'Such a girl!'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Is she all right?', 'What the fuck!?'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Nana is important!', 'Fuck school!'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Talk back', 'Apologize'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Not your business', 'Nothing'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('What a snitch', "You're right"): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Answer', 'Ignore'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Appreciate it', "Don't have to"): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('LOL! Asshole!', "Don't scare me"): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('You ok?', "I'm excited!"): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Love your tats', 'Too many tattoos'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Joke', 'Sounds dope'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Um... Why?', 'Kinda personal'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Yes', 'Joke'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('It could be better', 'It sucks'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Ignore him', 'Talk back'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Sure do', 'Show concern'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Good, huh?', 'Yeah'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Pay me for it', 'Sounds fun'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Had better oness', 'Back hurts'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ("I'm fine", "I'm pissed"): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Right...', 'Talk back'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('Not for everyone', 'Encourage her'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Help him out', "Don't look at me"): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('I can tell', 'Which ones?'): ('佐伊：坏小子倾向', '佐伊：暖男倾向'), ('Calm her down', 'Take her phone'): ('佐伊：暖男倾向', '佐伊：坏小子倾向'), ('It is too late', 'Thank you'): ('佐伊：坏小子倾向', '佐伊：暖男倾向')}
    # Embedded into a Ren'Py init block by the builder. No game values change at init.
    import copy as _sc_copy
    import re as _sc_re

    def sc_owner(key):
        return (persistent, key[11:]) if key.startswith('persistent.') else (renpy.store, key)

    def sc_get(key):
        owner, attr = sc_owner(key)
        return getattr(owner, attr, None)

    def sc_numeric(key):
        return type(sc_get(key)) in (int, float)

    def sc_boolean(key):
        return type(sc_get(key)) is bool

    def sc_commit(updates):
        # History is stored with rollback-aware game state and contains only changed keys.
        before = []
        for key, value in updates:
            owner, attr = sc_owner(key)
            old = getattr(owner, attr, None)
            if old != value:
                before.append((key, _sc_copy.deepcopy(old)))
        if not before:
            return
        for key, value in updates:
            owner, attr = sc_owner(key)
            setattr(owner, attr, value)
        renpy.store.sc_undo_log = (renpy.store.sc_undo_log + [before])[-30:]
        if any(k.startswith('persistent.') for k, v in updates):
            renpy.save_persistent()
        renpy.restart_interaction()

    def sc_undo():
        if not renpy.store.sc_undo_log:
            return
        before = renpy.store.sc_undo_log[-1]
        renpy.store.sc_undo_log = renpy.store.sc_undo_log[:-1]
        for key, value in before:
            owner, attr = sc_owner(key)
            setattr(owner, attr, value)
        if any(k.startswith('persistent.') for k, v in before):
            renpy.save_persistent()
            sc_refresh_gallery()
        renpy.restart_interaction()

    def sc_delta(key, delta):
        if key not in sc_numbers or not sc_numeric(key):
            return
        label, low, high = sc_numbers[key]
        if key == 'money':
            high = {0:5, 1:6, 2:8, 3:10}.get(sc_get('wallet_lvl'), 5)
        value = max(low, min(high, sc_get(key) + delta))
        changes = [(key, value)]
        if key == 'dik':
            dtype = (3 if value >= 15 else 2 if value >= 10 else 1 if value >= 5 else
                     -3 if value <= -15 else -2 if value <= -10 else -1 if value <= -5 else 0)
            if sc_numeric('dtype'):
                changes.append(('dtype', dtype))
        sc_commit(changes)

    def sc_toggle(key):
        if key in sc_flags and sc_boolean(key):
            sc_commit([(key, not sc_get(key))])

    def sc_affinity(value):
        if value in ('DIK', 'CHICK', 'NEUTRAL') and sc_get('affinity') in ('DIK', 'CHICK', 'NEUTRAL'):
            sc_commit([('affinity', value)])

    def sc_refresh_gallery():
        for name in ('calcScenes', 'calcRenders', 'calcWallpapers'):
            fn = getattr(renpy.store, name, None)
            if callable(fn):
                try:
                    fn()
                except Exception as e:
                    renpy.log('S3CN mod: gallery counter refresh failed: ' + name + ': ' + str(e))

    def sc_unlock(kind):
        # Exact gallery flags from Scrappy. Never touch seen-story or achievement flags.
        keys = sc_scenes if kind == 'scenes' else sc_rewards
        changes = [(k, True) for k in keys if sc_get(k) is not True]
        if kind == 'rewards':
            for attr, indices in sc_art_indices.items():
                current = sc_get('persistent.' + attr)
                if isinstance(current, list):
                    updated = list(current)
                    for i in indices:
                        if 0 <= i < len(updated):
                            updated[i] = True
                    changes.append(('persistent.' + attr, updated))
        sc_commit(changes)
        sc_refresh_gallery()
        renpy.notify('已解锁。可用“撤销上一步”还原本次修改。')

    def sc_group(key):
        if key in ('minigames', 'tutorials', 'permanent_affinity'):
            return '设置'
        if key.startswith(('branch', 'path', 'road')):
            return '路线'
        match = _sc_re.match(r'ep(\d+)', key)
        if match:
            return '第9–12章' if int(match.group(1)) >= 9 else '第1–8章'
        return '其他'

    def sc_choice_text(s):
        # Use the existing translation chain, before calculating the Chinese line width.
        return config.replace_text(s) if config.replace_text is not None else s

    def sc_choice_size(s):
        plain = _sc_re.sub(r'\{[^}]*\}', '', sc_choice_text(s))
        n = max(len(line) for line in plain.split('\n')) if plain else 0
        return int((52 if n <= 7 else 44 if n <= 12 else 36) * persistent.scale_factor)

    def sc_choice_hint(a, b, index):
        if not persistent.sc_hints:
            return ''
        return sc_choice_hints.get((_sc_re.sub(r'\s+', ' ', _sc_re.sub(r'\{[^}]*\}', '', a)).strip(), _sc_re.sub(r'\s+', ' ', _sc_re.sub(r'\{[^}]*\}', '', b)).strip()), ('', ''))[index]

    if 'sc_mod_button' not in config.overlay_screens:
        config.overlay_screens.append('sc_mod_button')

default sc_undo_log = []
default persistent.sc_hints = True

init 1100:
    style sc_text:
        font "fonts/s3_cn.ttf"
        size 28 * persistent.scale_factor
        color "#e5edf5"
    style sc_button_text is sc_text:
        hover_color "#ffb45b"
        selected_color "#ffb45b"
        insensitive_color "#687789"
    style sc_button:
        padding (12 * persistent.scale_factor, 6 * persistent.scale_factor)
        background Solid("#26394d")
        hover_background Solid("#385570")
    screen sc_mod_button():
        zorder 110
        if not main_menu and not _in_replay and not renpy.get_screen("sc_mod_menu"):
            key "K_F8" action Show("sc_mod_menu")
            textbutton "修改器 · F8" action Show("sc_mod_menu") style "sc_button" text_style "sc_button_text" xalign 0.99 yalign 0.02

    screen sc_mod_menu():
        modal True
        zorder 300
        default section = "数值"
        default flag_group = "第9–12章"
        key "K_F8" action Hide("sc_mod_menu")
        key "game_menu" action Hide("sc_mod_menu")
        add Solid("#08111dee")
        frame:
            xalign 0.5
            yalign 0.5
            xsize 1760 * persistent.scale_factor
            ysize 950 * persistent.scale_factor
            padding (28 * persistent.scale_factor, 24 * persistent.scale_factor)
            background Solid("#122033")
            vbox:
                spacing 16 * persistent.scale_factor
                hbox:
                    spacing 28 * persistent.scale_factor
                    text "S3 中文修改器 · 核心整合测试版" style "sc_text" size 38 * persistent.scale_factor
                    textbutton "撤销上一步" action Function(sc_undo) sensitive bool(sc_undo_log) style "sc_button" text_style "sc_button_text"
                    textbutton "关闭" action Hide("sc_mod_menu") style "sc_button" text_style "sc_button_text"
                text "修改作用于当前进度；建议先另存一份。路线开关不等同于补齐该路线的剧情历史。" style "sc_text" size 23 * persistent.scale_factor
                hbox:
                    spacing 16 * persistent.scale_factor
                    for item in ("数值", "关系", "剧情开关", "画廊", "说明"):
                        textbutton item action SetScreenVariable("section", item) selected section == item style "sc_button" text_style "sc_button_text"
                if section in ("数值", "关系"):
                    viewport:
                        ysize 690 * persistent.scale_factor
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        vbox:
                            spacing 14 * persistent.scale_factor
                            for field in sc_number_order:
                                if field.startswith("RP") == (section == "关系"):
                                    hbox:
                                        spacing 18 * persistent.scale_factor
                                        text sc_numbers[field][0] style "sc_text" xsize 470 * persistent.scale_factor
                                        text (str(sc_get(field)) if sc_numeric(field) else "此进度尚未载入") style "sc_text" xsize 250 * persistent.scale_factor
                                        for delta in (-10, -1, 1, 10):
                                            textbutton ("%+d" % delta) action Function(sc_delta, field, delta) sensitive sc_numeric(field) style "sc_button" text_style "sc_button_text"
                            if section == "数值":
                                hbox:
                                    spacing 18 * persistent.scale_factor
                                    text "当前倾向" style "sc_text" xsize 470 * persistent.scale_factor
                                    for en, zh in (("CHICK", "暖男"), ("NEUTRAL", "中立"), ("DIK", "坏小子")):
                                        textbutton zh action Function(sc_affinity, en) selected sc_get("affinity") == en sensitive sc_get("affinity") in ("CHICK", "NEUTRAL", "DIK") style "sc_button" text_style "sc_button_text"
                elif section == "剧情开关":
                    hbox:
                        spacing 14 * persistent.scale_factor
                        for g in ("第9–12章", "路线", "第1–8章", "设置", "其他"):
                            textbutton g action SetScreenVariable("flag_group", g) selected flag_group == g style "sc_button" text_style "sc_button_text"
                    viewport:
                        ysize 600 * persistent.scale_factor
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        vbox:
                            spacing 9 * persistent.scale_factor
                            for field in sc_flag_order:
                                if sc_group(field) == flag_group:
                                    hbox:
                                        spacing 18 * persistent.scale_factor
                                        text sc_flags[field] style "sc_text" xsize 850 * persistent.scale_factor
                                        textbutton ("是" if sc_get(field) is True else "否" if sc_get(field) is False else "此进度尚未载入") action Function(sc_toggle, field) sensitive sc_boolean(field) style "sc_button" text_style "sc_button_text"
                elif section == "画廊":
                    text "解锁仅在点击后执行，可撤销最近一次操作。不会把全部剧情标成已读。" style "sc_text"
                    textbutton "解锁 S3 回放条目" action Function(sc_unlock, "scenes") style "sc_button" text_style "sc_button_text"
                    textbutton "解锁 Mod 对应收藏与画作" action Function(sc_unlock, "rewards") style "sc_button" text_style "sc_button_text"
                elif section == "说明":
                    text "基于 Scrappy Mod 0.12.1 的数值、关系、事件开关和解锁规则移植。\n采用当前 S3 汉化脚本，未覆盖旧版的 89 个剧情文件。\n未包含：全章攻略、多路线追加剧情、小游戏跳关、收集物定位。\n气泡文字缩小；已定位的佐伊选项可显示倾向提示。\n当前为测试版，尚未在真实游戏中启动验证。" style "sc_text" xmaximum 1600 * persistent.scale_factor
                    textbutton ("气泡倾向提示：开" if persistent.sc_hints else "气泡倾向提示：关") action ToggleField(persistent, "sc_hints") style "sc_button" text_style "sc_button_text"
