# Being a DIK S3 间章：补充 Ren'Py 翻译提取器未收录的动态显示文本。
# 只作用于中文语言；不改变选项返回值、剧情变量或游戏逻辑。

init 999 python:
    _s3_interlude_prev_replace_text = config.replace_text

    _s3_interlude_cn_exact = {
        # 间章人物名与说话人身份（Character 名称不会自动进入翻译模板）。
        "Zoey": "Zoey",
        "Emma": "Emma",
        "Bret": "Bret",
        "Alison": "Alison",
        "Jonah": "Jonah",
        "Instructor": "教练",
        "Doris": "Doris",
        "Bartender": "酒保",
        "Owner": "老板",
        "Customer": "顾客",
        "Jenna": "Jenna",
        "Priest": "神父",
        "Stepdad": "继父",
        "Conductor": "列车员",
        "Sage": "Sage",

        # 自定义双选项界面。
        "Encourage him": "鼓励他",
        "Such a girl!": "真像个小姑娘！",
        "Is she all right?": "她没事吧？",
        "What the fuck!?": "搞什么鬼！？",
        "Fuck school!": "去他的学校！",
        "Talk back": "顶嘴",
        "Apologize": "道歉",
        "Not your business": "不关你的事",
        "Nothing": "没什么",
        "What a snitch": "真会告密",
        "You're right": "你说得对",
        "Blowjob": "口交",
        "Eat me": "舔我",
        "Continue": "继续",
        "Retry": "重试",
        "Get ready!": "准备！",
        "Doggystyle": "后入式",
        "Cum inside": "射在里面",
        "Cum outside": "射在外面",
        "Answer": "回答",
        "Ignore": "不理会",
        "Appreciate it": "表示感谢",
        "Don't have to": "不必这样",
        "LOL! Asshole!": "哈哈！混蛋！",
        "Don't scare me": "别吓我",
        "You ok?": "你还好吗？",
        "I'm excited!": "我太兴奋了！",
        "I am 21": "我满21岁了",
        "Love your tats": "喜欢你的纹身",
        "Too many tattoos": "纹身太多了",
        "Joke": "开个玩笑",
        "Sounds dope": "听起来很酷",
        "Um... Why?": "呃……为什么？",
        "Kinda personal": "有点私人",
        "Yes": "可以",
        "It could be better": "还可以更好",
        "It sucks": "烂透了",
        "Ignore him": "不理他",
        "Sure do": "当然",
        "Show concern": "表示关心",
        "Good, huh?": "不错吧？",
        "Yeah": "是啊",
        "Yeah.": "嗯。",
        "Pay me for it": "给我算工钱",
        "Sounds fun": "听起来挺有趣",
        "Had better ones": "有过更舒服的",
        "Back hurts": "背疼",
        "I'm fine": "我没事",
        "I'm pissed": "我很火大",
        "Right...": "也是……",
        "Not for everyone": "不是人人都适合",
        "Encourage her": "鼓励她",
        "Help him out": "帮他说话",
        "Don't look at me": "别看我",
        "Nope": "没有",
        "I can tell": "看得出来",
        "Which ones?": "哪些？",
        "Fuck": "做爱",
        "A guy": "一个男人",
        "A girl": "一个女人",
        "Jonah": "Jonah",
        "Bret": "Bret",
        "Calm her down": "让她冷静下来",
        "Take her phone": "抢走她的手机",
        "I didn't fuck him": "我没跟他上床",
        "It is too late": "已经太晚了",
        "Thank you": "谢谢",
        "Get revenge": "报复她",

        # 拍照玩法悬停提示。
        "Lower-body shot": "下半身特写",
        "Full-body shot": "全身照",
        "Upper-body shot": "上半身特写",
        "Tit-focused shot": "胸部特写",
        "Artistic shot": "艺术照",
        "Ass-focused shot": "臀部特写",
        "Side shot": "侧面照",
        "Front shot": "正面照",
        "Close-up shot": "近照",

        # 短信界面：原脚本直接向列表写入英文，未进入 strings.rpy。
        "Train's rolling fine. It's a start.": "火车开得挺顺利。算是个好开头。",
        "Now would be a good time to remember that you forgot to pack something.": "现在正适合突然想起自己漏带了什么。",
        "LOL! Don't scare me like that!": "哈哈！别这么吓我！",
        "As long as I've got my wallet, phone, and notebook, anything that I missed I can live without.": "只要钱包、手机和笔记本都在，其他漏带的东西没有也能活。",
        "Ok.": "好。",
        "I'll probably freak out if my charger's missing, though...": "不过，要是没带充电器我大概会抓狂……",
        "I guess I can get a new one if I forgot it.": "真忘了的话，再买一个就是了。",
        "I'm fine. Kinda difficult to type right now.": "我没事。现在不太方便打字。",
        "Not home yet?": "还没到家？",
        "I'm walking.": "我在走路。",
        "Haha. You never could do two things at once.": "哈哈，你果然还是没法一心二用。",
        "I'm so fucking excited about this!": "我他妈太兴奋了！",
        "I'm happy for you.": "真替你高兴。",
        "Thanks. I knew you'd understand. You're the best.": "谢了。我就知道你会理解。你最好了。",
        "Talk soon!": "回头聊！",
        "l8r sk8r": "回见，滑板仔",
        "The train didn't derail. I'm safe and sound, livin' life in SD.": "火车没脱轨。我平安到了，已经开始在圣迭戈生活了。",
        "That's good news. Found the hostel ok?": "那就好。旅舍找到了吗？",
        "Yep. It's a hostel, all right - or was it a prison? I keep forgetting since I have to wear this fucking wristband when I'm here.": "找到了。确实是旅舍——还是监狱来着？住这儿还得戴着这条该死的手环，我老是分不清。",
        "A wristband? What for?": "手环？干什么用的？",
        "Drinking rules. Green wristband says you can party. Red says your life still sucks. Mine's red.": "喝酒规定。绿手环代表可以尽情玩，红手环代表你的日子还是苦得要命。我的就是红的。",
        "You'll figure it out.": "你会想到办法的。",
        "True that.": "确实。",
        "How's the hostel?": "旅舍怎么样？",
        "Cleaner than both of our rooms. It has a weird smell, though.": "比我们俩的房间都干净。不过有股怪味。",
        "I have to share the room with whoever drops by. Kinda lame. Need to find something more...solitary.": "不管谁来入住，我都得跟人家同住一间房。挺烦的。得找个更……私密的地方。",
        "It's your first day. I'm sure you will.": "才第一天。你肯定能找到的。",
        "Aight. I'm gonna check out the neighborhood. l8r sk8ter": "行吧。我去附近转转。回见，滑板仔。",
        "Had a rad day. Started my class and landed a job - maybe.": "今天超棒。上了第一堂课，还找到了份工作——也许吧。",
        "Is surfing just as easy as skating?": "冲浪也和滑板一样容易吗？",
        "Since when did you think skating is easy? You can barely stand on a board.": "你什么时候觉得滑板容易了？你连在板上站稳都费劲。",
        "I meant for you. :P": "我是说对你而言。:P",
        "Haven't gotten to the good stuff yet, but next lesson, it will happen. And LOL, I missed your fake emojis.": "还没学到精彩的部分，不过下节课就该来了。还有，哈哈，我还挺想念你那些假表情的。",
        "I should get a wetsuit and a board of my own, too. They said you could borrow one, but I'd rather have my own gear.": "我也该买套潜水服和自己的冲浪板。他们说可以借，但我还是想用自己的装备。",
        "Sounds like you've got a lot going on for you...": "听起来你那边过得挺充实……",
        "Sure do. I like it so far.": "当然。目前为止我挺喜欢这里的。",
        "It's past bedtime over here, so...": "我这边已经过了睡觉时间，所以……",
        "Damn. Right. I forgot. Goodnight!": "靠，对哦，我忘了。晚安！",
        "What's up with the three dots?": "那三个省略号是什么意思？",
        "Nothing. It's past bedtime over here, so...": "没什么。我这边已经过了睡觉时间，所以……",
        "Zoey. You better check Rooster.": "Zoey，你最好看看 Rooster。",
        "Sup, Dragon Lord. What about it?": "怎么了，龙王？Rooster 怎么了？",
        "Emma just posted something about you.": "Emma刚发了些和你有关的东西。",

        # Rooster 评论浮层。
        "Wow! Is that you, Zoey?": "哇！这是你吗，Zoey？",
        "TITS!": "奶子！",
        "What a whore!": "真是个婊子！",
        "Slut!": "荡妇！",
        "A friend stealing your ex? That's disgusting!": "朋友抢你的前任？真恶心！",
        "Is it just me, or are those tits saggy for her age?": "只有我觉得她这年纪胸就有点下垂了吗？",
        "Haha! Oh my God! Zoey!": "哈哈！我的天啊！Zoey！",
    }

    # 带 {size} 标签的选项在 Ren'Py 7 系列里可能整串传入，也可能拆成片段。
    _s3_interlude_cn_fragments = (
        ("Nana is important!", "外婆更重要！"),
        ("Let him take control", "让他掌控"),
        ("Drink in my room", "在房间里喝"),
        ("Is that a problem?", "有问题吗？"),
        ("Discover our bodies", "探索彼此的身体"),
        ("What did Bret say?", "布雷特说了什么？"),
        ("Be a bigger person", "大度一点"),
    )

    def _s3_interlude_cn_active():
        try:
            return getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            return False

    def _s3_interlude_cn_replace_text(s):
        if _s3_interlude_prev_replace_text is not None:
            s = _s3_interlude_prev_replace_text(s)

        if not _s3_interlude_cn_active():
            return s

        if s in _s3_interlude_cn_exact:
            return _s3_interlude_cn_exact[s]

        for _src, _dst in _s3_interlude_cn_fragments:
            if _src in s:
                s = s.replace(_src, _dst)
        return s

    config.replace_text = _s3_interlude_cn_replace_text
