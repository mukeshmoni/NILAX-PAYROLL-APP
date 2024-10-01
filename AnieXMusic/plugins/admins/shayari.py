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
          " 💘💖⌚💔",
          " 😔👑😁🤗",
          " 💀😖😔〽️",
        ]
        ####
        
SHAYRI = [ "Kadhal oru azhagiya kanavu, kanavin kural naan ketten 💫",
  "Nizhalin thunaiyil naan nadanthen, un nilavugal en meedhu vilundhadhai arindhen 🌙",
  "En idhayam un kannil kaanaamal urugidhu, kaatru pol thaavum iniya sindhanai 🌬️",
  "Penmai endra thangathin vilayattu, un vizhigalil thavum oru oru kanavum 🌸",
  "Kaadhalin mugam un mozhi, idhayathil izhiyum varigalum 💌",
  "Neenda thoorathil nee poidivittai, aanaal idhayam un nenjilum 💔",
  "Mazhai thuli ennai naane marakkum, aanaal un ninaivugal naan marakka mattane 🌧️",
  "Un kannil thuligal thaan azhagi, adhu yen nenjil thuli pol padhithadhu 😢",
  "Kadhal solla varthaiye illai, un karpanai en idhayathil adi thavikkudhu 💖",
  "Un kaiyil naan kai pidithal, vazhiyil pothi paadu thodarum 🎶",
  "Iravil thookathin kavigal varugiraargal, aanaal un ninaivugal dhaan en kanavil 💭",
  "Vizhi moodinangalum un mugam marandhida koodaadhu, ninaivugal azhagiya sindhanai 🎨",
  "Oru thaalaattu paadi vizhigalum thookam thodangum, aanaal en kaadhal kanavilum vilundhadhadi 🎵",
  "Un kaiyil naan kai poda marandhu poyitene, ennodu vazhiyil nee marakka koodaadhu 🤝",
  "Azhaga oru naal, ennai serndhadhu un kanavu thaan 💫",
  "Nizhalin thunaiyil naan irundhaalum, un ninaivugalin sugam thavara maatene 🌙",
  "Kanavil vilaiyaadum sindhanai, un vaarthayin sugam thaan 💭",
  "Un kannin oli enakoru ezhuvizhudha aasaiya thandhadhu 🔥",
  "Yen idhayam thaane unakku padaithidum oru padam 🎨",
  "Mazhaiyin thuligal vizhiyil nizhalagi vilayadum velai 🌧️",
  "Un vizhigalil uraiyum kanavu, en kaviyaaga maari virundha 💖",
  "Poovizhi kannathile, enna ninaivugal vilaiyaadum 🌸",
  "Iravu idhu, un vizhiyil saalai nadakkum neram 🌙",
  "Un idhayathin rhythm, ennai adaikkum kalaigal 🎶",
  "Marandhidum varthai, un ninaivil vizhum 😢",
  "En vizhiyin sugam, un mozhi mazhai thuligal pole vizhigindradhu 🌧️",
  "Ninaivil paadhi naan, paadhi nee 💫",
  "Un mugathin paavai, en kaviya idhayathil padiyai kettu vilaiyadum 🎨",
  "Vizhiyin kanavu, unadhu mozhi kaviya pol theriyum 💭",
  "Kaadhal oru raagam, un kuralin metrum thaan 🎶",
  "Un ninaivil naan urangi, kanavilum thavikum kaadhal 💔",
  "Idhayam adaikkum un kannin mozhigal 💖",
  "Un ninaivil thavikum inbam, en kaalgalin payanathil mattum 🌸",
  "Kanavil naan, un kannin kaaranam pole thondriyadhadi 💫",
  "Vizhiyin naadi, un ninaivugalil dhaan thavithidum 💭",
  "Kadalin alai pole, un mozhi en idhayathin solladhudan 🎵",
  "Mugathin azhagi, en kanavugalil nadandhidum nizhal 🎨",
  "Un vizhiyin vilaiyaattu, naanum enna vilaiyadum neram 💖",
  "Oru kanniyin azhagi, un kuralin inbam pole ketkudhu 💫",
  "Ninaivil oru aasai, un sol vinai paavai kaviya paditthidum 🌸",
  "Kadhalin paadal, un mugam marakka marakka sollum 🎶",
   ]

# Command
    


@app.on_message(filters.command(["poem"  , "monipoem"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/shayaril  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
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
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
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


#

@app.on_message(filters.command(["shstop", "vshstop" , "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ STOP ♦")
