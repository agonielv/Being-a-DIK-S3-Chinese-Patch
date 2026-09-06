# Being a DIK S3 Episode 12 B15：补充翻译提取器未收录的 Bio、短信与动态记录。
# 仅替换最终显示文本，不修改作为条件判断或返回值使用的剧情变量。

init 1002 python:
    _s3_ep12_b15_prev_replace_text = config.replace_text

    _s3_ep12_b15_cn_exact = {
        "Dad": "爸爸",
        "Zoey": "Zoey",
        "Troy": "Troy",
        "Bianca": "Bianca",
        "Jill": "Jill",
        "Tybalt": "Tybalt",
        "Sally": "Sally",
        "Nick": "Nick",
        "Jamie": "Jamie",
        "Magnar": "Magnar",
        "Bert": "Bert",
        "Ron": "Ron",
        "Rich": "Rich",
        "Isabella": "Isabella",
        "Josy": "Josy",
        "Maya": "Maya",
        "Sage": "Sage",
        "Riona": "Riona",
        "Dawe": "Dawe",
        "Sarah": "Sarah",
        "Elena": "Elena",
        "Leon": "Leon",
        "Chen": "Chen",
        "Marc": "Marc",
        "I told Dad about Bella and our relationship. He was surprised to learn that she was my teacher, but agreed to meet her.":
            "我把贝拉和我们的关系告诉了爸爸。他得知贝拉是我的老师后很惊讶，但还是答应见她。",
        "Dad told me he gave me Mom's diary so I could learn the truth he couldn't tell me. I was upset that the diary showed him in a bad light and didn't want to read it anymore.":
            "爸爸说，他把妈妈的日记交给我，是想让我知道那些他无法亲口说出的真相。日记把他写得很不堪，这让我很难受，也不想再读下去了。",
        "I told Zoey what I had been up to since starting college. I didn't want to keep anything from her. She took the news well, and it didn't turn her away.":
            "我把上大学以来做过的事都告诉了Zoey，不想对她有所隐瞒。她接受得很好，也没有因此疏远我。",
        "I went to check up on Zoey during Christmas, and it didn't go well. We need to figure out whether we can stay friends or if we need to move on permanently.":
            "圣诞节期间我去看了Zoey，但结果并不愉快。我们必须弄清楚还能不能继续做朋友，还是该彻底放下彼此。",
        "Troy thanked me for not spreading information on his and Chad's relationship further.":
            "Troy感谢我没有继续散播他和Chad关系的消息。",
        "You had sex with Bianca in your room in episode 12.": "你在第12集和Bianca在自己的房间里发生了关系。",
        "We did it. We went all the way. It felt wrong, but also right.": "我们做了，而且做到了最后。感觉既不该如此，却又像是理所当然。",
        "I cheated on Jill with Bianca.": "我背着Jill和Bianca发生了关系。",
        "I fought in the fighting competition and won! It felt amazing to win in front of an audience, and a scout named Jen Byson approached me after to make a deal.":
            "我参加了格斗比赛并赢得冠军！在观众面前获胜的感觉太棒了。赛后，一位名叫Jen·拜森的星探找我谈合作。",
        "I fought in the fighting competition, but I lost. It was tough to accept defeat, but in the end, I wasn't good enough.":
            "我参加了格斗比赛，却输了。失败很难接受，但归根结底，是我的实力还不够。",
        "Nikita played bass at the faculty's Christmas party. She and her brother Tim were hired to perform together with Tybalt.":
            "Nikita在教职工圣诞派对上弹了贝斯。她和哥哥蒂姆受雇与Tybalt同台演出。",
        "I played at the faculty's Christmas party, and it went well. After my performance, I was approached by David Cerus Baxter, who offered me a summer job at his company.":
            "我在教职工圣诞派对上的演出很顺利。演出后，David·塞勒斯·巴克斯特找到我，并邀请我暑假去他的公司工作。",
        "Derek shoved Muriel Storch's trumpet up his asshole.": "Derek把穆丽尔·斯托奇的小号塞进了自己的屁眼。",
        "Tybalt performed at the Christmas party, and he didn't make a fool of himself. He introduced everyone to his new girlfriend, Paula.":
            "Tybalt在圣诞派对上表演了，而且没让自己出丑。他还向大家介绍了新女友保拉。",
        "Sally told me the truth about what the tri-betas had been up to.": "Sally把三贝塔一直在做的事情告诉了我。",
        "Nick watched porn on the DIKs' laptop, which led to Sally being able to swipe it.": "Nick用DIKs的笔记本电脑看色情片，给了Sally偷走电脑的机会。",
        "Jamie's lost phone was stolen by Sally. Magnar used it to find incriminating photos from the DIKs' PinkCloud account.":
            "Sally偷走了Jamie遗失的手机。Magnar利用它，从DIKs的PinkCloud账号里找到了能抓住他们把柄的照片。",
        "Magnar has been cheating on tests with the help of Excalibus, and he's used that USB stick to rule the tri-betas the way he wants.":
            "Magnar一直靠Excalibus考试作弊，还利用那个U盘按自己的意愿控制三贝塔。",
        "Ron, Magnar, and Bert were responsible for posting the cluck of Cathy.": "Ron、Magnar和Bert就是发布Cathy那条帖子的幕后黑手。",
        "Magnar and Ron caused the Halloween blackout.": "万圣节派对的停电是Magnar和Ron造成的。",
        "Rich's father sold the DIKs' mansion to them. In doing so, the tri-betas were evicted.": "Rich的父亲把豪宅卖给了DIKs，三贝塔因此被赶了出去。",
        "The box on my desk has been the reason why the DIKs have been involved in so much drama.": "我桌上的盒子正是DIKs卷入这么多风波的根源。",

        "I broke up with Bella to be with Zoey. Bella had learned about what I did with Jade and was severely disappointed in me.":
            "为了和Zoey在一起，我与贝拉分手了。贝拉得知我和Jade做过什么后，对我极度失望。",
        "Bella had learned about what I did with Jade and was severely disappointed in me.": "贝拉得知我和Jade做过什么后，对我极度失望。",
        "I broke up with Bella to be with Zoey. She was mature about it, but seemed hurt and annoyed.":
            "为了和Zoey在一起，我与贝拉分手了。她处理得很成熟，但显然既受伤又恼火。",
        "I talked to Bella about my concerns regarding her past. We didn't reach any clarity in what that meant for us.":
            "我把自己对贝拉过去的顾虑告诉了她，但我们依然没弄清这对我们的关系意味着什么。",
        "Bella broke up with me. What I had done to Jade and Sage was too much to deal with, on top of the other challenges we already faced.":
            "贝拉和我分手了。除了我们本就面对的难题，我对Jade和Sage做过的事更让她无法承受。",
        "Bella sat down and told me everything I needed to know about her past.": "贝拉坐下来，把我需要知道的过去全都告诉了我。",
        "I broke up with Bella because I felt that my heart wasn't fully in it.": "我觉得自己没有全心投入这段感情，因此和贝拉分手了。",
        "I told her that I loved her and she reciprocated. We both wanted to continue our relationship despite everything that had happened.":
            "我告诉她我爱她，她也回应了我的感情。尽管发生了这么多事，我们都想继续这段关系。",
        "I told her that I loved her, but she wasn't ready to say it back. We both wanted to continue our relationship despite everything that had happened.":
            "我告诉她我爱她，但她还没准备好说出同样的话。尽管发生了这么多事，我们都想继续这段关系。",
        "Bella met my dad and I was relieved when they got along.": "贝拉见了我爸爸，看到他们相处融洽，我松了一口气。",
        "Dad met Bella and I was relieved when they got along.": "爸爸见了贝拉，看到他们相处融洽，我松了一口气。",
        "I broke up with Jill to be with Zoey. Understandably, Jill didn't receive the news well.":
            "为了和Zoey在一起，我与Jill分手了。Jill自然无法平静地接受这个消息。",
        "Jill gave me Lana's guitar for Christmas. I found some weed hidden in the speaker and Jill got upset from learning about it.":
            "Jill把Lana的吉他作为圣诞礼物送给我。我在音箱里发现了一些大麻，Jill知道后很难过。",
        "I told Jill about what happened with Zoey and she got even more concerned about my friendship to Zoey.":
            "我把与Zoey之间发生的事告诉了Jill，她因此更加担心我和Zoey的友谊。",
        "Jill tried on Lana's old clothes for me. She seemed to like wearing them, even though they weren't her style.":
            "Jill为我试穿了Lana的旧衣服。尽管不是她平常的风格，她似乎还挺喜欢。",
        "I broke up with Josy and Maya to be with Zoey. Josy seemed hurt by it.": "为了和Zoey在一起，我与Josy和Maya分手了。Josy似乎深受伤害。",
        "I broke up with Josy and Maya to be with Zoey. Josy took it well, but she didn't think she could stay my friend after this.":
            "为了和Zoey在一起，我与Josy和Maya分手了。Josy接受得还算平静，但觉得以后无法继续和我做朋友。",
        "I broke up with Josy and Maya to be with Zoey. Maya seemed hurt by it.": "为了和Zoey在一起，我与Josy和Maya分手了。Maya似乎深受伤害。",
        "I broke up with Josy and Maya to be with Zoey. Maya admitted that she didn't feel the final click.":
            "为了和Zoey在一起，我与Josy和Maya分手了。Maya承认，她始终没感觉到关系真正契合。",
        "I told Josy and Maya about what happened with Zoey and they took it well. They could relate to the situation better than I thought they would.":
            "我把与Zoey之间发生的事告诉了Josy和Maya。她们接受得很好，也比我想象中更能理解这种处境。",
        "I visited Josy's mom Iris over Christmas. I defended Josy in the conversation, and Iris liked that.":
            "圣诞节期间，我拜访了Josy的妈妈Iris。谈话中我替Josy说话，Iris很欣赏这一点。",
        "I visited Josy's mom Iris over Christmas. I let Josy stand up for herself in the conversation.":
            "圣诞节期间，我拜访了Josy的妈妈Iris。谈话中我让Josy自己表达立场。",
        "You had sex with Josy at her mom's place in episode 12.": "你在第12集于Josy妈妈家和Josy发生了关系。",
        "You had sex with Maya in her dorm in episode 12.": "你在第12集和Maya在她的宿舍里发生了关系。",
        "I spent some time alone with Maya in her dorm. We joked around, shared personal stories and were intimate.":
            "我和Maya在她的宿舍里独处了一阵。我们互相打趣、分享私事，也有了亲密接触。",
        "Sage broke up with me after learning what I had done with Jade from Tybalt.": "Sage从Tybalt那里得知我和Jade做过什么后，和我分手了。",
        "Sage was inconsolable after learning what I had done with Jade from Tybalt.": "Sage从Tybalt那里得知我和Jade做过什么后，伤心得无法平复。",
        "I broke up with Sage to be with Zoey. Sage didn't take it well.": "为了和Zoey在一起，我与Sage分手了。Sage无法接受。",
        "I broke up with Sage without telling her the real reason why. She was hurt and didn't understand why I couldn't tell her the truth.":
            "我没有告诉Sage真正原因就与她分手了。她很受伤，也不明白我为什么不肯说出真相。",
        "Sage broke up with me after I told her what I had done with Jade. She was inconsolable and felt betrayed.":
            "我坦白自己和Jade做过什么后，Sage和我分手了。她伤心得无法平复，也觉得遭到了背叛。",
        "I told Sage about what happened with Zoey at the Christmas party. Sage was concerned about my friendship with Zoey.":
            "我把圣诞派对上与Zoey发生的事告诉了Sage。Sage对我和Zoey的友谊感到担忧。",
        "Sage surprised me after my finals with food, drinks and a movie. It showed me that she truly cared about me. It was heartwarming.":
            "期末考试后，Sage带着食物、饮料和电影给了我一个惊喜。她是真的在乎我，这让我心里很温暖。",

        "Hey, it's Bianca.": "嗨，我是Bianca。",
        "Hey, I changed my mind about this. I'm out. You should delete my number. I won't tell anyone what happened.":
            "嗨，我改变主意了。我退出。把我的号码删了吧，我不会把发生的事告诉任何人。",
        "Weird, but ok.": "有点奇怪，不过好吧。",
        "I was wondering when you'd shoot me a message.": "我还在想你什么时候才会给我发消息。",
        "It's been on my mind since the party. I went back and forth about whether to send one. How about you?":
            "派对之后我一直在想这件事，纠结了很久要不要发消息。你呢？",
        "I'm the same as you. We're bad...": "我也一样。我们真坏……",
        "Yep. So bad...": "对，坏透了……",
        "I ended my flirt with Bianca.": "我结束了和Bianca的暧昧。",
        "At least we're bad together. So, what are we going to do about it? mphone_emoji_tongue":
            "至少我们是一起使坏。那么，我们打算怎么办？mphone_emoji_tongue",
        "What do you want to do about it?": "你想怎么办？",
        "I asked you first. I wanna see how daring you'd get.": "是我先问你的。我想看看你到底有多大胆。",
        "I thought that instead of me touching myself while thinking about you... How about you touch yourself thinking about me?":
            "我在想，与其让我一边想着你一边自慰……不如你也想着我摸自己？",
        "I know what I want to do... I get hard thinking about you.": "我知道自己想做什么……一想到你，我就硬了。",
        "Do you touch yourself when you think about me?": "你想到我时会摸自己吗？",
        "I would do that, but my imagination sucks. I have a difficult time picturing your face and body. Can you help me out?":
            "我倒是想，可我的想象力太差，很难在脑海里看清你的脸和身体。能帮帮我吗？",
        "Tell me how.": "说说要我怎么帮。",
        "Send me some sexy pictures. That would get me going.": "发几张性感照片给我，那样我就有感觉了。",
        "I'll do it if you do it too.": "你也发的话，我就发。",
        "Deal.": "成交。",
        "How about that?": "这样怎么样？",
        "Wow! That was way more than I thought you'd send. You're so sexy! That will do the trick.":
            "哇！你发得比我想象中大胆多了。你太性感了！这下肯定管用。",
        "This one is for you.": "这张送给你。",
        "Fuck. It looks delicious. I want to put that in my mouth.": "操，看起来真美味。我想把它含进嘴里。",
        "I'm stroking it to you now.": "我现在正看着你撸。",
        "Mmm... I wish I were there. I'm rubbing myself to you.": "嗯……真希望我也在那里。我正看着你摸自己。",
        "What would you do if you were here with me?": "如果你现在和我在一起，你会怎么做？",
        "I'd tell myself to take it slow with you, but honestly, I'd sit on you and let you penetrate me hard.":
            "我会告诉自己要慢慢来，但老实说，我会直接骑到你身上，让你狠狠插进来。",
        "I'd bounce up and down on you and push your face into my tits.": "我会在你身上上下起伏，把你的脸按进我的奶子里。",
        "Fuck! You're gonna make me cum talking like that. Go on.": "操！你再这么说，我就要射了。继续。",
        "My tight pussy could barely handle your big cock, and I'd moan loudly from having it inside.":
            "我的小穴紧得几乎容不下你的大鸡巴，被你插进去时我会大声呻吟。",
        "You'd bend me over on your bed and take me from behind. I would push my ass toward you forcefully until you came inside me.":
            "你会把我按在床上，从后面狠狠干我。我会用力把屁股迎向你，直到你射进我体内。",
        "Look at what you made me do...": "看看你害我做了什么……",
        "Mmm... I like the look of that. I want to clean that up with my tongue...": "嗯……我喜欢这个样子。真想用舌头帮你舔干净……",
        "I wish you did.": "真希望你能来。",
        "Do you have time to meet me soon? It has to be discreet.": "最近有时间见面吗？必须保密。",
        "How about during winter break? Most will leave and go back home to their families. I bet I can get the place to myself. At least, there will be fewer prying eyes.":
            "寒假怎么样？大多数人都会回家，我应该能独占这里。至少到时候不会有那么多人盯着。",
        "Let me know when. But I'll need a heads up.": "时间定了告诉我，不过得提前通知。",
        "Let me know when. Even if it's on short notice.": "时间定了告诉我，就算临时通知也行。",
        "You got it. Thanks for the pictures. I'll put them to good use until we meet.": "没问题。谢谢你的照片，见面前我会好好利用它们。",
        "I continued my flirt with Bianca. We shared some lewd pictures with each other.": "我继续和Bianca暧昧，还互相分享了一些色情照片。",

        "Riona told me what happened to her, and I tried to nudge her toward patching things up with Quinn. She didn't like that.":
            "Riona告诉我她经历了什么。我试着劝她和Quinn修复关系，但她不喜欢这个建议。",
        "Riona told me what happened to her, and I told her she should stay away from Quinn. Riona was relieved that I saw it her way.":
            "Riona告诉我她经历了什么。我劝她远离Quinn。见我站在她这边，她松了一口气。",
        "Josy was contacted by a famous blogger called TheDiane. I bought her lingerie photos.": "知名博主TheDiane联系了Josy。我购买了她的内衣照。",
        "Josy was contacted by a famous blogger called TheDiane. I didn't buy her lingerie photos.": "知名博主TheDiane联系了Josy。我没有购买她的内衣照。",
        "Will you remember me when you're famous?": "等你出名了还会记得我吗？",
        "HAHA! I guess you saw the news. It's huge, isn't it?": "哈哈！看来你看到消息了。很轰动，对吧？",
        "Congrats, Josy. I saw the big news! mphone_emoji_smile": "恭喜你，Josy。我看到那个大消息了！mphone_emoji_smile",
        "THANKS!!! I'm so excited!!! It's friggin' huge!": "谢谢！！！我太激动了！！！这事真的太大了！",
        "I have to admit, I didn't know who TheDiane was, but I checked her page and she had a crazy number of followers.":
            "得承认，我之前不知道TheDiane是谁，但我看了她的主页，粉丝多得吓人。",
        "Have you and Maya lived under the same rock? She's like number one in the blogosphere. I mean, I guess it depends on what blogs you read, but she's number one on CB!":
            "你和Maya都与世隔绝了吗？她在博客圈几乎就是头号人物。当然也得看你平时看什么博客，但她在CB绝对是第一！",
        "I don't read blogs, Josy. I barely read my DMs on Rooster. Anything that takes longer than a couple of sentences to say online is a waste of time.":
            "我不看博客，Josy。我连Rooster私信都很少看。网上要是两句话还说不完，我就觉得是在浪费时间。",
        "Bah!!! I'm gonna show you some of TheDiane's posts. You'll see how much impact she has.": "切！！！我给你看看TheDiane的帖子，你就知道她影响力有多大了。",
        "Yep. Maya and I are rock people. She's indie rock, and I'm hard rock.": "对，Maya和我都喜欢摇滚。她是独立摇滚，我是硬摇滚。",
        "I'm gonna show you some of TheDiane's posts. You'll see how much impact she has.": "我给你看看TheDiane的帖子，你就知道她影响力有多大了。",
        "I don't doubt it. You wrote she was going to feature you. What does that mean?": "我不怀疑。你说她要推荐你，具体是什么意思？",
        "Remember the winter photos you helped me shoot? She will use those in her blog.": "还记得你帮我拍的冬季写真吗？她会把那些照片用在博客里。",
        "Wow! That means I'm famous too.": "哇！那我也算出名了。",
        "HAHA! I guess it does!": "哈哈！好像还真是！",
        "So, where do I send the invoice?": "那账单该寄到哪里？",
        "I'm not getting paid for this. If I were, I would give you a cut.": "这次合作没有报酬。要是有的话，我肯定分你一份。",
        "I was joking anyway. Why isn't she paying you?": "我本来就是开玩笑。不过她为什么不给你钱？",
        "I'm getting paid in notoriety. You can't put a price on that.": "她给我的报酬是知名度，这可没法用钱衡量。",
        "So, I was free labor all along...": "原来我一直都是免费劳动力……",
        "You and Maya. She's helping me take pictures now.": "你和Maya都是。她现在正在帮我拍照。",
        "I work for free and I get fired? I suck.": "我免费干活还被炒了？我可真惨。",
        "No you don't suck. You did great! You can still take photos of me if you want. I didn't realize you wanted to.":
            "你才不惨，你拍得很棒！想拍的话，以后还是可以帮我。我之前不知道你这么想拍。",
        "It's cool. I'll always help you if you want my assistance, but I'm sure Maya will do a great job at it, too. Anyway, I hope the feature brings you success! mphone_emoji_heart":
            "没关系。需要帮忙时我随时都在，Maya肯定也会拍得很好。总之，希望这次推荐能让你大获成功！mphone_emoji_heart",
        "You're the best! mphone_emoji_heart": "你最好了！mphone_emoji_heart",
        "I took some photos of myself by the lake for my blog, and she will repost those on her page along with some other creators who're getting the same deal.":
            "我在湖边为博客拍了些照片。她会把照片转发到自己的主页上，还有一些创作者也得到了同样的机会。",
        "She'll credit me and link my page. If people like what they see, they'll sign up for my blog and that will bring me both traffic and money.":
            "她会标注我的名字并附上主页链接。大家喜欢的话就会订阅我的博客，这既能带来流量，也能赚钱。",
        "Hey, that's awesome! From just one post of TheDiane you could end up with an even bigger following.":
            "嘿，这太棒了！TheDiane只要发一篇帖子，就可能给你带来更多粉丝。",
        "I know! Isn't it great? mphone_emoji_laugh": "我知道！是不是很棒？mphone_emoji_laugh",
        "You're worth it! You should take some more photos for your blog then. To prepare for the influx of new subscribers.":
            "你值得！那你该多拍些照片放到博客上，好迎接即将涌入的新订阅者。",
        "I'm already on it. Or, Maya is already on it, I should say. She's helping me take pictures now.":
            "已经在拍了。准确地说，是Maya已经开始了，她现在正帮我拍照。",
        "I'm sure Maya will do a great job at it. Anyway, I hope the feature brings you success! mphone_emoji_heart":
            "Maya肯定会拍得很好。总之，希望这次推荐能让你大获成功！mphone_emoji_heart",
        "Josy told me about her collaboration with TheDiane. It seemed like a big deal for her.": "Josy告诉我她与TheDiane合作的事。这对她来说似乎是个大好机会。",
        "I accepted Jen's offer to represent me as a fighter.": "我接受了Jen的邀请，让她担任我的格斗经纪人。",
        "I declined Jen's offer to represent me as a fighter.": "我拒绝了Jen担任我格斗经纪人的邀请。",

        "Dawe wanted a visible line to separate DIKs from jocks at the New Year's Eve party.": "Dawe要求在跨年派对上划出一条明显的界线，把DIKs和橄榄球队员隔开。",
        "I let Sarah handle the feminists showing up at the New Year's Eve party on her own.": "跨年派对上女权社团的人出现时，我让Sarah独自处理。",
        "I helped Sarah handle the feminists showing up at the New Year's Eve party.": "跨年派对上女权社团的人出现时，我帮Sarah一起处理。",
        "Nick showed up to our New Year's Eve party. Sage had invited him.": "Nick出现在我们的跨年派对上，是Sage邀请他来的。",
        "Sage wanted us to bury the hatchet with Nick at our New Year's Eve party.": "Sage希望我们在跨年派对上与Nick冰释前嫌。",
        "Elena was worried that the DIKs would end up fighting the jocks at the New Year's Eve party.": "Elena担心DIKs和橄榄球队员会在跨年派对上打起来。",
        "Leon was concerned that the dorm girls who put up posters of Cathy were at the New Year's Eve party.": "Leon担心那些张贴Cathy海报的宿舍女生也来到了跨年派对。",
        "Leon and I hazed Marc and Chen by making them pull a mean prank on the alphas.": "我和Leon给Marc、Chen下马威，让他们对阿尔法兄弟会搞了个恶毒的恶作剧。",
        "Leon and I hazed Marc and Chen by making them pull a harmless prank on the alphas.": "我和Leon给Marc、Chen下马威，让他们对阿尔法兄弟会搞了个无伤大雅的恶作剧。",
        "I talked to Jade about my breakup with Sage.": "我和Jade谈了自己与Sage分手的事。",
        "I talked to Jade about my situation with Sage.": "我和Jade谈了自己与Sage之间的状况。",
        "Matthew thanked me for outing his relationship with Olivia to Bianca. I didn't pick a fight with him over it.":
            "Matthew感谢我把他和奥莉维亚的关系告诉了Bianca。我没有因此找他吵架。",
        "Matthew thanked me for outing his relationship with Olivia to Bianca. I gave him an earful.":
            "Matthew感谢我把他和奥莉维亚的关系告诉了Bianca。我狠狠训了他一顿。",
        "I gave Matthew an earful for sneaking around with Olivia at the New Year's Eve party.": "Matthew在跨年派对上偷偷和奥莉维亚来往，我为此狠狠训了他一顿。",
    }

    def _s3_ep12_b15_cn_replace_text(s):
        if _s3_ep12_b15_prev_replace_text is not None:
            s = _s3_ep12_b15_prev_replace_text(s)
        try:
            active = getattr(renpy.store._preferences, "language", None) in ("chinese", "schinese")
        except Exception:
            active = False
        if active:
            s = _s3_ep12_b15_cn_exact.get(s, s)
        return s

    config.replace_text = _s3_ep12_b15_cn_replace_text
