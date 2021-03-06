# rikka-telegram-bot
Multipurpose chat bot

## Requirements:
+ Python 3.5
+ ImageMagick

### Libraries:
+ [python-telegram-bot](https://github.com/python-telegram-bot)
+ [py_bing_search](https://github.com/tristantao/py-bing-search)
+ [legofy](https://github.com/JuanPotato/Legofy)
+ Pillow
+ psutil
+ requests
+ uptime
+ [PyBooru](https://github.com/LuqueDaniel/pybooru)

## How to
Configure your token, api key and paths in config.yml (without any quotations)
```
    keys:
        telegram_token: 123455
        bing_api_key: 123456

    path:
        gifs: examples/gifs/
        memes: examples/memes/
        meme_font: resources/impact.ttf
        glitch: examples/glitch/
        lego: examples/lego/
        nya: examples/nya/
        kek: examples/kek/
        instagram: examples/instagram/
```

## Available functions:
+ /start - start a bot or view welcome message
+ /leet - convert text to 1337 5P34K
+ /roll [1] or [2] - choose one option randomly
+ /toribash [username] - show Toribash stats
+ /glitch - break an image
+ /lego [from 1 to 100] - legofy image
+ /gif - get random gif, "/gif help" to see folders
+ /nya - get random asian girl pic
+ /meme [top text] @ [bottom text] - make a meme from image
+ /kek [-l, -r, -t, -b] - mirror one side of an image to another
+ /instagram - add filter to an image
+ /img, /vid, /news [query] - Bing search for random result
+ /a [tag] - get pic from yande.re
+ /status - show server cpu, ram, hdd load and uptime
