init 1200 python:
    import re as scw_re
    import json as scw_json
    import ast as scw_ast
    with renpy.file('s3_walkthrough/data.json') as scw_f:
        scw_data = scw_json.load(scw_f)
    scw_node_map = {}
    scw_diagnostics = []

    def scw_plain(text):
        return scw_re.sub(r'\s+', ' ', scw_re.sub(r'\{[^}]*\}', '', str(text))).strip()

    def scw_signature(choices):
        return tuple(scw_plain(c) for c in choices)

    def scw_register():
        """Match all occurrences within a file; repeated 'Kiss' menus cannot share hints."""
        groups = {}
        seen = set()
        for node in renpy.game.script.namemap.values():
            if id(node) in seen or type(node).__name__ != 'Menu':
                continue
            seen.add(id(node))
            filename = str(node.filename).replace('\\', '/')
            if '/tl/' in filename:
                continue
            file = next((f for f in scw_data['menus'] if filename.endswith('/'+f) or filename == f), None)
            if file is None:
                continue
            sig = scw_signature([i[0] for i in node.items if i[2] is not None])
            groups.setdefault((file, sig), []).append(node)
        expected = {}
        for file, menus in scw_data['menus'].items():
            for menu in menus:
                expected.setdefault((file, scw_signature(menu['choices'])), []).append(menu)
        for key, menus in expected.items():
            nodes = sorted(groups.get(key, []), key=lambda n: n.linenumber)
            if len(nodes) != len(menus):
                if any(m['hints'] for m in menus):
                    scw_diagnostics.append('%s: source occurrences %d, loaded %d' % (key[0], len(menus), len(nodes)))
                continue
            for node, menu in zip(nodes, menus):
                if menu['hints']:
                    scw_node_map[node.name] = menu
        renpy.log('S3 walkthrough: %d annotated menus matched; %d mismatches' % (len(scw_node_map), len(scw_diagnostics)))
        for problem in scw_diagnostics:
            renpy.log('S3 walkthrough mismatch: '+problem)

    scw_register()

    def scw_node():
        return renpy.game.script.namemap.get(renpy.game.context().current)

    def scw_enabled():
        return getattr(persistent, 'scw_enabled', True) is not False

    def scw_text(text):
        text = scw_data['names'].get(text, text)
        text = renpy.translate_string(text)
        text = renpy.substitute(text)
        if config.replace_text:
            text = config.replace_text(text)
        return text

    def scw_env(truth=False):
        env = dict(vars(renpy.store))
        # Single-route baseline. These are LOCAL values; no route flags are created or changed.
        env.setdefault('wt_ep9_branch_numbers', 1)
        env.setdefault('wt_ep11_zoey_kiss_others', False)
        if truth:
            count = 3
            if not env.get('_in_replay', False):
                for cond, delta in scw_data['truth_terms']:
                    if scw_test(cond, env):
                        count += delta
            env['tmpInt'] = count
        return env

    def scw_test(condition, env):
        try:
            return bool(eval(condition, {'__builtins__': {}}, env))
        except (NameError, TypeError, KeyError, IndexError, AttributeError):
            return False

    def scw_effect(record):
        if not scw_enabled():
            return ''
        truth = record['file'].endswith('ep9_freeroam_ph3_events.rpy') and record['source_line'] == 2707
        env = scw_env(truth)
        chunks = []
        for part in record['parts']:
            text = ''
            for cond, value in part:
                if cond is None or scw_test(cond, env):
                    text = value
            if text and text not in chunks:
                chunks.append(text)
        if record['literal'] and record['literal'] not in chunks:
            chunks.append(record['literal'])
        if not chunks and not record['parts']:
            chunks.append('原 Mod 标注选项')
        return ' '.join(chunks)

    def scw_menu_hint(caption):
        if not scw_enabled():
            return ''
        node = scw_node()
        menu = scw_node_map.get(getattr(node, 'name', None))
        if menu:
            matches = []
            for index, record in menu['hints'].items():
                original = menu['choices'][int(index)]
                if scw_plain(caption) in (scw_plain(original), scw_plain(scw_text(original))):
                    matches.append(scw_effect(record))
            if len(set(matches)) == 1:
                return matches[0]
        return scw_guess(caption, node)

    def scw_guess(caption, node):
        if node is None or type(node).__name__ != 'Menu' or not str(node.filename).endswith('ep11_freeroam_party_events.rpy'):
            return ''
        try:
            names = [i[0] for i in node.items if i[2] is not None]
            if len(names) < 3 or not all(n in scw_data['names'] for n in names):
                return ''
            expected = renpy.store.guess_who_list[renpy.store.tmpInt][0].replace('ep11_pp_act2_event_', '').capitalize()
            if scw_plain(caption) in (expected, scw_plain(scw_text(expected))):
                return '猜人小游戏：正确答案'
        except (AttributeError, IndexError, TypeError):
            pass
        return ''

    def scw_extra(kind, base, context):
        if not scw_enabled():
            return ''
        matches = []
        for record in scw_data['extras']:
            if record['kind'] != kind or scw_plain(record['base']) != scw_plain(base):
                continue
            if kind == 'bubble':
                same = scw_signature(record['context']) == scw_signature(context)
            else:
                same = record['context'] == context
            if same:
                matches.append(scw_effect(record))
        return matches[0] if matches and len(set(matches)) == 1 else ''

    def scw_phone(base):
        hint = scw_extra('phone', base, list(getattr(renpy.store, 'mphone_replies', [])))
        text = mphone_get_chat_str(base)
        return scw_text(text) + ('\n{size=-5}{color=#16713e}'+hint+'{/color}{/size}' if hint else '')

    def scw_major(base):
        info = getattr(renpy.store, 'mc_info', [])
        context = [info[i] for i in (1, 3, 5)] if len(info) >= 6 else []
        hint = scw_extra('major', base, context)
        return scw_text(base) + ('\n{size=-8}'+hint+'{/size}' if hint else '')

    def scw_camera(x, i):
        hint = scw_extra('camera', x[i][0], [list(v[1:]) for v in x])
        return scw_text(x[i][0]) + ('\n{size=-8}'+hint+'{/size}' if hint else '')

    def sc_choice_hint(a, b, index):
        if getattr(persistent, 'sc_hints', True) is False:
            return ''
        return scw_extra('bubble', (a, b)[index], [a, b])

    def scw_collectibles():
        roam = getattr(renpy.store, 'freeRoamID', '')
        section = scw_data['collectibles'].get(roam, {})
        result = []
        for kind, title in [('money_list', '现金'), ('rewards_list', '收藏图'), ('pack_list', '收集任务')]:
            for item in section.get(kind, []):
                if not item['var'].strip():
                    continue
                if kind == 'pack_list':
                    if not getattr(renpy.store, 'pack_quest_active', False):
                        continue
                    try:
                        found = renpy.store.pack_quest_list[item['index']][item['episode']]
                    except (AttributeError, IndexError, TypeError):
                        found = None
                else:
                    target = renpy.store if kind == 'money_list' else persistent
                    found = getattr(target, item['found'], None)
                result.append((title, item, found))
        return result

    def scw_marks():
        if not scw_enabled() or not getattr(persistent, 'scw_marks', True) or getattr(renpy.store, 'phone_opened', False) or not getattr(renpy.store, 'map_fast_travel_enabled', False):
            return []
        label = getattr(renpy.store, 'currentFreeRoamLabel', '')
        # All free-roam overlays must stop as soon as a dialogue/event starts.
        return [(title, item) for title, item, found in scw_collectibles() if found is not None and not found and item['var'] == label]

    def scw_boxes():
        events = getattr(renpy.store, 'event_list', [])
        pairs = [('ep11_fr_deco_box1_event_label', '左侧走廊'), ('ep11_fr_deco_box2_event_label', '厨房'), ('ep11_fr_deco_box3_event_label', '雅各布的房间')]
        return [name for label, name in pairs if label in events]

    def scw_words():
        if not renpy.get_screen('english_screen'):
            return []
        return [(n, ', '.join(str(w).upper() for w in getattr(renpy.store, 'eng_list%d' % n, []))) for n in (3,4,5,6) if getattr(renpy.store, 'eng_list%d' % n, [])]

    def scw_notes():
        chapter = str(getattr(renpy.store, 'currentEpisode', 0))
        return scw_data['warnings'].get(chapter, [])

    if 'scw_overlay' not in config.overlay_screens:
        config.overlay_screens.append('scw_overlay')


    def scw_menu_height(items):
        total = 0
        for item in items:
            caption = item.caption if hasattr(item, 'caption') else item[0]
            # Weighted length bounds the layout; viewport scrolling handles unusually long translations.
            text = scw_plain(scw_text(caption))
            units = sum(1.0 if ord(c) > 255 else 0.52 for c in text)
            main_rows = max(1, int((units + 15) // 16))
            hint = scw_menu_hint(caption)
            hint_rows = max(1, int((len(hint) + 22) // 23)) if hint else 0
            total += max(70, main_rows * 38 + hint_rows * 28 + 24) + 4
        return min(790, total + 12) * persistent.scale_factor

default persistent.scw_enabled = True
default persistent.scw_marks = True

init 1202:
    screen choice(items):
        style_prefix "choice"
        viewport:
            xalign 1.0
            yalign 0.8
            xsize int(config.screen_width * 0.31)
            ysize scw_menu_height(items)
            mousewheel True
            draggable True
            vbox:
                xfill True
                spacing 4 * persistent.scale_factor
                for item in items:
                    $ caption = item.caption if hasattr(item, "caption") else item[0]
                    $ action = item.action if hasattr(item, "action") else item[1]
                    $ hint = scw_menu_hint(caption)
                    if action and " (disabled)" in caption:
                        button:
                            style "menu_sex_style_button_disabled"
                            ymaximum None
                            text caption.replace(" (disabled)", "") style "menu_sex_style_disabled" xoffset 0 xmaximum int(config.screen_width * 0.28)
                    elif action:
                        button:
                            style "menu_sex_style_button"
                            ymaximum None
                            action action
                            vbox:
                                xfill True
                                text scw_text(caption) style "menu_sex_style" xoffset 0 xmaximum int(config.screen_width * 0.28) text_align 0.5 xalign 0.5
                                if hint:
                                    text hint font "fonts/s3_cn.ttf" size 22 * persistent.scale_factor color "#b2efca" xmaximum int(config.screen_width * 0.28) text_align 0.5 xalign 0.5
                    else:
                        text scw_text(caption) style "menu_sex_style" xoffset 0 xmaximum int(config.screen_width * 0.28) text_align 0.5 xalign 0.5

    screen scw_overlay():
        zorder 190
        if not main_menu:
            key "K_F7" action ToggleScreen("scw_guide")
            textbutton "攻略 · F7" action ToggleScreen("scw_guide") xalign 0.99 ypos 65 * persistent.scale_factor text_font "fonts/s3_cn.ttf" text_size 23 * persistent.scale_factor
            for title, item in scw_marks():
                add "s3_walkthrough/collect_circle.png" xpos max(0, item['posx']) * persistent.scale_factor ypos max(0, item['posy']) * persistent.scale_factor zoom persistent.scale_factor
            if scw_enabled() and scw_words():
                frame:
                    xalign 0.02
                    yalign 0.03
                    xmaximum 760 * persistent.scale_factor
                    background "#13221ce8"
                    padding (12, 10)
                    vbox:
                        text "英语课答案（已输入的单词会移除）" font "fonts/s3_cn.ttf" size 21 * persistent.scale_factor
                        for length, words in scw_words():
                            text ("%d字母：%s" % (length, words)) font "fonts/s3_cn.ttf" size 19 * persistent.scale_factor

    screen scw_guide():
        modal True
        zorder 201
        key "K_F7" action Hide("scw_guide")
        key "K_ESCAPE" action Hide("scw_guide")
        frame:
            background "#111e29f5"
            xalign 0.5
            yalign 0.5
            xsize 1060 * persistent.scale_factor
            ysize 870 * persistent.scale_factor
            padding (24, 20)
            vbox:
                spacing 14 * persistent.scale_factor
                hbox:
                    spacing 35 * persistent.scale_factor
                    text "第三季攻略" font "fonts/s3_cn.ttf" size 34 * persistent.scale_factor
                    textbutton "关闭 · F7" action Hide("scw_guide") text_font "fonts/s3_cn.ttf" text_size 25 * persistent.scale_factor
                hbox:
                    spacing 30 * persistent.scale_factor
                    textbutton ("选项提示：开" if scw_enabled() else "选项提示：关") action ToggleField(persistent, "scw_enabled") text_font "fonts/s3_cn.ttf" text_size 24 * persistent.scale_factor
                    textbutton ("收集物标记：开" if persistent.scw_marks else "收集物标记：关") action ToggleField(persistent, "scw_marks") text_font "fonts/s3_cn.ttf" text_size 24 * persistent.scale_factor
                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    yfill True
                    vbox:
                        spacing 14 * persistent.scale_factor
                        xmaximum 970 * persistent.scale_factor
                        text "选项下方显示原 Mod 的效果提示；手机回复、重大抉择、拍照和间章气泡也已接入。未标注的选项不代表没有后果。" font "fonts/s3_cn.ttf" size 24 * persistent.scale_factor
                        text "本章路线提醒" font "fonts/s3_cn.ttf" size 28 * persistent.scale_factor color "#91debd"
                        for note in scw_notes():
                            text note font "fonts/s3_cn.ttf" size 24 * persistent.scale_factor
                        text "出轨点数：原 Mod 对 tc 的称呼。＋／－表示数值增减。多角色共同出现的提示保留原 Mod 的合并写法。" font "fonts/s3_cn.ttf" size 23 * persistent.scale_factor
                        text "当前自由探索收集清单" font "fonts/s3_cn.ttf" size 28 * persistent.scale_factor color "#91debd"
                        if not scw_collectibles():
                            text "当前没有对应清单，或尚未进入自由探索。" font "fonts/s3_cn.ttf" size 23 * persistent.scale_factor
                        for title, item, found in scw_collectibles():
                            text (("已收集" if found else "状态未知" if found is None else "待收集") + " · " + title + " · " + item['name']) font "fonts/s3_cn.ttf" size 23 * persistent.scale_factor color ("#9aa9a3" if found else "#ffffff")
                        if scw_boxes():
                            text ("装饰箱剩余位置：" + "、".join(scw_boxes())) font "fonts/s3_cn.ttf" size 24 * persistent.scale_factor
                        text "机关盒第一面操作顺序" font "fonts/s3_cn.ttf" size 28 * persistent.scale_factor color "#91debd"
                        text "1. 四个旋钮全部朝上。\n2. 左上、左下转到朝左。\n3. 右上、右下转到朝右。\n4. 按中间按钮。\n5. 四个旋钮重新全部朝上。\n6. 左上、右上转到朝右。\n7. 再按中间按钮。" font "fonts/s3_cn.ttf" size 24 * persistent.scale_factor
                        text "英语课开始后会显示当前剩余答案；猜人小游戏会在正确选项下显示提示。机关盒原 Mod 仅提供第一面步骤。" font "fonts/s3_cn.ttf" size 23 * persistent.scale_factor
                        if scw_diagnostics:
                            text "部分攻略未能匹配当前游戏脚本，请提供 log.txt 排查。" font "fonts/s3_cn.ttf" size 23 * persistent.scale_factor color "#ffbc82"
