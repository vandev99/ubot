import requests
import os
import urllib.parse
from pyrogram import Client, filters
from pyrogram.types import Message

__MODULE__ = "costum enc"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴀsɪ 4<b>

<blockqoute><b>⎆ perintah :
ᚗ <code>{0}hypo</code> 
ᚗ <code>{0}bulan</code> 
ᚗ <code>{0}music</code> 
ᚗ <code>{0}sinyal</code> 
ᚗ <code>{0}dot</code> 
ᚗ <code>{0}car</code></b></blockqoute>
"""
# API Obfuscator
OBFUSCATOR_API_URL = "https://otaku-rest-api.vercel.app/api/obfuscated?apikey=jerzz&code="

@Client.on_message(filters.command("costumenc") & filters.reply)
async def encrypt_js(client: Client, message: Message):
    """ Fitur untuk mengenkripsi file JavaScript (.js) menggunakan API Otaku """
    
    # Pastikan ada file yang di-reply
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("❌ Balas file JavaScript (.js) dengan perintah ini.")
        return

    file = message.reply_to_message.document

    # Pastikan format file adalah .js
    if not file.file_name.endswith(".js"):
        await message.reply("❌ File harus berekstensi `.js`.")
        return
    
    # Download file sementara
    file_path = await client.download_media(file)
    
    # Baca isi file JavaScript
    with open(file_path, "r", encoding="utf-8") as f:
        js_code = f.read()

    # Encode ke URL agar bisa dikirim ke API
    encoded_code = urllib.parse.quote(js_code)

    # Kirim request ke API
    response = requests.get(f"{OBFUSCATOR_API_URL}{encoded_code}")

    # Hapus file sementara
    os.remove(file_path)

    # Cek jika API mengembalikan hasil
    if response.status_code == 200 and "result" in response.json():
        obfuscated_code = response.json()["result"]

        # Simpan hasil obfuscate ke file baru
        obfuscated_file_path = f"{file.file_name.replace('.js', '_obf.js')}"
        with open(obfuscated_file_path, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        # Kirim balik file hasil obfuscation
        await message.reply_document(obfuscated_file_path, caption="🔒 File berhasil dienkripsi!")

        # Hapus file hasil setelah dikirim
        os.remove(obfuscated_file_path)
    else:
        await message.reply("❌ Gagal mengenkripsi file. API mungkin sedang bermasalah.")
