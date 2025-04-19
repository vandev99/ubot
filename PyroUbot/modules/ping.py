import os
import json
import asyncio
import psutil
# import speedtest

from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import *

@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping_formatted = round((end - start).microseconds / 10000, 2)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    pantek = await STR.PONG(client)
    ngentod = await STR.OWNER(client)
    kontol = await STR.UBOT(client)
    devs = await STR.DEVS(client)
    babi = client.me.is_premium
    if babi:
        _ping = f"""
<b>🜲 Userbot Speed!</b>
 • Pong: <code>{str(delta_ping_formatted).replace('.', ',')} ms</code>
 • Owner: @jerzzofficial
"""
        await message.reply(_ping)
    else:
        _ping = f"""
<b>🜲 Userbot Speed!</b>
 • Pong: <code>{str(delta_ping_formatted).replace('.', ',')} ms</code>
 • Owner: @jerzzofficial"""
        await message.reply(_ping)

@PY.INDRI("1ping")
async def _(client, message):
    command = message.text.split()
    if len(command) < 2:
        return
    
    haku = command[1].replace("@", "")

    if client.me.username != haku:
        return
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping_formatted = round((end - start).microseconds / 10000, 2)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    babi = client.me.is_premium
    if babi:
        _ping = f"""
<b>🜲 Userbot Speed!</b>
 • Pong: <code>{str(delta_ping_formatted).replace('.', ',')} ms</code>
 • Owner: @jerzzofficial"""
        await message.reply(_ping)
    else:
        await message.reply(f"<blockquote>pong : {str(delta_ping_formatted).replace('.', ',')} ms</blockquote>\n\n<blockquote><b>👾 USERBOT 👾</b></blockquote>")


