import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from LUCY.events import register
from LUCY import telethn as tbot


LUCY = "https://telegra.ph/file/70657821f00fc1fb8e539.jpg"

@register(pattern=("/lucy"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm lucy bot.** \n\n"
  TEXT += "💞 **LUCY IS ALIVE** \n\n"
  TEXT += f"💞 **Owner : [SAIZO](https://t.me/LUCY_OWNER)** \n\n"
  TEXT += f"💞 **Library Version :** `{telever}` \n\n"
  TEXT += f"💞 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💞 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For using lucy 💞**"
  BUTTON = [[Button.url("Help", "https://t.me/LUCY_MANAGER2_bot?start=help"), Button.url("Support", "https://t.me/lucyhelp")]]
  await tbot.send_file(event.chat_id, LUCY, caption=TEXT,  buttons=BUTTON)
