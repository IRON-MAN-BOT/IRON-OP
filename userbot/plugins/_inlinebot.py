from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from LEGENDBOT.utils import *
from userbot.Config import Config
from userbot import ALIVE_NAME
LEGEND_row = Config.BUTTONS_IN_HELP
LEGEND_emoji = Config.EMOJI_IN_HELP
# thats how a lazy guy imports
# LEGENDBOT

def button(page, modules):
    Row = LEGEND_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{LEGEND_emoji} " + pair + f" ✯", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )
        
    buttons.append(
        [
            custom.Button.inline(
               f"⭅ϐαϲκ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"💝 ❌ 💝", data="close"
            ),
            custom.Button.inline(
               f"ղҽxԵ⭆", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in LEGENDBOT channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@LEGEND_Userbot":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            result = await builder.article(
                f"Hey! Only use .help please", 
                text=f"🔰[{ALIVE_NAME}](https://t.me/Legend_Mr_Hacker)\n\n📁ղօ. օբ ρℓµɠเɳร ιиѕταℓℓє∂⭆ `{len(CMD_HELP)}` \n🗂τοταℓ ϲοммαи∂ѕ⭆ `{len(apn)}`\n📙թαցҽ⭆ 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            result = builder.article(
                "@LEGEND_Userbot",
                text="""**Hey! This is [ℓєgєи∂ϐοτ.](https://t.me/Legend_Mr_Hacker) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 ϲяєατοя 🔥", "https://t.me/Legend_Mr_Hacker"),
                        custom.Button.url(
                            "⚡ οωиєя ⚡", "https://t.me/Legend_Mr_Hacker"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ яєρο ✨", "https://github.com/LEGEND-OS/LEGENDBOT"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "мιℓ gγι ταѕαℓℓι..? καϐѕє мєяє ϐοτ мє υиgℓι κя янє н. κнυ∂κα ϐиα ℓο иα αgя ϲнαιγє το ρτα инι καнα ѕє ααנατє н ∂ιѕτυяϐ κяиє. ©ℓєgєи∂ϐοτ™(https://t.me/Legend_Userbot)",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        await event.edit(
            f"🛡️[{ALIVE_NAME}](https://t.me/Legend_Mr_Hacker) ฬ๏гкเภﻮ.....\n\n📁ղօ. օբ ρℓµɠเɳร ιиѕταℓℓє∂⭆ `{len(CMD_HELP)}`\n🗂τοταℓ ϲοммαи∂ѕ⭆ `{len(apn)}` \n📙թαցҽ⭆ {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_LEGEND(event,
              "⚜️ℓεɠεɳ∂ɓσƭ ตҽղմ թɾօѵíժҽɾ ís ղօա clօsҽժ.💫\n\n            **[©ℓєgєи∂ϐοτ](https://t.me/Legend_Mr_Hacker)**", 5, link_preview=False
            )
        else:
            LEGEND_alert = "οн ϲοммοи γαяя υ τнιиκ υ ϲαи ϲℓιϲκ οи ιτ😁😁😁. ∂єρℓογ υя οωи ϐοτ ©ℓεɠεɳ∂ɓσƭ(https://t.me/Legend_Userbot)"
            await event.answer(_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "∂οиτ τяγ το ϐє ονєяѕмαяτ ∂єρℓογ υя οωи ©ℓεɠεɳ∂ɓσƭ(https://t.me/Legend_Userbot)",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "💫 " + cmd[0] + " 💫", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("☚ɓαcҡ", data=f"page({page})")])
        await event.edit(
            f"📗 Fɪʟᴇ: `{commands}`\n🔢 иο. οƒ ϲοммαи∂ѕ☞ `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "ᵃᵇʰⁱ ᵗᵃᵏ ⁿʰⁱ ˢᵃᵐʲʰᵃ ᵏʰᵘᵈᵏᵃ ᵇᵃⁿᵃ ˡᵒ ⁿᵃ ᵗᵒʰ ᵘˢᵉ ᵏᵃʳⁿᵃ ʰ ᵗᵒʰ ᵏʸᵃ ᵘⁿᵍˡⁱ ᵏᵃʳ ʳʰᵉ ʰᵒ.🤦‍♂️🤦‍♂️🤦‍♂️ ©ℓєgєи∂ϐοτ ",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"📗 Fɪʟᴇ: `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ σƒƒเcเαℓ ᚛** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ ωαяиιиg ᚛** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ σƒƒเcเαℓ ᚛** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ σƒƒเcเαℓ ᚛** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ ɪɴғᴏ ᚛** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ ɪɴғᴏ ᚛** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"🛠 ℭ𝔬𝔪𝔪𝔞𝔫𝔡𝔰: `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"🛠 ℭ𝔬𝔪𝔪𝔞𝔫𝔡𝔰: `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"💬 𝔈𝔵𝔭𝔩𝔞𝔦𝔫𝔞𝔱𝔦𝔬𝔫: `{command['usage']}`\n\n"
        else:
            result += f"💬 𝔈𝔵𝔭𝔩𝔞𝔦𝔫𝔞𝔱𝔦𝔬𝔫: `{command['usage']}`\n"
            result += f"⌨️ ℱℴ𝓇 ℰ𝓍𝒶𝓂𝓅𝓁ℯ: `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("☚ɓαcҡ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
