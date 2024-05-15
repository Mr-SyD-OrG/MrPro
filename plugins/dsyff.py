import asyncio 
from database.users_chats_db import Database, db
from Script import script
from pyrogram import Client, filters, enums
from .test import get_configs, update_configs, CLIENT, parse_buttons
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import ChatAdminRequired

CLIENT = CLIENT()

@Client.on_message(filters.command('clon'))
async def settings(client, message):
   await message.reply_text(
     "<b>📝 Eᴅɪᴛ Δɴᴅ ᴄʜᴀɴɢᴇ ꜱΞᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.......\n<blockquote>ᴩʀᴏ ✨</blockquote></b>",
     reply_markup=main_buttons()
     )

@Client.on_callback_query(filters.regex(r'^clon'))
async def settings_query(bot, query):
  user_id = query.from_user.id
  i, type = query.data.split("#")
  buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data="clon#main")]]
  if type=="main":
     await query.message.edit_text(
       "<b>📝 Eᴅɪᴛ Δɴᴅ ᴄʜᴀɴɢᴇ ꜱΞᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.......\n<blockquote>ᴩʀᴏ ✨</blockquote></b>",
       reply_markup=main_buttons())

  elif type=="bots":
     buttons = [] 
     _bot = await db.get_bot(user_id)
     if _bot is not None:
        buttons.append([InlineKeyboardButton(_bot['name'],
                         callback_data=f"clon")])
     else:
        buttons.append([InlineKeyboardButton('✚ Aᴅᴅ ʙᴏᴛ ✚', 
                         callback_data="clon#addbot")])
        buttons.append([InlineKeyboardButton('✚ Aᴅᴅ Uꜱᴇʀ ʙᴏᴛ ✚', 
                         callback_data="clon#adduserbot")])
     buttons.append([InlineKeyboardButton('«« ʙΔᴄᴋ', 
                      callback_data="settingsn")])
     await query.message.edit_text(
       "<b><u>Mʏ 8ᴏᴛꜱ</b></u>\n\n<b>Yoᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʙᴏᴛ'ꜱ ʜᴇʀᴇ😜</b>",
       reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addbot":
     await query.message.delete()
     bot = await CLIENT.add_bot(bot, query)
     if bot != True: return
     await query.message.reply_text(
        "<b>Bᴏᴛ ꜱUᴄᴄᴇꜱꜱ ꜰUʟʟʏ Δᴅᴅᴇᴅ ᴛᴏ Sʏᴅ-ʙᴀꜱᴇ</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="editbot": 
     bot = await db.get_bot(user_id)
     TEXT = Script.BOT_DETAILS if bot['is_bot'] else Script.USER_DETAILS
     buttons = [[InlineKeyboardButton('❌ Remove ❌', callback_data=f"settings#removebot")
               ],
               [InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data="clon#bots")]]
     await query.message.edit_text(
        TEXT.format(bot['name'], bot['id'], bot['username']),
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="removebot":
     await db.remove_bot(user_id)
     await query.message.edit_text(
        "<b>successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))
def main_buttons():
  buttons = [[
       InlineKeyboardButton('🤖 Бᴏᴛꜱ 🤖',
                    callback_data=f'clon#addbot'),
       InlineKeyboardButton('👣 CʜᴀИИᴇʟꜱ 👣',
                    callback_data=f'clon')
  ]]
  return InlineKeyboardMarkup(buttons)
