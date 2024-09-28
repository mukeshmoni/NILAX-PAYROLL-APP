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

TAGMES = [  "ɴᴀᴀɴ sᴜᴘᴇʀ ʜᴀᴘᴘʏ, ʟɪғᴇ ғᴜʟʟ ᴏɴ!",
"ᴄʜɪʟʟ ᴘᴀɴɴᴀᴍᴀ, ʀᴀsᴀᴍ sᴛʏʟᴇ!",
"ᴠᴇʀᴀ ʟᴇᴠᴇʟ ᴋᴏʟʟʏᴡᴏᴏᴅ ᴠɪʙᴇs!",
"Mᴀᴅʀᴀs Mᴀɢɪᴄ, Sᴀᴍʙᴀʀ Pᴏᴡᴇʀ!",
"Nᴀʟʟᴀ Mᴏᴏᴅ, Fᴜʟʟ Oɴ Fᴜɴ!",
"Sᴀᴍʙᴀʀ & Sᴜɴsʜɪɴᴇ, Pᴇʀғᴇᴄᴛ Cᴏᴍʙᴏ!",
"Pᴀᴋᴋᴀ Lᴏᴄᴀʟ Sᴛʏʟᴇ, Jᴏʟʟʏ Mᴏᴍᴇɴᴛs!"
"Kᴜᴛʜᴛʜᴜ Bᴇᴀᴛs, Hᴀᴘᴘʏ Fᴇᴇʟs!",
"Aᴀsᴀɪ Vɪʙᴇs, Rᴀsᴀᴍ Lᴇᴠᴇʟ!",
"Superstar Mood, Full Enjoyment!",
"Tʜᴀᴍɪᴢʜ Fᴜɴ, Sᴀᴍʙᴀʀ Pᴜɴᴄʜ!",
"Kᴏʟʟʏᴡᴏᴏᴅ Cʀᴀᴢʏ, Nᴀʟʟᴀ Jᴏʏ!",
"Cʜɪʟʟ Mᴀᴀʀᴜ, Tʜᴀᴍɪᴢʜ Lɪғᴇ!",
"Rᴀsᴀᴍ Rᴜʟᴢ, Fᴜʟʟ Oɴ Pᴀʀᴛʏ!",
"Jᴏʟʟʏ Aɴʙᴜ, Vɪʙᴇ Tʜᴀᴀɴ!",
"Pᴀᴛᴛᴀɪ Lᴇᴠᴇʟ Fᴜɴ, Rᴀsᴀᴍ Jᴏʏ!",
"Kᴜᴛʜᴛʜᴜ Dᴀɴᴄᴇ, Fᴜʟʟ Oɴ Eɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ!",
"Mᴀᴅʀᴀs Mᴀsᴛɪ, Lɪғᴇ's A Pᴀʀᴛʏ!",
"Tʜᴀᴍɪᴢʜ Tʜʀɪʟʟs, Nᴀᴀɴ Hᴀᴘᴘʏ!",
"Cʜɪʟʟ Tɪᴍᴇ, Kᴏʟʟʏᴡᴏᴏᴅ Gʀᴏᴏᴠᴇ!",
"Vᴇʀᴀ Lᴇᴠᴇʟ Sᴀᴍʙᴀʀ, Fᴜʟʟ Eɴᴊᴏʏᴍᴇɴᴛ!",
"Sᴀᴍʙᴀʀ Mᴏᴍᴇɴᴛs, Hᴀᴘᴘʏ Vɪʙᴇs!",
"Nᴀʟʟᴀ Kᴏᴏᴛᴜ, Sᴜᴘᴇʀ Fᴜɴ!",
"Mᴀᴅʀᴀs Mᴀɢɪᴄ, Kᴜᴛʜᴛʜᴜ Rᴏᴄᴋs!",
"Tʜᴀᴍɪᴢʜ Cᴏᴏʟ, Fᴜʟʟ Oɴ Lɪғᴇ!",
"Pᴀᴋᴋᴀ Fᴜɴ, Kᴏʟʟʏᴡᴏᴏᴅ Sᴛʏʟᴇ!",
"Cʜɪʟʟ Vɪʙᴇs, Rᴀsᴀᴍ Hᴀᴘᴘɪɴᴇss!",
"Sᴜᴘᴇʀsᴛᴀʀ Sᴛʏʟᴇ, Hᴀᴘᴘʏ Lɪғᴇ!",
"Nᴀᴀɴ Nᴀᴀɴ Jᴏʟʟʏ, Fᴜʟʟ Eɴᴊᴏʏᴍᴇɴᴛ!",
"Sᴀᴍʙᴀʀ Pᴀʀᴛʏ, Kᴏʟʟʏᴡᴏᴏᴅ Kɪᴄᴋ!",
"Aᴀsᴀɪ Fᴜɴ, Mᴀᴅʀᴀs Mᴏᴏᴅ!",
"Kᴜᴛʜᴛʜᴜ Gʀᴏᴏᴠᴇs, Tʜᴀᴍɪᴢʜ Bᴇᴀᴛs!",
"Vɪʙᴇ Tʜᴀᴀɴ, Sᴀᴍʙᴀʀ Mᴀɢɪᴄ!",
"Jᴏʟʟʏ Mᴏᴍᴇɴᴛs, Fᴜʟʟ Oɴ Fᴜɴ!",
"Rᴀsᴀᴍ & Sᴀᴍʙᴀʀ, Pᴇʀғᴇᴄᴛ Cᴏᴍʙᴏ!",
"Pᴀᴋᴋᴀ Cᴏᴏʟ, Nᴀʟʟᴀ Vɪʙᴇs!",
"Mᴀᴅʀᴀs Mᴀsᴀʟᴀ, Tʜᴀᴍɪᴢʜ Tʜʀɪʟʟs!",
"Kᴏʟʟʏᴡᴏᴏᴅ Cʀᴀᴢʏ, Sᴀᴍʙᴀʀ Pᴀʀᴛʏ!",
"Tʜᴀᴍɪᴢʜ Fᴜɴ, Jᴏʟʟʏ Tɪᴍᴇs!",
"Cʜɪʟʟ Pᴀɴɴᴀᴍᴀ, Sᴀᴍʙᴀʀ Gʀᴏᴏᴠᴇ!",
"Vᴇʀᴀ Lᴇᴠᴇʟ Tʜᴀᴍɪᴢʜ Mᴏᴍᴇɴᴛs!",
"Nᴀʟʟᴀ Lɪғᴇ, Rᴀsᴀᴍ Sᴛʏʟᴇ!",
"Sᴜᴘᴇʀsᴛᴀʀ Fᴜɴ, Fᴜʟʟ Oɴ Jᴏʟʟʏ!",
"Pᴀᴛᴛᴀɪ Vɪʙᴇs, Kᴏʟʟʏᴡᴏᴏᴅ Mᴀɢɪᴄ!",
"Sᴀᴍʙᴀʀ Fᴜɴ, Hᴀᴘᴘʏ Tɪᴍᴇs!",
"Kᴜᴛʜᴛʜᴜ Lɪғᴇ, Nᴀᴀɴ Hᴀᴘᴘʏ!",
"Mᴀᴅʀᴀs Mᴏᴏᴅ, Sᴀᴍʙᴀʀ Tʜʀɪʟʟs!",
"Cʜɪʟʟ Mᴀᴀʀᴜ, Fᴜɴ Oᴠᴇʀʟᴏᴀᴅ!",
"Aᴀsᴀɪ Vɪʙᴇs, Fᴜʟʟ Oɴ Rᴀsᴀᴍ!",
"Vᴇʀᴀ Lᴇᴠᴇʟ Jᴏʟʟʏ, Mᴀᴅʀᴀs Sᴛʏʟᴇ!"
           ]

@app.on_message(filters.command(["tagall", "vtag", "tagmember", "utag", "Sandytag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
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