from PyroUbot import *

__MODULE__ = "ʜᴇʟᴘ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ⦫</b>

<blockquote><b>⎆ perintah :
ᚗ <code>{0}help</code>
  Untuk menampilkan semua fitur dari @alo</b></blockquote>
"""

@PY.UBOT("help")
async def show_inline_help(client, message):
    try:
        results = await client.get_inline_bot_results("GreatestJerzzUbot ", "help")

        if results.results:
            await client.send_inline_bot_result(
                chat_id=message.chat.id,
                query_id=results.query_id,
                result_id=results.results[0].id
            )
        else:
            await message.reply("Tidak ada hasil dari @alo.")
    except Exception as e:
        await message.reply(f"Error ambil hasil dari @alo:\n<code>{e}</code>")
