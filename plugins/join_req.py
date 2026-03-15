from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL, SYD_CHANNEL


@Client.on_chat_join_request()
async def join_reqs(client, message: ChatJoinRequest):
    authchnl = await db.get_fsub_list()
    if message.chat.id not in authchnl:
      #  await handle_join_request(client, message)
        return
    try:
        await db.add_join_req(message.from_user.id, message.chat.id)
    except Exception as e:
        await client.send_message(1733124290, e)
    data = await db.get_stored_file_id(message.from_user.id)
    if data:
        file_id = data["file_id"]
        messyd = int(data["mess"])
        is_sub = await is_subscribed(client, message)
        fsub, ch1, ch2 = await get_authchannel(client, message)
        try:
            syd = await client.get_messages(chat_id=message.from_user.id, message_ids=messyd)
        except:
            syd = None
        if not (fsub and is_sub) and syd:
            try:
                invite_link, invite_link2 = None, None
                if ch1:
                    invite_link = await client.create_chat_invite_link(int(ch1), creates_join_request=True)
                if ch2:
                    invite_link2 = await client.create_chat_invite_link(int(ch2), creates_join_request=True)
                btn = []

                if invite_link:
                    btn.append([InlineKeyboardButton("⊛ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ CʜᴀɴɴᴇL ¹⊛", url=invite_link.invite_link)])
 
                if invite_link2:
                    btn.append([InlineKeyboardButton("⊛ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ CʜᴀɴɴᴇL ²⊛", url=invite_link2.invite_link)])
                
                if not is_sub:
                    btn.append([InlineKeyboardButton("⊛ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ CʜᴀɴɴᴇL ³⊛", url=f"https://t.me/{FSUB_UNAME}")])
                  
            
                btn.append([InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ ↻", callback_data=f"checksub##{file_id}")])
                
                await syd.edit_text(
                    text="<b>Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ</b> Aɴᴅ Tʜᴇɴ Cʟɪᴄᴋ Oɴ Tʀʏ Aɢᴀɪɴ Tᴏ Gᴇᴛ Yᴏᴜʀ Rᴇǫᴜᴇꜱᴛᴇᴅ Fɪʟᴇ.",
                    reply_markup=InlineKeyboardMarkup(btn),
                    parse_mode=enums.ParseMode.HTML
                )
                return
            except Exception as e:
                await client.send_message(1733124290, f"{e} Fsub Error ")
               
        try:
            files_ = await get_file_details(file_id)
            f_caption = None
            if files_:
                files = files_[0]
                title = '' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files.file_name.replace('_', ' ').split()))
                size = get_size(files.file_size)
                f_caption = f"<code>{title}</code>"
                sydcp = await extract_audio_subtitles_formatted(files.caption)
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption = CUSTOM_FILE_CAPTION.format(
                            file_name=title or '',
                            file_size=size or '',
                            file_caption='',
                            sydaudcap=sydcp if sydcp else ''
                        )
                    except:
                        pass
        except:
            pass
        msg = await client.send_cached_media(
            chat_id=message.from_user.id,
            file_id=file_id,
            caption=f_caption,
            reply_markup=InlineKeyboardMarkup(
                [[
                  InlineKeyboardButton('〄 Ғᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ / Wᴀᴛᴄʜ Oɴʟɪɴᴇ 〄', callback_data=f'generate_stream_link:{file_id}'),
                 ],[
                  InlineKeyboardButton('◈ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ◈', url=f'https://t.me/Bot_Cracker') #Don't change anything without contacting me @LazyDeveloperr
                 ]]
            )
        )
        btn = [[
            InlineKeyboardButton("! ɢᴇᴛ ꜰɪʟᴇ ᴀɢᴀɪɴ !", callback_data=f'delfile#{file_id}')
        ]]
        k = await client.send_message(chat_id = message.from_user.id, text=f"<b>❗️ <u>ɪᴍᴘᴏʀᴛᴀɴᴛ</u> ❗️</b>\n\n<b>ᴛʜɪꜱ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ</b> <b><u>10 ᴍɪɴᴜᴛᴇꜱ</u> </b><b>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ).</b>\n<blockquote><b><i>📌 ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ.</i></b></blockquote>")
        try:
            await syd.delete()
        except:
            pass
        await db.remove_stored_file_id(message.from_user.id)
        await asyncio.sleep(600)
        await msg.delete()
        await k.edit_text("<blockquote><b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!\n\nᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴅᴇʟᴇᴛᴇᴅ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ 👇</b></blockquote>",reply_markup=InlineKeyboardMarkup(btn))
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

@Client.on_message(filters.command("jreq") & filters.user(ADMINS))
async def jreq_menu(client, message):
    btn = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("[ − ] Remove A Channel", "jsyd:remove"),
            InlineKeyboardButton("[ × ] Delete All JReQ", "jsyd:del_all")
        ],
        [
            InlineKeyboardButton("[ # ] View Count", "jsyd:count"),
            InlineKeyboardButton("[ + ] Add Channel", "jsyd:add")
        ],
        [
            InlineKeyboardButton("[ − ] Remove One", "jsyd:remove_one"),
            InlineKeyboardButton("[ ⌫ ] Clear List", "jsyd:clear")
        ],
        [
            InlineKeyboardButton("[ ≡ ] View List", "jsyd:view"),
            InlineKeyboardButton("[ ✕ ] Close", "jsyd:close")
        ]
    ])

    await message.reply(
        "**Join-Request Manager**\nSelect an action:",
        reply_markup=btn
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❌ Remove Channel from All Users", callback_data="jrq:remove")],
        [InlineKeyboardButton("❌ Delete ALL Join-Requests", callback_data="jrq:del_all")],
        [InlineKeyboardButton("📊 View Count", callback_data="jrq:count")],
        [InlineKeyboardButton("➕ Add Channel", callback_data="fsyd_add")],
        [InlineKeyboardButton("🗑 Remove One", callback_data="fsyd_remove_one")],
        [InlineKeyboardButton("❌ Clear All", callback_data="fsyd_clear")],
        [InlineKeyboardButton("📄 View List", callback_data="fsyd_view")],
        [InlineKeyboardButton("✖ Close", callback_data="fsyd_close")]
    ])

   #₹ await message.reply(
    #    "**📂 Join-Request Manager**\nSelect an option:",
 #       reply_markup=keyboard
 #   )

#@Client.on_callback_query(filters.regex("^bot_fsub_back$") & filters.user(ADMINS))
async def fsub_back(client, cb):
    await jreq_menu(client, cb.message)
    await cb.message.delete()

#@Client.on_callback_query(filters.regex("^fsud_del_") & filters.user(ADMINS))
async def fsub_delet_one(client, cb):
    chat_id = int(cb.data.split("_")[-1])
    await db.remove_fsub_channel(chat_id)
    modified = await db.remove_channel_from_all_users(chat_id)
    await cb.message.edit_text(f"✅ Removed `{chat_id}`, `{modified}` from force-sub list.")
    

#@Client.on_callback_query(filters.regex("^fsyd_") & filters.user(ADMINS))
async def fsub_callacks(client, cb):
    data = cb.data
    if data == "fsyd_close":
        return await cb.message.delete()

    if data == "fsyd_view":
        try:
           channels = await db.get_fsub_list()
        except Exception as e:
            await cb.message.edit_text(e)
        if not channels:
            return await cb.answer("No force-sub channels set", show_alert=True)

        text = "📄 **Force-Sub Channels:**\n\n"
        for ch in channels:
            text += f"`{ch}`\n"

        return await cb.message.edit_text(text)

    if data == "fsyd_clear":
        await db.clear_fsub()
        await db.del_all_join_req()
        return await cb.message.edit_text("✅ Force-sub list cleared.")

    if data == "fsyd_add":
        await cb.message.edit_text(
            "➕ **Send channel ID or forward a channel message**\n\n"
            "Use /cancel to abort."
        )

        try:
            msg = await client.listen(cb.from_user.id, timeout=120)
        except:
            return await cb.message.edit_text("⏳ Timeout.")

        if msg.text and msg.text.lower() == "/cancel":
            return await cb.message.edit_text("❌ Cancelled.")

        if msg.forward_from_chat:
            chat_id = msg.forward_from_chat.id
        else:
            try:
                chat_id = int(msg.text.strip())
            except:
                return await cb.message.edit_text("❌ Invalid channel ID.")

        await db.add_fsub_channel(chat_id)
        return await cb.message.edit_text(f"✅ Added `{chat_id}` to force-sub list.")
    
    if data == "fsyd_remove_one":
        channels = await db.get_fsub_list()
        if not channels:
            return await cb.answer("List is empty", show_alert=True)

        btn = [
            [InlineKeyboardButton(str(ch), callback_data=f"fsud_del_{ch}")]
            for ch in channels
        ]
        btn.append([InlineKeyboardButton("⬅ Back", callback_data="bot_fsub_back")])

        return await cb.message.edit_text(
            "🗑 **Select channel to remove**",
            reply_markup=InlineKeyboardMarkup(btn)
        )


@Client.on_callback_query(filters.regex("^jsyd:") & filters.user(ADMINS))
async def jsyd_callback(client, cb):
    d = cb.data.split(":", 1)[1]
    await cb.answer()

    if d == "remove":
        ask = await cb.message.reply("📨 Send the **channel ID** you want to remove from all users.")
        try:
            r = await client.listen(cb.from_user.id, timeout=60)
            if not r.text.isdigit():
                return await r.reply("❌ Invalid ID. Only numbers allowed.")
            cid = int(r.text)
            m = await db.remove_channel_from_all_users(cid)
            return await r.reply(f"✅ Removed `{cid}` from **{m}** users.")
        except TimeoutError:
            return await ask.edit("⏳ Timed out. Try again.")

    if d == "del_all":
        await db.del_all_join_req()
        return await cb.message.reply("🗑️ All join-requests deleted.")

    if d == "count":
        return await cb.message.reply(
            f"📊 Total join-requests: `{await db.req.count_documents({})}`"
        )

    if d == "close":
        return await cb.message.delete()

    if d == "view":
        ch = await db.get_fsub_list()
        return (
            await cb.answer("No force-sub channels set", show_alert=True)
            if not ch else
            await cb.message.edit_text(
                "📄 **Force-Sub Channels:**\n\n" + "\n".join(f"`{x}`" for x in ch)
            )
        )

    if d == "clear":
        await db.clear_fsub()
        await db.del_all_join_req()
        return await cb.message.edit_text("✅ Force-sub list cleared.")

    if d == "add":
        await cb.message.edit_text(
            "➕ **Send channel ID(s) or forward channel message**\n"
            "• Multiple IDs allowed (space / newline separated)\n"
            "• Use /cancel to abort."
        )
        try:
            m = await client.listen(cb.from_user.id, timeout=120)

            if m.from_user.id != cb.from_user.id:
                return await cb.message.edit_text("❌ Unauthorized input.")

            if m.text and m.text.lower() == "/cancel":
                return await cb.message.edit_text("❌ Cancelled.")

            ids = []

            if m.forward_from_chat:
                ids = [m.forward_from_chat.id]
            else:
                for x in m.text.replace("\n", " ").split():
                    if x.lstrip("-").isdigit():
                        ids.append(int(x))

            if not ids:
                return await cb.message.edit_text("❌ No valid channel IDs found.")

            for cid in ids:
                await db.add_fsub_channel(cid)

            return await cb.message.edit_text(
                f"✅ Added **{len(ids)}** channel(s) to force-sub list."
            )

        except Exception as e:
            return await cb.message.edit_text(f"❌ Invalid input or timeout. {e}")


    if d == "remove_one":
        ch = await db.get_fsub_list()
        if not ch:
            return await cb.answer("List is empty", show_alert=True)
        btn = [[InlineKeyboardButton(str(x), f"jsyd:del_{x}")] for x in ch]
        btn.append([InlineKeyboardButton("⬅ Back", "jsyd:menu")])
        return await cb.message.edit_text(
            "🗑 **Select channel to remove**",
            reply_markup=InlineKeyboardMarkup(btn)
        )

    if d.startswith("del_"):
        cid = int(d.split("_", 1)[1])
        await db.remove_fsub_channel(cid)
        m = await db.remove_channel_from_all_users(cid)
        return await cb.message.edit_text(f"✅ Removed `{cid}`, `{m}` from force-sub list.")

    if d == "menu":
        return await send_jsyd_menu(cb.message)
        
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
  
