# Being a DIK S3 Episode 11：补充翻译提取器未收录的动态显示文本。
# 仅在中文语言下替换显示字符串，不修改剧情变量、返回值或游戏逻辑。

init 1000 python:
    _s3_ep11_prev_replace_text = config.replace_text

    _s3_ep11_cn_exact = {
        "Everything ok? I've tried calling you. I'm getting worried here.":
            "一切都好吗？我打过电话了，一直没人接。我开始担心了。",
        "Been busy.": "一直在忙。",
        "Ok. Good to know that you're alive at least. I'm back home over the weekend. I'm available on Sunday if you need me for something.":
            "好吧，至少知道你还活着。我周末回家了。你周日要是有事需要我，我有空。",
        "Ok.": "好。",
        "Maya found out that she didn't have a co-signed loan and she could get a student loan to get out of her situation with Patrick.":
            "Maya发现自己并没有共同签署的贷款，因此可以申请学生贷款，摆脱Patrick对她的控制。",
        "Jill offered Maya her help with applying for a student loan.":
            "Jill提出帮助Maya申请学生贷款。",
        "Patrick loaned money from a banking partner to cover the tuition and living expenses for Derek and Maya.":
            "Patrick向合作银行借款，用于支付Derek和Maya的学费及生活费。",
        "I didn't agree with Maya when she chose to focus on college instead of finding another way to get the contract from Patrick.":
            "Maya决定专注学业，不再想其他办法从Patrick手里拿到合同，我并不赞同她的选择。",
        "I chose to respect Maya's choice and let her focus on college instead of finding another way to get the contract from Patrick.":
            "我选择尊重Maya，让她专注学业，不再想其他办法从Patrick手里拿到合同。",
        "Maya chose to focus on college and stop wasting time trying to solve her issues with Patrick.":
            "Maya决定专注学业，不再浪费时间设法解决她和Patrick之间的问题。",
        "I tried to tell Dad about my relationship with Josy and Maya, but he didn't understand it and feared I'd end up hurting them.":
            "我试着把自己和Josy、Maya的关系告诉爸爸，但他无法理解，还担心我最终会伤害她们。",
        "I told Dad about my relationship with Bella but hid the fact that she was my teacher and closer to his age than mine.":
            "我告诉爸爸自己正和贝拉交往，却隐瞒了她是我的老师，而且年龄更接近爸爸。",
        "I visited Zoey and tried to explain to her how I felt. She understood what I meant, and we hugged it out.":
            "我去看了Zoey，试着向她说明自己的感受。她明白了我的意思，我们拥抱着化解了隔阂。",
        "I visited Zoey and tried to explain to her how I felt. She understood what I meant.":
            "我去看了Zoey，试着向她说明自己的感受。她明白了我的意思。",
        "I nudged Nick to come clean and didn't try to keep his secret.":
            "我示意Nick主动坦白，没有替他保守秘密。",
        "Nick snapped after I nudged him to come clean about what he did together with Heather. It turned into a big fight, and he started throwing every DIK under the bus, telling everyone what they had told him in confidence.":
            "我示意Nick坦白他和Heather做过的事后，他彻底失控，引发了一场激烈争吵，还把每个DIK私下告诉他的秘密全都抖了出来。",
        "I didn't nudge Nick to come clean and kept his secret.":
            "我没有示意Nick坦白，替他保守了秘密。",
        "Nick snapped when he had to come clean about what he did together with Heather. It turned into a big fight, and he started throwing every DIK under the bus, telling everyone what they had told him in confidence.":
            "Nick被迫坦白他和Heather做过的事后彻底失控，引发了一场激烈争吵，还把每个DIK私下告诉他的秘密全都抖了出来。",
        "Nick said Rusty was in love with Jill and was salty about my relationship.":
            "Nick说Rusty一直爱着Jill，因此对我和Jill的关系心怀不满。",
        "Jacob told Nick he wanted to fuck Heather and Zoey.":
            "Jacob曾告诉Nick，他想和Heather及Zoey上床。",
        "Heather broke up with Tommy. Tommy went haywire because he found out someone had fucked her on Halloween.":
            "Heather和Tommy分手了。Tommy得知万圣节那晚有人和她上过床后彻底失控。",
        "Heather broke up with Tommy.": "Heather和Tommy分手了。",
        "Tommy accused Nick of being a traitor and did his best to expose him as one.":
            "Tommy指控Nick是叛徒，并竭力证明这一点。",
        "Nick admitted he was with the laptop during the party when Cathy's cluck got posted, but he denied having posted it.":
            "Nick承认Cathy的Rooster动态发布时，笔记本电脑在他手里，但否认是自己发的。",
        "John Boy was shocked and hurt to hear that I had lied to him about what I did with Heather on Halloween.":
            "John Boy Boy得知我对万圣节那晚与Heather发生的事撒了谎，既震惊又受伤。",
        "Leon, Marc, and Chen caught Beth putting up posters of Cathy and the DIKs.":
            "Leon、Marc和Chen抓到Beth正在张贴Cathy与DIKs们的海报。",
        "According to Leon, Beth conspired together with dorm girls against the DIKs.":
            "据Leon所说，Beth与宿舍女生合谋对付DIKs们。",
        "According to Leon, Kylie conspired together with dorm girls against the DIKs.":
            "据Leon所说，Kylie与宿舍女生合谋对付DIKs们。",
        "According to Leon, Tara conspired together with dorm girls against the DIKs.":
            "据Leon所说，Tara与宿舍女生合谋对付DIKs们。",
        "Derek confronted the DIKs about the hidden camera in his room, but no one confessed.":
            "Derek就房间里的隐藏摄像头质问DIKs们，但没人承认。",
        "I was accused of sending letters to the jocks with pictures of DIKs having sex with Arieth.":
            "我被指控向运动员兄弟会寄信，附上DIKs们与Arieth做爱的照片。",
        "Even though Heather cheated on him with me, Tommy defended me when Nick tried to throw me under the bus.":
            "尽管Heather背着Tommy和我发生了关系，Nick试图把我拖下水时，Tommy仍替我说话。",
        "Tommy defended me when Nick tried to throw me under the bus.":
            "Nick试图把我拖下水时，Tommy替我说了话。",
        "Nick didn't want to stay a DIK after the huge fight.":
            "那场激烈争吵后，Nick不想再留在DIK兄弟会。",
        "I told Derek that Nick couldn't be trusted.":
            "我告诉Derek，Nick不值得信任。",
        "I told Derek we needed more answers before we blamed Nick for everything.":
            "我告诉Derek，在把一切都怪到Nick头上前，我们需要更多答案。",
        "She tried to explain herself to me and told me how she was involved with the other dorm girls. I ended up telling her off.":
            "塔拉试着解释自己，并告诉我她如何卷入其他宿舍女生的计划。最后我严厉斥责了她。",
        "She tried to explain herself to me and told me how she was involved with the other dorm girls.":
            "塔拉试着解释自己，并告诉我她如何卷入其他宿舍女生的计划。",
        "Lily tried to make me feel better when I was bummed out about the big fight with the DIKs.":
            "我因DIKs们的激烈争吵而情绪低落时，Lily试着安慰我。",
        "Lily was annoyed that I wanted to talk to Quinn when I was with her.":
            "我陪着Lily时还想去找Quinn谈话，这让Lily很不高兴。",
        "I tried talking to Quinn on campus, but she didn't want to share what was bothering her. She also made a dig at me for hanging out with Lily.":
            "我在校园里试着和Quinn谈，但她不愿说出烦心事，还讽刺我和Lily待在一起。",
        "I tried talking to Quinn on campus, but she didn't want to share what was bothering her.":
            "我在校园里试着和Quinn谈，但她不愿说出烦心事。",
        "Jade confronted me about the Hell Week sex tape I recorded. Someone had sent it to her husband, and he wanted to file for a divorce.":
            "Jade就我在地狱周录下的性爱录像质问我。有人把录像发给了她丈夫，而他想提出离婚。",
        "I talked to Jade about her divorce, but she didn't want me to care about her anymore. I figured that was talk and tried to show her I still wanted to care.":
            "我和Jade谈了她离婚的事，但她不希望我再关心她。我觉得那只是气话，仍试着表明自己在乎她。",
        "I talked to Jade about her divorce, but she didn't want me to care about her anymore.":
            "我和Jade谈了她离婚的事，但她不希望我再关心她。",
        "Jade seemed sad. I bet it had something to do with her divorce.":
            "Jade看起来很难过，我猜这和她离婚有关。",
        "Ashley was worried that Anthony would find out that she had sex with Derek.":
            "Ashley担心Anthony会发现她和Derek上过床。",
        "I talked to Ashley about the letters the jocks had received. She had misunderstood Anthony about who sent them.":
            "我和Ashley谈起运动员兄弟会收到的信。她误解了Anthony关于寄信者的说法。",
        "I talked to Anthony about the letters the jocks had received. He told me he knew it wasn't me who sent them but that Chad blamed me.":
            "我和Anthony谈起运动员兄弟会收到的信。他知道信不是我寄的，但Chad认定是我。",
        "According to Anthony, Chad blamed me for sending letters to the jocks.":
            "据Anthony所说，Chad认定那些寄给运动员兄弟会的信是我送的。",
        "Camila told me she was sexually frustrated.":
            "Camila告诉我，她一直欲求不满。",
        "Camila told me that Riona was sick.":
            "Camila告诉我，Riona病了。",
        "I helped Camila with her sexual frustration by having sex with her on campus after class.":
            "下课后，我在校园里和Camila做爱，帮她纾解了欲望。",
        "You had sex with Camila on campus in episode 11.":
            "你在第11集中和Camila在校园里做了爱。",
        "Chad explained why he accused me of sending the letters to the jocks. He got mad when I told him it wasn't me. Someone blackmailed him for a reason I didn't understand.":
            "Chad解释了为何指控我向运动员兄弟会寄信。我说信不是自己寄的后，他非常生气。有人以我不清楚的理由勒索他。",
        "Nora banned Linda from the lab after she caught her eating multiple times.":
            "Nora多次抓到Linda在实验室吃东西后，禁止她再进入实验室。",
        "To Sally's dismay, Nora paired me with her in lab class after Linda was banned.":
            "Linda被禁止进入实验室后，Nora把我和Sally分到一组，这让Sally很不情愿。",
        "I told Nora I found lab work interesting and wanted to learn more about it.":
            "我告诉Nora，自己觉得实验工作很有趣，想进一步学习。",
        "I told Nora I didn't find lab work interesting when she asked me if I wanted to learn more about it.":
            "Nora问我是否想进一步学习实验工作时，我告诉她自己并不感兴趣。",
        "Sally tried to take full credit for the work we did together in lab class.":
            "Sally试图把我们在实验课上共同完成的工作全算成她的功劳。",
        "I told Derek that I thought my relationship with Sage would be long-term.":
            "我告诉Derek，自己认为和Sage会长期交往。",
        "I told Derek that I thought my relationship with Sage would be short-term.":
            "我告诉Derek，自己认为和Sage的关系不会长久。",
        "I told Derek I didn't know what kind of a relationship I would have with Sage in the future.":
            "我告诉Derek，自己不知道将来会和Sage保持怎样的关系。",
        "Derek advised me on what to do about the situation with Jade and Sage. I didn't like his reasoning, but I didn't have a better solution for my problem either.":
            "Derek建议我如何处理Jade和Sage的事。我不喜欢他的思路，却也想不出更好的办法。",
        "We wrote a lab report together, and it went better than I had expected. We started bonding.":
            "我和莎莉一起写了实验报告，过程比预想顺利，我们开始拉近了距离。",
        "I went to Lana's grave together with Jill. Jill told me about how Lana died and about Lana's boyfriend Jonathan.":
            "我和Jill一起去了Lana的墓地。Jill告诉我Lana的死因，以及Lana的男友Jonathan。",
        "How does you and me on Friday sound?":
            "周五你和我一起过，怎么样？",
        "Like the best Friday imaginable. Is Josy coming?":
            "听起来会是能想象到的最棒周五。Josy也来吗？",
        "I thought we could spend some time alone together if you don't mind. And with the whole relationship excuse and all, maybe it's best if we don't hang out together here this weekend? Also, Tommy's still pissed off at me.":
            "如果你不介意，我想和你单独待一会儿。考虑到对外那套关系说辞，也许这周末我们最好别在这里一起出现？而且Tommy还在生我的气。",
        "Understandable. It's a date. mphone_emoji_heart":
            "可以理解。那就约好了。mphone_emoji_heart",
        "Are you free on Friday night? I'd like to spend it with you.":
            "周五晚上有空吗？我想和你一起过。",
        "Free as a bird. Your place?":
            "自由得像只鸟。去你那里？",
        "Tommy's still pissed at me. Can we do your place?":
            "Tommy还在生我的气。能去你那儿吗？",
        "I'll check with Heather if she'll be here or not. Either way, we'll make it work. mphone_emoji_kiss":
            "我会问问Heather那天在不在。不管怎样，我们总有办法。mphone_emoji_kiss",
        "Hi, Maya! I hope it's not inappropriate, but I'd like to spend Friday night with you if you're up for it.":
            "嗨，Maya！希望不会太唐突，如果你愿意，我想和你一起过周五晚上。",
        "You wanna talk, huh?":
            "你想聊聊，是吧？",
        "I miss hanging out with you, and I feel like we should get together. I hope you agree.":
            "我很怀念和你一起玩的日子，觉得我们该聚一聚。希望你也这么想。",
        "I miss you too. I'll drop by, and we'll take it from there. Ok?":
            "我也想你。我会过去，到时再看怎么安排，好吗？",
        "Hi, Maya! Can we hang out on Friday? I'd love to catch up with you. It's been a while.":
            "嗨，Maya！周五能一起玩吗？我很想和你叙叙旧，我们有段时间没见了。",
        "It sure has. I'd love to. What do you wanna do?":
            "确实有一阵子了。我很乐意。你想做什么？",
        "We'll figure something out. My place or yours?":
            "到时总能想到的。去我那儿还是你那儿？",
        "I need to clean my room, and I'm not feeling up for it. Let's do yours. mphone_emoji_laugh":
            "我得打扫房间，可现在一点都不想动。去你那儿吧。mphone_emoji_laugh",
        "Wanna spend some quality time with me on Friday? It's been a while since we hung out, just the two of us.":
            "周五想和我好好待一会儿吗？我们已经很久没有两个人单独相处了。",
        "I'd love to. My place or yours? mphone_emoji_smile":
            "当然愿意。去我那儿还是你那儿？mphone_emoji_smile",
        "Yours, please. I need a change of scenery after studying all day in my room. mphone_emoji_smile":
            "去你那儿吧。我在房间里学了一整天，需要换个环境。mphone_emoji_smile",
        "Haha! Ok, I'll check with Heather if it's ok. mphone_emoji_laugh":
            "哈哈！好，我会问问Heather方不方便。mphone_emoji_laugh",
        "I punched Patrick when I saw him abusing Maya.":
            "我看到Patrick虐待Maya时，揍了他一拳。",
        "I confronted Patrick when I saw him abusing Maya.":
            "我看到Patrick虐待Maya时，出面制止了他。",
        "I defused the situation with Patrick when I saw him abusing Maya.":
            "我看到Patrick虐待Maya时，设法缓和了局面。",
        "I managed to steal Maya's contract from Patrick at Thanksgiving.":
            "感恩节时，我成功从Patrick手里偷到了Maya的合同。",
        "I failed to steal Maya's contract from Patrick at Thanksgiving.":
            "感恩节时，我没能从Patrick手里偷到Maya的合同。",
        "Derek opened his heart to me and told me about his family and why he's in college.":
            "Derek向我敞开心扉，讲了他的家庭，以及他上大学的原因。",
        "Maya": "Maya",
        "Jill": "Jill",
        "Patrick": "Patrick",
        "Dad": "爸爸",
        "Josy": "Josy",
        "Bella": "贝拉",
        "Zoey": "Zoey",
        "Nick": "Nick",
        "Rusty": "Rusty",
        "Jacob": "Jacob",
        "Tommy": "Tommy",
        "Heather": "Heather",
        "John Boy": "John Boy Boy",
        "Beth": "Beth",
        "Kylie": "Kylie",
        "Tara": "Tara",
        "Derek": "Derek",
        "You": "你",
        "Lily": "Lily",
        "Quinn": "Quinn",
        "Jade": "Jade",
        "Ashley": "Ashley",
        "Anthony": "Anthony",
        "Chad": "Chad",
        "Camila": "Camila",
        "Riona": "Riona",
        "Linda": "Linda",
        "Sally": "Sally",
        "Nora": "Nora",
        "Sage": "Sage",
        "Lana": "Lana",
        "Jonathan": "Jonathan",
        "Find out who X is": "查明谁是X",
        "Replace the cucumbers with something": "寻找黄瓜的替代品",
        "Get the girl a drink": "给那个女孩拿杯酒",
        "Dirty Bowl Mission [ep11_db_mission_progress]/5": "污污碗任务[ep11_db_mission_progress]/5",
        "DIKs' happiness increased!": "DIKs的满意度提高了！",
        "• The lack of activity decreased [name]'s happiness by {color=ff0000}-2%{/color}.":
            "• 缺少活动使[name]的满意度降低了{color=ff0000}-2%{/color}。",
        "• The {color=ffed00}Wet T-shirt Competition{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.":
            "• {color=ffed00}湿身T恤比赛{/color}使[name]的满意度提高了{color=00ff00}+2%{/color}。",
        "Say goodbye to Bianca": "向Bianca告别",
        "Talk to Camila": "和Camila谈谈",
        "Deal with unwanted guests": "处理不速之客",
        "Greet Tara": "迎接Tara",
        "Talk to Bianca": "和Bianca谈谈",
        "Talk to Nicole": "和Nicole谈谈",
        "Get approached by Becky": "等贝姬来搭话",
        "Talk to Elena": "和Elena谈谈",
        "Find Elena": "找到Elena",
        "Talk to Quinn": "和Quinn谈谈",
        "A totally random question... Do you think Camila is hot?":
            "随便问个问题……你觉得Camila性感吗？",
        "Another totally random question... Would you do her? You know, in a threesome?":
            "再随便问一个……你愿意和她做吗？我是说，来个三人行？",
        "Camila says hi.": "Camila向你问好。",
        "Talk to Lily": "和Lily谈谈",
        "Talk to Tara": "和Tara谈谈",
        "Talk to Tiffani": "和Tiffani谈谈",
        "Inspect the table with refreshments": "查看摆放茶点的桌子",
        "You failed to do The Dirty Bowl Mission.": "污污碗任务失败。",
        "Go to the fireplace": "前往壁炉旁",
        "Sandy": "Sandy",
        "Nicole": "Nicole",
        "Tiffani": "Tiffani",
        "Micha": "Micha",
        "Tania": "Tania",
        "Becky": "贝姬",
        "Clara": "Clara",
        "Gina": "Gina",
        "Leanne": "Leanne",
        "Mia": "Mia",
        "Carla": "Carla",
        "Erin": "Erin",
        "Felicia": "Felicia",
        "Rose": "萝丝",
    }

    def _s3_ep11_cn_active():
        try:
            return getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            return False

    def _s3_ep11_cn_replace_text(s):
        if _s3_ep11_prev_replace_text is not None:
            s = _s3_ep11_prev_replace_text(s)

        if not _s3_ep11_cn_active():
            return s

        return _s3_ep11_cn_exact.get(s, s)

    config.replace_text = _s3_ep11_cn_replace_text
