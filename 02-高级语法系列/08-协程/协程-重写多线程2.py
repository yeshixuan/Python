movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁与.rmvb", "xxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]

import asyncio
import time


# @asyncio.coroutine
async def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("now playing movie name {}".format(i))
            #             yield time.sleep(3)
            await asyncio.sleep(3)
        elif i.split(".")[1] in music_format:
            print("now playing music name {}".format(i))
            #             yield time.sleep(3)
            await asyncio.sleep(3)
        else:
            print("No supported")


loop = asyncio.get_event_loop()
task = [play(music_list), play(movie_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()