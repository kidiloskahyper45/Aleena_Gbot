from MashaRoBot import telethn as bot
from MashaRoBot import telethn as tbot
from MashaRoBot.events import register
from telethon import *
from telethon import Button, custom, events, functions
from MashaRoBot.helper_extra.badmedia import is_nsfw
import requests
import string 
import random 
from MashaRoBot.modules.sql_extended.nsfw_watch_sql import add_nsfwatch, rmnsfwatch, get_all_nsfw_enabled_chat, is_nsfwatch_indb
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
async def can_change_info(message):
    result = await tbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.change_info
    )
@register(pattern="^/nsfw")
async def nsfw(event):
    if event.is_private:
       return   
    if event.is_group:
            pass
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.reply("`This Chat has Enabled NSFW watch`")
    else:
        await event.reply("`NSfw Watch is off for this chat`")

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
@register(pattern="^/addnsfw")
async def nsfw_watch(event):
    if event.is_private:
       return   
    if event.is_group:
        if not await can_change_info(message=event):
            return
        else:
            pass
    if is_nsfwatch_indb(str(event.chat_id)):
        await event.reply("`This Chat Has Already Enabled Nsfw Watch.`")
        return
    add_nsfwatch(str(event.chat_id))
    await event.reply(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Groups Nsfw Contents Will Be Deleted And Logged in Logging Group**")

@register(pattern="^/rmnsfw ?(.*)")
async def disable_nsfw(event):
    if event.is_private:
       return   
    if event.is_group:
        if not await can_change_info(message=event):
            return
        else:
            pass
    if not is_nsfwatch_indb(str(event.chat_id)):
        await event.reply("This Chat Has Not Enabled Nsfw Watch.")
        return
    rmnsfwatch(str(event.chat_id))
    await event.reply(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Nsfw Watch**")
    
@bot.on(events.NewMessage())        
async def ws(event):
    warner_starkz = get_all_nsfw_enabled_chat()
    if len(warner_starkz) == 0:
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        return
    if not event.media:
        return
    if not (event.gif or event.video or event.video_note or event.photo or event.sticker):
        return
    hmmstark = await is_nsfw(event)
    his_id = event.sender_id
    if hmmstark is True:
        try:
            await event.delete()
            await event.client(EditBannedRequest(event.chat_id, his_id, MUTE_RIGHTS))
        except:
            pass
        lolchat = await event.get_chat()
        ctitle = event.chat.title
        if lolchat.username:
            hehe = lolchat.username
        else:
            hehe = event.chat_id
        wstark = await event.client.get_entity(his_id)
        if wstark.username:
            ujwal = wstark.username
        else:
            ujwal = wstark.id
        try:
            await tbot.send_message(event.chat_id, f"**#NSFW_WATCH** \n**Chat :** `{hehe}` \n**Nsfw Sender - User / Bot :** `{ujwal}` \n**Chat Title:** `{ctitle}`")  
            return
        except:
            return


__help__ = """
*Special Commands for Aleena's Creator/ Dev / Owner*



*Groups Info:*
  /groups*:* List the groups with Name, ID, members count as a txt
  /leave <ID>*:* Leave the group, ID must have hyphen
  /stats*:* Shows overall bot stats
  /getchats*:* Gets a list of group names the user has been seen in. Bot owner only
  /ginfo username/link/ID*:* Pulls info panel for entire group
  
*Access control:* 
 ❍ /ignore*:* Blacklists a user from using the bot entirely
 ❍ /lockdown <off/on>*:* Toggles bot adding to groups
 ❍ /notice*:* Removes user from blacklist
 ❍ /ignoredlist*:* Lists ignored users
 
*Speedtest:*
 ❍ /speedtest*:* Runs a speedtest and gives you 2 options to choose from, text or image output
 
*Module loading:*
 ❍ /listmodules*:* Lists names of all modules
 ❍ /load modulename*:* Loads the said module to memory without restarting.
 ❍ /unload modulename*:* Loads the said module frommemory without restarting memory without restarting the bot 
 
*Remote commands:*
 ❍ /rban*:* user group*:* Remote ban
 ❍ /runban*:* user group*:* Remote un-ban
 ❍ /rpunch*:* user group*:* Remote punch
 ❍ /rmute*:* user group*:* Remote mute
 ❍ /runmute*:* user group*:* Remote un-mute
 
*Windows self hosted only:*
 ❍ /reboot*:* Restarts the bots service
 ❍ /gitpull*:* Pulls the repo and then restarts the bots service
 
*Chatbot:* 
 ❍ /listaichats*:* Lists the chats the chatmode is enabled in
 
*Debugging and Shell:* 
  /debug <on/off>*:* Logs commands to updates.txt
  /logs*:* Run this in support group to get logs in pm
  /eval*:* Self explanatory
  /sh*:* Runs shell command
  /shell*:* Runs shell command
  /clearlocals*:* As the name goes
  /dbcleanup*:* Removes deleted accs and groups from db
  /py*:* Runs python code
 
*Global Bans:*
 > /gban <id> <reason>*:* Gbans the user, works by reply too
 > /ungban*:* Ungbans the user, same usage as gban
 > /gbanlist*:* Outputs a list of gbanned users
*Global Blue Text*
 > /gignoreblue*:* <word>*:* Globally ignorea bluetext cleaning of saved word across MashaRoBot.
 > /ungignoreblue*:* <word>*:* Remove said command from global cleaning list
 
*Aleena Core*
*Owner only*
(DEVS) /send*:* <module name>*:* Send module
(DEVS)/install*:* <reply to a .py>*:* Install module 
 
*Heroku Settings*
*Owner only*
> /usage*:* Check your heroku dyno hours remaining.
> /see var <var>*:* Get your existing varibles, use it only on your private group!
> /set var <newvar> <vavariable>*:* Add new variable or update existing value variable.
> /del var <var>*:* Delete existing variable.
> /logs Get heroku dyno logs.

*NSFW*
Aleena can protect your group from NSFW senders
 ❍ /addnsfw*:* Adds The Group to nsfw Watch List
 ❍ /rmnsfw*:* Removes The Group From nsfw Watch List
"""

__mod_name__ = "ACCΣƧƧ"
