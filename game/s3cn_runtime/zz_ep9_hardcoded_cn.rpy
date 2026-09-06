# Being a DIK S3 Episode 9：补充 Ren'Py 翻译提取器未收录的动态显示文本。
# 仅在简体中文语言下替换显示字符串，不修改返回值、剧情变量或游戏逻辑。

init 999 python:
    _s3_ep9_prev_replace_text = config.replace_text

    _s3_ep9_cn_exact = {
        # 人物资料页标题。
        "Tommy": "Tommy",
        "Jade": "Jade",
        "Sage": "Sage",
        "Maya": "Maya",
        "Josy": "Josy",
        "Zoey": "Zoey",
        "Derek": "Derek",
        "Isabella": "Isabella",
        "Jill": "Jill",

        # 派对策划器中由列表动态生成的活动名称。
        "Body Shots": "人体酒杯",
        "Drinking Competition": "饮酒比赛",
        "Scary Stories": "恐怖故事会",
        "Haunted Mansion": "鬼屋",
        "CUM-petition": "射精大赛",
        "Don't care": "无所谓",
        "Any activity": "任意活动",

        # 姓氏输入框提示。
        "What is your last name?": "你姓什么？",

        # 手机统计与人物资料更新文本。
        "Tommy wanted to plan the party with me, but he's not doing what we agreed on.":
            "Tommy想和我一起策划派对，可他根本没按我们的约定办事。",
        "You had sex with Jade in her kitchen in episode 9.":
            "你在第 9 集里和Jade在她家的厨房做了爱。",
        "I fucked Jade in her kitchen while her family was at home.":
            "Jade的家人都在家时，我在厨房里和她做了爱。",
        "I resisted Jade in the kitchen of her home. Her family was in the other room, and it was too risky.":
            "我在Jade家的厨房拒绝了她。她的家人就在隔壁，风险太大了。",
        "Jade was mad at me for dating Sage. She thought it was too risky and wanted me to end our relationship. I told her I wasn't going to stop dating Sage.":
            "Jade因为我和Sage约会而生气。她觉得这样风险太大，要我结束这段关系，但我告诉她，我不会停止和Sage约会。",
        "Jade was mad at me for being Sage's friend. She thought it was too risky and wanted me to end our friendship. I told her I wasn't going to stop being her friend.":
            "Jade因为我和Sage来往而生气。她觉得这样风险太大，要我结束这段友谊，但我告诉她，我不会不再和Sage做朋友。",
        "Sage's last name is Morgan Burke...but she uses Morgan.":
            "Sage的全姓是摩根·伯克……但她平时只用摩根这个姓。",
        "Sage told me her dad wouldn't help Maya with her tuition.":
            "Sage告诉我，她爸爸不愿帮Maya解决学费问题。",
        "Maya didn't get any help from Stephen Burke.":
            "Maya没能从Stephen·伯克那里得到任何帮助。",
        "Zoey is back in town, and she tried to reach me on my old number... Dad lied and covered for what really happened.":
            "Zoey回来了，还试着拨打我的旧号码联系我……爸爸撒了谎，替我隐瞒了真相。",
        "Sage is creating troll accounts to fuck with Tybalt on Rooster. She seems to hate her brother. While I'm not surprised that someone would hate Tybalt, I'm a bit surprised that she would hate her brother.":
            "Sage在 Rooster 上注册小号捉弄Tybalt。她似乎很讨厌自己的哥哥。有人讨厌Tybalt并不奇怪，但连亲妹妹都这么讨厌他，倒让我有点意外。",
        "Sage recommended that Maya get legal help, and Josy told Maya she'd ask around for it.":
            "Sage建议Maya寻求法律援助，Josy也答应替Maya四处问问。",
        "When I met Zoey, I told her that I was mad at her.":
            "和Zoey见面时，我告诉她自己还在生她的气。",
        "When I met Zoey, I told her my feelings were all over the place.":
            "和Zoey见面时，我告诉她自己现在百感交集。",
        "I told Zoey my side of the story, and we both cried. I just can't let go of her. She's meant too much to me over the years. But I'm not ready to just forget about this last year.":
            "我把自己的感受告诉了Zoey，我们俩都哭了。我就是放不下她，这些年来她对我太重要了。但我还没准备好把过去这一年发生的事一笔勾销。",
        "I told Derek that Zoey is a better friend to me than he is.":
            "我告诉Derek，对我来说，Zoey是比他更好的朋友。",
        "I told Derek that he is a better friend to me than Zoey.":
            "我告诉Derek，对我来说，他是比Zoey更好的朋友。",
        "I broke up with Jill. Well, we weren't a couple, but I told her I couldn't date her anymore, and she didn't take it well.":
            "我和Jill分手了。严格来说，我们还不是情侣，但我告诉她不能再继续约会，她很难接受。",
        "I opened up to Jill about my feelings for Bella. It was awful breaking her heart like that, but I had to be honest with her.":
            "我向Jill坦白了自己对贝拉的感情。这样伤透她的心让我非常难受，但我必须对她诚实。",
        "When I broke up with her, Jill tried to kiss me, and I kissed her back. Maybe it was stupid, but I have feelings for her too.":
            "分手时，Jill试着吻我，而我也回吻了她。也许这样做很蠢，可我对她同样有感情。",
        "I opened up to Jill about my feelings for Bella. It was weird, but I hope that Jill will understand our relationship someday.":
            "我向Jill坦白了自己对贝拉的感情。场面很尴尬，但我希望有一天Jill能理解我们的关系。",
        "I talked to Jill about our relationship. It went well, and we left as friends.":
            "我和Jill谈了彼此的关系。谈得很顺利，最后我们仍然是朋友。",
        "Bella talked to Jill, but it turned into a fight. It made Bella very sad.":
            "贝拉去找Jill谈话，最后却吵了起来，这让贝拉非常难过。",
        "I had sex with Bella in my room after the Halloween party, and she spent the night.":
            "万圣节派对结束后，我和贝拉在自己的房间做了爱，她也留宿了一晚。",
        "You had sex with Bella after the Halloween party in episode 9.":
            "你在第 9 集的万圣节派对后和贝拉做了爱。",
        "Jill wanted me to take an STD test before continuing to have sex without a condom.":
            "Jill希望我先做性病检测，再继续和她进行无套性爱。",
        "Jill didn't want to have sex without a condom, so we ended up trying new things together.":
            "Jill不愿意无套做爱，所以我们一起尝试了其他新玩法。",
        "You had fun with Jill on her bed in episode 9.":
            "你在第 9 集里和Jill在她的床上亲热了一番。",
        "Jill told me about her father. Apparently, the death of her sister changed him.":
            "Jill向我说起了她的父亲。显然，她姐姐的死彻底改变了他。",
        "I told Jill about Matthew cheating on Bianca with Olivia.":
            "我告诉Jill，Matthew背着Bianca和Olivia偷情。",
        "I didn't tell Jill about Matthew cheating on Bianca with Olivia.":
            "我没有告诉Jill，Matthew背着Bianca和Olivia偷情。",
        "I had sex with Jill after the Halloween party, and she stayed the night.":
            "万圣节派对结束后，我和Jill做了爱，她也留宿了一晚。",
        "You had sex with Jill after the Halloween party in episode 9.":
            "你在第 9 集的万圣节派对后和Jill做了爱。",
        "I went with Maya into the fitting booth.":
            "我陪Maya进了试衣间。",
        "I went with Josy into the fitting booth.":
            "我陪Josy进了试衣间。",

        # 本批新增：自由活动任务提示、地图房间名和艺术解锁条件。
        "Task: Investigate the blackout.": "任务：调查停电原因。",
        "- Got episode 8 lewd scene": "- 已解锁第8集色情场景",
        "- Got episode 8 solo lewd scene": "- 已解锁第8集单人色情场景",
        "- Got episode 6 lewd scene": "- 已解锁第6集色情场景",
        "- Played the Interlude": "- 已游玩间章",
        "Your room": "你的房间",
        "Derek's room": "Derek的房间",
        "Dining room": "餐厅",
        "Jacob's room": "Jacob的房间",
        "Jamie's room": "Jamie的房间",
        "John Boy's room": "John Boy的房间",
        "Leon's room": "Leon的房间",
        "Main party room": "派对主厅",
        "Nick's room": "Nick的房间",
        "Right hallway": "右侧走廊",
        "Left hallway": "左侧走廊",
        "Rusty's room": "Rusty的房间",
        "Tommy's room": "Tommy的房间",
        "Upper main room": "楼上主厅",
        "Find your sword": "找到你的剑",
        "Talk to Jamie": "和Jamie交谈",
        "Talk to Sally": "和Sally交谈",
        "Talk to Rusty": "和Rusty交谈",
        "Talk to the group outside your room": "和你房间外的众人交谈",
        "Talk to Zoey": "和Zoey交谈",
        "Talk to Derek": "和Derek交谈",
        "Talk to the girls": "和姑娘们交谈",
        "Text Maya": "给Maya发消息",
        "Text Josy": "给Josy发消息",
        "Text Jill": "给Jill发消息",
        "Talk to Sage": "和Sage交谈",
        "Talk to Josy": "和Josy交谈",
        "Talk to Quinn": "和Quinn交谈",
        "Take picture with Riona": "和Riona合影",
        "Talk to Sarah": "和Sarah交谈",
        "Restock cakes": "补充蛋糕",
        "Give Jill a tour": "带Jill参观",
        "Check the dining room": "查看餐厅",
        "Talk to Jill": "和Jill交谈",
        "Dance with Sage": "和Sage跳舞",
        "Dance with Josy & Maya": "和Josy、Maya跳舞",
        "Take picture with Bella": "和Bella合影",
        "Have Bella talk to Jill": "让Bella和Jill谈谈",
        "Dance with Camila": "和Camila跳舞",
        "Attend scary stories": "参加恐怖故事会",
        "Try the Haunted Mansion": "体验鬼屋",
        "Pass time": "消磨时间",
        "Check upstairs": "查看楼上",
        "Talk to Nicole": "和Nicole交谈",
        "Find Becky": "寻找Becky",
        "Talk to Heather": "和Heather交谈",
        "Talk to Josy & Maya": "和Josy、Maya交谈",
        "Help John Boy": "帮助John Boy",
        "Find Sandy": "寻找Sandy",
        "Check Jamie's room": "查看Jamie的房间",
        "Find Riona": "寻找Riona",
        "Check Rusty's room": "查看Rusty的房间",
        "Talk to the ghost": "和幽灵交谈",

        # 本批新增：Zoey手机聊天记录。
        "Hey, [name]. I got your new number from Neil. Hit me up when you have time for it. /Zoey":
            "嘿，[name]。我从Neil那里拿到了你的新号码。有空时联系我。/Zoey",
        "Hey. What's up?": "嘿，怎么了？",
        "Dude... Hey!!! mphone_emoji_smile": "老兄……嘿！！！mphone_emoji_smile",
        "I don't wanna have this chat over text. Can we meet up somewhere? You know, when you got time to kill. When or where, that's up to ya.":
            "我不想用短信聊这件事。我们能找个地方见面吗？等你有空的时候。时间地点都由你定。",
        "Tomorrow afternoon, maybe? I don't know where, though.": "明天下午怎么样？不过我不知道该约在哪里。",
        "Awesome! How about 2 p.m. at that park we used to go to? You know, the one on 5th?":
            "太好了！下午2点，在我们以前常去的公园怎么样？就是第五街那个。",
        "Ok.": "好。",
        "Great. Tomorrow, then. L8r Sk8r": "太好了，那就明天见。回见啦，小滑手。",
        "Thanks for hearing me out today. I knew it was gonna be emotional and shit, but I didn't expect to cry that much.":
            "谢谢你今天愿意听我说完。我知道肯定会他妈很伤感，可没想到自己会哭成那样。",
        "Thanks for hearing me out today. I knew it was gonna be emotional, but I didn't expect to cry that much.":
            "谢谢你今天愿意听我说完。我知道肯定会很伤感，可没想到自己会哭成那样。",
        "Yeah.": "嗯。",
        "It felt good to finally say those things out loud to you. Don't worry about the crying. I know you only do that when things matter a lot to you.":
            "终于能亲口把那些话告诉你，感觉很好。别在意哭出来，我知道只有遇到对你特别重要的事，你才会这样。",
        "Halloween's closing in. Were you serious about that invite?": "万圣节快到了。之前的邀请是认真的吗？",
        "Yeah, you're welcome to come if you want to.": "当然，你想来就尽管来。",
        "I'm coming, for sure. Things are different in this town. It gets pretty boring when there aren't many left.":
            "我肯定会去。这座镇子已经和以前不同了，没剩下多少熟人时真的很无聊。",
        "I felt the same this summer. So, no one's left?": "今年夏天我也有同感。所以，大家全都走了？",
        "Debbie's still around. But she's working full-time at Shoes and Laces these days.":
            "Debbie还在，不过她最近一直在Shoes and Laces做全职。",
        "Say hi from me the next time you see her.": "下次见到她时替我问好。",
        "Sure thing.": "没问题。",
        "Dude! Did you see the news?": "老兄！你看到新闻了吗？",
        "No?": "没有，怎么了？",
        "ShitFaced are releasing a new album!": "ShitFaced要发新专辑了！",
        "No way! It's been what? 6 years since their last one?": "不会吧！他们上一张专辑是多少年前了？6年？",
        "Yeah, this is amazing! There's a teaser video of it. I'll link you on Rooster!":
            "对啊，太棒了！还有一段预告视频。我会在Rooster上把链接发给你！",
        "Do you think this means they'll tour again?": "你觉得这代表他们会重新巡演吗？",
        "If they do, I'm SO there! And you're coming too!": "要是他们巡演，我绝对会去！你也必须一起！",
        "I gotta go. Talk another time.": "我得走了，改天再聊。",
        "Sure! mphone_emoji_laugh": "当然！mphone_emoji_laugh",
        "I'd love to see them live before I die.": "真想在死前看一次他们的现场演出。",
        "Before YOU die? Haha! I'm pretty sure they'll be dead a long time before you go. They're getting old. mphone_emoji_laugh":
            "在你死前？哈哈！他们年纪都大了，肯定比你早死很久。mphone_emoji_laugh",
        "Did you send the link?": "链接发了吗？",
        "So, Floyd's still a pain in the ass.": "话说，Floyd还是那么讨人嫌。",
        "That doesn't surprise me. What's he up to now?": "一点也不意外。他这次又干什么了？",
        "He fucking smirks and laughs every time Mom mentions I'm back to living at home. Almost as if he's telling me \"Told ya it wouldn't work\".":
            "妈妈每次提起我搬回家住，他都会他妈地坏笑，仿佛在说‘早告诉你行不通了’。",
        "That's annoying. How are you handling it?": "真烦人。你是怎么应付他的？",
        "I tell him to go fuck himself. What else can I do?": "我叫他滚去自个儿玩蛋。还能怎么办？",
        "I'd probably do that too.": "换成我大概也会这么做。",
        "Tell me about it...": "可不是嘛……",
        "You could try to turn the other cheek, maybe?": "也许你可以试着别和他计较？",
        "Nah. That wouldn't work.": "算了吧，那不会管用。",
        "I just ignore him. It still annoys me, but I'm not gonna show him that I care. That would just give him some weird satisfaction.":
            "我直接无视他。虽然还是很烦，但我不会让他看出自己在意，那只会给他一种莫名其妙的满足感。",
        "Yeah. Fuck him.": "对。去他的。",
        "Meh.": "切。",
        "I think that's a smart way of handling him.": "我觉得这样处理很明智。",
        "Yeah. Me too.": "嗯，我也这么觉得。",
        "Halloween's tomorrow. I sent you the directions on Rooster.": "明天就是万圣节。我已经在Rooster上把地址发给你了。",
        "Thanks, I just saw it. Sorry for the radio silence today. I was busy.":
            "谢谢，刚刚看到了。抱歉今天一直没回消息，我很忙。",
        "I'm used to it.": "我已经习惯了。",
        "Yeah... Anyway, I can't wait for tomorrow!": "好吧……不管怎样，我已经等不及明天了！",
        "No need to apologize. We don't have to talk every day. What did you do?":
            "不用道歉，我们不必每天都聊天。你今天做什么了？",
        "Mom said she could get me a temp job at the makeup store. I went with her to work to see how it's done.":
            "妈妈说能在化妆品店给我找份临时工作。我今天跟她去上班，看看具体要做什么。",
        "The makeup store? You? Haha! mphone_emoji_laugh": "化妆品店？你？哈哈！mphone_emoji_laugh",
        "Parallel universe Zoey, checking in. Look, I need to do something aside from climbing the walls of my room, skating, and sketching. This is better than nothing.":
            "平行宇宙Zoey前来报到。听着，除了闷在房间里发疯、滑板和画画，我总得找点事做。这总比什么都没有强。",
        "What? I might not be a girly girl, but I use makeup.": "怎么？我可能不算很有女人味，但也会化妆。",
        "No way? That's nice of Alison. Do you think it will be fun?": "不会吧？Alison人真好。你觉得工作会有趣吗？",
        "Uh... No? Look, I need to do something aside from climbing the walls of my room, skating, and sketching. This is better than nothing.":
            "呃……不会吧？听着，除了闷在房间里发疯、滑板和画画，我总得找点事做。这总比什么都没有强。",
        "Not so much. Definitely not compared to Tattoos.": "不怎么样，肯定比不上纹身店。",
        "It would be like working the reception, but there's a lot more to it than just that.":
            "有点像做前台，不过实际工作远不止这些。",
        "Tell me more about it.": "再多说一点。",
        "Yeah, I can bore you with it tomorrow, maybe?": "好啊，也许明天我可以拿这些事烦死你？",
        "Call me if you can't find the place.": "找不到地方就给我打电话。",

        # 本批新增：Sage手机聊天与寻人提示。
        "Are you still getting ready?": "你们还在准备吗？",
        "Put your dick back inside your pants; we're coming.": "把鸡巴塞回裤子里，我们就要到了。",
        "How did you know?": "你怎么知道的？",
        "I took a course in probability and stochastics; it was the most likely guess.":
            "我上过概率论和随机过程，这显然是最有可能的答案。",
        "Can't wait to see you.": "等不及见到你了。",
        "I'm not wearing pants; I'm kinda wearing a skirt.": "我没穿裤子，算是穿了一条裙子。",
        "Should I be concerned?": "我是不是该担心了？",
        "Haha! Maybe? Come here and find out.": "哈哈！也许吧？过来亲自确认。",
        "Guess where I am...": "猜猜我在哪里……",
        "What are you up to?": "你在搞什么名堂？",
        "You said you would be able to find me no matter what. I'm putting it to the test.":
            "你说过无论怎样都能找到我。现在我要考验一下这句话。",
        "I recognize those tiles. You're in the downstairs bathroom.": "我认得那些瓷砖。你在楼下洗手间。",
        "Hm... Am I?": "嗯……是吗？",
        "Ok, where are you, really?": "好了，你到底在哪里？",
        "I'm not in the bathroom anymore; I can tell you that much. Maybe this will help you find me?":
            "反正我已经不在洗手间了，这点可以告诉你。也许这个能帮你找到我？",
        "I recognize those tiles. You're in the upstairs bathroom.": "我认得那些瓷砖。你在楼上洗手间。",
        "Ok. You're not here. Where are you?": "好吧，你不在这里。你在哪儿？",
        "Wrong bathroom. Besides, I'm not there anymore. Maybe this will help you find me?":
            "洗手间猜错了。而且我已经不在那里。也许这个能帮你找到我？",
        "Hah! I got you now.": "哈！这次抓到你了。",
        "You must be completely off because I waited and couldn't even spot you.":
            "你肯定猜得离谱，我在那里等了半天，连你的人影都没看到。",
        "Final clue. If you don't get this, I'll question your sanity.": "最后一条线索。再猜不到，我就要怀疑你的智商了。",
        "Haha! Close! But you just missed me.": "哈哈！很接近！不过你刚好和我错过了。",
        "Final clue.": "最后一条线索。",

        # 本批新增：Nora手机聊天记录。
        "It's really pouring tonight.": "今晚雨下得真大。",
        "Lovely, isn't it? I turned off my TV and cracked open a window to listen. But it's almost stopped raining here.":
            "很惬意，对吧？我关掉电视，开了一条窗缝听雨声。不过我这边几乎已经停了。",
        "How nice. Here it's still going. I'm sitting here watching my window, drinking a beer.":
            "真好。我这里还在下，正坐着望向窗外喝啤酒。",
        "That sounds awfully sad. Are you all right?": "听起来也太伤感了。你还好吗？",
        "Yeah, I'm fine. I didn't realize it sounded sad. I'm not just drinking; I'm eating crackers too. mphone_emoji_smile":
            "我没事，没想到听起来这么伤感。我不只是在喝酒，还吃着饼干呢。mphone_emoji_smile",
        "I was picturing you in black and white, staring out your window with a beer in one hand and the phone in the other, deciding to text me to keep up your morale.":
            "我都脑补出一幅黑白画面了：你一手拿啤酒，一手拿手机，望着窗外，最后决定给我发消息振作精神。",
        "I'm not sad or in black and white, but you're not far off. That's what I look like right now.":
            "我并不难过，画面也不是黑白的，不过你猜得很接近。我现在确实差不多就是这样。",
        "What about you? What do you look like now?": "你呢？现在是什么样子？",
        "I'm unwinding on my couch in comfortable clothes.": "我穿着舒服的衣服，正在沙发上放松。",
        "Comfortable clothes? Sounds hot.": "舒服的衣服？听着很性感。",
        "Not particularly. Well... I'm not wearing a bra, so there's that.": "没那么性感。不过……我没穿胸罩，也算有点吧。",
        "Sorry, I was gonna say something, but I completely lost my train of thought.":
            "抱歉，我刚才本来想说点什么，可思路突然完全断了。",
        "Haha! I won't mention my bra again, then. I wouldn't want you to stop talking to me. mphone_emoji_smile":
            "哈哈！那我不再提胸罩了，免得你一句话也说不出来。mphone_emoji_smile",
        "I've felt better.": "状态不太好。",
        "Oh, dear. What's got you feeling down?": "哎呀，什么事让你这么低落？",
        "Honestly, I don't know. I guess I've felt kind of lonely lately.": "说真的，我也不知道。可能是最近有点孤单吧。",
        "In my experience, loneliness means you don't enjoy your own company. Work on being comfortable with yourself, and you won't feel as lonely when you're alone.":
            "按我的经验，孤独意味着你还不懂得享受独处。试着和自己自在相处，一个人时就不会那么寂寞。",
        "Aha, is that something you've done?": "哦？这是你的亲身经验？",
        "I've always been a blast to be around. I do love my own company.": "和我待在一起向来很有趣，我确实很享受自己的陪伴。",
        "I'm sure I'd love it too.": "我相信自己也会喜欢你的陪伴。",
        "Such a charmer. mphone_emoji_smile": "真会讨人欢心。mphone_emoji_smile",
        "Will I see you at the gym next week?": "下周能在健身房见到你吗？",
        "Next week will be a bit hectic, but I'll try to squeeze in some workout. However, I can't say when.":
            "下周会有点忙，不过我会尽量挤时间锻炼，只是说不准哪天。",
        "Hopefully, I'll run into you then.": "希望到时候能偶遇你。",
        "We'll see what chance brings us. If nothing, then at least we can talk like this.":
            "那就看看缘分怎么安排吧。即使碰不到，至少我们还能像这样聊天。",
        "Absolutely. Or maybe we can meet up someplace else? If you're interested, that is.":
            "当然。或者我们可以约在别的地方见面？前提是你有兴趣。",
        "Maybe I am.": "也许我有。",
        "Enjoy your evening, [name]. Thanks for the pleasant distraction.":
            "好好享受今晚吧，[name]。谢谢你带来的愉快消遣。",
        "You too.": "你也是。",

        # 本批新增：Nicole、Jade与Quinn手机聊天记录。
        "How are you?": "你好吗？",
        "[name]! I'm fine, but super tired. I just got off work and am about to head home.":
            "[name]！我很好，就是特别累。刚下班，正准备回家。",
        "I hope you brought an umbrella.": "希望你带了伞。",
        "No! Is it raining?": "没有！下雨了吗？",
        "It is here. You might get wet.": "我这里在下，你可能会淋湿。",
        "Thanks for the heads up. I'll check if there's an umbrella in the lost and found.":
            "谢谢提醒。我去失物招领处看看有没有伞。",
        "Gotta go! Talk another time, sweetie. Mwah!": "得走了！改天再聊，亲爱的。啵！",
        "Good evening...": "晚上好……",
        "Not the best time.": "现在不是时候。",
        "Got it.": "明白了。",
        "Did you want something?": "你有什么事？",
        "No. Well...": "没有。这个嘛……",
        "Spit it out.": "有话直说。",
        "I wanted to talk to you. And check that everything is good after last time.":
            "我想和你聊聊，也想确认上次之后一切是否安好。",
        "Yes. We're in the clear. But let's never meet like that again.":
            "没事了，我们没有暴露。不过以后绝不能再那样见面。",
        "I'll try my best to stay clear of it. When will I see you again?":
            "我会尽力避免。什么时候才能再见到你？",
        "I'll talk to you at school, ok? Ironically, it's much safer to flirt with a student there than at home. mphone_emoji_kiss":
            "我们在学校聊，好吗？讽刺的是，在学校和学生调情反而比在家里安全得多。mphone_emoji_kiss",
        "Haha! Deal. mphone_emoji_kiss": "哈哈！说定了。mphone_emoji_kiss",
        "I got my outfit ready for the party.": "我已经准备好派对服装了。",
        "Let me guess. Gimp suit?": "让我猜猜，性奴装？",
        "Almost. Spartan warrior.": "差不多。斯巴达战士。",
        "Ah! You're going as the quintessential college douchebag. Gotcha.":
            "啊！你要扮成最典型的大学人渣。懂了。",
        "Come on, it's not. Is it?": "拜托，没那么夸张吧？",
        "I never saw someone wear it who didn't do it for scoring pussy.":
            "我就没见过哪个穿这套的人，不是为了泡妞上床。",
        "Sounds to me like I chose the perfect costume.": "听起来我选到了最合适的服装。",
        "Pff.": "切。",
        "What about you?": "你呢？",
        "My costume will make you cum in your pants faster than you ever have before.":
            "我的服装会让你以前所未有的速度射在裤子里。",
        "Sounds sexy. I'm in.": "听着很性感，算我一个。",
        "Earn it.": "那就凭本事争取。",
        "How?": "怎么争取？",
        "Keep your dick in your pants during the party, and I'll take you home to my lair.":
            "派对期间管好裤子里的鸡巴，我就带你回自己的巢穴。",
        "Is that some kind of a challenge?": "这算是一种挑战？",
        "I don't think you can do it.": "我觉得你做不到。",
        "If you're the prize, I can.": "如果奖品是你，我就能。",
        "Doubt it.": "我才不信。",
        "Besides, I'm wearing some kind of a skirt, so it's technically not pants I'd be cumming in.":
            "再说，我穿的算是一条裙子，所以严格来说，射到的也不是裤子。",
        "You've already lost.": "你已经输了。",
        "Haha! Nah. You'll see.": "哈哈！才没有。等着瞧。",
        "You're right. I can't. Especially not when I'm dressed as a sexy Spartan warrior.":
            "你说得对，我做不到。尤其是穿着性感斯巴达战士服的时候。",
        "Then you have already lost. Shame.": "那你已经输了。真可惜。",
        "Well, your costume would have to be really worth it.": "那你的服装最好真的值得。",
        "It is.": "当然值得。",

        # 本批新增：Lily与Riona手机聊天记录。
        "Are you free?": "你有空吗？",
        "For you, I'll make time. What's up?": "是你找的话，我会腾出时间。怎么了？",
        "Not much. I'm kind of bored. I've been browsing Rooster and whatnot.":
            "没什么，就是有点无聊，一直在刷Rooster之类的。",
        "Dude, if you're bored, just call me. I can...entertain you.":
            "老兄，无聊就直接打给我。我可以……让你开心一下。",
        "Oh yeah? Doing what?": "是吗？怎么让我开心？",
        "You know what. mphone_emoji_evil": "你知道是什么。mphone_emoji_evil",
        "Haha!": "哈哈！",
        "I've been meaning to ask you... You don't post a lot on Rooster. What's up with that?":
            "我一直想问……你很少在Rooster上发动态，怎么回事？",
        "I don't know. I prefer to browse and comment on others' clucks.":
            "不知道。我更喜欢浏览和评论别人的咯咯文。",
        "Post more.": "多发一点。",
        "Like what?": "比如发什么？",
        "Like a picture of yourself or something. It doesn't have to be much.":
            "比如发张自拍之类的，不用多特别。",
        "Wait, I found a picture of you. Yeah... This one will work.":
            "等等，我找到一张你的照片。嗯……这张可以。",
        "Work for what?": "拿来做什么？",
        "Hey, you're not here with me, and I'm in the mood.": "喂，你又不在我身边，而我现在有兴致了。",
        "Don't tell me you're using my picture for it.": "别告诉我，你要看着我的照片做那件事。",
        "Hot, huh? I'm looking at it right now as I touch myself.":
            "很性感吧？我现在就一边看着它，一边摸自己。",
        "I don't believe you.": "我不信。",
        "What are you up to?": "你在做什么？",
        "Not much. Listening to some music and annoying Cammy with my off-pitch singing. You?":
            "没什么。听听音乐，再用跑调的歌声折磨Cammy。你呢？",
        "I'm fiddling with my phone. I'm pretty bored, actually. And it's too late to do something fun.":
            "我在摆弄手机。说真的，挺无聊的，而且现在太晚，做不了什么有趣的事。",
        "Feels nice to have some time off between midterms and new classes, huh?":
            "期中考试结束、新课程开始前能歇一阵，感觉真不错，对吧？",
        "Yeah. With the Halloween planning and some drama put aside, my stress levels are way lower after the midterms.":
            "是啊。撇开万圣节策划和一些破事不谈，期中考试结束后我的压力小多了。",
        "Good for you.": "那很好啊。",
        "Same here, but mostly thanks to your help with my paranoia.":
            "我也一样，不过主要是因为你帮我解决了那件让我疑神疑鬼的事。",
        "It wasn't paranoia. You were right.": "那不是疑神疑鬼，你是对的。",
        "Yeah. It's so fucking creepy. I get chills thinking about it still.":
            "是啊，真的太他妈瘆人了。现在想起来我还会起鸡皮疙瘩。",
        "Let me know if that dude bothers you again.": "那家伙要是再骚扰你，就告诉我。",
        "You'd be the first one I'd call. mphone_emoji_kiss": "你会是我第一个打电话的人。mphone_emoji_kiss",
        "Say hi to Cammy for me.": "替我向Cammy问好。",
        "She said \"swiggity swooty\" to you.": "她让我转告你‘swiggity swooty’。",
        "Huh? What does that mean?": "啊？那是什么意思？",
        "Nothing. She's being an ass. Haha!": "没什么，她只是在犯贱。哈哈！",
        "Anyway, have a good one!": "总之，祝你今晚过得愉快！",

        # EP9累计第5001—7000条：自由活动中未进入翻译模板的动态文本。
        "Becky": "Becky",
        "Bianca": "Bianca",
        "Camila": "Camila",
        "Dany": "Dany",
        "Heather": "海瑟",
        "Jamie": "Jamie",
        "Leon": "Leon",
        "Micha": "Micha",
        "Nick": "Nick",
        "Nicole": "Nicole",
        "Olivia": "Olivia",
        "Quinn": "Quinn",
        "Riona": "Riona",
        "Rusty": "Rusty",
        "Sally": "Sally",
        "Sarah": "Sarah",
        "Tiffani": "Tiffani",
        "Tybalt": "Tybalt",

        "Derek's room": "Derek的房间",
        "Jacob's room": "Jacob的房间",
        "Jamie's room": "Jamie的房间",
        "Leon's room": "Leon的房间",
        "Nick's room": "Nick的房间",
        "Rusty's room": "Rusty的房间",
        "Tommy's room": "Tommy的房间",
        "Talk to Jamie": "和Jamie交谈",
        "Talk to Sally": "和Sally交谈",
        "Talk to Rusty": "和Rusty交谈",
        "Talk to Zoey": "和Zoey交谈",
        "Talk to Derek": "和Derek交谈",
        "Text Maya": "给Maya发消息",
        "Text Josy": "给Josy发消息",
        "Text Jill": "给Jill发消息",
        "Talk to Sage": "和Sage交谈",
        "Talk to Josy": "和Josy交谈",
        "Talk to Quinn": "和Quinn交谈",
        "Take picture with Riona": "和Riona合影",
        "Talk to Sarah": "和Sarah交谈",
        "Give Jill a tour": "带Jill参观",
        "Talk to Jill": "和Jill交谈",
        "Dance with Sage": "和Sage跳舞",
        "Dance with Josy & Maya": "和Josy、Maya跳舞",
        "Take picture with Bella": "和贝拉合影",
        "Have Bella talk to Jill": "让贝拉和Jill谈谈",
        "Dance with Camila": "和Camila跳舞",
        "Talk to Nicole": "和Nicole交谈",
        "Find Becky": "寻找Becky",
        "Talk to Heather": "和海瑟交谈",
        "Talk to Josy & Maya": "和Josy、Maya交谈",
        "Check Jamie's room": "查看Jamie的房间",
        "Find Riona": "寻找Riona",
        "Check Rusty's room": "查看Rusty的房间",
        "Talk to Tommy": "和Tommy交谈",
        "Talk to Riona": "和Riona交谈",
        "Take a picture with Quinn": "和Quinn合影",
        "Find punch for Sarah": "替Sarah找潘趣酒",
        "Bring punch to Sarah": "把潘趣酒拿给Sarah",
        "Take a picture with Camila": "和Camila合影",
        "Dance with Jill": "和Jill跳舞",
        "Help Sage": "帮助Sage",
        "Help Josy": "帮助Josy",
        "Find Rusty": "寻找Rusty",

        "DIKs' happiness increased!": "DIKs成员的快乐值提升了！",
        "• The {color=ffed00}Drinking Competition{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}饮酒比赛{/color}让Jamie的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Drinking Competition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}饮酒比赛{/color}让Leon的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Drinking Competition{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}饮酒比赛{/color}让Rusty的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Drinking Competition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}饮酒比赛{/color}让Tommy的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Body Shots{/color} activity increased Jacob's happiness by {color=00ff00}+3%{/color}.":
            "• {color=ffed00}人体酒杯{/color}让Jacob的快乐值提升了{color=00ff00}+3%{/color}。",
        "• The {color=ffed00}Body Shots{/color} activity increased Jamie's happiness by {color=00ff00}+3%{/color}.":
            "• {color=ffed00}人体酒杯{/color}让Jamie的快乐值提升了{color=00ff00}+3%{/color}。",
        "• The {color=ffed00}Body Shots{/color} activity increased Nick's happiness by {color=00ff00}+3%{/color}.":
            "• {color=ffed00}人体酒杯{/color}让Nick的快乐值提升了{color=00ff00}+3%{/color}。",
        "• The {color=ffed00}Body Shots{/color} activity increased Tommy's happiness by {color=00ff00}+3%{/color}.":
            "• {color=ffed00}人体酒杯{/color}让Tommy的快乐值提升了{color=00ff00}+3%{/color}。",
        "• The {color=ffed00}Scary Stories{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}恐怖故事会{/color}让Derek的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Scary Stories{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}恐怖故事会{/color}让Jacob的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Scary Stories{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}恐怖故事会{/color}让John Boy的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Haunted Mansion{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}鬼屋{/color}让Jacob的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Haunted Mansion{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}鬼屋{/color}让Jamie的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Haunted Mansion{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}鬼屋{/color}让John Boy的快乐值提升了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}Haunted Mansion{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}鬼屋{/color}让Nick的快乐值提升了{color=00ff00}+2%{/color}。",

        "I did body shots with Tiffani during the competition. She's wild!":
            "比赛时我和Tiffani搭档玩了人体酒杯。她可真够野的！",
        "I did body shots with Becky during the competition. She gets bossy.":
            "比赛时我和Becky搭档玩了人体酒杯。她一较起劲来就爱发号施令。",
        "Rusty seems to be interested in Micha. He sure likes to talk to her.":
            "Rusty似乎对Micha有意思，他可真喜欢找她聊天。",
        "Leon was upset that Jamie bailed on their theme costume and went back to Dany.":
            "Jamie放弃了和Leon一起穿主题服装，又回到了Dany身边，这让Leon很不爽。",
        "Jamie bailed on the theme costume idea with Leon, thinking it was just talk.":
            "Jamie以为和Leon一起穿主题服装只是随口一说，最后放了Leon鸽子。",
        "When Jamie and Leon argued, I took Jamie's side.":
            "Jamie和Leon争吵时，我站在了Jamie这边。",
        "When Jamie and Leon argued, I took Leon's side.":
            "Jamie和Leon争吵时，我站在了Leon这边。",
        "Zoey seems to have changed a lot during this last year.":
            "过去这一年里，Zoey似乎变了很多。",
        "Zoey and I took a Halloween picture together.":
            "我和Zoey一起拍了一张万圣节合影。",
        "I had sex with Sage during the Haunted Mansion tour. We were being careless, and Penny saw everything.":
            "体验鬼屋时，我和Sage做了爱。我们太不小心，被Penny看了个一清二楚。",
        "You had sex with Sage during the Haunted mansion activity in episode 9.":
            "你在第9集的鬼屋活动中和Sage做了爱。",
        "Jill came to our Halloween party. I had a friendly talk with her and her friend, Bianca.":
            "Jill来参加了我们的万圣节派对。我和她及她的朋友Bianca友好地聊了一会儿。",
        "Jill came to our Halloween party with her friends. I made an effort to talk with her. It was a bit awkward, but I'm glad I did it.":
            "Jill和朋友们来参加了我们的万圣节派对。我特意去和她谈了谈，虽然有些尴尬，但我很庆幸自己这么做了。",
        "Quinn fooled the tri-alphas at Halloween by using Arieth.":
            "万圣节时，Quinn利用Arieth耍了三个Alpha一通。",
        "Quinn told me that Arieth is pregnant.":
            "Quinn告诉我，Arieth怀孕了。",
        "I told Quinn that I was dating someone, and she got mad. She said she only cared about sex when it came to me.":
            "我告诉Quinn自己正在和别人交往，她生气了。她说对于我，她只在乎性爱。",
        "I took a picture together with Quinn at the Halloween party.":
            "我在万圣节派对上和Quinn合了影。",
        "I had sex with Camila on the dance floor at the Halloween party.":
            "万圣节派对上，我和Camila在舞池里做了爱。",
        "You had sex with Camila on the dance floor in episode 9.":
            "你在第9集里和Camila在舞池里做了爱。",
        "I tried helping Derek hook up with Camila. It didn't go well since he's been talking too much about Ashley in front of her.":
            "我试着帮Derek追Camila，但他当着Camila的面总提起Ashley，结果并不顺利。",
        "Camila said that Derek was talking about Ashley a lot and that she wasn't interested in hooking up with him.":
            "Camila说Derek总在谈论Ashley，而且她对和Derek上床没兴趣。",
        "I took a picture together with Jill and Bianca at the Halloween party.":
            "我在万圣节派对上和Jill、Bianca一起合了影。",
        "Jill wanted our relationship to be official soon, but I hadn't broken up with Josy and Maya yet...":
            "Jill希望我们尽快正式确定关系，可我还没有和Josy、Maya分手……",
        "Jill wanted our relationship to be official soon.":
            "Jill希望我们尽快正式确定关系。",
        "I didn't have any STDs. I guess Jill won't make a fuss about me skipping the condom from now on.":
            "我的性病检测结果是阴性。看来以后不戴套时，Jill不会再为此担心了。",
        "Josy could definitely tell that there was something off with me. I tried to play it cool before I got the chance to break up with her and Maya, but I don't think it worked.":
            "Josy显然看出了我的异样。在有机会和她、Maya分手前，我试着装作若无其事，但恐怕没有骗过她。",
        "I told Josy I think about her and our relationship all the time. What would it have been like if things were different?":
            "我告诉Josy，自己经常想起她和我们之间的关系，也会想如果当初不同，现在会是什么样。",
        "I told Josy I think about her and our relationship from time to time. What would it have been like if things were different?":
            "我告诉Josy，自己偶尔会想起她和我们之间的关系，也会想如果当初不同，现在会是什么样。",
        "I told Josy I thought our relationship would have been doomed to fail, even if it weren't for her and Maya.":
            "我告诉Josy，即使没有她和Maya之间的事，我觉得我们的关系也注定会失败。",
        "I took a picture together with Josy at the Halloween party.":
            "我在万圣节派对上和Josy合了影。",
        "I took a picture together with Josy and Maya at the Halloween party.":
            "我在万圣节派对上和Josy、Maya一起合了影。",

        # EP9累计第7001—8000条：自由活动遗漏的任务、人物资料与统计文本。
        "Go to the theater": "前往放映厅",
        "Dance with Bella": "和贝拉跳舞",
        "Check right hallway": "查看右侧走廊",
        "Find Maya": "寻找Maya",
        "Check the porch": "查看门廊",
        "Check your room": "查看你的房间",
        "Find Josy & Maya": "寻找Josy和Maya",
        "Say goodbye to Zoey": "向Zoey道别",

        "I took a picture together with Sage at the Halloween party.":
            "我在万圣节派对上和Sage合了影。",
        "I took a picture together with Bella at the Halloween party.":
            "我在万圣节派对上和贝拉合了影。",
        "I took a picture of Riona at the Halloween party.":
            "我在万圣节派对上给Riona拍了照片。",
        "I took a picture of Camila at the Halloween party.":
            "我在万圣节派对上给Camila拍了照片。",
        "I took a picture together with Sarah and Melanie at the Halloween party.":
            "我在万圣节派对上和Sarah、Melanie一起合了影。",
        "I took a picture of Sarah and Melanie at the Halloween party.":
            "我在万圣节派对上给Sarah和Melanie拍了照片。",
        "Bella played drinking games together with Josy, Maya, and Sage.":
            "贝拉和Josy、Maya及Sage一起玩了喝酒游戏。",
        "I punched Oscar after he insulted Josy at the Halloween party.":
            "Oscar在万圣节派对上侮辱Josy后，我揍了他。",
        "I made Oscar leave after he insulted Josy at the Halloween party.":
            "Oscar在万圣节派对上侮辱Josy后，我把他赶走了。",
        "I comforted Josy after she was insulted by Oscar at the Halloween party.":
            "Josy在万圣节派对上遭到Oscar侮辱后，我安慰了她。",
        "Sage and I poured pumpkin pulp on Tybalt's bed as a prank.":
            "我和Sage把南瓜瓤铺在Tybalt的床上，捉弄了他一番。",
        "I talked to Josy's dad, Pete, over the phone. It led to us talking about meeting parents.":
            "我在电话里和Josy的父亲Pete交谈，这也让我们谈起了见家长的事。",
        "Maya got frisky with me in public. But she stopped after I mentioned that Josy wasn't there with us.":
            "Maya在众目睽睽下和我亲热，但我提起Josy没有和我们在一起后，她便停了下来。",
        "I was about to have sex with Maya behind the green screen at the Halloween party, but we were interrupted by people having their pictures taken. It was wild!":
            "万圣节派对上，我差点和Maya在绿幕后做爱，却被前来拍照的人打断了。实在太疯狂了！",
        "You had sex with Maya behind the green screen in episode 9.":
            "你在第9集里和Maya在绿幕后做了爱。",
        "Riona was upset at the Halloween party, but I didn't press her on it.":
            "Riona在万圣节派对上情绪低落，但我没有追问。",
        "Riona was upset at the Halloween party, and I cheered her up.":
            "Riona在万圣节派对上情绪低落，而我逗她开心了。",
        "Riona told me that she and Quinn have some issues.":
            "Riona告诉我，她和Quinn之间出了一些问题。",

        # EP9累计第8001—8308条：任务与人物资料动态文本。
        "Tara": "Tara",
        "I kissed Tara at the Halloween party, but she felt a bit iffy about it since she's dating Oscar.":
            "我在万圣节派对上吻了Tara，但她因为正在和Oscar交往，心里多少有些不自在。",
        "Bella and I snuck away from the party to make out in the college's library.":
            "我和贝拉偷偷离开派对，躲到学校图书馆里亲热。",
        "Talk to Jill & Bianca": "和Jill、Bianca谈谈",
        "I caught Jill's friends, Matthew and Olivia, making out in Rusty's room at the Halloween party.":
            "万圣节派对上，我撞见Jill的朋友Matthew和Olivia在Rusty的房间里亲热。",
        "I caught Bianca's boyfriend, Matthew, making out with Olivia in Rusty's room at the Halloween party.":
            "万圣节派对上，我撞见Bianca的男友Matthew和Olivia在Rusty的房间里亲热。",
        "Pick top three costumes": "选出前三名的装扮",

        # EP9累计第8309—10308条：任务、人物资料、统计及活动记录。
        "Becky": "Becky",
        "Riona": "Riona",
        "Sally": "Sally",
        "Heather": "Heather",
        "Envy": "Envy",
        "Christian": "Christian",
        "Lucas": "Lucas",
        "Gordon": "Gordon",
        "Rusty": "Rusty",
        "Micha": "Micha",
        "Vinny": "Vinny",
        "Leon": "Leon",
        "Lily": "Lily",
        "Nicole": "Nicole",
        "Sandy": "Sandy",
        "Camila": "Camila",

        "Warn Jacob": "提醒Jacob",
        "Find Zoey": "寻找Zoey",
        "Kick out the preps": "赶走富家帮的人",
        "Check the theater": "查看放映厅",
        "Talk to Sarah & Melanie": "和Sarah、Melanie谈谈",
        "Find Sally": "寻找Sally",
        "Talk to Lily & Nicole": "和Lily、Nicole谈谈",
        "Check downstairs bathroom": "查看楼下洗手间",
        "Say goodbye to Rio & Cammy": "向里奥、卡米道别",
        "Find Jamie": "寻找Jamie",

        "Becky fell into the bathtub and ruined her costume at the Halloween party. She was mad and stormed off with Jacob's DIK jacket.":
            "万圣节派对上，Becky掉进浴缸毁了装扮。她气冲冲地穿着Jacob的DIK夹克离开了。",
        "I made out with Riona at the Halloween party.":
            "我在万圣节派对上和Riona亲热了。",
        "I told Riona that I was in a relationship at the Halloween party.":
            "万圣节派对上，我告诉Riona自己已经有对象了。",
        "I rejected Riona's advances at the Halloween party.":
            "万圣节派对上，我拒绝了Riona的求欢。",
        "Sally's costume ripped, and I didn't help her with it.":
            "Sally的装扮裂开了，而我没有帮她。",
        "Sally's costume ripped, but I helped her by lending her some of my clothes.":
            "Sally的装扮裂开了，我把自己的衣服借给她救急。",
        "Heather was drunk and mad at Tommy. She suspected that he was fucking Christie at the Halloween party.":
            "Heather喝醉后对Tommy很生气，怀疑他在万圣节派对上干了Christie。",
        "I refused Heather's advances at the Halloween party.":
            "万圣节派对上，我拒绝了Heather的求欢。",
        "I refused Heather's advances and told her that I'd maybe do it in the future if things were different for me.":
            "我拒绝了Heather的求欢，并告诉她，等以后我的情况不同了，也许会答应。",
        "I got a blowjob and boobjob from Heather in Leon's room.":
            "Heather在Leon的房间里给我口交和乳交。",
        "You got a boobjob and a blowjob from Heather at the Halloween party in episode 9.":
            "你在第9集的万圣节派对上享受了Heather的乳交和口交。",
        "Josy, Maya, and I coined \"The Dare Game\" and dared each other to do lewd things.":
            "我和Josy、Maya发明了‘大冒险游戏’，互相挑战去做淫荡的事。",
        "Nicole was disappointed when I told her that I was getting involved with someone.":
            "我告诉Nicole自己正在和别人发展关系，她对此很失望。",
        "I let the preps into our Halloween party.":
            "我让富家帮的人进入了我们的万圣节派对。",
        "I didn't let the preps into our Halloween party.":
            "我没有让富家帮的人进入我们的万圣节派对。",
        "I broke up with Josy and Maya at the end of the Halloween party. It sucked, but it had to be done.":
            "万圣节派对结束时，我和Josy、Maya分手了。这很痛苦，但我必须这么做。",
        "Rusty had to sell his car to pay for fixing the mansion.":
            "Rusty不得不卖掉汽车，支付修缮豪宅的费用。",
        "I had a heart-to-heart with Rusty about Micha. Apparently, she's got a boyfriend and led Rusty on.":
            "我和Rusty敞开心扉谈了Micha。原来她已经有男朋友，却一直吊着Rusty。",
        "Apparently, she's got a boyfriend and led Rusty on.":
            "原来她已经有男朋友，却一直吊着Rusty。",
        "I threw Lucas out of the Halloween party after he snuck in.":
            "Lucas偷溜进万圣节派对后，我把他赶了出去。",
        "I threw Christian out of the Halloween party after he snuck in.":
            "Christian偷溜进万圣节派对后，我把他赶了出去。",
        "• The {color=ffed00}CUM-petition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}射精大赛{/color}活动让Leon的满意度提高了{color=00ff00}+2%{/color}。",
        "• The {color=ffed00}CUM-petition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}射精大赛{/color}活动让Tommy的满意度提高了{color=00ff00}+2%{/color}。",
        "I won the CUM-petition, but Lily and Nicole made it very hard for me.":
            "我赢下了射精大赛，不过Lily和Nicole让我赢得非常艰难。",
        "Leon lost the CUM-petition. Poor guy... I wouldn't want to be him. That punishment didn't sound too good to me.":
            "Leon输掉了射精大赛。可怜的家伙……我可不想成为他，那惩罚听起来一点也不好受。",
        "Lily and Nicole entertained you during the CUM-petition at the Halloween party in episode 9.":
            "第9集的万圣节派对上，Lily和Nicole在射精大赛期间招待了你。",
        "I offered to let Zoey crash on my couch.":
            "我提出让Zoey睡在自己的沙发上。",
        "Sandy wanted me to fuck her against the railing in the hallway.":
            "Sandy想让我在走廊栏杆旁干她。",
        "Sandy wanted to fuck me, but I declined.":
            "Sandy想和我做爱，但我拒绝了。",
        "Sandy wanted to fuck me, but I told her I couldn't do stuff like that with her anymore.":
            "Sandy想和我做爱，但我告诉她，自己不能再和她做这种事了。",
        "Sandy wanted to fuck me, but I told her I could only have fun with her at The Pink Rose.":
            "Sandy想和我做爱，但我告诉她，我们只能在粉红玫瑰俱乐部寻欢。",
        "I punched Vinny when he shoved me in my room.":
            "Vinny在我房间里推搡我时，我揍了他。",
        "I told Vinny off when he shoved me in my room.":
            "Vinny在我房间里推搡我时，我严厉警告了他。",
        "I tried to act friendly with Vinny and defuse the situation when he shoved me in my room.":
            "Vinny在我房间里推搡我时，我试着友善应对，缓和局面。",
        "Vinny threatened me with a prop gun at the Halloween party.":
            "Vinny在万圣节派对上用道具枪威胁了我。",
        "Bella won the best costume contest at our Halloween party.":
            "贝拉赢得了万圣节派对的最佳装扮比赛。",
        "Leon won the best costume contest at our Halloween party.":
            "Leon赢得了万圣节派对的最佳装扮比赛。",
        "Jill won the best costume contest at our Halloween party.":
            "Jill赢得了万圣节派对的最佳装扮比赛。",
        "Maya won the best costume contest at our Halloween party.":
            "Maya赢得了万圣节派对的最佳装扮比赛。",
        "Josy won the best costume contest at our Halloween party.":
            "Josy赢得了万圣节派对的最佳装扮比赛。",
        "Riona won the best costume contest at our Halloween party.":
            "Riona赢得了万圣节派对的最佳装扮比赛。",
        "Camila won the best costume contest at our Halloween party.":
            "Camila赢得了万圣节派对的最佳装扮比赛。",
        "Lily won the best costume contest at our Halloween party.":
            "Lily赢得了万圣节派对的最佳装扮比赛。",
        "Zoey won the best costume contest at our Halloween party.":
            "Zoey赢得了万圣节派对的最佳装扮比赛。",
    }

    def _s3_ep9_cn_active():
        try:
            return getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            return False

    def _s3_ep9_cn_replace_text(s):
        if _s3_ep9_prev_replace_text is not None:
            s = _s3_ep9_prev_replace_text(s)

        if not _s3_ep9_cn_active():
            return s

        if s.startswith("{size=-") and s.endswith("If you experience lag, disable Settings > Special effects{/size}"):
            return s.replace(
                "If you experience lag, disable Settings > Special effects",
                "如果游戏卡顿，请关闭“设置 > 特效”",
            )

        return _s3_ep9_cn_exact.get(s, s)

    config.replace_text = _s3_ep9_cn_replace_text
