import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1ebc3393692680b98c7ef.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
∆ ʜᴇʏ {message.from_user.mention()} !
        ᴛʜɪs ɪs [misscutiemusic](t.me/BROKEN_MUSIC_ROBOT),  ɪ ᴀᴍ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ, ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ....
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀs : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [•••••](t.me/surya12p)
┣★
┗━━━━━━━━━━━━━━┛
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ 
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•Add me your group•", url=f"https://t.me/BROKEN_MUSIC_ROBOT?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "•sᴏᴜʀᴄᴇ•", url=f"https://github.com/Team-techno/misscutiemusic"
                    ),
                    InlineKeyboardButton(
                        "•sᴜᴘᴘᴏʀᴛ•", url=f"https://t.me/misscuitesupport"
                    )
                ],[
                    InlineKeyboardButton(
                        "•✞︎ᴅᴇᴠᴇʟᴏᴘᴇʀ✞︎︎︎•", url="https://t.me/surya12p"
                    )]
            ]
       ),
    )
