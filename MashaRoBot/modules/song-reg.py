#code by @nousername_psycho
#-----------------------------------------req
from cinderella import pbot as app
from pyrogram import filters
from shazamio import Shazam
import youtube_dl
from youtube_search import YoutubeSearch
import requests
import time
import os
#-----------------------------------------ok
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

#----------------------------------------- time conv 4 duration 

@app.on_message(filters.command('find'))
async def sonf_REG(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    
    if not message.reply_to_message:
        await message.reply_text("Reply to a short video to recognize song.")
        return
    if not message.reply_to_message.video:
        await message.reply_text("Reply to a short video to recognize song.")
        return
    m = await message.reply_text("Listening 🎶")
    
    target = message.reply_to_message.video.file_id
    print(target) #-------------------test
    await app.download_media(target, file_name=f"downloads/blackmusic-{message.message_id}.mp4")
    
    
    shazam = Shazam()
    out = await shazam.recognize_song(f'downloads/blackmusic-{message.message_id}.mp4')
    try:
        await m.edit("Analysing 🔎")
        item = out.get("track")
        title = item.get("title")
        artist = item.get("subtitle")
        query = (f"{title} - {artist}")
    except Exception: 
        await m.edit("Sorry, failed to find your song ☹️")
        return
    
    #------------------------------------------------------+ new func
    await m.edit('Trying to download 😎')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            duration = results[0]["duration"]
            if time_to_seconds(duration) >= 900:  
                await m.edit("**Sorry!**\n\nMax Duration is 15min")
                return           
            
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"][:35]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            
            title_turple = (str(chat_id),title)
            user_turple = (str(user_id), title)

   
       
        except Exception as e:
            print(e)
            await m.edit(
                f"**No results Error 🐞**"
                f"\n\nSorry {message.from_user.first_name} i did't find anything with your keyword: `{query}`"
                )
            return
    except Exception as e:
        await m.edit(
            ""
        )
        print(str(e))
        return



    await m.edit("⏬ Downloading.")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        song = await message.reply_audio(audio_file, parse_mode='md',quote=False,thumb=thumb_name,
                                   reply_to_message_id=message.message_id, 
                                   title=title, duration=dur,
                                   caption=f"☈ Title**: {title}"
                                                        f"\n**☈ Duration**: `{duration}`"
                                                        f"\n**☈ Link**: [Click here]({link})"
                                                        f"\n**☈ Requested by**: {mention}")
        await m.delete()

        
    except Exception as e:
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
        os.remove(f'downloads/blackmusic-{message.message_id}.mp4')
    except Exception as e:
        print(e)


__help__ = """
 X /find -  reply to a short video to find song. \ncode by @nousername_psycho 
"""

__mod_name__ = "SHAZAM"


