from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "๐๐ข ๐๐ฒ๐ฎ๐ฌ๐ฌ :) <๐\n๐๐ง๐ฒ ๐๐๐ฅ๐ฉ ๐๐ฆ ๐๐ฒ ๐๐ฐ๐๐๐ญ ๐\n๐๐๐ฌ๐ญ๐๐ซ ๐ธ :- [โ-เผ๐ฆแถฆแถฐแตแญเผโฆอ๐จ๐บ๐ฏ๐น๐จ๐ญโอแถอแดฟอแดฌอแถปอแดตอแดฑอแธโโโโ ฬฬฐแดทอแตอแดฌอแตอเผเผโฐ๐โเฟ](https://t.me/itz_me_monuuz) โค๏ธ\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM Permit Enabled")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM Permit Disabled")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Auto Approved ...")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
