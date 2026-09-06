# v1.1 TEST: presentation-only repair; do not alter game/save identifiers.
init 1009 python:
    import re as _s3_fix_re
    _s3_fix_previous = config.replace_text
    _s3_fix_ui = {'History': '历史', 'Back': '回退', 'Skip': '快进', 'Auto': '自动', 'Save': '保存', 'Load': '读取', 'Q.Save': '快存', 'Q.Load': '快读', 'Prefs': '设置', 'Guide': '攻略', 'Main Menu': '主菜单', 'Quit': '退出', 'Audio': '音频', 'Dialogue': '对白', 'Settings': '设置', 'Return': '返回', 'Save Collectibles': '保存收藏进度', 'Save Name': '存档名称', 'Empty slot': '空存档位', 'Import': '导入', 'Continue': '继续', 'DLC': '扩展内容', 'Options': '选项', 'Gallery': '画廊', 'Music': '音乐', 'Yes': '是', 'No': '否', 'End Replay': '结束回放', 'Do you want to load this save?': '要读取这个存档吗？', 'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.': '确定返回主菜单吗？\n未保存的进度将会丢失。', 'Are you sure you want to quit?': '确定退出游戏吗？', 'Are you sure you want to overwrite your save?': '确定覆盖这个存档吗？', 'Are you sure you want to delete this save?': '确定删除这个存档吗？', 'Music Volume': '音乐音量', 'Sound Volume': '音效音量', 'Sex Sound Volume': '亲密场景音量', 'Mute All': '全部静音', 'Phone Notifications': '手机通知', 'Rollback Side': '回退区域', 'Disable': '关闭', 'Disabled': '已关闭', 'Enabled': '已开启', 'Left': '左侧', 'Right': '右侧', 'Text Speed': '文字速度', 'Auto-Forward Time': '自动播放间隔', 'Text Box Opacity': '对话框不透明度', 'Text Box': '对话框', 'Skip Unseen Text': '跳过未读文本', 'Skip After Choice': '选择后继续快进', 'Skip Transitions': '跳过转场', 'Resolution': '分辨率', '4K files not installed': '未安装 4K 资源', 'Restart needed': '需要重启', 'Display': '显示模式', 'Window': '窗口', 'Fullscreen': '全屏', 'Tutorials': '教程', 'Fast Travel Button': '快速移动按钮', 'Autosave (Occasional Lag Spikes)': '自动存档（偶有卡顿）', 'Autosave (No Lag Spikes)': '自动存档（无卡顿）', 'Special Effects (Better Experience)': '特效（更佳体验）', 'Special Effects (Better Performance)': '特效（更高性能）', 'Color-Blind Accessible Mini-games': '小游戏色盲辅助', 'Gallery Buttons': '画廊按钮', 'On Hover': '悬停时显示', 'Quick Menu': '快捷菜单', 'Customize Quick Menu': '自定义快捷菜单', 'Affinity:': '倾向：', 'Chosen road:': '所选路线：', 'Date:': '日期：', 'CHICK': '暖男', 'DIK': '坏小子', 'Neutral': '中立', 'HISTORY': '历史', 'BACK': '回退', 'SKIP': '快进', 'AUTO': '自动', 'SAVE': '保存', 'LOAD': '读取', 'Q.SAVE': '快存', 'Q.LOAD': '快读', 'PREFS': '设置', 'GUIDE': '攻略', 'MAIN MENU': '主菜单', 'QUIT': '退出', 'AUDIO': '音频', 'DIALOGUE': '对白', 'SETTINGS': '设置', 'RETURN': '返回', 'SAVE COLLECTIBLES': '保存收藏进度', 'SAVE NAME': '存档名称', 'EMPTY SLOT': '空存档位', 'IMPORT': '导入', 'CONTINUE': '继续', 'OPTIONS': '选项', 'GALLERY': '画廊', 'MUSIC': '音乐', 'YES': '是', 'NO': '否', 'END REPLAY': '结束回放', 'DO YOU WANT TO LOAD THIS SAVE?': '要读取这个存档吗？', 'ARE YOU SURE YOU WANT TO RETURN TO THE MAIN MENU?\nTHIS WILL LOSE UNSAVED PROGRESS.': '确定返回主菜单吗？\n未保存的进度将会丢失。', 'ARE YOU SURE YOU WANT TO QUIT?': '确定退出游戏吗？', 'ARE YOU SURE YOU WANT TO OVERWRITE YOUR SAVE?': '确定覆盖这个存档吗？', 'ARE YOU SURE YOU WANT TO DELETE THIS SAVE?': '确定删除这个存档吗？', 'MUSIC VOLUME': '音乐音量', 'SOUND VOLUME': '音效音量', 'SEX SOUND VOLUME': '亲密场景音量', 'MUTE ALL': '全部静音', 'PHONE NOTIFICATIONS': '手机通知', 'ROLLBACK SIDE': '回退区域', 'DISABLE': '关闭', 'DISABLED': '已关闭', 'ENABLED': '已开启', 'LEFT': '左侧', 'RIGHT': '右侧', 'TEXT SPEED': '文字速度', 'AUTO-FORWARD TIME': '自动播放间隔', 'TEXT BOX OPACITY': '对话框不透明度', 'TEXT BOX': '对话框', 'SKIP UNSEEN TEXT': '跳过未读文本', 'SKIP AFTER CHOICE': '选择后继续快进', 'SKIP TRANSITIONS': '跳过转场', 'RESOLUTION': '分辨率', '4K FILES NOT INSTALLED': '未安装 4K 资源', 'RESTART NEEDED': '需要重启', 'DISPLAY': '显示模式', 'WINDOW': '窗口', 'FULLSCREEN': '全屏', 'TUTORIALS': '教程', 'FAST TRAVEL BUTTON': '快速移动按钮', 'AUTOSAVE (OCCASIONAL LAG SPIKES)': '自动存档（偶有卡顿）', 'AUTOSAVE (NO LAG SPIKES)': '自动存档（无卡顿）', 'SPECIAL EFFECTS (BETTER EXPERIENCE)': '特效（更佳体验）', 'SPECIAL EFFECTS (BETTER PERFORMANCE)': '特效（更高性能）', 'COLOR-BLIND ACCESSIBLE MINI-GAMES': '小游戏色盲辅助', 'GALLERY BUTTONS': '画廊按钮', 'ON HOVER': '悬停时显示', 'QUICK MENU': '快捷菜单', 'CUSTOMIZE QUICK MENU': '自定义快捷菜单', 'AFFINITY:': '倾向：', 'CHOSEN ROAD:': '所选路线：', 'DATE:': '日期：', 'NEUTRAL': '中立'}
    _s3_fix_names = {'Alex': '亚历克斯', 'Alison': '艾莉森', 'Amelia': '阿米莉亚', 'Andy': '安迪', 'Anthony': '安东尼', 'Arieth': '阿丽丝', 'Ashley': '阿什莉', 'Avery': '艾弗里', 'Becky': '贝琪', 'Bert': '伯特', 'Beth': '贝丝', 'Bianca': '碧安卡', 'Brandi': '布兰迪', 'Bret': '布雷特', 'Brian': '布莱恩', 'Bruce': '布鲁斯', 'Caleb': '卡莱布', 'Camila': '卡米拉', 'Carla': '卡拉', 'Cathy': '凯茜', 'Chad': '查德', 'Chao': '赵', 'Charlotte': '夏洛特', 'Chen': '陈', 'Christian': '克里斯蒂安', 'Christie': '克里斯蒂', 'Clara': '克拉拉', 'Clive': '克莱夫', 'Dany': '丹妮', 'Darius': '达里厄斯', 'David': '戴维', 'Dawe': '道威', 'Derek': '德里克', 'Doris': '多丽丝', 'Dwyane': '德韦恩', 'Elena': '埃琳娜', 'Emma': '艾玛', 'Erin': '艾琳', 'Eugene': '尤金', 'Felicia': '菲莉西亚', 'Floyd': '弗洛伊德', 'Geoff': '乔治', 'Gina': '吉娜', 'Gordon': '戈登', 'Heather': '希瑟', 'Helen': '海伦', 'Ida': '艾达', 'Iris': '艾瑞丝', 'Isabella': '伊莎贝拉', 'Jacob': '雅各布', 'Jade': '杰德', 'James': '詹姆斯', 'Jamie': '杰米', 'Jeff': '杰夫', 'Jen': '珍', 'Jenna': '珍娜', 'Jill': '吉尔', 'Jimmy': '吉米', 'John Boy': '约翰小子', 'John': '约翰', 'Jonah': '乔纳', 'Jonathan': '乔纳森', 'Josy': '乔西', 'Karen': '凯伦', 'Kylie': '凯莉', 'Lana': '拉娜', 'Leanne': '莉安', 'Leon': '里昂', 'Lily': '莉莉', 'Linda': '琳达', 'Lucas': '卢卡斯', 'Luis': '路易斯', 'Lynette': '莉奈特', 'Madame Rose': '罗丝夫人', 'Magnar': '马格纳尔', 'Marc': '马克', 'Matthew': '马修', 'Maya': '玛雅', 'Melanie': '梅兰妮', 'Mia': '米娅', 'Micha': '米莎', 'Mick': '米克', 'Minny': '米妮', 'Miranda': '米兰达', 'Mona': '莫娜', 'Monica': '莫妮卡', 'Mr. Dahl': '达尔先生', 'Mr. Wallace': '华莱士先生', 'Muriel': '穆里尔', 'Neil': '尼尔', 'Nick': '尼克', 'Nicole': '妮可', 'Nikita': '尼基塔', 'Nora': '诺拉', 'Oliver': '奥利弗', 'Olivia': '奥利维亚', 'Oscar': '奥斯卡', 'Patrick': '帕特里克', 'Paula': '葆拉', 'Penny': '佩妮', 'Pete': '皮特', 'Philip': '菲利普', 'Priscilla': '普里西拉', 'Professor Burke': '伯克教授', 'Quinn': '奎恩', 'Rich': '里奇', 'Riona': '里奥娜', 'Ron': '罗恩', 'Rox': '洛克丝', 'Rusty': '拉斯蒂', 'Sage': '赛琪', 'Sandy': '桑迪', 'Sarah': '莎拉', 'Sally': '莎莉', 'Stanley': '斯坦利', 'Stephen': '斯蒂芬', 'Steve': '史蒂夫', 'Suzy': '苏西', 'Tania': '塔妮娅', 'Tara': '塔拉', 'Tate': '泰特', 'The Ice Queen': '冰雪女王', 'Tiffani': '蒂芙尼', 'Tina': '蒂娜', 'Tommy': '汤米', 'Trent': '特伦特', 'Troy': '特洛伊', 'Tybalt': '提伯特', 'Ursula': '厄休拉', 'Vinny': '维尼', 'Vivian': '维维安', 'Wendy': '温蒂', 'Zoey': '佐伊'}
    _s3_fix_pattern = _s3_fix_re.compile(r"(?<![A-Za-z])(" + "|".join(_s3_fix_re.escape(n) for n in sorted(_s3_fix_names, key=len, reverse=True)) + r")(?![A-Za-z])")
    def _s3_fix_plain(s):
        # Preserve whitespace and tags; never replace within variable expressions.
        core = s.strip()
        if core in _s3_fix_ui:
            return s[:len(s)-len(s.lstrip())] + _s3_fix_ui[core] + s[len(s.rstrip()):]
        if _s3_fix_re.match(r"^Page [0-9]+$", core):
            return s.replace(core, "第 " + core[5:] + " 页")
        # Restrict name substitution to name labels and already-Chinese prose.
        if core in _s3_fix_names or _s3_fix_re.search(u"[\u3400-\u9fff]", s):
            player = getattr(renpy.store, "name", None)
            return _s3_fix_pattern.sub(lambda m: m.group(0) if m.group(0) == player else _s3_fix_names[m.group(0)], s)
        return s
    def _s3_fix_replace(s):
        if _s3_fix_previous is not None:
            s = _s3_fix_previous(s)
        if renpy.store._preferences.language != "schinese":
            return s
        if s in _s3_fix_ui:
            return _s3_fix_ui[s]
        parts = _s3_fix_re.split(r"(\{[^}]*\}|\[[^\]]*\])", s)
        return "".join(p if i % 2 else _s3_fix_plain(p) for i,p in enumerate(parts))
    config.replace_text = _s3_fix_replace
    for _s3_fix_font in ['fonts/ApeMount.ttf', 'fonts/Audrey-Bold.otf', 'fonts/Creepster-Regular.ttf', 'fonts/DejaVuSans.ttf', 'fonts/Museo500.otf', 'fonts/Precious.ttf', 'fonts/Redressed.ttf', 'fonts/Roboto-Regular.ttf', 'fonts/bradhitc.ttf', 'fonts/briarwood_heavy_font.ttf', 'fonts/cabin-regular.ttf', 'fonts/candara.ttf', 'fonts/centurygothicbold.ttf', 'fonts/centurygothicregular.ttf', 'fonts/collegiate.ttf', 'fonts/daisy.ttf', 'fonts/symbolfont.ttf']:
        for _s3_fix_b in (False, True):
            for _s3_fix_i in (False, True):
                config.font_replacement_map[(_s3_fix_font, _s3_fix_b, _s3_fix_i)] = ("fonts/s3_cn.ttf", _s3_fix_b, _s3_fix_i)
    # Explicit defaults cover dialogue, labels and styles not using a fonts/ path.
    style.default.font = "fonts/s3_cn.ttf"
    style.say_dialogue.font = "fonts/s3_cn.ttf"
    style.say_label.font = "fonts/s3_cn.ttf"
    gui.text_font = "fonts/s3_cn.ttf"
    gui.name_text_font = "fonts/s3_cn.ttf"
    gui.interface_text_font = "fonts/s3_cn.ttf"
    # The main menu uses imagebuttons, not translatable textbuttons.
    # Substitute only their displayables; retain the original actions/positions.
    _s3_fix_buttons = {"new_game_btn":"导入", "continue_btn":"继续", "dlc_btn":"扩展", "options_btn":"选项", "menu_gallery_btn":"画廊", "music_credits_btn":"音乐", "quit_btn":"退出"}
    for _s3_fix_image, _s3_fix_label in _s3_fix_buttons.items():
        for _s3_fix_suffix, _s3_fix_color in (("", "#ffffff"), ("_hover", "#fe9416")):
            renpy.image(_s3_fix_image + _s3_fix_suffix, Text(_s3_fix_label, font="fonts/s3_cn.ttf", size=int(58 * persistent.scale_factor), color=_s3_fix_color, outlines=[(1, "#000000", 0, 0)]))
