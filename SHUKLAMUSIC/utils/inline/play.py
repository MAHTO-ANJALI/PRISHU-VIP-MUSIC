import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from SHUKLAMUSIC import app
import config
from SHUKLAMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    SHUKLAMUSIC = math.floor(percentage)
    if 0 < SHUKLAMUSIC <= 10:
        bar = "𖢵—————————"
    elif 10 < SHUKLAMUSIC < 20:
        bar = "—𖢵————————"
    elif 20 <= SHUKLAMUSIC < 30:
        bar = "——𖢵———————"
    elif 30 <= SHUKLAMUSIC < 40:
        bar = "———𖢵——————"
    elif 40 <= SHUKLAMUSIC < 50:
        bar = "————𖢵—————"
    elif 50 <= SHUKLAMUSIC < 60:
        bar = "—————𖢵————"
    elif 60 <= SHUKLAMUSIC < 70:
        bar = "——————𖢵———"
    elif 70 <= SHUKLAMUSIC < 80:
        bar = "———————𖢵——"
    elif 80 <= SHUKLAMUSIC < 95:
        bar = "————————𖢵—"
    else:
        bar = "—————————𖢵"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❚❚",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Skip {videoid}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="✚", callback_data=f"add_playlist|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="[🇮🇳] Dᴇᴠ", url=f"https://t.me/N3ON_xD"),
            InlineKeyboardButton(
                text="Cʜᴀᴛ Gʀᴏᴜᴘ", url=f"https://t.me/DANGEROUS_FIGHTER_GROUP"
            ),
        ],
        [
            InlineKeyboardButton(
                text="• Cʟᴏsᴇ •", callback_data=f"ADMIN CloseA|{chat_id}"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    OpVirMusic = math.floor(percentage)
    if 0 < SHUKLAMUSIC <= 10:
        bar = "⬤─────────"
    elif 10 < SHUKLAMUSIC < 20:
        bar = "━⬤────────"
    elif 20 <= SHUKLAMUSIC < 30:
        bar = "━━⬤───────"
    elif 30 <= SHUKLAMUSIC < 40:
        bar = "━━━⬤──────"
    elif 40 <= SHUKLAMUSIC < 50:
        bar = "━━━━⬤─────"
    elif 50 <= SHUKLAMUSIC < 60:
        bar = "━━━━━⬤────"
    elif 60 <= SHUKLAMUSIC < 70:
        bar = "━━━━━━⬤───"
    elif 70 <= SHUKLAMUSIC < 80:
        bar = "━━━━━━━⬤──"
    elif 80 <= SHUKLAMUSIC < 95:
        bar = "━━━━━━━━⬤─"
    else:
        bar = "━━━━━━━━━⬤"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❚❚",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(
                text="↻", callback_data=f"ADMIN Skip {videoid}|{chat_id}"
            ),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="✚", callback_data=f"add_playlist|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="• Cʟᴏsᴇ •", callback_data=f"ADMIN CloseA|{chat_id}"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❚❚",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Skip {videoid}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="✚", callback_data=f"add_playlist|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="• Cʟᴏsᴇ •", callback_data=f"ADMIN CloseA|{chat_id}"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❚❚",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Skip {videoid}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="• Cʟᴏsᴇ •", callback_data=f"ADMIN CloseA|{chat_id}"
            )
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
