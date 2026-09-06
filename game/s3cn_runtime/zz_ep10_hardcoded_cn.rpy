# Being a DIK S3 Episode 10：补充 Ren'Py 翻译提取器未收录的动态显示文本。
# 仅在简体中文语言下替换显示字符串，不修改返回值、剧情变量或游戏逻辑。

init 999 python:
    _s3_ep10_prev_replace_text = config.replace_text

    _s3_ep10_cn_exact = {
        "Derek found a security camera in one of the ceiling spotlights in his room. He confided in me about it but didn't want anyone else to know until he could investigate it more.":
            "Derek在自己房间的一盏天花板射灯里发现了监控摄像头。他把这事告诉了我，但在进一步调查前不想让其他人知道。",
        "I chose to sit with Lily instead of Derek during English class.":
            "英语课上，我没有和Derek坐，而是选择了Lily。",
        "I chose to sit with Derek instead of Lily during English class.":
            "英语课上，我没有和Lily坐，而是选择了Derek。",
        "Someone put up posters on campus of our Hell Week photos with derogatory comments, and Derek got upset.":
            "有人把我们的地狱周照片配上侮辱性文字，贴遍校园，Derek对此很生气。",
        "Sally attended my science class, and I triggered her a bit about it.":
            "Sally来上了我的科学课，我拿这件事稍微刺激了她一下。",
        "Maya let Jill and Bella know about her student loan issues, and we all tried to come up with a plan to help her.":
            "Maya把学生贷款的问题告诉了Jill和贝拉，我们一起设法帮助她。",
        "Jill was supportive when Maya let her know about her student loan issues, and we all tried to come up with a plan to help her.":
            "Maya向Jill说明学生贷款的问题后，Jill很支持她，我们一起设法帮助Maya。",
        "Bella was supportive when Maya let her know about her student loan issues, and we all tried to come up with a plan to help her.":
            "Maya向贝拉说明学生贷款的问题后，贝拉很支持她，我们一起设法帮助Maya。",
        "Josy came up with the idea to have me act like Maya's boyfriend during Thanksgiving so that we could steal the contract Maya signed from Patrick.":
            "Josy提议让我在感恩节假扮Maya的男朋友，好趁机偷走Maya与Patrick签下的合同。",
        "I agreed to help Maya steal the contract she signed from Patrick by showing up at Thanksgiving dinner as Derek's and Maya's friend.":
            "我答应以Derek和Maya朋友的身份参加感恩节晚餐，帮Maya偷走她与Patrick签下的合同。",
        "Bella caught me cheating on the midterms but didn't report me for it. She warned me that she would if I did it again, and I told her she was overreacting.":
            "贝拉发现我在期中考试作弊，却没有举报。她警告我再犯就会举报，而我说她反应过度。",
        "Bella caught me cheating on the midterms but didn't report me for it. She warned me that she would if I did it again.":
            "贝拉发现我在期中考试作弊，却没有举报。她警告我再犯就会举报。",
        "Jill confronted me about Hell Week, and I told her what happened. She was obviously hurt by what I had done and had a hard time forgiving me.":
            "Jill质问我地狱周的事，我把经过告诉了她。我的所作所为显然伤透了她的心，她很难原谅我。",
        "I upset the DIKs when they found out that I had let preps into the mansion during our Halloween party.":
            "DIKs们发现我在万圣节派对上放富家子弟进了豪宅，对我很不满。",
        "DIKs' happiness decreased!": "DIKs们的满意度下降了！",
        "• Letting preps into the party decreased Jacob's happiness by {color=ff0000}10%{/color}.":
            "• 允许富家子弟参加派对，使Jacob的满意度下降了{color=ff0000}10%{/color}。",
        "• Letting preps into the party decreased Leon's happiness by {color=ff0000}10%{/color}.":
            "• 允许富家子弟参加派对，使Leon的满意度下降了{color=ff0000}10%{/color}。",
        "• Letting preps into the party decreased Rusty's happiness by {color=ff0000}10%{/color}.":
            "• 允许富家子弟参加派对，使Rusty的满意度下降了{color=ff0000}10%{/color}。",
        "• Letting preps into the party decreased Tommy's happiness by {color=ff0000}10%{/color}.":
            "• 允许富家子弟参加派对，使Tommy的满意度下降了{color=ff0000}10%{/color}。",
        "I let him crash on my couch because he felt weird about sleeping in his room.":
            "他觉得睡在自己房间里不自在，所以我让他在我的沙发上过夜。",
        "In math class, I could feel that I was on Philip's radar after cheating on the midterms.":
            "期中考试作弊后，我在数学课上能感觉到Philip已经盯上我了。",
        "Jacob": "Jacob",
        "Zoey": "Zoey",
        "Jonah": "Jonah",
        "Derek": "Derek",
        "Sup! The Halloween pics are almost ready. I'll send you a link for them later.":
            "嗨！万圣节的照片快弄好了，晚点把链接发给你。",
        "Dope! Can't wait. Loved the party, by the way.":
            "太棒了！等不及了。对了，我很喜欢那场派对。",
        "Awesome! It was so cool that you came. You've got such a great vibe. After Halloween, you got yourself a standing invite to all our parties. LOL":
            "太好了！你能来真的很酷，而且特别合群。万圣节之后，我们所有派对都长期欢迎你。哈哈",
        "Or if you wanna hang, you can drop by any time.":
            "或者你想一起玩的话，随时都可以过来。",
        "Cool.": "好啊。",
        "What up?": "最近怎么样？",
        "Not much. Stopped by Bret to check up on him. You?":
            "没什么。刚顺路去看了看Bret。你呢？",
        "Say hi from me. I'm working with Mom at a makeup store/beauty salon.":
            "替我向他问好。我在妈妈的美妆店兼美容院帮忙。",
        "You traded a tattoo parlor for a beauty salon? Haha!":
            "你从纹身店转战美容院了？哈哈！",
        "I know. I have to wear casual clothes to fit in here, too. And I'm not allowed to sketch while I'm at the register. Shit blows.":
            "我知道。我在这里还得穿休闲装来融入环境，而且站收银台时不准画画。真他妈烦。",
        "Yeah, dressing like a girl for once must suck. mphone_emoji_laugh":
            "是啊，难得穿得像个女孩，肯定难受坏了。mphone_emoji_laugh",
        "Yeah, you'd fit in here way better than I do. Slap on a dress and come join me. I'm happy to be back home, but the days feel different.":
            "对，你肯定比我更适合这里。套条裙子来陪我吧。回家我很开心，但每天的感觉都不一样了。",
        "LOL! And what about [name]?": "哈哈！那[name]呢？",
        "It's tough. He's not as happy to see me as I am to see him. I'm not sure if he will forgive me.":
            "很难说。他见到我时，没我见到他那么开心。我不知道他会不会原谅我。",
        "You're awesome, and he knows it. If he doesn't want you in his life anymore, it's his loss.":
            "你这么棒，他心里清楚。要是他不想再让你进入他的生活，那是他的损失。",
        "It's my loss, too. I can't believe I might lose my best friend like that.":
            "也是我的损失。我不敢相信自己可能就这样失去最好的朋友。",
        "I don't know what to tell you. I wish I had some words of wisdom for you, but I'm blank.":
            "我也不知道该说什么。真希望能给你几句明智的建议，可我脑子一片空白。",
        "It went better than I thought it would. We were both quite emotional about seeing each other again, but I think that's a good sign.":
            "比我预想的顺利。再次见面时我们都很激动，不过我觉得这是个好兆头。",
        "It sounds like it. Hell, I'd be emotional too if I reunited with a lifelong friend.":
            "听起来确实如此。要是和一辈子的老朋友重逢，我也会激动。",
        "Seeing him again made me realize how much I missed him. I've been thinking about him constantly since I got back home...":
            "再次见到他，我才意识到自己有多想他。回家以后，我一直在想他……",
        "How was the party?": "派对怎么样？",
        "It was great. He's got a lot of fun friends, and they were very interested in me. Some more than others.":
            "很棒。他有一群很有趣的朋友，他们对我都很感兴趣——有些人尤其感兴趣。",
        "Any cute guys?": "有帅哥吗？",
        "You sound like such a girl.": "你说话真像个小女生。",
        "That wasn't a no.": "你可没说没有。",
        "Whatever.": "随你怎么说。",
        "Give it time. Heading out. Bret says hi!":
            "慢慢来吧。我先走了。Bret向你问好！",
        "Later, chrome dome.": "回头见，亮脑门。",
        "I had to cancel my date with Nicole because I wanted to date Nora.":
            "因为想改约Nora，我不得不取消和Nicole的约会。",
        "Vinny tried to get under my skin when I was waiting for Quinn to finish her business with her uncle Buddy.":
            "我等Quinn和她叔叔Buddy谈完生意时，Vinny故意想激怒我。",
        "Quinn told me she was selling drugs and about how she does it. She used my company as protection without letting me know, and I told her I would have done it even if she asked.":
            "Quinn告诉我她在贩毒，也说明了交易方式。她没告诉我就拿我当掩护，而我告诉她，即使她开口请求，我也会帮她。",
        "Quinn told me she was selling drugs and about how she does it. She used my company as protection without letting me know, and I told her I didn't want to be a part of it.":
            "Quinn告诉我她在贩毒，也说明了交易方式。她没告诉我就拿我当掩护，而我告诉她，我不想参与其中。",
        "You had sex with Quinn in Rusty's car in episode 10.":
            "你在第10集中与Quinn在Rusty的车里发生了关系。",
        "I hung out with Zoey and showed her Mom's diary. There was an awkward tension between us, and she left without talking about it.":
            "我和Zoey一起玩，还给她看了妈妈的日记。我们之间的气氛很微妙，她没有谈这件事便离开了。",
        "She thanked me for telling her about Matthew and Olivia.":
            "我把Matthew和Olivia的事告诉她后，她向我道了谢。",
        "I messed with Tybalt during yoga class.":
            "我在瑜伽课上戏弄了Tybalt。",
        "Heather apologized for using me at the Halloween party. She felt remorseful about that night and said she planned on talking to Tommy about her feelings.":
            "Heather为万圣节派对上利用我而道歉。她对那晚很后悔，并说打算向Tommy坦白自己的感受。",
        "Heather apologized for her behavior at the Halloween party. She felt remorseful about that night and said she planned on talking to Tommy about her feelings.":
            "Heather为万圣节派对上的行为道歉。她对那晚很后悔，并说打算向Tommy坦白自己的感受。",
        "She invited me to a yoga class, and it ended up being too weird for my taste. I made fun of it, and I think she got annoyed.":
            "她邀请我去上瑜伽课，结果那套东西实在不合我的胃口。我拿它开了玩笑，她似乎有点生气。",
        "She invited me to a yoga class, and it ended up being too weird for my taste.":
            "她邀请我去上瑜伽课，结果那套东西实在不合我的胃口。",
        "Fight Troy to Quit.": "击败Troy即可退出。",
        "You had sex with Maya during movie night in episode 10.":
            "你在第10集的电影之夜与Maya发生了关系。",
        "I had a wonderful night alone with Maya in my room. We watched a movie and had sex.":
            "我和Maya在房间里度过了美好的二人之夜。我们看了电影，还发生了关系。",
        "I had a movie night with Maya in my room. But I ruined it by confessing that I still have feelings for her.":
            "我和Maya在房间里度过了电影之夜，却因坦白自己仍对她有感情而毁掉了气氛。",
        "I had a movie night with Maya in my room. We talked about our breakup and tried to get over it together.":
            "我和Maya在房间里度过了电影之夜。我们谈起分手的事，试着一起放下过去。",
        "I had a movie night with Maya in my room. It felt great to spend some alone time with her.":
            "我和Maya在房间里度过了电影之夜。能和她单独相处，感觉很好。",
        "I hung out with Josy, and we ended up confessing our feelings to each other. But we both felt guilty doing it because she's with Maya.":
            "我和Josy一起玩，最后彼此坦白了感情。但因为她正和Maya交往，我们都为此感到内疚。",
        "I hung out with Josy, and she ended up confessing her feelings to me.":
            "我和Josy一起玩，最后她向我坦白了感情。",
        "I hung out with Josy and had such a great time with her. We built a pillow fort that we had sex in.":
            "我和Josy一起玩，度过了非常愉快的时光。我们搭了一座枕头堡，还在里面发生了关系。",
        "You had sex with Josy in a pillow fort in episode 10.":
            "你在第10集中与Josy在枕头堡里发生了关系。",
        "Derek told me about his mom and her illness. It was tough hearing about it, and I understood why it was a sensitive issue for him and Maya.":
            "Derek告诉了我他妈妈的病情。听到这些很难受，我也明白这件事为什么会触动他和Maya。",
        "Nora is our teacher...and I have dated and fucked her in the past. She seemed worried about that.":
            "Nora是我们的老师……而我以前和她约会、上过床。她似乎对此很担心。",
        "Nora is our teacher...and I fucked her in the past. She seemed concerned about it.":
            "Nora是我们的老师……而我以前和她上过床。她似乎对此很担心。",
        "Nora doesn't have any humor when it comes to fucking around in her class.":
            "在Nora的课堂上胡闹，她可一点都不会觉得好笑。",
        "I ran into Cathy, and she told me she was happy with her new job. That felt good to hear, especially considering that she left B&R on such a bad note.":
            "我偶遇Cathy，她说自己很喜欢新工作。想到她当初与B&R闹得那么不愉快，听到这话让我很欣慰。",
        "I ran into Cathy, and she told me she was happy with her new job. I ended up having coffee with her at her place. We talked about the past, but that's all that happened.":
            "我偶遇Cathy，她说自己很喜欢新工作。后来我去她家喝了咖啡，我们聊了聊过去，仅此而已。",
        "I ran into Cathy, and she told me she was happy with her new job. I ended up having coffee with her at her place. We talked about the past and ended up having sex.":
            "我偶遇Cathy，她说自己很喜欢新工作。后来我去她家喝了咖啡，我们聊起过去，最后发生了关系。",
        "You had sex with Cathy at her place in episode 10.":
            "你在第10集中与Cathy在她家发生了关系。",
        "Check this sign out.": "看看这块牌子。",
        "LMAO! BE GRATEFUL! OR ELSE!": "笑死我了！给我感恩！不然有你好看！",
        "Right!? LOL! mphone_emoji_laugh": "对吧！？哈哈！mphone_emoji_laugh",
        "At the DIKs' Thanksgiving party, I ended the night in my tent together with Lily. It surprised me that she was cool with it since it didn't feel like it was a part of our rolling deal.":
            "在DIKs的感恩节派对上，我和Lily在帐篷里共度了夜晚。没想到她并不介意，因为这似乎不属于我们的轮换约定。",
        "I cleared it up with Nick. He promised he wouldn't tell anyone about us.":
            "我已经和Nick说清楚了。他保证不会把我们的事告诉别人。",
        "Are you sure you can trust him?": "你确定能信任他吗？",
        "Yes. I can trust him. But we should be more careful.":
            "确定，我信得过他。不过我们以后得更小心。",
        "Ok. I feel queasy thinking about this, but I have no choice but to let you handle it.":
            "好吧。一想到这件事我就不安，但也只能交给你处理了。",
        "Drive safely. Talk later.": "开车小心，回头再聊。",
        "I feel that I can trust him, but I'm not 100% sure. I will talk to him more about it later to make sure he's still cool with it. We should be more careful.":
            "我觉得可以信任他，但还不能百分之百确定。之后我会再和他谈谈，确认他真的不会介意。我们以后得更小心。",
        "Ok... Do that.": "好吧……就这么办。",
        "Nick told me he wouldn't tell anyone about seeing Bella and I kiss.":
            "Nick答应不会把他看到我和贝拉接吻的事告诉别人。",
        "I had lunch with Bella, and she told me she dreamt of starting her own business when she was younger.":
            "我和贝拉共进午餐，她告诉我，年轻时曾梦想开创自己的事业。",
        "During TV night with Bella, we ended up having anal sex on her couch while watching porn.":
            "和贝拉一起看电视时，我们边看色情片，边在她的沙发上做了肛交。",
        "You had anal sex with Bella at her place in episode 10.":
            "你在第10集于贝拉家中和她进行了肛交。",
        "Bella tried to talk to me about James, but it was very hard for her to discuss her marriage.":
            "贝拉试着和我谈起James，但要她谈论自己的婚姻非常艰难。",
        "The morning after Halloween, Jill tried to bond with my friends during breakfast.":
            "万圣节后的早晨，Jill在早餐时试着和我的朋友们拉近关系。",
        "Jill confronted me about Hell Week, and I told her what happened. She believed me, but it felt like I had disappointed her by doing what I did.":
            "Jill质问我地狱周发生的事，我把经过告诉了她。她相信我，但我的所作所为似乎令她很失望。",
        "Jill asked me to tell Bianca about what I saw Matthew do with Olivia during Halloween, and I did.":
            "Jill让我把万圣节时看到Matthew和Olivia之间发生的事告诉Bianca，我照做了。",
        "I told Bianca that Matthew was cheating on her with Olivia. Jill and I tried to console her when she got angry and upset.":
            "我告诉Bianca，Matthew背着她和Olivia偷情。她既愤怒又伤心，我和Jill试着安慰她。",
        "I met Jill's parents for lunch at their place. Jill was upset that it didn't match her expectations for different reasons.":
            "我去Jill父母家和他们共进午餐。由于种种原因，午餐没有达到Jill的预期，她很失落。",
        "Jill and I announced our relationship on social media.":
            "我和Jill在社交媒体上公开了恋情。",
        "You had sex with Jill in the hot tub in episode 10.":
            "你在第10集和Jill在热水浴缸中发生了关系。",
        "We had sex in the bathroom. She felt much more comfortable being sexual with me and wanted to try new things.":
            "我们在浴室里发生了关系。她和我做爱时自在了许多，也想尝试新花样。",
        "Tommy wanted to kick my ass when he found out that I had sex with Josy, but I did my best to defuse it.":
            "Tommy发现我和Josy上床后想揍我，我尽力平息了冲突。",
        "Josy was more positive than Maya when I told the DIKs they were my girlfriends.":
            "我告诉DIKs们Josy和Maya都是我的女朋友时，Josy的态度比Maya积极。",
        "Maya was concerned when I told the DIKs that Josy and Maya were my girlfriends.":
            "我告诉DIKs们Josy和Maya都是我的女朋友时，Maya对此感到担忧。",
        "According to Becky, there was a rumor about Josy, Maya, and me, saying that we were in a sexual three-way relationship.":
            "据Becky说，外面在传我、Josy和Maya是三人性爱关系。",
        "I told Nicole that I wanted to date her.": "我告诉Nicole，我想和她约会。",
        "I told Nicole that I didn't want to date her because I wasn't ready to commit to someone with a kid.":
            "我告诉Nicole，自己还没准备好和有孩子的人认真交往，所以不想和她约会。",
        "I told her that we could roll, and she was very excited about it. I wasn't sure what that meant, but she seemed to have it figured out.":
            "我告诉她我们可以维持轮换关系，她非常兴奋。我不太清楚那究竟意味着什么，但她似乎早有打算。",
        "I told her that I wasn't interested in rolling with her but still wanted to fuck her.":
            "我告诉她，自己对轮换关系没兴趣，但仍然想和她上床。",
        "She got mad at me for staying at the HOTs and eating breakfast despite her telling me to leave.":
            "她让我离开HOT姐妹会后，我却留下来吃早餐，因此她生我的气。",
        "Nicole says hi.": "Nicole向你问好。",
        "NO FUCKING WAY! YOU'RE NOT LYING!?": "绝不可能！你没骗我吧！？",
        "Never was. mphone_emoji_cool": "从来没有。mphone_emoji_cool",
        "You had sex with Nicole during your date at her place in episode 10.":
            "你在第10集和Nicole约会时，在她家中发生了关系。",
        "I had an awesome date with Nicole at her place, and we talked in a way we hadn't before.":
            "我在Nicole家和她度过了一次美妙的约会，也聊了许多以前从未谈过的话题。",
        "Nicole asked me questions related to dating her, and I answered as I saw fit.":
            "Nicole问了我一些与交往有关的问题，我按照自己的想法作答。",
        "You had sex with Nora during your date at her place in episode 10.":
            "你在第10集和Nora约会时，在她家中发生了关系。",
        "I told her to stop flirting with the DIKs to get my attention.":
            "我让她别再通过和DIKs们调情来吸引我的注意。",
        "Mini-[name] says thanks for the date. mphone_emoji_kiss":
            "迷你[name]感谢你的约会。mphone_emoji_kiss",
        "Thanks for the date. mphone_emoji_kiss": "谢谢你陪我约会。mphone_emoji_kiss",
        "I had a great time today. Thanks, Rio. mphone_emoji_heart":
            "今天玩得很开心。谢谢你，里奥娜。mphone_emoji_heart",
        "We spent the day at the arcade together. It was a fun date, but she didn't realize it was one until I pointed it out to her.":
            "我们一起在游戏厅玩了一整天。那是一次愉快的约会，可直到我点明，她才意识到这算约会。",
        "Tommy found out I'm having sex with Sage, and he wanted me to tell him all the details, while he overshared lots of his past experiences.":
            "Tommy发现我和Sage上了床，逼我说出所有细节，还过度分享了自己过去的大量经历。",
        "I told Sage about dating Josy and Maya and how they felt when I broke up with them. She was surprised and concerned about whether she could stay friends with them.":
            "我向Sage坦白了自己曾与Josy和Maya交往，以及分手后她们的感受。她很惊讶，也担心还能否继续和她们做朋友。",
        "I told Sage about my concerns when it comes to bringing her bad news and asking her sensitive questions. It felt good to bring it up, and she seemed understanding.":
            "我向Sage说出了自己在告诉她坏消息、询问敏感问题时的顾虑。能坦白这些让我感觉很好，她似乎也能理解。",
        "Sage told me about her youth and past hobbies, and we decided to go out on our first official date.":
            "Sage向我讲起年轻时的生活和爱好，我们决定进行第一次正式约会。",
        "Camila helped me and Sage talk about dating. And while playing Dots together, Sage used her to cheat in an arousing way.":
            "Camila帮助我和Sage聊起约会。一起玩Dots时，Sage还借她的身体用一种诱人的方式作弊。",
        "I'm outside. mphone_emoji_smile": "我在外面。mphone_emoji_smile",
        "Sage gave you a blowjob in the movie theater in episode 10.":
            "Sage在第10集的电影院里为你口交。",
        "Sage and I had a great classic date together. It started off weird, but as the night progressed, we found we were enjoying each other's company more than before. And, oh... She gave me a blowjob in the movie theater.":
            "我和Sage度过了一次很棒的传统约会。开场有些尴尬，但随着夜色渐深，我们比以往更享受彼此的陪伴。对了……她还在电影院里给我口交。",
        "Sage and I had a great classic date together. It started off weird, but as the night progressed, we found we were enjoying each other's company more than before.":
            "我和Sage度过了一次很棒的传统约会。开场有些尴尬，但随着夜色渐深，我们比以往更享受彼此的陪伴。",
        "Sage spent the night together with me in my tent. We had sex and shared an overall great night.":
            "Sage和我在帐篷里共度了一夜。我们发生了关系，整晚都很美好。",
        "You had sex with Sage in your tent after the DIKs' Thanksgiving party in episode 10.":
            "你在第10集DIKs感恩节派对后，于帐篷里和Sage发生了关系。",
        "Greet the blueberry": "和蓝莓人打招呼",
        "Talk to the nude man": "和裸体男人交谈",
        "Greet Zoey": "和Zoey打招呼",
        "Talk to John Boy": "和John Boy Boy交谈",
        "Acquire floating sphere": "取得漂浮的球体",
        "Talk to Derek": "和Derek交谈",
        "Find the shapeshifter": "寻找变形者",
        "Find Riona": "寻找Riona",
        "Play guitar by the fire": "在篝火旁弹吉他",
        "Play the Bard's song": "演奏吟游诗人的歌",
        "Talk to the elf": "和精灵交谈",
        "Talk to Jill": "和Jill交谈",
        "Find the white-haired maiden": "寻找白发少女",
        "Talk to Quinn": "和Quinn交谈",
        "Find your queen": "寻找你的女王",
        "Find Lily": "寻找Lily",
        "Inspect the rogue and the druid": "查看游荡者和德鲁伊",
        "Find Josy and Maya": "寻找Josy和Maya",
        "Talk to the druid": "和德鲁伊交谈",
        "Talk to Maya": "和Maya交谈",
        "Find the unicorn": "寻找独角兽",
        "Talk to Nora": "和Nora交谈",
        "Listen to the mermaid's song": "聆听美人鱼的歌声",
        "Go to the lake": "前往湖边",
        "Find the lifeguard": "寻找救生员",
        "Find the village idiot": "寻找村里的傻瓜",
        "Talk to the wicked witch": "和邪恶女巫交谈",
        "Find Heather": "寻找Heather",
        "Find Arieth": "寻找Arieth",
        "Talk to Sally": "和Sally交谈",
        "Talk to the rogue": "和游荡者交谈",
        "Talk to Josy": "和Josy交谈",
        "Talk to Rusty": "和Rusty交谈",
        "Play Beer Pong": "玩啤酒乒乓球",
        "Throw the white sphere": "投掷白色球体",
        "Talk to the blueberry": "和蓝莓人交谈",
        "Talk to Princess Nadia": "和娜迪亚公主交谈",
        "Fend off mosquitos": "赶走蚊子",
        "Talk to Jacob": "和Jacob交谈",
        "Go to the forest": "前往森林",
        "Explore the forest": "探索森林",
        "Your room": "你的房间",
        "Derek's room": "Derek的房间",
        "Dining room": "餐厅",
        "Jacob's room": "Jacob的房间",
        "Jamie's room": "Jamie的房间",
        "John Boy's room": "John Boy Boy的房间",
        "Left hallway": "左侧走廊",
        "Leon's room": "Leon的房间",
        "Main party room": "主派对厅",
        "Nick's room": "Nick的房间",
        "Outside": "室外",
        "Right hallway": "右侧走廊",
        "Rusty's room": "Rusty的房间",
        "Tommy's room": "Tommy的房间",
        "Upper main room": "楼上大厅",
        "Clean the mansion 0/5": "清理豪宅 0/5",
        "Check rooms for hidden cameras 0/5": "检查房间里的隐藏摄像头 0/5",
        "Check your desk": "检查你的书桌",
        "Talk to Leon": "和Leon交谈",
        "Talk to Melanie": "和Melanie交谈",
        "Water your flowers": "给花浇水",
        "Talk to Elena": "和Elena交谈",
        "Talk to Sarah": "和Sarah交谈",
        "Talk to Derek again": "再次和Derek交谈",
        "I chose to have a shroom at the DIKs' Thanksgiving, and I may have encouraged others to have one too.":
            "我在DIKs感恩节派对上吃了迷幻蘑菇，可能还怂恿了其他人一起吃。",
        "I didn't eat a shroom at the DIKs' Thanksgiving.":
            "我没有在DIKs感恩节派对上吃迷幻蘑菇。",
        "I didn't eat a shroom at the DIKs' Thanksgiving, and I tried to discourage my brothers from having one, with little success.":
            "我没有在DIKs感恩节派对上吃迷幻蘑菇，还劝兄弟们别吃，可没什么效果。",
        "I played Beer Pong with her but ended up losing. At least that's what people tell me. I don't even remember it.":
            "我和她玩啤酒乒乓球，结果输了。至少大家都这么说，我自己完全不记得。",
        "I played Beer Pong with her and won! And I made her strip as punishment.":
            "我和她玩啤酒乒乓球并赢了，还让她脱衣服作为惩罚。",
        "I played Beer Pong with her and won! But I was nice about it, and she didn't have to strip.":
            "我和她玩啤酒乒乓球并赢了，不过我手下留情，没有让她脱衣服。",
        "I played Beer Pong with her but ended up losing.":
            "我和她玩啤酒乒乓球，最后输了。",
        "I encouraged Jill to report Tybalt to the disciplinary committee.":
            "我鼓励Jill向纪律委员会举报Tybalt。",
        "I asked Jill to show Tybalt some mercy. Yes, he did a horrible thing, but ruining his life over it is a bit over the top.":
            "我劝Jill对Tybalt手下留情。他确实做了很过分的事，但因此毁掉他的人生也有些过头。",
        "You had sex with Riona during the DIKs' Thanksgiving party in episode 10.":
            "你在第10集DIKs感恩节派对期间和Riona发生了关系。",
        "I had sex with Riona at the DIKs' Thanksgiving, and we had a nice heart-to-heart about dating.":
            "我在DIKs感恩节派对上和Riona发生了关系，还就约会问题进行了一次真诚的交谈。",
        "I tried my best to talk to Sally without pissing her off. It didn't go well.":
            "我尽力不惹Sally生气地和她交谈，但结果并不顺利。",
        "Jacob asked me if I was cool with him hooking up with Zoey. I told him I was. I didn't want to make that choice for Zoey if that was something she wanted.":
            "Jacob问我是否介意他和Zoey勾搭。我说不介意，因为如果Zoey也愿意，我不想替她作决定。",
        "Jacob asked me if I was cool with him hooking up with Zoey. I told him I wasn't.":
            "Jacob问我是否介意他和Zoey勾搭，我告诉他自己很介意。",
        "Jill was concerned about me when she realized I had eaten a shroom. She asked me not to do drugs again.":
            "Jill发现我吃了迷幻蘑菇后很担心，让我别再碰毒品。",
        "Jill and I talked about her sister and seasons. I made her listen to some of my - and Lana's - favorite music.":
            "我和Jill聊起她的姐姐和四季，还让她听了几首我和Lana都喜欢的歌。",
        "John Boy asked me if I found Elena hot and floated the idea of having a threesome with her, or maybe he just wanted me to fuck her. I don't know what it was, but it was weird.":
            "John Boy Boy问我是否觉得Elena性感，还试探着提起和她三人行——也可能只是想让我操她。我也不清楚，反正很奇怪。",
        "Nick told me he fucked Heather and that he's in love with her. I told him that she used me at Halloween.":
            "Nick告诉我，他和Heather上了床，而且爱上了她。我告诉他，Heather在万圣节时利用过我。",
        "Nick told me he fucked Heather and that he's in love with her. I told him that she tried to use me at Halloween.":
            "Nick告诉我，他和Heather上了床，而且爱上了她。我告诉他，Heather在万圣节时试图利用我。",
        "Nick told me he fucked Heather and that he's in love with her. I advised him not to tell Tommy about it.":
            "Nick告诉我，他和Heather上了床，而且爱上了她。我建议他不要把这件事告诉Tommy。",
        "Nick told me he fucked Heather and that he's in love with her. I advised him to tell Tommy about it.":
            "Nick告诉我，他和Heather上了床，而且爱上了她。我建议他把这件事告诉Tommy。",
        "Lily explained to me why she didn't want us to do romantic things together and get to know each other at a deeper level. It sounded like she was trying to protect herself from it. I let her give me a blowjob to deflect the talk. It sounds weird, but I think it worked.":
            "Lily解释了为什么不想和我做浪漫的事，也不愿彼此深入了解。听起来她是在保护自己。我让她给我口交来转移话题——虽然很奇怪，但似乎奏效了。",
        "Lily gave you a blowjob during the DIKs' Thanksgiving party in episode 10.":
            "Lily在第10集DIKs感恩节派对期间为你口交。",
        "Zoey wanted me to open up about my feelings for her, and I did. She seemed stunned when I told her that she was my first love.":
            "Zoey希望我坦白对她的感情，我照做了。听说她是我的初恋时，她似乎惊呆了。",
        "Sage and I agreed that we're a couple. She felt a bit iffy about it happening this fast, but in the end, she couldn't deny that we've reached that point in our relationship.":
            "我和Sage确认成了情侣。她对进展如此迅速有些迟疑，但最终也无法否认我们的关系已经走到了这一步。",
        "Sage and I played Beer Pong, and I beat her ass without showing her any mercy.":
            "我和Sage玩啤酒乒乓球，并且毫不留情地击败了她。",
        "Sage and I played Beer Pong, and she made me strip in front of people.":
            "我和Sage玩啤酒乒乓球，她让我当众脱了衣服。",
        "I won at Beer Pong against Jill, but she wasn't comfortable playing with the strip rules.":
            "我在啤酒乒乓球中赢了Jill，但她不适应脱衣惩罚规则。",
        "I lost at Beer Pong against Jill and showed my dick to people watching.":
            "我玩啤酒乒乓球输给了Jill，还向围观的人露出了鸡巴。",
        "I lost at Beer Pong against Jill but didn't show my dick to people watching.":
            "我玩啤酒乒乓球输给了Jill，但没有向围观的人露出鸡巴。",
        "Josy got dared to play Beer Pong against me, and I beat her hard. She had to strip in front of people and felt embarrassed.":
            "Josy接受大冒险和我玩啤酒乒乓球，被我轻松击败。她不得不当众脱衣，感觉很尴尬。",
        "Josy got dared to play Beer Pong against me, and somehow I lost to her. I ended up showing people my dick as a part of the game.":
            "Josy接受大冒险和我玩啤酒乒乓球，不知怎么我竟输给了她，最后按照规则向众人露出了鸡巴。",
        "Nora called me and said she couldn't continue to date me because of the teacher-student relationship we have. I asked her to rethink her decision, but she felt decided on it.":
            "Nora打电话说，由于我们的师生关系，她无法继续和我约会。我请她重新考虑，可她似乎心意已决。",
        "Nora called me and said she couldn't continue to date me because of the teacher-student relationship we have. I told her I understood what she was getting at, even though I didn't want to stop seeing her like that.":
            "Nora打电话说，由于我们的师生关系，她无法继续和我约会。虽然我不想停止这种关系，但还是告诉她自己理解她的顾虑。",
        "Quinn told me she's not planning on staying in college for long and that her goal with selling drugs is to make lots of money.":
            "Quinn告诉我，她不打算在大学久留，贩毒的目标就是赚一大笔钱。",
        "The Dare Game lives on, and because of it, I had public sex with Josy and Maya at the DIKs' Thanksgiving party.":
            "大冒险游戏仍在继续，我也因此在DIKs感恩节派对上和Josy、Maya当众做爱。",
        "You had sex with Josy and Maya at the DIKs' Thanksgiving party in episode 10.":
            "你在第10集DIKs感恩节派对上和Josy、Maya发生了关系。",
        "Josy told me I was delusional for thinking she'd want to remain my friend after breaking up with her.":
            "Josy说我太异想天开，竟以为分手后她还愿意继续和我做朋友。",
        "Josy tried to explain Maya's concerns about me telling everyone about our relationship. I felt stupid for not realizing it myself, but when I told Tommy and the rest about us, it felt like the smart solution to our problem.":
            "Josy试着解释Maya为什么担心我公开我们的关系。我没能自己意识到这一点，感觉很蠢，但向Tommy等人坦白时，那明明像是解决问题的明智办法。",
        "I talked to Nick about Vinny being at our Halloween party, but he didn't know he'd been there until Tommy had mentioned it.":
            "我和Nick聊起Vinny参加万圣节派对的事，可在Tommy提起之前，他根本不知道Vinny来过。",
        "The jocks were pissed that Quinn fooled them at Halloween, and the DIKs agreed to share the HOTs with them to get an end to the constant fighting between the frats.":
            "运动员们因万圣节被Quinn耍了而非常愤怒，DIKs们同意和他们共享HOT姐妹，以结束两个兄弟会之间持续不断的争斗。",
        "Rusty felt bad about Micha, and I tried my best to be there for him.":
            "Rusty因Micha的事很难受，我尽力陪在他身边。",
        "I helped Derek search the DIKs' mansion for hidden cameras, but I couldn't find any.":
            "我帮Derek在DIKs豪宅里寻找隐藏摄像头，但一无所获。",
        "John Boy told me he saw Heather exit Jacob's or Nick's room, thinking she spent the night with one of them. I shared what I knew about Heather with him.":
            "John Boy Boy说他看到Heather从Jacob或Nick的房间出来，怀疑她和其中一人过了夜。我把自己知道的Heather的事告诉了他。",
        "John Boy told me he saw Heather exit Jacob's or Nick's room, thinking she spent the night with one of them. I didn't share what I knew about Heather with him.":
            "John Boy Boy说他看到Heather从Jacob或Nick的房间出来，怀疑她和其中一人过了夜。我没有把自己知道的Heather的事告诉他。",
        "Riona flirted with Jamie in front of me.": "Riona当着我的面和Jamie调情。",
        "Maya felt weird about letting people know about our relationship, even if the lie I told about us protected her and Josy somewhat.":
            "Maya对公开我们的关系感到不自在，尽管我编造的说法在一定程度上保护了她和Josy。",
        "DIKs' happiness increased slightly!": "DIKs们的满意度略有提升！",
        "DIKs' happiness increased!": "DIKs们的满意度提升了！",
        "All DIKs' happiness increased!": "所有DIKs的满意度都提升了！",
    }

    _s3_ep10_cn_wrapped = {
        "Change your quote as you wish.": "按你的想法修改留言。",
        "Type your quote as you wish.": "按你的想法填写留言。",
        "Yearbook quote cannot be empty.": "年鉴留言不能为空。",
        "Keep words shorter than 20 characters each.": "每个单词请控制在20个字符以内。",
        "Keep it clean. No profanity.": "请文明填写，不要使用脏话。",
        "You can turn on color blindness support in Settings.": "你可以在设置中开启色盲辅助模式。",
        "The Brawler app works during some free roam events.": "格斗应用可在部分自由活动事件中使用。",
    }

    def _s3_ep10_cn_active():
        try:
            return getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            return False

    def _s3_ep10_cn_replace_text(s):
        if _s3_ep10_prev_replace_text is not None:
            s = _s3_ep10_prev_replace_text(s)

        if not _s3_ep10_cn_active():
            return s

        if s.startswith("{size=-") and s.endswith("Your Nerd Notes perk lost its effect{/size}"):
            return s.replace("Your Nerd Notes perk lost its effect", "你的‘学霸笔记’特长已失效")

        if s.startswith("{size=-") and s.endswith("{/size}"):
            for _old, _new in _s3_ep10_cn_wrapped.items():
                if _old in s:
                    return s.replace(_old, _new)

        if s.startswith("DIKs' Thanksgiving Party\n"):
            return (s.replace("DIKs' Thanksgiving Party", "DIK感恩节派对")
                     .replace("Activities:", "活动：")
                     .replace("Total Party Score:", "本场派对得分：")
                     .replace("Total Score:", "总分：")
                     .replace("Multiplier:", "倍率：")
                     .replace("Rank:", "评级："))

        if s.startswith("Clean the mansion "):
            return s.replace("Clean the mansion", "清理豪宅", 1)

        if s.startswith("Check rooms for hidden cameras "):
            return s.replace("Check rooms for hidden cameras", "检查房间里的隐藏摄像头", 1)

        if s.startswith("• The {color=ffed00}"):
            _increased = " activity increased " in s
            _decreased = " activity decreased " in s
            s = (s.replace("Hot Dogs", "热狗")
                 .replace("B.Y.O.B.", "自带酒水")
                 .replace("Leftover Alcohol", "剩余酒水")
                 .replace("New Alcohol", "新购酒水")
                 .replace("BBQ Pork", "烤猪肉")
                 .replace("BBQ Quality Meat", "优质烧烤肉")
                 .replace("Beer Pong", "啤酒乒乓球")
                 .replace("Derek's happiness", "德里克的满意度")
                 .replace("Jamie's happiness", "杰米的满意度")
                 .replace("John Boy's happiness", "约翰小子的满意度")
                 .replace("Leon's happiness", "利昂的满意度")
                 .replace("Nick's happiness", "尼克的满意度")
                 .replace("Rusty's happiness", "拉斯蒂的满意度")
                 .replace("Tommy's happiness", "汤米的满意度")
                 .replace("Jacob's happiness", "雅各布的满意度")
                 .replace("all DIKs' happiness", "所有DIK的满意度"))
            if _increased:
                return s.replace("• The ", "• ", 1).replace(" activity increased ", "活动使", 1).replace(" by ", "提升", 1)
            if _decreased:
                return s.replace("• The ", "• ", 1).replace(" activity decreased ", "活动使", 1).replace(" by ", "下降", 1)

        if s.startswith("• Having {color=ffed00}Nothing{/color} as an activity decreased all DIKs' happiness by "):
            return (s.replace("• Having {color=ffed00}Nothing{/color} as an activity decreased all DIKs' happiness by ",
                              "• {color=ffed00}没有安排活动{/color}使所有DIK的满意度下降", 1))

        return _s3_ep10_cn_exact.get(s, s)

    config.replace_text = _s3_ep10_cn_replace_text
