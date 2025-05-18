from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL

@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id):
    await db.add_join_req(message.from_user.id)
    file_id = await db.get_stored_file_id(message.from_user.id)
    if not file_id:
        try:
            await client.send_message(message.from_user.id, "<b> Tʜᴀɴᴋꜱ ɢᴏᴛ ᴏɴᴇ ᴩʟᴇᴀꜱᴇ <u>ᴄᴏɴᴛɪɴᴜᴇ... </u>⚡ </b>")
        except:
            pass
        return
    msg = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        reply_markup=InlineKeyboardMarkup(
            [
             [
              InlineKeyboardButton('〄 Ғᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ / Wᴀᴛᴄʜ Oɴʟɪɴᴇ 〄', callback_data=f'generate_stream_link:{file_id}'),
             ],
             [
              InlineKeyboardButton('◈ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ◈', url=f'https://t.me/Bot_Cracker') #Don't change anything without contacting me @LazyDeveloperr
             ]
            ]
        )
    )
    btn = [[
        InlineKeyboardButton("! ɢᴇᴛ ꜰɪʟᴇ ᴀɢᴀɪɴ !", callback_data=f'delfile#{file_id}')
    ]]
    k = await client.send_message(chat_id = message.from_user.id, text=f"<b>❗️ <u>ɪᴍᴘᴏʀᴛᴀɴᴛ</u> ❗️</b>\n\n<b>ᴛʜɪꜱ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ</b> <b><u>10 ᴍɪɴᴜᴛᴇꜱ</u> </b><b>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ).</b>\n\n<b><i>📌 ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ.</i></b>")
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!\n\nᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇʟᴇᴛᴇᴅ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
    return

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
    await db.del_join_req()    
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")
