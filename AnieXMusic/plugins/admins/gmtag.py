from AnieXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "💖🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "Good morning da! Oru fresh start ah begin pannalama? 🌞",
  "Good morning buddy! Indha naal super ah irukkattum! 🌅",
  "Good morning machi! Kalakkura plans ah pannikala? ☀️",
  "Good morning bro! Full energy mode ku vandhuttiya? ⚡",
  "Good morning sis! Semma bright day ah irukkum nu nenaikkiraen! ✨",
  "Good morning da! Unga pakkam ella set ah? 😊",
  "Good morning friend! Naalu positive vibes oda start pannalama? 🌻",
  "Good morning akka! Indha naal unaku oru special ah irukkattum! 🌸",
  "Good morning thambi! Vera level day irukkum nu feel pannuraen! 🔥",
  "Good morning thala! Indha naal oru mega success ku pogattum! 💪",
  "Good morning buddy! Fresh ah, full power ah start panniduvom! 💥",
  "Good morning da! Sun ah pola shining mood ku iruppiya? 🌞",
  "Good morning machi! Oru energetic day kaaga get ready! 🚀",
  "Good morning bro! Full charge mode ku vandhutta? 🔋",
  "Good morning sis! Smile potutu indha naalai kick start pannu! 😊",
  "Good morning akka! Vizhundha kooda thirumbikitte pogattum indha day! 🌅",
  "Good morning thambi! Unakku success varaikum thookitu povom da! 💯",
  "Good morning boss! Full positive vibes oda start pannalaam! 🌟",
  "Good morning friend! Indha naal unakku oru semma achievement kudukkum nu nenaikkiraen! 🏆",
  "Good morning da! Ella plans um vera level ah nadakkattum! 💥",
  "Good morning machi! Oru semma productive day start panniduvom! 🚀",
  "Good morning bro! Indha naal super energy oda mudikkattum! 💪",
  "Good morning thala! Shine ah irundha podhum nu start pannuva! 🌞",
  "Good morning sis! Oru fresh start ku edhuvum better illa! 🌅",
  "Good morning buddy! Oru beautiful morning ku welcome pannu! 🌸",
  "Good morning thambi! Semma vibe ku irundha indha naal vera level! ✨",
  "Good morning akka! Smile podra moment ah irundha mattum podhum 😊",
  "Good morning da! Fresh ku kicku kudukkara morning ☀️",
  "Good morning machi! Enthusiasm oda start panniduvom 💥",
  "Good morning bro! Indha naal super productive a irukkattum nu nenaikren 🏆",
  "Good morning akka! Fresh ah erumai pol kalakalama? 🐂",
  "Good morning thambi! Oru pazhagiya semma day irukkattum da! ✨",
  "Good morning da! Fresh start pannu! Unakku indha naal success ku poradhanu confirm ☀️",
  "Good morning friend! Oru cool breeze pola peaceful morning! 🌬️",
  "Good morning sis! Semma happy ah irukka, kalakkalam 🌸",
  "Good morning machi! Vibe vera level ah start aagattum 🚀",
  "Good morning da! Oru pazhagiya full mood booster day ☀️",
  "Good morning bro! Oru powerful ah start panni katthi vara da! 🔥",
  "Good morning akka! Unakku nalla success ku vanthuta nu confirm nu solren 🌞",
  "Good morning buddy! Oru fun filled day irukkum nu expect pannu! 🌅",
  "Good morning thambi! Oru mega power ah pona naal irukkum da! 💯",
  "Good morning sis! Smile potutu semma day start pannu! 😊",
  "Good morning friend! Vizhudhu, thirumbikittu po, indha naal semma irukkum! 💪",
  "Good morning machi! Full energy mode ku switch panniduvom! 🔋",
  "Good morning bro! Oru day full of achievements irukkum nu feel pannuraen! 🏆",
  "Good morning da! Morning ku fresh air iruntha, naan ready ah iruppen nu nenachaen! 🌬️",
  "Good morning akka! Semma vibe ku irukkum naal nu confirm! ☀️",
  "Good morning thambi! Challenge yaarum vandha nee thooki veppa da! 💥",
  "Good morning boss! Shine ah start pannu nu solraen! 🌞",
  "Good morning sis! Fresh mood ku vandhutu indha naalai success pannidu! 🌸",
  "Good morning machi! Oru energetic start, super plans ku kalakkittom nu! 💪",
  "Good morning bro! Indha morning kick start, success da 💯",
  "Good morning akka! Naalai start pannuna oru mass kalakkal! 🌅",
  "Good morning da! Oru kick starter morning la irundha mattum pothum 🌞",
  "Good morning thambi! Semma naal irukkattum nu full confidence da! 🔥",
  "Good morning buddy! Fresh start ku vandha adhu super productive aagattum! 🏆",
  "Good morning sis! Oru fun ah irukkum nu feel pannuraen 🌟",
  "Good morning friend! Unna pathi ella naalukum special nu feel pannu 😊",
  "Good morning machi! Full josh ku start pannidu da! 🚀",
  "Good morning bro! Naalai kadhaikulam start pannuva da! 🐅",
  "Good morning akka! Oru mega shine podra morning irukkattum! 🌞",
  "Good morning da! Oru special surprise ku indha naal! 🎁",
  "Good morning friend! Positivity ooti varum pola irukku ☀️",
  "Good morning thambi! Oru fresh start panni, mass plans ku ready! 💯",
  "Good morning buddy! Indha day ku semma achievement kaaga wait pannida! 🏆",
  "Good morning machi! Enthusiasm ku super boost ah irukkattum! 💥",
  "Good morning bro! Oru semma energetic day, kalakkiduvom! 🔋",
  "Good morning akka! Smile potu indha naalai kick start pannu 🌻",
  "Good morning da! Fresh ah start pannuna adhu success ah mudiyum! 🌟",
  "Good morning thambi! Oru semma productive day irukkum nu feel pannuraen! 💯",
  "Good morning buddy! Kalakkura energy oda start pannalam nu solraen! 🌅",
  "Good morning sis! Semma fun ah irukkum pola theriyudhu! 😊",
  "Good morning bro! Challenge nu vaazhum morning ku ready ah irukka da? 💥",
  "Good morning machi! Oru vera level energy mood ku vandhutta da! 🚀",
  "Good morning thala! Oru power ku start panni indha naal semma irukkum! 🔥",
  "Good morning friend! Oru fresh breeze pola, indha naal vera maari! 🌬️",
  "Good morning thambi! Indha naal full positive vibes ku pogattum nu solraen! 💪",
  "Good morning akka! Semma shine ah start panni kalakkalama? 🌞",
  "Good morning da! Unna paatha podhu feel aagudhu, indha naal super ah irukkum nu! ✨",
  "Good morning bro! Oru successful day ku ready ah? 💯",
  "Good morning sis! Fresh morning start ku vazhi pattu pogattum! 🌅",
  "Good morning thambi! Oru semma fun filled day irukkum nu solraen! 💥",
  "Good morning da! Unakku indha naal perfect a irukkum nu guarantee! 🏆",
  "Good morning friend! Semma smile potu un vibe ku reach panna start pannu! 😊",
  "Good morning akka! Semma energy ku start pannura maadhiri theriyudhu! 🌟",
  "Good morning bro! Oru mega kalakkal ku ready aagidu da! 💯",
  "Good morning machi! Oru full boost ku, semma day ku start pannu! 🔋",
  "Good morning buddy! Fresh air la, perfect start ku vandhuttom! 🌬️",
  "Good morning thambi! Semma positive energy oda start pannu nu! 💥",
  "Good morning da! Oru success ku pogara morning la irundhoma nu theriyudhu! 🌅",
  "Good morning sis! Smile pottu semma day ku prepare pannura? 😊",
  "Good morning akka! Shine pol irundha podhum nu start pannidu! 🌞",
           ]

VC_TAG = ["Good morning da! VC la pesiduvom! ☀️🎙️",
  "Good morning buddy! VC la oru fresh start ah pesala? 🌞🎧",
  "Good morning machi! VC ku join pannu, pesidalam! 💬🎤",
  "Good morning bro! VC la onnu pesi kalakiduvom da! 🌅🎙️",
  "Good morning sis! Unna VC la paathutu pesalam! ☀️🎧",
  "Good morning thambi! VC la pesiduvom nu ready ah irukka? 🎤✨",
  "Good morning akka! VC la meet panni onnu pesalam! 🌞🎙️",
  "Good morning boss! VC la oru energetic convo pannalam! 🔥🎧",
  "Good morning da! Oru fresh morning VC la pesi start pannu! 🌅🎤",
  "Good morning buddy! VC ku vandhu oru fun chat pannu da! ☀️🎙️",
  "Good morning friend! VC la onnu kalakkalama? 🌞🎧",
  "Good morning thala! VC pesi oru positive day start pannu da! 🎤🔥",
  "Good morning machi! VC ku vandhu pesiduvom, plan pannikala? ☀️🎧",
  "Good morning bro! VC la pesi oru semma vibe kuduthiduvom! 🌞🎤",
  "Good morning sis! VC ku vandha oru happy convo panniduvom! 🌅🎧",
  "Good morning da! VC la pesi oru productive day start pannalama? ☀️🎙️",
  "Good morning thambi! VC ku vandhu pesiduvom, energy set ah irukkum! 🔋🎤",
  "Good morning akka! Oru semma VC convo ku ready ah? 🌞🎧",
  "Good morning boss! VC la pesi un vibes ku reach panna pannu da! 🎙️✨",
  "Good morning buddy! VC ku vandhu oru productive chat pannu! ☀️🎧",
  "Good morning machi! VC la pesi oru fresh start pannalam! 🌅🎤",
  "Good morning bro! VC la pesi kalakkara plans ah discuss pannalam da! 🔥🎧",
  "Good morning friend! Oru VC ku join panni pesiduvom, semma vibe irukkum! 🎙️✨",
  "Good morning thala! VC la pesi oru energetic morning ku start pannu da! 🌞🎤",
  "Good morning sis! Unakku oru fun VC convo panni fresh aagiduvom da! ☀️🎧",
  "Good morning thambi! VC la pesi full day super ah irukkum! 🔋🎙️",
  "Good morning da! VC la onnu pesi indha day ku kick start pannu da! 🌅🎧",
  "Good morning akka! VC ku vandhu oru chill convo pannikala? ☀️🎤",
  "Good morning bro! Oru fun VC chat panni naala energize aagiduvom da! 🔥🎧",
  "Good morning friend! VC la pesi oru mass conversation ku kalakkiduvom! 🎙️✨",
  "Good morning machi! VC ku join pannidu, pesiduvom da! 🌅🎧",
  "Good morning buddy! VC la pesi indha day ku vera level energy koduthiduvom! ☀️🎤",
  "Good morning thambi! Unakku oru semma VC convo ku time irukkattum! 🎧🔥",
  "Good morning sis! VC la pesi naal fulla fresh feel panniduvom da! 🌞🎙️",
  "Good morning da! VC la oru positive chat pannu nu ready ah irukka? 🌅🎧",
  "Good morning bro! VC pesi kalakkara vibe set ah irukkum! 🎤✨",
  "Good morning akka! Oru VC la pesi naalai vera level start pannalam! ☀️🎧",
  "Good morning friend! VC ku vandhu onnu pesi indha day ku kick start panniduvom! 🌞🎙️",
  "Good morning buddy! VC la pesi naalai full power ku reach panna pannu! 🔋🎧",
  "Good morning machi! VC la pesi oru super plan discuss panniduvom! 🌅🎤",
  "Good morning thambi! Unakku VC la pesi oru positive energy kodukkalam! ☀️🎧",
  "Good morning bro! VC la pesi indha day ku fun chat panniduvom da! 🌞🎤",
  "Good morning da! VC ku vandhu pesi oru chill convo pannalam! 🔥🎧",
  "Good morning sis! VC la pesi oru semma morning ku start panni kalakkalama? 🎙️✨",
  "Good morning akka! VC ku join panni pesi energy kuduthiduvom! 🌅🎧",
  "Good morning boss! VC la oru productive convo ku vandhuttana? ☀️🎤",
  "Good morning buddy! VC la pesi indha day ku perfect start panniduvom da! 🌞🎧",
  "Good morning machi! VC pesi oru fresh start ku kalakkiduvom! 🔋🎙️",
  
        ]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


                                   
@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
