# Being a DIK Season 3 - 简体中文运行时兼容与可见文本补漏层
# 目标版本：Steam 0.12.2.1
# 只影响字体、语言选择和最终显示文本；不修改存档键、剧情变量或 label。

define config.default_language = "schinese"

init 999 python:
    _s3_cn_font = "fonts/s3_cn.ttf"

    _s3_cn_fonts = [
        "ApeMount.ttf",
        "Audrey-Bold.otf",
        "Creepster-Regular.ttf",
        "DejaVuSans.ttf",
        "Museo500.otf",
        "Precious.ttf",
        "Redressed.ttf",
        "Roboto-Regular.ttf",
        "bradhitc.ttf",
        "briarwood_heavy_font.ttf",
        "cabin-regular.ttf",
        "candara.ttf",
        "centurygothicbold.ttf",
        "centurygothicregular.ttf",
        "collegiate.ttf",
        "daisy.ttf",
    ]

    for _s3_cn_font_name in _s3_cn_fonts:
        for _s3_cn_font_source in (_s3_cn_font_name, "fonts/" + _s3_cn_font_name):
            for _s3_cn_bold in (False, True):
                for _s3_cn_italic in (False, True):
                    config.font_replacement_map[
                        (_s3_cn_font_source, _s3_cn_bold, _s3_cn_italic)
                    ] = (_s3_cn_font, _s3_cn_bold, _s3_cn_italic)


init 1005 python:
    _s3_cn_global_previous_replace_text = config.replace_text

    # 标准翻译模板无法提取的 screen/text/show text。全部采用严格整串匹配。
    _s3_cn_global_exact = {
        # 第二季存档导入
        "Load a save from Season 2": "从第二季导入存档",
        "These are your saves from the end of Season 2. If you don't see any saves, you need to go back to Season 2 and choose which saves to transfer.": "这里显示第二季结尾导出的存档。如果没有看到存档，请返回第二季并选择要转移的存档。",
        "{color=007db5}For safety reasons, you cannot delete saves from here. Please manage your saves at the end of Season 2.{/color}": "{color=007db5}为确保安全，此处不能删除存档。请在第二季结尾管理转移存档。{/color}",
        "For safety reasons, you cannot delete saves from here. Please manage your saves at the end of Season 2.": "为确保安全，此处不能删除存档。请在第二季结尾管理转移存档。",
        "Loading Steam save data - Click to change source": "正在读取 Steam 存档数据——点击切换来源",
        "Loading Patreon/GOG save data - Click to change source": "正在读取 Patreon/GOG 存档数据——点击切换来源",
        "{size=-%d}Click here to overwrite save file{/size}": "{size=-%d}点击此处覆盖存档{/size}",
        "Click to name your save": "点击为存档命名",
        "{color=#ff0000}Incompatible save{/color}": "{color=#ff0000}不兼容的存档{/color}",
        "In library": "已在库中",
        "Available now": "现已可用",
        "Installed": "已安装",
        "Not installed": "未安装",
        "Not owned": "未拥有",
        "Other game": "其他游戏",

        # 通用界面与手机
        "Free roam": "自由活动",
        "Complete the tasks in the Tasks app": "完成任务应用中的任务",
        "Music - Now Playing": "音乐——正在播放",
        "Minimize Music app": "最小化音乐应用",
        "Home Screen Bar: Hide": "主屏栏：隐藏",
        "Home Screen Bar: Show": "主屏栏：显示",
        "Filter by genre: %s": "按流派筛选：%s",
        "All songs": "全部歌曲",
        "Set as wallpaper": "设为壁纸",
        "Set as current wallpaper": "设为当前壁纸",
        "Accept gift": "接受礼物",
        "Try again": "重试",
        "New Game": "新游戏",
        "High Scores": "最高分",
        "High scores": "最高分",
        "General": "综合",
        "Gallery": "相册",
        "Golden Phone Skin": "金色手机皮肤",
        "Jacob's Art Shop": "雅各布的艺术商店",
        "Level %d/3": "等级 %d/3",
        "Budget:": "预算：",
        "Next tip": "下一条提示",

        # 奖励页
        "Rewards": "奖励",
        "Special renders are unlocked by finding hidden magazines during free roam events and by winning mini-games.\nPatrons help decide who is featured in the special renders.": "在自由活动中找到隐藏杂志或赢得小游戏，即可解锁特殊渲染图。\n赞助者可以参与决定特殊渲染图中的角色。",
        "2D Art shop": "2D 艺术商店",
        "Drawing": "绘画",
        "English Class": "英语课",
        "English Finals": "英语期末考试",
        "Math Class": "数学课",
        "Math Finals": "数学期末考试",
        "Science Class": "科学课",
        "Faculty party": "教职工派对",
        "{size=-5}Fighting competition{/size}": "{size=-5}格斗比赛{/size}",
        "Interlude": "间章",
        "Interlude - Vault": "间章——保险库",

        # 搏击小游戏
        "Fight": "战斗",
        "Fight again": "再战一次",
        "Choose your opponent": "选择对手",
        "Difficulty": "难度",
        "Health": "生命值",
        "Block": "格挡",
        "Counter": "反击",
        "Get ready": "准备好",
        "You win!": "你赢了！",
        "You lose!": "你输了！",
        "COUNTER!!!": "反击！！！",
        "{color=b7b7b7}Normal Difficulty{/color}": "{color=b7b7b7}普通难度{/color}",
        "{color=870600}Hard Difficulty{/color} {color=#ffffff}|{/color} Lower Difficulty": "{color=870600}困难难度{/color} {color=#ffffff}|{/color} 降低难度",
        "{size=-%d}Click to permanently lower the difficulty{/size}": "{size=-%d}点击可永久降低难度{/size}",
        "{size=-%d}Unknown{/size}": "{size=-%d}未知{/size}",
        "{size=-%d}Progress further in Brawler to unlock.{/size}": "{size=-%d}继续推进搏击小游戏即可解锁。{/size}",
        "{size=-%d}Flurry{/size}": "{size=-%d}连击{/size}",
        "{size=-%d}Crippling leg kick{/size}": "{size=-%d}致残扫腿{/size}",
        "{size=-%d}High kick combo{/size}": "{size=-%d}高踢连招{/size}",
        "{color=1df400}Win{/color} / {color=bb433b}Lose{/color}": "{color=1df400}胜{/color} / {color=bb433b}负{/color}",
        "{color=e10d00}Highest {font=fonts/ApeMount.ttf}Rage{/font}{/color}": "{color=e10d00}最高{font=fonts/ApeMount.ttf}怒气{/font}{/color}",
        "{color=00b0ff}Highest Damage{/color}": "{color=00b0ff}最高伤害{/color}",
        "{i}New Record!{/i}": "{i}新纪录！{/i}",

        # 啤酒乒乓
        "Arc shot": "弧线球",
        "Fastball ": "快速球 ",
        "Bounce shot": "反弹球",
        "Rest\n{size=-%d}{color=fe9416}Recover +3 AP{/color}{/size}": "休息\n{size=-%d}{color=fe9416}恢复 3 点行动力{/color}{/size}",
        "{color=ffffff}%d cups{/color}": "{color=ffffff}%d 杯{/color}",

        # 科学小游戏
        "Science 101": "科学基础",
        "{size=+%d}Science 101{/size}": "{size=+%d}科学基础{/size}",
        "Add to": "加入",
        "Add to beaker": "加入烧杯",
        "Add to round flask": "加入圆底烧瓶",
        "Stir settings": "搅拌设置",
        "Turn in": "提交",
        "Discard": "丢弃",
        "Cancel": "取消",
        "Liquids": "液体",
        "Salts": "盐类",
        "Volumetric flask": "容量瓶",
        "Round flask": "圆底烧瓶",
        "Bunsen burner": "本生灯",
        "Burner": "燃烧器",
        "Fast": "快速",
        "Medium": "中速",
        "How much do you want to measure?": "你想量取多少？",
        "Retry ({color=bb433b}-5 seconds{/color})": "重试（{color=bb433b}-5 秒{/color}）",
        "Experiment 1": "实验 1",
        "Experiment 2": "实验 2",
        "Experiment 3": "实验 3",

        # 派对策划与鱼缸
        "Activities": "活动",
        "Guests": "宾客",
        "Items": "物品",
        "Trash Cans": "垃圾桶",
        "Skip Tutorial": "跳过教程",
        "Connections": "人脉",
        "Crowdfunding": "众筹",
        "Finger Food": "手抓小食",
        "Jello Shots": "果冻酒",
        "Black Friday": "黑色星期五",
        "DIK Party": "DIK 派对",
        "Easy to Please": "容易满足",
        "Hard to Let Down": "不易失望",
        "Multiplier Madness": "倍率狂潮",
        "Below Budget": "低于预算",
        "Fish Tank": "鱼缸",
        "{u}Fish (%d){/u}": "{u}鱼（%d）{/u}",
        "{color=fe67b2}Female{/color}: %d": "{color=fe67b2}雌性{/color}：%d",
        "{color=39e4db}Male{/color}: %d": "{color=39e4db}雄性{/color}：%d",
        "{color=1df400}Young{/color}: %d": "{color=1df400}幼鱼{/color}：%d",
        "{color=f72400}Dead{/color}: %d": "{color=f72400}死亡{/color}：%d",
        "{color=ffc27b}Sick{/color}: %d": "{color=ffc27b}生病{/color}：%d",
        "{color=ffc015}Air Pump{/color}": "{color=ffc015}气泵{/color}",
    }

    _s3_cn_route_names = {
        "Story": "主线",
        "Free roam": "自由活动",
        "Vault": "保险库",
        "Pack Quest": "收集任务",
        "Others": "其他人",
        "Locked": "未解锁",
        "Jill": "吉尔",
        "Josy": "乔西",
        "Maya": "玛雅",
        "Josy & Maya": "乔西与玛雅",
        "Isabella": "伊莎贝拉",
        "Sage": "赛琪",
        "Zoey": "佐伊",
        "Quinn": "奎恩",
        "Camila": "卡米拉",
        "Lily": "莉莉",
        "Nicole": "妮可",
        "Nora": "诺拉",
        "Riona": "里奥娜",
        "Jade": "杰德",
        "Cathy": "凯茜",
        "Madame": "夫人",
        "Becky": "贝姬",
        "Elena": "埃琳娜",
        "Lynette": "莉奈特",
        "Melanie": "梅兰妮",
        "Sarah": "莎拉",
        "Tara": "塔拉",
        "Tiffani": "蒂芙妮",
        "Sally": "莎莉",
        "Sandy & Tania": "桑迪与塔妮娅",
        "Sage & Camila": "赛琪与卡米拉",
        "Lily & Nicole": "莉莉与妮可",
        "Sarah & Mel": "莎拉与梅兰妮",
        "CUM-petition": "射精大赛",
        "Card Game": "纸牌游戏",
        "Beer Pong": "啤酒乒乓",
        "Brawler": "搏击",
        "Puzzle Box": "谜盒",
        "DIKmas": "DIK 圣诞节",
    }

    _s3_cn_reward_names = {
        "Isabella": "伊莎贝拉",
        "Jill": "吉尔",
        "Josy": "乔西",
        "Maya": "玛雅",
        "Sage": "赛琪",
        "Zoey": "佐伊",
        "Lily": "莉莉",
        "Camila": "卡米拉",
        "Mixed": "混合",
        "2D Art": "2D 艺术",
    }

    def _s3_cn_global_replace_text(s):
        if _s3_cn_global_previous_replace_text is not None:
            s = _s3_cn_global_previous_replace_text(s)

        try:
            _s3_cn_active = getattr(renpy.store._preferences, "language", None) == "schinese"
        except Exception:
            _s3_cn_active = False

        if not _s3_cn_active:
            return s

        if s in _s3_cn_global_exact:
            return _s3_cn_global_exact[s]

        # 相册和奖励页统一采用“Ep N - 类别/人物”格式。
        if s.startswith("Ep ") and " - " in s:
            _s3_cn_left, _s3_cn_right = s.split(" - ", 1)
            _s3_cn_ep = _s3_cn_left[3:]
            if _s3_cn_ep.isdigit() and _s3_cn_right in _s3_cn_route_names:
                return "第%s集——%s" % (_s3_cn_ep, _s3_cn_route_names[_s3_cn_right])

        # 奖励页标题和带颜色标签的人名计数：只在奖励专用字符串中替换。
        if s.startswith("Rewards - "):
            s = s.replace("Rewards - ", "奖励——", 1)
            for _s3_cn_en, _s3_cn_zh in _s3_cn_reward_names.items():
                s = s.replace(_s3_cn_en, _s3_cn_zh)
            return s

        if "persistent.rew_" in s:
            for _s3_cn_en, _s3_cn_zh in _s3_cn_reward_names.items():
                s = s.replace(_s3_cn_en, _s3_cn_zh)
            return s

        # 导入存档信息为动态格式化文本，必须保留实际数值与日期。
        if s.startswith("Affinity: ") and "\nChosen road: " in s and "\nDate: " in s:
            s = s.replace("Affinity: ", "倾向：", 1)
            s = s.replace("\nChosen road: ", "\n选择路线：", 1)
            s = s.replace("\nDate: ", "\n日期：", 1)
            for _s3_cn_en, _s3_cn_zh in _s3_cn_route_names.items():
                s = s.replace(_s3_cn_en, _s3_cn_zh)
            return s

        return s

    config.replace_text = _s3_cn_global_replace_text
