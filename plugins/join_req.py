from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL, SYD_CHANNEL

@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id, AUTH_CHANNEL):
    await db.add_join_req(message.from_user.id, AUTH_CHANNEL)
    data = await db.get_stored_file_id(message.from_user.id)
    
    if not data:
        try:
            await client.send_message(message.from_user.id, "<b>ᴛʜᴀɴᴋꜱ ғᴏʀ ᴊᴏɪɴɪɴɢ ! ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ <u>ᴄᴏɴᴛɪɴᴜᴇ</u> ɴᴏᴡ ⚡</b>")
        except:
            pass
        return
    file_id = data["file_id"]
    messyd = int(data["mess"])
     
    try:
        syd = await client.get_messages(chat_id=message.from_user.id, message_ids=messyd)
    except:
        syd = None
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
    await syd.delete()
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!\n\nᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇʟᴇᴛᴇᴅ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
    await db.remove_stored_file_id(message.from_user.id)
    return


@Client.on_chat_join_request(filters.chat(SYD_CHANNEL))
async def join_reqqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id, SYD_CHANNEL):
    await db.add_join_req(message.from_user.id, SYD_CHANNEL)
    data = await db.get_stored_file_id(message.from_user.id)
    
    if not data:
        return 
        try:
            await client.send_message(message.from_user.id, "<b>ᴛʜᴀɴᴋꜱ ғᴏʀ ᴊᴏɪɴɪɴɢ ! ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ <u>ᴄᴏɴᴛɪɴᴜᴇ</u> ɴᴏᴡ ⚡</b>")
        except:
            pass
        return
    file_id = data["file_id"]
    messyd = int(data["mess"])
     
    try:
        syd = await client.get_messages(chat_id=message.from_user.id, message_ids=messyd)
    except:
        syd = None
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
    await syd.delete()
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!\n\nᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇʟᴇᴛᴇᴅ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
    await db.remove_stored_file_id(message.from_user.id)
    return

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
    await db.delete_all_join_req()    
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")


@Client.on_callback_query(filters.regex("^jrq:") & filters.user(ADMINS))
async def jreq_callback(client, cq):
    action = cq.data.split(":")[1]

    if action == "del_auth":
        result = await db.delete_channel_users(AUTH_CHANNEL)
        await cq.message.reply(f"🗑️ Deleted **{result.deleted_count}** users from AUTH_CHANNEL.")
        return await cq.answer("Deleted!")

    if action == "del_syd":
        result = await db.delete_channel_users(SYD_CHANNEL)
        await cq.message.reply(f"🗑️ Deleted **{result.deleted_count}** users from SYD_CHANNEL.")
        return await cq.answer("Deleted!")

    if action == "del_all":
        await db.delete_all_join_req()
        await cq.message.reply("🗑️ All join requests deleted.")
        return await cq.answer("Cleared!")

    if action == "count":
        auth_count = await db.req.count_documents({"channel_id": AUTH_CHANNEL})
        syd_count = await db.req.count_documents({"channel_id": SYD_CHANNEL})
        total = await db.req.count_documents({})

        await cq.message.reply(
            f"📊 **Join Request Count:**\n"
            f"• AUTH_CHANNEL: `{auth_count}`\n"
            f"• SYD_CHANNEL : `{syd_count}`\n"
            f"• Total       : `{total}`"
        )
        return await cq.answer("Loaded!")

@Client.on_message(filters.command("jreq") & filters.user(ADMINS))
async def jreq_menu(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🗑️ Delete AUTH Channel", callback_data="jrq:del_auth")],
        [InlineKeyboardButton("🗑️ Delete SYD Channel", callback_data="jrq:del_syd")],
        [InlineKeyboardButton("🗑️ Delete ALL", callback_data="jrq:del_all")],
        [InlineKeyboardButton("📊 View Count", callback_data="jrq:count")],
    ])

    await message.reply(
        "**📂 Join-Request Manager**\nSelect an option:",
        reply_markup=keyboard
    )
