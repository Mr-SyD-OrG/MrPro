from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL, SYD_CHANNEL


@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  try:
      await db.add_join_req(message.from_user.id, message.chat.id)
  except Exception as e:
      await client.send_message(1733124290, e)
  data = await db.get_stored_file_id(message.from_user.id)
  if data:
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
    await db.remove_stored_file_id(message.from_user.id)
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!\n\nᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇʟᴇᴛᴇᴅ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ 👇</b>",reply_markup=InlineKeyboardMarkup(btn))
    return


#@Client.on_chat_join_request(filters.chat(SYD_CHANNEL))
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

@Client.on_callback_query(filters.regex("^jrq:") & filters.user(ADMINS))
async def jreq_callback(client, cq):
    action = cq.data.split(":")[1]

    # ---- REMOVE CHANNEL FLOW ----
    if action == "remove":
        ask = await cq.message.reply("📨 Send the **channel ID** you want to remove from all users.")
        await cq.answer()

        try:
            # WAIT FOR ADMIN INPUT
            response = await client.listen(
                chat_id=cq.from_user.id,
                timeout=60
            )
        except TimeoutError:
            await ask.edit("⏳ Timed out. Try again.")
            return

        if not response.text.isdigit():
            return await response.reply("❌ Invalid ID. Only numbers allowed.")

        channel_id = int(response.text)
        modified = await db.remove_channel_from_all_users(channel_id)

        return await response.reply(
            f"✅ Removed `{channel_id}` from **{modified}** users."
        )

    # ---- DELETE ALL ----
    if action == "del_all":
        await db.del_all_join_req()
        await cq.message.reply("🗑️ All join-requests deleted.")
        return await cq.answer("Cleared!")

    if action == "count":
        total = await db.req.count_documents({})
        await cq.message.reply(f"📊 Total join-requests: `{total}`")
        return await cq.answer("Loaded!")

      
@Client.on_message(filters.command("jreq") & filters.user(ADMINS))
async def jreq_menu(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❌ Remove Channel from All Users", callback_data="jrq:remove")],
        [InlineKeyboardButton("❌ Delete ALL Join-Requests", callback_data="jrq:del_all")],
        [InlineKeyboardButton("📊 View Count", callback_data="jrq:count")],
    ])

    await message.reply(
        "**📂 Join-Request Manager**\nSelect an option:",
        reply_markup=keyboard
    )


@Client.on_message(filters.command("jreq_user") & filters.user(ADMINS))
async def jreq_user_info(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/jreq_user <user_id>`")

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply("❌ Invalid user_id.")

    doc = await db.syd_user(user_id)
    if not doc:
        return await message.reply("❌ No such user in join-req database.")

    channels = doc.get("channels", [])
    count = doc.get("count", 0)
    timestamp = doc.get("time", 0)

    if timestamp:
        from datetime import datetime
        time_text = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    else:
        time_text = "Not set"

    text = (
        f"📌 **User Join-Req Info**\n\n"
        f"👤 **User ID:** `{user_id}`\n"
        f"📚 **Channels:** `{channels}`\n"
        f"⏱ **Time:** `{time_text}`\n"
        f"🔢 **Count:** `{count}`"
    )

    await message.reply(text)
  
