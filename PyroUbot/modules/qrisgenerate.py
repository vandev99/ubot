import requests
import qrcode
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ǫʀɪs ɢᴇɴᴇʀᴀᴛᴏʀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk QRIS Generator</b>

Perintah:
<code>{0}qris [nominal]</code> → Membuat QRIS sesuai nominal yang dimasukkan (Hanya untuk Owner)

Sumber: API OkeConnect.</blockquote></b>
"""

# Data OrderKuota
MERCHANT_ID = "OK2144154"
API_KEY = "715443817341525532144154OKCT4D1E6B6714A1A0AD686F47D2FC7A6E21"
CODE_QR = "00020101021126670016COM.NOBUBANK.WWW01189360050300000879140214520578090269750303UMI51440014ID.CO.QRIS.WWW0215ID20243618485650303UMI5204541153033605802ID5924HANXZ OFFICIAL OK21441546015JAKARTA SELATAN61051211062070703A0163048EBF"

# API URL
API_URL = f"https://gateway.okeconnect.com/api/mutasi/qris/{MERCHANT_ID}/{API_KEY}"

# ID Telegram Owner
OWNER_ID = [5574764542]  # Ganti dengan ID Owner Telegram kamu

@PY.UBOT("qris")
@PY.TOP_CMD
async def _(client, message):
    if message.from_user.id not in OWNER_ID:
        return await message.reply("❌ Anda tidak memiliki izin untuk menggunakan fitur ini!")

    msg = await message.reply("⏳ Sedang memproses QRIS...")

    # Ambil nominal dari pesan
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        return await msg.edit("❌ Format salah! Gunakan: <code>.qris [nominal]</code>")

    NOMINAL = int(args[1])

    # Kirim request ke API
    payload = {
        "merchant_id": MERCHANT_ID,
        "api_key": API_KEY,
        "code_qr": CODE_QR,
        "amount": NOMINAL
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            qris_data = response.json()
            qris_code = qris_data.get("qris_code")

            # Generate QR Code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qris_code)
            qr.make(fit=True)

            # Simpan QR ke file
            qr_filename = f"qris_{NOMINAL}.png"
            img = qr.make_image(fill="black", back_color="white")
            img.save(qr_filename)

            await message.reply_document(qr_filename, caption=f"✅ QRIS Rp{NOMINAL} berhasil dibuat!")

        else:
            await msg.edit("❌ Gagal membuat QRIS: " + response.text)

    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")
