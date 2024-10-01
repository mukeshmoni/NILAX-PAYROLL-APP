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

TAGMES =  [
  "Enna boss, ready ah? 🔥",
  "Thalaivaa, semma speed! 🚀",
  "Nalla sapteengala? 🍛",
  "Bro, party eppo? 🎉",
  "Chumma chill da! 😎",
  "Weekend plans ready ah? 🏖️",
  "Inimey semma scene poduvom! 🎬",
  "Machan, thookathula irukke? 😴",
  "Ippo yenna, on fire ah? 🔥",
  "Vera level moment da! 🏆",
  "Indha vibe sema mass! 🎶",
  "Time waste panna koodadhu da! ⏳",
  "Ada paavi, seekiram va! 🚶‍♂️",
  "Pesama naalu thooki pottu thallunga! 💪",
  "Enna bro, full motivation ah? 💥",
  "Romba confuse aagita da! 🤯",
  "Atho, unga periya entry! 💥",
  "Sema twist da story la! 🎭",
  "Nee dhan kalakkura thala! 🕺",
  "Indha aattam vera level! 🎊",
  "Semma respect bro! 🙏",
  "Yaaru mass da inga! 🎯",
  "Ithu dhan namma ooru style! 😎",
  "Oray comedy ah irukke da! 😂",
  "Podhum da, ippo party thaane! 🎂",
  "Unga punch dhaan vera! 🥊",
  "Thani oruvan da nee! 👑",
  "Nee thaan inimey viral! 🚀",
  "Unga dance vera level! 🕺",
  "Vera ticket ah vachu mass podra! 🎟️",
  "Scene poda time aachu! 🎬",
  "Unga swag over ah irukku! 😎",
  "Semma kadhal da! 💕",
  "Kaasu kadaichala call pannunga! 💸",
  "Appadiye fly podu bro! ✈️",
  "Nee dhan boss da inga! 🧑‍💼",
  "Inga irukku oru periya superstar! 🌟",
  "Goal ah achieve pannirke! 🏅",
  "Athuvum oru talent dhaan bro! 🎯",
  "Podhum da, idhu podhum! ✋",
  "Work la full speed ah poitu irukke! 💻",
  "Vazhkai la vera punch da! 💥",
  "Kalakkuringa da unga range! 🔝",
  "Enaku semma aasa paduthura style! 🕶️",
  "Yenna matter nu ondrum puriyale! 🤔",
  "Semma motivation thambi! 💪",
  "Apo party ready ah? 🎈",
  "Indha punch ku semma response da! 🎤",
  "Unga memes vera level! 😂",
  "Time spend panna super la irukke! ⏱️",
  "Inga oru chill vibes! 🌴",
  "Pudhu challenge ah? Bring it on! 🎯",
  "Unga smile ah paathale full energy! 😊",
  "Adutha level plan enna da? 🚀",
  "Comedy ku full time mood ah irukke! 😆",
  "Azhagana day bro! 🌞",
  "Boss, yenakku ticket vachiruke! 🎫",
  "Indha poster ku mass response bro! 🖼️",
  "Nee thaan namma next superstar! 🌟",
  "Success ku vera route illa bro! 🛤️",
  "Life la full positivity! ✨",
  "Sari, ipo goal pottu thalla da! 🎯",
  "Oru chill ah irukke bro! 🧊",
  "Indha song ku vera flow! 🎵",
  "Vera performance bro! 💃",
  "Sema reach bro! 📈",
  "Inga irukku motivation overload! 🔥",
  "Party mood ah va? 🎉",
  "Enakku inime onnum vendam, just rest! 😴",
  "Ticket vachu booking confirmed! 🎟️",
  "Semma energy da unga team la! 💥",
  "Athu over style aachu! 😎",
  "Yaaru ivaru, semma punch a podra! 🥊",
  "Neenga chill dhaan boss! 🍹",
  "Unga attitude la vera range! 🎯",
  "Bro, thooki adichidu bro! 💥",
  "Sema roast podra bro! 🔥",
  "Over mass scene bro! 🎬",
  "Vibe vera level irukku! 🎶",
  "Challenge accepted! 🏆",
  "Mokka jokes irundhalum unga vibe vera! 😄",
  "Bro, viral la pora scene! 🚀",
  "Party mood da! 🥳",
  "Semma range da unga voice! 🎤",
  "Nee oru semma achiever da! 🏅",
  "Kalakudhu bro unga team! 💥",
  "Mass la plan poda! 🧠",
  "Enakku coffee kudikaravan thaan venum! ☕",
  "Ticket miss aagidum da bro! 🎟️",
  "Nee dhaan inga thalaivaa! 👑",
  "Boss, ipo chance vachachu da! 🎯",
  "Oru puthusu start pannirke da! 🌱",
  "Sema energy la life irukku! 🌟",
  "Dance floor la full fire da! 💃",
  "Enna kalakkuringa da! 😎",
  "Full speed ku thooki vittirke! 🚀",
  "Indha performance la full hype! 📢",
  "Bro, vera look dhan pa! 😎",
  "Challenge lam overtake pannitom! 🎯",
  "Full fire irukku unga swag! 🔥",
  "Nee oru firecracker da! 🎇",
  "Boss, chill pannunga! 😎",
  "Semma confident da unga face la! 😁",
  "Challenge ku full support da! 🤝",
  "Sema plan ah, athu execute pannunga! 💼",
  "Vera hype va irundhuchu! 📢",
  "Team la full motivation! 💪",
  "Enakku vera vibe ah irukkudhu! 🌊",
  "Over style ah podra! 😎",
  "Bro, unga roast ku semma response da! 🔥",
  "Andha swag ah paakumbodhu oru thooku da! 🎶",
  "Full range va poitu irukke da! 📈",
  "Nee dhan next superstar ah irukka? 🌟",
  "Inime next level entry ready! 🚀",
  "Over punch da unga plan la! 🥊",
  "Semma swag thambi! 🔥",
  "Unga hype la full mood change! 🎉",
  "Enna scene da, semma punch! 🥋",
  "Ticket ready ah, nee dhan entry ku! 🎟️",
  "Mass start podra da unga performance la! 💥",
  "Boss, full-on energy la irukke! 💣",
  "Sari, ipo chill mode ku po da! 😌",
  "Full-time swag ah irukku! 👓",
  "Next level meme da! 😂",
  "Indha roast semma mass da! 🔥",
  "Success ah reach pannirke da! 🏅",
  "Challenge ku oru semma punch podunga! 🥊",
  "Vera level fire ah poitu irukke! 🔥",
  "Boss, unga style ku adichu vidunga! 💣",
  "Enakku oru semma vibe dhan! 🌊",
  "Indha time la full chill mode da! 🧊",
  "Sema entry da unga team la! 🚪",
  "Full swag da unga performance la! 😎",
  "Boss, ipo next challenge ready ah! 🏆",
  "Energy full da unga meme ku! 🔥",
  "Vera punch da unga speech la! 🎤",
  "Challenge podra time da ippo! ⏳",
  "Indha vibe ku full support! ✨",
  "Oru semma entry poda ready ah! 🚪",
  "Kalakudhu da unga roast! 🔥",
  "Nee semma swag poda ready ah irukka! 👓",
  "Andha punch la life irukkudhu da! 🥋",
  "Boss, unga team la vera motivation! 💥",
  "Kalakudhu unga plan la full fire! 🔥",
  "Challenge ku mass ready ah irukke! 🏆",
  "Sari, chill pannu da! 🍹",
  "Boss, inga vera vibes dhan irukku! ✨",
  "Inime oru semma performance poda! 💃",
  "Bro, unga plan vera level da! 🧠",
  "Party ku ready ah va? 🎉",
  "Andha moment la vera punch da! 🎬",
  "Sema hype podra scene! 🎤",
  "Challenge ku ready ah, inga vara! 💥",
  "Oru scene va semma hype da! 📢",
  "Swag ku vera response irundhadhu da! 😎",
  "Full swag ku poitu irukku da! 🚀",
  "Success ku indha vibe irundha podhum! ✨",
  "Energy full da unga roast ku! 🔥",
  "Boss, unga attitude ku thooku! 💥",
  "Challenge ku full fire ah irukke da! 🔥",
  "Unga meme semma scene! 😂",
  "Sari, ipo semma rest da! 🛌",
  "Swag ku vera range! 😎",
  "Kalakudhu unga entry ku! 🚪",
  "Full-time roast da unga response! 🔥",
  "Challenge accept pannirke da! 🏆",
  "Mass ah handle pannirke da! 💼",
  "Kalakudhu unga style la! 🎶",
  "Bro, unga vibes semma positive! ✨",
  "Vibe ku oru perfect match da! 💫",
  "Party mood ah da, inga vandha! 🎊",
  "Boss, full swing la irukke da! 🏌️",
  "Challenge ku enna ready? 🤔",
  "Sema look poda bro! 😎",
  "Next level goal set pannirke! 🎯",
  "Boss, ipo semma mode ku irukke! 🚀",
  "Enakku indha swag vera mass da! 🎤",
  "Enakku challenge vendam, full chill! 🧊",
  "Success ah semma handle pannirke! 🏆",
  "Party ku over hype da unga dance la! 🕺",
  "Full motivation ku vera vibes da! 💥",
  "Swag ku semma punch da! 🎯",
  "Energy ku oru vera flow da! 🔥",
  "Kalakudhu unga roast ku! 💥",
  "Next level challenge ku ready ah irukke! 💪",
  "Sema moment da unga team la! 🎊",
  "Boss, unga swag vera mass da! 👑",
  "Challenge ku oru full plan ready! 🧠",
  "Inime next level la poitu irukku da! 🚀",
]

           

@app.on_message(filters.command(["tagall", "vtag", "tagmember", "utag", "KingOfAttittudetag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

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
        return await message.reply("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ...")
    else:
        return await message.reply("/tagall  ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ..")
    if chat_id in spam_chats:
        return await message.reply("ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴘʀᴏᴄᴇss ...")
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

@app.on_message(filters.command(["tagoff", "tagstop" , "vstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("sᴛᴏᴘ ᴀᴀɢɪᴠɪᴛᴀᴛʜᴜ..")
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
        return await message.reply("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦sᴛᴏᴘ ᴀᴀɢɪᴠɪᴛᴀᴛʜᴜ ♦")
