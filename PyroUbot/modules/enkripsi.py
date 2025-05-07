import aiohttp
import os
from io import BytesIO
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "enc js"
__HELP__ = """
Command for <b>Enc Js</b>

<b>Enc Invisible</b>
   <code>{0}encinvis [ reply file js ]</code>

<b>Enc Case Break</b>
   <code>{0}enccase [ reply file js ]</code>

"""

API_KEY = "jerzz"
OBFUSCATE_API = "http://tramway.proxy.rlwy.net:21218/api/obfuscated"
CASEBREAK_API = "http://tramway.proxy.rlwy.net:21218/api/casebreak"


async def upload_file(buffer: BytesIO, filename: str) -> str:
    buffer.seek(0)
    form = aiohttp.FormData()
    form.add_field(
        'fileToUpload',
        buffer,
        filename=filename,
        content_type="application/javascript"
    )
    form.add_field('reqtype', 'fileupload')

    async with aiohttp.ClientSession() as session:
        async with session.post('https://catbox.moe/user/api.php', data=form) as response:
            if response.status != 200:
                raise Exception(f"Failed to upload file: {response.status}")
            return await response.text()

async def process_file(api_url: str, upload_url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}?apikey={API_KEY}&fileurl={upload_url}") as response:
            if response.status != 200:
                raise Exception(f"Failed to process file: {response.status}")
            data = await response.json()
            if data.get("status"):
                return data.get("result")
            raise Exception("Failed to retrieve processed file")

async def download_file(url: str, filename: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to download file: {response.status}")
            with open(filename, "wb") as f:
                f.write(await response.read())

async def process_enc(client, message, api_url):
    reply_message = message.reply_to_message
    if reply_message and reply_message.document and reply_message.document.file_name.endswith(".js"):
        downloaded_file = await reply_message.download()
        file_name = reply_message.document.file_name
        
        with open(downloaded_file, 'rb') as f:
            buffer = BytesIO(f.read())

            try:
                upload_url = await upload_file(buffer, file_name)
                processed_url = await process_file(api_url, upload_url)

                await download_file(processed_url, file_name)
                await message.reply_document(file_name, caption="✅ Proses berhasil!")

                os.remove(file_name)

            except Exception as e:
                await message.reply(f"❌ Error: {e}")

    else:
        await message.reply("❌ Reply ke file JavaScript (.js) untuk diproses.")

@PY.UBOT("encinvis")
@PY.TOP_CMD
async def encinvis(client, message):
    await process_enc(client, message, OBFUSCATE_API)

@PY.UBOT("enccase")
@PY.TOP_CMD
async def enccase(client, message):
    await process_enc(client, message, CASEBREAK_API)
