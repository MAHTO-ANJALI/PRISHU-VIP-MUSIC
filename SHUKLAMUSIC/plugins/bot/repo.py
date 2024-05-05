from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ 𝗞𝗬𝗔 𝗕𝗘 𝗕𝗦𝗗𝗞 ✪
 
 ➲ 𝗥𝗘𝗣𝗢 𝗖𝗛𝗔𝗛𝗜𝗬𝗘 ✰
 
 ➲ 𝗟𝗔𝗡𝗗 𝗟𝗘 𝗠𝗘𝗥𝗔 ✰
 
 ➲ 𝗩𝗢 𝗕𝗛𝗜 𝗠𝗨𝗛 𝗠𝗔𝗜𝗡 ✰
 
 ➲ 𝗣𝗔𝗛𝗟𝗘 𝗧𝗨 𝗠𝗨𝗝𝗘 ✰
 
 ➲ 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗧𝗔𝗕 ✰
 
 ► 𝗥𝗘𝗣𝗢 𝗗𝗨𝗡𝗚𝗔
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⚡ 𝗔𝗗𝗗 𝗠𝗘 ⚡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("🤍 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🤍", url="https://t.me/RBGOFFICIAL1"),
          InlineKeyboardButton("👑 𝗢𝗪𝗡𝗘𝗥 👑", url="https://t.me/l_MR_ll_KING_l"),
          ],
               [
                InlineKeyboardButton("🖤 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🖤", url="http://t.me/+YvPfBPHypFgzOTY9"),

],
[
              InlineKeyboardButton("🔥 𝐌𝐔𝐒𝐈𝐂 𝐑𝐄𝐏𝐎 🔥", url=f"https://t.me/NOBiTA_FIREX"),
              InlineKeyboardButton("︎", url=f""),
              ],
              [
              InlineKeyboardButton("", url=f""),
InlineKeyboardButton("", url=f""),
],
[
InlineKeyboardButton("", url=f""),
InlineKeyboardButton("", url=f""),
],
[
              InlineKeyboardButton("", url=f""),
              InlineKeyboardButton("", url=f""),
              ],
              [
              InlineKeyboardButton("", url=f""),
InlineKeyboardButton("", url=f""),
],
[
InlineKeyboardButton("", url=f""),
InlineKeyboardButton("", url=f""),
],
[
InlineKeyboardButton("", url=f""),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/27bc3892175c6edcd76fe.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/MAHTO-ANJALI/PRISHUxMUSICxBOT/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/MAHTO-ANJALI/PRISHUxMUSICxBOT) | [UPDATES](https://t.me/N3ON_BIO)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


