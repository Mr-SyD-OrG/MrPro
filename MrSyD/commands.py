from info import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from pyrogram import Client, filters, enums
from database.users_chats_db import db
from pyrogram import Client, filters
import datetime
import time
from utils import broadcast_messages, is_subscribed, broadcast_messages_group
import asyncio



@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")

@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_group(bot, message):
    groups = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages To Groups...'
    )
    start_time = time.time()
    total_groups = await db.total_chat_count()
    done = 0
    failed =0

    success = 0
    async for group in groups:
        pti, sh = await broadcast_messages_group(int(group['id']), b_msg)
        if pti:
            success += 1
        elif sh == "Error":
                failed += 1
        done += 1
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Groups {total_groups}\nCompleted: {done} / {total_groups}\nSuccess: {success}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Groups {total_groups}\nCompleted: {done} / {total_groups}\nSuccess: {success}")
        

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        try:
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
        except:
            pass
    if not await is_subscribed(client, message):
        btn = [[InlineKeyboardButton("⊛ Jᴏɪɴ Uᴘᴅᴀᴛᴇꜱ CʜᴀɴɴᴇL ⊛", url=f"https://t.me/{FSUB_UNAME}")]]
        await client.send_message(
            message.from_user.id,
            "Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ ᴀɴᴅ Tʜᴇɴ Cʟɪᴄᴋ Oɴ /start \n<blockquote>Tʜɪꜱ ɪꜱ ᴀ ꜰʀᴇᴇ ꜱᴇʀᴠɪᴄᴇ ꜱᴏ, ᴩʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ 🙃</blockquote>",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return
    if len(message.command) != 2:
        await message.reply_text(
             text=f"<b>OUR BOTS:\n\n• @MovSearch_X5_Bot\n• {USERNAME} ✅\n• @MovFil_Bot ✅\n\n<i>One Of The Bot Maybe Down Use Others</i></b>",   
             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🥶 ᴏʀ ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ 🥶", url=f"https://t.me/+5n7vViwKXJJiMjhl")]])
        )
        return
    if len(message.command) == 2 and message.command[1] in ["error", "goon"]:
        await message.reply_text(
             text="<b>Tʜᴀɴᴋꜱ ᴜꜱᴇ ᴛʜᴀᴛ ʙᴏᴛ ɴᴏᴡ..! \n• @Mr_MovSearch_X1_Bot </b>",   
             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CONTINUE GETTING...", url=f"https://t.me/Mr_MovSearch_X1_Bot")]])
        )
        
    if len(message.command) == 2 and message.command[1] in ["syd", "gon"]:
        await message.reply_text(
             text=f"<b>Tʜᴀɴᴋꜱ ᴜꜱᴇ ᴛʜᴀᴛ ʙᴏᴛ ɴᴏᴡ..! \n• @{USERNAME} </b>",   
             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CONTINUE GETTING...", url=f"https://t.me/{USERNAME}")]])
        )

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    await message.reply_text(
         text=f"<b>OUR BOTS:\n\n• @MovSearch_X6_Bot ❄️\n• {USERNAME} \n• @MovFil_Bot\n\n<i>One Of The Bot Maybe Down Use Others</i></b>",   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ꜱᴇɴᴅ ʜᴇʀᴇ 🫧", url=f"https://t.me/+5n7vViwKXJJiMjhl")]])
    )
    return


 
