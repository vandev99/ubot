
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *

@ubot.on_message(filters.command("unprem") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ"
__HELP__ = f"""
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ ⦫</b>

<blockquote><b>⎆ perintah : <code>/ʙᴄ</code>
ᚗ  ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ʟᴇᴡᴀᴛ ʙᴏᴛ
"""

@PY.BOT("bc")
@PY.OWNER
async def broadcast_bot(client, message):
    msg = await message.reply("<b>⌭ sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>", quote=True)
    done = 0
    if not message.reply_to_message:
        return await msg.edit("<b>⌭ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴘᴇsᴀɴ</b>")
    for x in ubot._ubot:
        try:
            await x.unblock_user(bot.me.username)
            await message.reply_to_message.forward(x.me.id)
            done += 1
        except Exception:
            pass
    return await msg.edit(f"⌭ ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ {done} ᴜʙᴏᴛ")

@PY.BOT("bcast")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("<blockquote><b>okee proses Boy...</blockquote></b>\n\n<blockquote><b>mohon bersabar untuk menunggu proses broadcast sampai selesai</blockquote></b>", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("mohon balaꜱ atau ketik ꜱeꜱuatu...")
        
    susers = await get_list_from_vars(client.me.id, "SAVED_USERS")
    done = 0
    for chat_id in susers:
        try:
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<blockquote><b>Pesan broadcast berhasil terkirim ke {done} user</blockquote></b>\n\n<blockquote><b>`USERBOT 5K/BULAN BY` @Ipaaaaajaalaah_bot</b></blockquote>")
            
