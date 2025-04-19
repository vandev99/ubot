from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "VideoChat"
__HELP__ = """
Command for <b>VideoChat</b>

<b>Start a video chat</b>
   <code>{0}startvc</code> [title chat]

<b>Join the video chat</b>
   <code>{0}joinvc</code>

<b>Leave current video chat</b>
   <code>{0}leavevc</code>

<b>End a video chat</b>
   <code>{0}stopvc</code>

"""

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply(f"Video call group not found {err_msg}")
    return False

@PY.UBOT("jjjjjvccc")
async def joinvc(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        meira = await message.reply(f"{prs} <b>Processing...</b>")
    else:
        meira = await message.reply(f"{prs} <b>Processing...</b>")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await meira.edit(f"<b>Error {e}</b>")
    await meira.edit(
        "{} <b>Successfully joined voice chat\n• Chat :</b> {}".format(sks,message.chat.title)
    )
    await asyncio.sleep(5)
    await client.group_call.set_is_mute(True)
    await sleep(3)
    await client.group_call.set_is_mute(True)


@PY.UBOT("llllbleavevc")
async def leavevc(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        meira = await message.reply(f"{prs} <b>Processing...</b>")
    else:
        meira = await message.reply(f"{prs} <b>Processing...</b>")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await meira.edit(message, f"<b>ERROR:</b> `{e}`")
    msg = (f"{sks} <b>Successfully left voice chat</b>\n<b>• Chat :</b><code>{chat_id}</code>")
    await meira.edit(msg)

@PY.UBOT("startvc")
async def opengc(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    flags = " ".join(message.command[1:])
    meira = await message.edit(f"{prs} <b>Processing</b>...")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"{sks} <b>Voice chat enabled</b>\n • <b>Chat</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await meira.edit(args)
    except Exception as e:
        await meira.edit(f"<b>Info:</b> `{e}`")

@PY.UBOT("stopvc")
async def end_vc_(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    meira = await message.edit(f"{prs} <b>Processing</b>...")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", ᴇʀʀᴏʀ!"))
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await meira.edit(
        f"{sks} <b>Voice chat is disabled</b>\n • <b>Chat</b> : {message.chat.title}"
    )
