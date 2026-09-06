# Being a DIK S3 Episode 12：补充翻译提取器未收录的动态显示文本。
# 仅在中文语言下替换显示字符串，不修改剧情变量、返回值或游戏逻辑。

init 1001 python:
    import re as _s3_ep12_re
    _s3_ep12_prev_replace_text = config.replace_text

    _s3_ep12_cn_exact = {
        "Nikita": "Nikita",
        "Cathy": "Cathy",
        "Jade": "Jade",
        "Lynette": "Lynette",
        "Philip": "Philip",
        "Derek": "Derek",
        "I approached Nikita in class after learning her name from Derek. She seems to enjoy the attention she gets from me.":
            "Derek告诉我她的名字后，我在课堂上主动接近了Nikita。她似乎很享受我对她的关注。",
        "Hi, [name]. This is Cathy.": "嗨，[name]。我是Cathy。",
        "Hi! This was a surprise.": "嗨！真没想到你会发消息来。",
        "I hope my text didn't alarm you. I talked to Jade, and I wanted to reach out.":
            "希望这条消息没有吓到你。我和Jade聊过，所以想联系你。",
        "How so?": "怎么说？",
        "It's a conversation I'd rather have in person. Are you free later tonight? mphone_emoji_kiss":
            "这件事我更想当面谈。你今晚晚些时候有空吗？mphone_emoji_kiss",
        "I hope this isn't too direct or presumptuous, but I'm sort of in a relationship now. If the meeting is of that nature, I can't come.":
            "希望我没有太直接或自作多情，不过我现在算是有伴了。如果你想见我是为了那种事，我不能去。",
        "Oh? Jade didn't mention that. I'm sorry.": "哦？Jade没提过这件事。抱歉。",
        "Don't worry about it. It's recent, but yeah, I'm no longer available.":
            "别在意。也是最近才确定的，不过对，我现在已经不是单身了。",
        "Thanks for the honest answer, [name].": "谢谢你坦诚回答，[name]。",
        "I'm in town for science class all afternoon. I'm free after 6 p.m., maybe earlier.":
            "我下午一直在城里上科学课。晚上六点后有空，也可能更早。",
        "In town, you say. How about if you drop by my office after? It should be close by.":
            "你在城里啊。下课后来我办公室怎么样？应该离得不远。",
        "Sure! I'll call you when I get out of class.": "好！下课后我给你打电话。",
        "Splendid. I'll send you the address.": "太好了，我把地址发给你。",
        "Nora showed me her lab. What started out as a genuine interest in her work ended up with her on top of me.":
            "Nora带我参观了她的实验室。本来只是对她的工作感兴趣，最后她却骑到了我身上。",
        "You had sex with Nora in her lab in episode 12.": "你在第12集和Nora在她的实验室里发生了关系。",
        "Nora showed me her lab. She tried to rekindle something between us, but I shut it down.":
            "Nora带我参观了实验室，还想和我重燃旧情，但我拒绝了她。",
        "Nora showed me her lab. I was genuinely interested in learning what it was like to work in a lab environment.":
            "Nora带我参观了实验室，我也认真了解了实验室里的工作是什么样的。",
        "Was there a change of plans?": "计划有变吗？",
        "[name]? Hello?": "[name]？在吗？",
        "I'm guessing you got held up. I'm heading back home. Let's reschedule.":
            "你大概被什么事耽搁了。我先回家了，我们改天再约吧。",
        "Hi. Yeah, something else came up. I'm sorry, but I missed your calls.":
            "嗨。对，临时出了点事。抱歉，我没接到你的电话。",
        "I chose to have sex with Nora instead of going to visit Cathy.": "我没有去见Cathy，而是选择和Nora发生了关系。",
        "I rejected Cathy's advances at her office.": "我在Cathy的办公室拒绝了她的求欢。",
        "No way. You didn't!": "不会吧，你们没有！",
        "We're still doing it. His tongue feels amazing swirling around my clit. mphone_emoji_tongue":
            "我们还在继续。他的舌头绕着我的阴蒂打转，感觉太棒了。mphone_emoji_tongue",
        "Video chat?": "视频通话？",
        "If you're in private.": "只要你身边没人。",
        "You had sex with Cathy at her office while Jade was on a video call with her in episode 12.":
            "你在第12集和Cathy在她的办公室发生了关系，当时Jade正和她视频通话。",
        "I had sex with Cathy at her office as Jade was on a video call with her. It was like a virtual threesome.":
            "我在Cathy的办公室和她发生了关系，Jade则通过视频通话观看，简直像一场线上三人行。",
        "Lily wanted to stop rolling with me as it affected her job. I told her I was fine with it since I entered a relationship with Zoey.":
            "Lily觉得我们的炮友关系影响了工作，想就此结束。我告诉她没关系，因为我已经和Zoey开始交往。",
        "Lily wanted to stop rolling with me as it affected her job.":
            "Lily觉得我们的炮友关系影响了工作，想就此结束。",
        "Lily wanted to stop rolling with me as it affected her job. I told her I had feelings for her.":
            "Lily觉得我们的炮友关系影响了工作，想就此结束。我告诉她自己对她有感情。",
        "Lily wanted to stop rolling with me as it affected her job. I told her she should stick to her plan.":
            "Lily觉得我们的炮友关系影响了工作，想就此结束。我告诉她应该坚持自己的计划。",
        "Lily wanted to stop rolling with me as it affected her job. I told her I was fine with it since I didn't have any feelings for her.":
            "Lily觉得我们的炮友关系影响了工作，想就此结束。我告诉她没关系，因为我对她没有感情。",
        "Nick tried to convince me that the tri-betas were plotting behind the DIKs' backs.":
            "Nick试图说服我相信三贝塔正在背地里算计DIKs。",
        "I told Sandy that Nicole and I were dating when she wanted to have some fun with me.":
            "Sandy想和我找点乐子时，我告诉她自己正和Nicole交往。",
        "I told Sandy that Nicole and I were just fucking when she wanted to have some fun with me.":
            "Sandy想和我找点乐子时，我告诉她自己和Nicole只是炮友。",
        "Sandy wanted to take me to a private room for some fun, but I declined.":
            "Sandy想带我去私人房间找点乐子，但我拒绝了。",
        "Sandy wanted to have some fun, but I declined.": "Sandy想和我找点乐子，但我拒绝了。",
        "Sandy wanted to have some fun, but remembered that I didn't want to do that with her anymore.":
            "Sandy想和我找点乐子，但想起我已经不愿再和她做那种事。",
        "I had a threesome with Sandy and Tania in a private room at The Pink Rose.":
            "我在粉红玫瑰的私人房间里和Sandy、Tania玩了三人行。",
        "You had a threesome with Sandy and Tania in a private room at the Pink Rose in episode 12.":
            "你在第12集于粉红玫瑰的私人房间里和Sandy、Tania玩了三人行。",
        "Fancy Buffet": "豪华自助餐",
        "Decent Buffet": "普通自助餐",
        "Don't care": "无所谓",
        "Not Cheap Buffet": "不要廉价自助餐",
        "Card Game": "纸牌游戏",
        "Fireworks": "烟花表演",
        "Some Fireworks": "少量烟花",
        "Anything": "都可以",
        "According to Mom's diary, Dad punched my grandpa when he was fired from his job.":
            "根据妈妈的日记，爸爸失业时一拳打了外公。",
        "Mom was told to stop dating Dad, but she wouldn't.": "妈妈被要求和爸爸分手，但她不肯。",
        "I helped Tommy when he had a medical emergency. He told me about his diabetes, and it explained a lot.":
            "Tommy突发病情时，我帮了他。他告诉我自己患有糖尿病，也让我明白了很多事。",
        "Rusty told me that Tommy started the DIKs' secret code as a way to not have people mock him for his diabetes.":
            "Rusty告诉我，Tommy创立DIKs暗语，是为了不让别人拿他的糖尿病取笑他。",
        "Professor Hoff watched me closely during the finals.": "霍夫教授在期末考试时一直严密盯着我。",
        "Derek accidentally registered for another Gender Studies class.": "Derek不小心又选了一门性别研究课。",
        "Nicole dumped me after talking to Sandy about my recent visit to The Pink Rose.":
            "Nicole和Sandy谈过我最近去粉红玫瑰的事后，甩了我。",
        "I told Nicole about Zoey, and she was upset that I hadn't told her sooner.":
            "我把Zoey的事告诉了Nicole，她因为我没有早点坦白而生气。",
        "Nicole asked me out for a date after the finals.": "期末考试后，Nicole约我出去约会。",
        "The girls started distancing themselves from me. Maya at least acknowledged me.":
            "女孩们开始疏远我，至少Maya还愿意理我。",
        "The girls started distancing themselves from me.": "女孩们开始疏远我。",
        "Isabella wasn't very chatty with me after the finals.": "期末考试后，Isabella不太愿意和我说话。",
        "You had sex with Nicole in episode 12.": "你在第12集和Nicole发生了关系。",
        "I got high together with Nicole during our date. We ended up having sex on her couch.":
            "我和Nicole约会时一起嗨了起来，最后在她的沙发上发生了关系。",
        "I ditched Nicole to spend the night together with Quinn.": "我甩下Nicole，选择和Quinn共度一夜。",
        "I ditched Quinn to spend the night together with Nicole.": "我甩下Quinn，选择和Nicole共度一夜。",
        "You had sex with Quinn in your room in episode 12.": "你在第12集和Quinn在自己的房间里发生了关系。",
        "Quinn surprised me in my room. After having sex, she shared what she had been up to. She reassured me that she was safe, but what she told me bothered me.":
            "Quinn突然出现在我的房间。做爱后，她告诉我最近都做了什么。她保证自己很安全，但那些话还是让我很不安。",
        "Tommy gave me a shirt for Christmas and told me he appreciated me. It was the nicest thing he ever did for me.":
            "Tommy送了我一件衬衫作圣诞礼物，还说很感谢我。这是他对我做过最贴心的事。",
        "I told the DIKs that I didn't want to share my room with new DIKs.":
            "我告诉DIKs们，自己不想和新加入的DIKs共用房间。",
        "I stayed out of the conversation when the DIKs talked about sharing rooms with new DIKs.":
            "DIKs们讨论和新人共用房间时，我没有表态。",
        "I offered to share a part of my room with a new DIK if it was needed.":
            "如果有需要，我愿意把房间的一部分让给新加入的DIK。",
        "Josy invited me to her mom's place during winter break. She wanted me to meet her mom, even though it felt weird that Maya couldn't come with us.":
            "Josy邀请我寒假去她妈妈家。她想让我见见她妈妈，尽管Maya不能同行让这件事显得有些奇怪。",
    }

    def _s3_ep12_cn_active():
        try:
            return getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            return False

    def _s3_ep12_cn_replace_text(s):
        if _s3_ep12_prev_replace_text is not None:
            s = _s3_ep12_prev_replace_text(s)
        if not _s3_ep12_cn_active():
            return s
        s = _s3_ep12_cn_exact.get(s, s)
        s = _s3_ep12_re.sub(r'^(\{size=-\d+\})Stick to your guns(\{/size\})$', r'\1坚持立场\2', s)
        s = _s3_ep12_re.sub(r'^(\{size=-\d+\})Stay out of it(\{/size\})$', r'\1不掺和\2', s)
        s = _s3_ep12_re.sub(r'^(\{size=-\d+\})Offer a part of your room(\{/size\})$', r'\1让出一部分房间\2', s)
        return s

    config.replace_text = _s3_ep12_cn_replace_text
