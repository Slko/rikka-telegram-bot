import yaml
import subprocess
import datetime
import requests
import re

# import path
with open('config.yml', 'r') as f:
    kek_folder = yaml.load(f)["path"]["kek"]


# kek process + send
def kekify(bot, update, kek_param):
    try:
        if kek_param == "-l" or kek_param == "":
            crop = "50%x100% "
            piece_one = "result-0.jpg "
            piece_two = "result-1.jpg "
            flip = "-flop "
            order = kek_folder + piece_one + kek_folder + piece_two
            append = "+append "
        elif kek_param == "-r":
            crop = "50%x100% "
            piece_one = "result-1.jpg "
            piece_two = "result-0.jpg "
            flip = "-flop "
            order = kek_folder + piece_two + kek_folder + piece_one
            append = "+append "
        elif kek_param == "-t":
            crop = "100%x50% "
            piece_one = "result-0.jpg "
            piece_two = "result-1.jpg "
            flip = "-flip "
            order = kek_folder + piece_one + kek_folder + piece_two
            append = "-append "
        elif kek_param == "-b":
            crop = "100%x50% "
            piece_one = "result-1.jpg "
            piece_two = "result-0.jpg "
            flip = "-flip "
            order = kek_folder + piece_two + kek_folder + piece_one
            append = "-append "
        cut = "convert " + kek_folder + "original.jpg -crop " + crop + kek_folder + "result.jpg"
        subprocess.run(cut, shell=True)
        mirror = "convert " + kek_folder + piece_one + flip + kek_folder + piece_two
        subprocess.run(mirror, shell=True)
        append = "convert " + order + append + kek_folder + "kek.jpg"
        subprocess.run(append, shell=True)
        with open(kek_folder+"kek.jpg", "rb") as f:
            bot.sendPhoto(update.message.chat_id, f, reply_to_message_id=update.message.message_id)
        print(datetime.datetime.now(), ">>>", "Done kek", ">>>", update.message.from_user.username)
    except:
        bot.sendMessage(update.message.chat_id,
                        text="Unknown kek parameter.\nUse -l, -r, -t or -b",
                        reply_to_message_id=update.message.message_id)


# init; checking if it is photo, reply with photo or reply with link
def kek(bot, update):
    if update.message.reply_to_message is not None:
        if "/kek" in update.message.text:
            kek_param = "".join(update.message.text[5:7])
            try:
                if "http" in update.message.reply_to_message.text:
                    url = re.findall('http[s]?://\S+?\.(?:jpg|jpeg|png|gif)', update.message.reply_to_message.text)
                    link = str(url)
                    r = requests.get(link[2:-2])
                    with open(kek_folder+"original.jpg", "wb") as code:
                        code.write(r.content)
                    kekify(bot, update, kek_param)
                else:
                    bot.getFile(update.message.reply_to_message.photo[-1].file_id).download(kek_folder+"original.jpg")
                    kekify(bot, update, kek_param)
            except:
                bot.sendMessage(update.message.chat_id,
                                text="I can't get the image! :c",
                                reply_to_message_id=update.message.message_id)
    elif "/kek" in update.message.caption:
        kek_param = "".join(update.message.caption[5:7])
        bot.getFile(update.message.photo[-1].file_id).download(kek_folder+"original.jpg")
        kekify(bot, update, kek_param)
