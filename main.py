# -*- coding: utf-8 -*-
import chatbot, random, shutil, time, urllib, sys, upsidedown, threading
from PIL import Image
from imgurpython import ImgurClient
import  numpy as np

client_id = 'fb1b922cb86bb0f'  # Imgur module setup
client_secret = 'cffaf5da440289a8923f9be60c22b26e25675d3d'
clientImg = ImgurClient(client_id, client_secret)

reload(sys)
sys.setdefaultencoding('utf8')

# Initialization

session = chatbot.login()


# Utility

def removeUselessSpace(name, path=''):
    image = Image.open(path + name)

    image=image.crop(image.getbbox())

    image.save(path + 'cropped_' + name)


#


coolTables = {
    "tablesList": ["(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”»", "(ãƒŽà² ç›Šà² )ãƒŽå½¡â”»â”â”»", "Ê•ãƒŽâ€¢á´¥â€¢Ê”ãƒŽ ï¸µ â”»â”â”»", "(/Â¯â—¡ â€¿ â—¡)/Â¯ ~ â”»â”â”»", "(ãƒŽ-_-)ãƒŽ ~â”»â”â”»", "(ï¾‰ï¼›ï¼›)ï¾‰~â”»â”â”»",
                   "(ï¾‰-_-)ï¾‰ ~â”»â”â”» â˜†`", "(ãƒŽ-_-)ãƒŽãƒ»ãƒ»ãƒ»~~â”»â”â”»", "(ãƒŽ-_-)ãƒŽ~â”»â”â”»", "ãƒŽï¿£â–¡ï¿£)ãƒŽ ~â”»â”â”»", "(ï¾‰ê¦ âŠ™æ›²à° )ï¾‰å½¡â”»â”â”»", "(ï¾‰ï½€â–¡Â´)ï¾‰âŒ’â”»â”â”»",
                   "(ï¾‰ê¦ à¹‘Â´Ð”`à¹‘)ï¾‰å½¡â”»â”â”»", "â”»â”â”»ãƒŸï¼¼ï¼ˆâ‰§ãƒ­â‰¦ï¼¼ï¼‰", "(ï¾‰ï¿£â–¡ï¿£)ï¾‰ ~â”»â”â”»", "ï¼ˆãƒŽâ™¯ï½€â–³Â´ï¼‰ãƒŽ~â€™â”»â”â”»", "ï¼ˆãƒŽTï¼¿T)ãƒŽ ï¼¾â”»â”â”»", "(â”›à² Ð”à² )â”›å½¡â”»â”â”»",
                   "(ãƒŽÂ°â–½Â°)ãƒŽï¸µâ”»â”â”»", "(ï¾‰*â€™Ï‰â€™*)ï¾‰å½¡â”»â”â”»", "â€Ž(ï¾‰à²¥ç›Šà²¥ï¼‰ï¾‰ â”»â”â”»", "(â•¯â€™â–¡â€™)â•¯ï¸µ â”»â”â”»", "(ï¾‰à²¥Ð”à²¥)ï¾‰ï¸µâ”»â”â”»ï½¥/", "(._.) ~ ï¸µ â”»â”â”»",
                   "â”—[Â© â™’ Â©]â”› ï¸µ â”»â”â”»", "â”»â”â”» ï¸µ áƒš(âŒ’-âŒ’áƒš)", "(ï¾‰ï¼¾â—¡ï¼¾)ï¾‰ï¸µ â”»â”â”»", "à¼¼ á•¤ ÂºÙ„ÍŸÂº à¼½á•¤ ï¸µâ”»â”â”»", "ãƒ½à¼¼ ãƒ„ à¼½ï¾‰ ï¸µâ”»â”â”»",
                   "à¼¼ Í àºˆ ÍŸÙ„Íœ Í àºˆà¼½à¸‡ï¸µâ”»â”â”»", "ãƒ½à¼¼àºˆÙ„Íœàºˆà¼½ï¾‰ï¸µâ”»â”â”»", "(â•¯àºˆÙ„Íœàºˆ) â•¯ï¸µ â”»â”â”»", "à¼¼ãƒŽà² Ù„ÍŸà² à¼½ãƒŽ ï¸µ â”»â”â”»", "à¼¼ï¾‰àºˆÙ„Íœàºˆà¼½ï¾‰ï¸µâ”»â”â”»",
                   "(â•¯ ÍÂ° ÍœÊ–Í¡Â°)â•¯ï¸µ â”»â”â”»", "(ã¤â˜¢ç›Šâ˜¢)ã¤ï¸µâ”»â”â”»", "ãƒ½à¼¼àºˆÙ„Íœàºˆà¼½ï¾‰ï¸µ â”»â”â”»", "(â”›â—‰Ð”â—‰)â”›å½¡â”»â”â”»", "(ï¾‰â‰§âˆ‡â‰¦)ï¾‰ ï¾ â”¸â”â”¸", "â”»â”â”»ãƒŸï¼¼(â‰§ï¾›â‰¦ï¼¼)",
                   "(ãƒŽï½€Â´)ãƒŽ ~â”»â”â”» ï½ž", "Ê• âŠƒï½¥ â—¡ ï½¥ Ê”âŠƒï¸µâ”»â”â”»", "(ï¾‰â–¼Ð´â–¼)ï¾‰ ~â”»â”â”» â˜†`", "(â”›âá´¥â)â”›å½¡â”»â”â”»", "(Ê˜âˆ‡Ê˜)ã‚¯ å½¡ â”»â”â”»",
                   "â”»â”â”» ï¸µ áƒš(à² ç›Šà² áƒš)", "(â•¯à² _à²°à³ƒ)â•¯ï¸µ â”»â”â”»", "/(Ã².Ã³)â”›å½¡â”»â”â”»", "(â•¯=â–ƒ=)â•¯ï¸µâ”»â”â”»", "(ãƒŽï½€ãƒ¼Â´)ãƒŽãƒ»ãƒ»ãƒ»~~â”»â”â”»", "(ï¾‰ï½€â—‡Â´)ï¾‰~â”»â”â”»",
                   "â”»â”â”» ãƒ˜â•°( â€¢Ì€Îµâ€¢Ì â•°)", "(ãƒŽï½€Ð”Â´)ãƒŽ~â”»â”â”»", "(ï¾‰ï½€â–³Â´)ï¾‰~â”»â”â”»", "(â‘…ãƒŽ-_-)ãƒŽ~â”»â”â”»    ", "(â•¯ ï½¥ á—œ ï½¥ )â•¯ï¸µ â”»â”â”»  ",
                   "(ãƒŽ ï¾ŸÐ”ï¾Ÿ)ãƒŽã€€ï¼ï¼ï¼ï¼ã€€â”»â”â”â”»", "!!!!|â”›*ï½€Ð”Â´|â”›ãƒ»ãƒ»~~â”»â”â”»ã€€â”³â”â”³", "(/#-_-)/~â”»â”»ã€ƒ", "(/ToT)/ ~â”»â”»", "ï¼ˆãƒŽï¼ï¼¿ï¼ï¼‰ãƒŽï½¥ï½¥ï½¥~â”»â”»    ",
                   "(ï¾‰*â€™â€â€™)ï¾‰ ï¾ â”¸â”¸", "(ãƒŽ#-_-)ãƒŽ ãƒŸã€€â”´â”´", "ï¼ˆãƒŽï½€_Â´ï¼‰ï¾‰~~â”´â”´", "(ãƒŽï½€Â´ï¼‰ãƒŽãƒŸâ”»â”»", "ãƒŽToT)ãƒŽ ~â”»â”»", "(ï¾‰ï½€Ð”)ï¾‰:ãƒ»â€™âˆµ:.â”»â”»",
                   "(ï¾‰ToT)ï¾‰ ï¾ â”¸â”¸", "(ãƒ¡â€“)ãƒŽãƒŽã€‚ã€‚ã€‚â”»â”»", "(ï¾‰â‰§âˆ‡â‰¦)ï¾‰ ï¾ â”¸â”¸", "(ãƒŽToT)ãƒŽ ~â”»â”»", "â”³â”³ãƒ¾(T(ã‚¨)Tãƒ½)",
                   "(ï¾‰TwT)ï¾‰ â”«:ï½¥â€™.::ï½¥â”»â”»:ï½¥â€™.::ï½¥", "(ãƒŽÍ¡Â° ÍœÊ– Í¡Â°)ãƒŽï¸µâ”»â”»  ", "ï¼ˆãƒŽï¼ï¼¿ï¼ï¼‰ãƒŽãƒ»ãƒ»ãƒ»~~~â”»â”»", "(ãƒŽï¼›oï¼›)ãƒŽ â”«:ï½¥â€™.::ï½¥â”»â”»:ï½¥â€™.::ï½¥",
                   "(ãƒŽï¼›Ï‰ï¼›)ãƒŽ â”«:ï½¥â€™.::ï½¥â”»â”»:ï½¥â€™.::ï½¥", "(ãƒŽToT)ãƒŽ â”«:ãƒ»â€™.::ãƒ»â”»â”»:ãƒ»â€™.::ãƒ»", "(ãƒŽTÐ”T)ãƒŽ â”«:ï½¥â€™.::ï½¥â”»â”»:ï½¥â€™.::ï½¥",
                   "(ãƒŽToT)ãƒŽã€€â”«ï¼šï½¥â€™.::ï½¥â”»â”»:ï½¥â€™.::ï½¥", "ï¼ˆï¾‰ï½€Ð”Â´ï¼‰ï¾‰ï¼ï¼ï¼ï¼ï¼â”»â”»ã€€-ï¼“-ï¼“", "ï¼ˆãƒŽï¿£ï¼¾ï¿£ï¼‰ãƒŽã€€â”³â”³ã€€â”£ã€€â”»â”»ã€€â”«ã€€â”³â”³",
                   "(ï¾‰Â´â–¡ï½€)ï¾‰ â”«:ï½¥â€™âˆµ:.â”»â”»:ï½¥â€™.:â”£âˆµï½¥:. â”³â”³", "(ãƒŽï½€ï¼)ãƒŽ âŒ’â”«ï¼šãƒ»â€™.ï¼šï¼šãƒ»â”»â”»ï¼šãƒ»â€™.ï¼šï¼šãƒ»", "(ï¾‰ï½€âŒ’Â´)ï¾‰ â”«ï¼šãƒ»â€™.ï¼šï¼šãƒ»â”»â”»ï¼šãƒ»â€™.ï¼šï¼šãƒ»",
                   "(ãƒŽï½€âŒ’Â´)ãƒŽ â”«ï¼šãƒ»â€™.ï¼šï¼šãƒ»â”»â”»ï¼šãƒ»â€™.ï¼šï¼šãƒ»", "( ï½€o)ï¾‰ï¾‰ â”«", "( ï¾‰o|o)ï¾‰ â”«ï½¡ï¾Ÿ:.:", "ï¼ˆï¼›ï¼ï¼ï¼‰ãƒŽãƒŽ â”«ï¼šãƒ»ã‚œâ€™", "(/-o-)/ âŒ’ â”¤",
                   "(/ï½€Î¿Â´)/ âŒ’ â”«:â€™ï¾Ÿ:ï½¡ï½¥,. ã€‚ã‚œ", "(/ToT)/_â”«ãƒ»..", "(ãƒŽï¼ï¼¿ï¼ï¼‰ãƒŽã€€â”«ã€ã€Ÿâˆµ", "(ãƒŽ-0-)ãƒŽã€€â”«âˆµï¼šï¼Ž", "(ï¾‰-ï½-)ï¾‰ ~â”«ï¼šãƒ»â€™.ï¼šï¼šãƒ»",
                   "(ãƒŽ-o-)ãƒŽâŒ’â”³ â”«â”»â”£", "(ãƒŽï¿£ï¼¿ï¿£ï¼‰ãƒŽã€€â”«ã€ã€Ÿâˆµ", "(ä¸¿>ãƒ­<)ä¸¿ â”¤âˆµ:.", "ï¼ˆãƒŽï¿£ãƒ¼ï¿£ï¼‰ãƒŽã€€â”«ï¼šãƒ»â€™.::", "(ãƒŽï¿£ãƒ¼ï¿£ï¼‰ãƒŽã€€â”«ã€ã€Ÿâˆµ",
                   "(ï¾‰ï¼ï¾Ÿï¾›ï¾Ÿ)ï¾‰ âŒ’â”«:ï½¥â€™.::", "(ãƒŽï¼žoï¼œ)ãƒŽ â”«:ï½¥â€™.::", "ï¼ˆãƒŽâ‰§âˆ‡â‰¦ï¼‰ãƒŽã€€â”«ã€€ã‚œãƒ»âˆµã€‚", "ï¼ˆãƒŽâ‰§Î¿â‰¦ï¼‰ãƒŽã€€â”«ã€€ã‚œãƒ»âˆµã€‚", "ï¼ˆãƒŽâ—‹Ð”â—‹ï¼‰ãƒŽï¼ï¼ï¼â” ",
                   "ï¼ˆãƒŽãƒ¼â€ãƒ¼ï¼‰ãƒŽã€€â”«ã€€ã‚œãƒ»âˆµã€‚", "(ãƒŽToT)ãƒŽ â”«:ãƒ»â€™.::ãƒ»", "((((ï¾‰ï½€çš¿Â´)ï¾‰ âŒ’â”«:ï½¥â”«â”»â” â€™.", "(ï¾‰*ï½€â–½Â´*)ï¾‰ âŒ’â”« â”» â”£ â”³", "(ãƒŽï¿£çš¿ï¿£ï¼‰ãƒŽ âŒ’=== â”«",
                   "ï½¥.:ï¾Ÿï½¡â”£ï¼¼(â€™ï¾›Â´ï¼¼)", "(ï¾‰#â–¼oâ–¼)ï¾‰ â”«:ï½¥â€™.::ï½¥", "â”£Â¨â”£Â¨â”£Â¨ãƒ¾(ã‚œÐ”ã‚œ )ãƒŽâ”£Â¨â”£Â¨â”£", "â”£Â¨ à­§(à¹‘ â¼Ì´Ì€áœâ¼Ì´Ìà¹‘)à«­",
                   "((|||||â”ï¼¼(ï½€Ð´Â´)ï¼â”¥|||||))", "â”ï¼¼( â€˜âˆ‡^*)^â˜†ï¼â”¥  ", "(ï¾‰ï¾Ÿâˆ€ï¾Ÿ)ï¾‰ â”«:ï½¡ï½¥:*:ï½¥ï¾Ÿâ€™â˜…,ï½¡ï½¥:*:â™ªï½¥ï¾Ÿâ€™â˜†â”â”â”!!!!",
                   "â”»â”â”» ï¸µ Â¯\\\ (ãƒ„)/Â¯ ï¸µ â”»â”â”»", "â”»â”â”» ï¸µãƒ½(`Ð”Â´)ï¾‰ï¸µ â”»â”â”»", "â”»â”â”» ï¸µãƒ½(`Ð”Â´)ï¾‰ï¸µ â”»â”â”»", "â”»â”â”» ï¸µ Â¯\\\(ãƒ„)/Â¯ ï¸µ â”»â”â”»",
                   "â”«â”»â” âŒ’ãƒ¾(-_-ãƒ¾ ä¸‰ ï¾‰-_-)ï¾‰âŒ’â”«:ï½¥â”«â”»", "ï¼ˆ/ï¼žâ–¡ï¼œï¼‰/äº äº ", "(ãƒŽï¿£ï¼¿ï¿£)ãƒŽï¼¼ã€‚:ãƒ»ã‚›ã€‚", "(ãƒŽÃ’ç›ŠÃ“)ãƒŽå½¡â–”â–”â–", "_|___|_ â•°(Âº o Âºâ•°)  ",
                   "(ãƒŽï¿£ï¿£âˆ‡ï¿£ï¿£)ãƒŽ~~~~~âŒ’â”â”â”»â”â”â”»â”â”", "âŠ‚(ï¾‰ï¿£ï¿£ï¿£(å·¥)ï¿£ï¿£ï¿£)âŠƒï¾‰~~~~~â”â”â”â”»â”â”â”»â”â”â”", "(ãƒŽ-o-)ãƒŽâ”¸â”¸)`3ã‚œ)ãƒ»;â€™.",
                   "(ãƒŽ-ã€‚-ï¼‰ãƒŽâ”»â”â”»â˜†(ã€€ã€€^)", "(ãƒŽ-_-)ãƒŽ ~â”»â”â”» (/oï¼¼)", "(ãƒŽ#-â—‡-)ãƒŽ ~~~~â”»â”â”»â˜†(x _ x)ãƒŽ", "(ãƒŽï½€ï¼)ãƒŽ âŒ’â”« â”» â”£ â”³â˜†(x x)",
                   "(ãƒŽï½€mÂ´)ãƒŽ ~â”»â”â”» (/oï¼¼)", "(ï¾‰`Ð”Â´)ï¾‰.:ï½¥â”»â”»)ï½€Ð·ã‚œ)ï½¥:ï¾ž;    ", "(ãƒŽï¿£â–½ï¿£)ãƒŽâ”»â”â”»â˜†)*ï¿£â–¡)ãƒŽ))", "(ãƒŽï¿£â—‡ï¿£)ãƒŽ~â”»â”â”»/(Ã—ã€‚Ã—)",
                   "(ï¾‰ToT)ï¾‰ â”«:ï½¥â€™.::ï½¥ï¼¼â”»â”»(ï½¥_ï¼¼)", "(â•¯Â°â–¡Â°)â•¯ï¸µ â”»â”â”» ï¸µ â•¯(Â°â–¡Â° â•¯)", "(ãƒŽ^_^)ãƒŽâ”»â”â”» â”¬â”€â”¬ ãƒŽ( ^_^ãƒŽ)", "ï¾â”»â”»(ï¾‰>ï½¡<)ï¾‰",
                   ".::ï½¥â”»â”»â˜†()ï¾ŸOï¾Ÿ)", "(ï¾‰ï½€Aâ€)ï¾‰ âŒ’â”« â”» â”£ â”³â˜†(x x)", "(ãƒŽï½€mÂ´)ãƒŽ ~â”»â”â”» (/oï¼¼)", "âŒ’â”« â”» â”£ âŒ’â”»â˜†)ï¾ŸâŠ¿ï¾Ÿ)ï¾‰",
                   "(ï¾‰â‰§âˆ‡â‰¦)ï¾‰ ï¾ â”¸â”¸)`Î½ï¾Ÿ)ï½¥;â€™.", "(ï¾‰ToT)ï¾‰ â”«:ï½¥â€™.::ï½¥ï¼¼â”»â”»(ï½¥_ï¼¼)", "ï¼ˆãƒŽï¼ï½ï¼ï¼‰ãƒŽã€€â€â€³â”»â”â”»â˜†ï¼ˆ>â—‹<ï¼‰",
                   "ãƒŸ(ãƒŽï¿£^ï¿£)ãƒŽ!â‰¡â‰¡â‰¡â‰¡â‰¡â”â”³â”â˜†()ï¿£â–¡ï¿£)/", "ï¼ˆãƒ¡ï½€Ð´Â´ï¼‰â”«ï½žâ”»â”» ï½žâ”£ï½žâ”³â”³ã€€ã€€ï¼ˆã€‚@ï¾@ã€‚å·", "ãƒŸ(ãƒŽï¿£^ï¿£)ãƒŽâ‰¡â‰¡â‰¡â‰¡â‰¡â”â”³â”â˜†()ï¿£â–¡ï¿£)/",
                   "(â•¯Â°Ð”Â°ï¼‰â•¯ï¸µ/(.â–¡ . )", "(ãƒŽà²  âˆ©à² )ãƒŽå½¡( oÂ°o)", "/( .â–¡.) ï¸µâ•°(ã‚œç›Šã‚œ)â•¯ï¸µ /(.â–¡. /)",
                   "â‰¡/( .-.)\\\ ï¸µâ•°(Â«â—‹Â»ç›ŠÂ«â—‹Â»)â•¯ï¸µ /(.â–¡. /)Ì¨", "(/ .â–¡.)\\\ ï¸µâ•°(ã‚œÐ”ã‚œ)â•¯ï¸µ /(.â–¡. \\\)", "ï¼ˆâ•¯Â°â–¡Â°ï¼‰â•¯ï¸µ( .o.)",
                   "(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ (\\\ . 0 .)(/ï¿£(ï½´)ï¿£)/ âŒ’ â—‹â”¼<", "(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ /( â€¿âŒ“â€¿ )ãƒŽâ”¬â”€â”¬ãƒŽ ï¸µ ( oÂ°o)", "â”¬â”€â”¬ ï¸µ /(.â–¡. \\\ï¼‰",
                   "â”¬â”€â”€â”¬â•¯ï¸µ /(.â–¡. \\\ï¼‰", "â”¬â”€â”€â”¬ ï¸µ(â•¯ã€‚â–¡ã€‚ï¼‰â•¯", "ãƒ˜(Â´Â° â–¡Â°)ãƒ˜â”³â”â”³", "(â•¯Â°â–¡Â°)â•¯ï¸µ ÊžooqÇÉ”Éâ„²", "(â•¯Â°â–¡Â°)â•¯ï¸µ É¹ÇÊ‡Ê‡Ä±ÊâŠ¥",
                   "(âˆ¿Â°â—‹Â°)âˆ¿ ï¸µ ÇÊŒol", "(â•¯Â°â–¡Â°)â•¯ï¸µ É¯sÄ±É¥dÉ¹oÉ¯ouÇÊžs", "(â•¯Â°â–¡Â°)â•¯ï¸µ sÉ¯ÉxÇ", "(â•¯Â°â–¡Â°)â•¯ï¸µ ÆƒuÄ±ÊŽpnÊ‡s", "(â•¯Â°â–¡Â°)â•¯ï¸µ ÊžÉ¹oÊ",
                   "(à©­ â—•ã‰¨â—•)à©­ =ÍŸÍŸÍžÍž=ÍŸÍŸÍžÍžä¸‰â†)â€™Ð´Âº);,â€™:=ÍŸÍŸÍžÍž", "(ï¾‰ê¦ â—Žæ›²â—Ž)ï¾‰=ÍŸÍŸÍžÍž âŒ¨", "(ã£ ÂºÐ”Âº)ã£ ï¸µ âŒ¨", "(â•¯^â–¡^)â•¯ï¸µ â„â˜ƒâ„",
                   "(â•¯ `Ð” Ì)â•¯ï¸µ (à¸¿)", "â™¡â•°(*ï¾Ÿxï¾Ÿâ€‹*)â•¯â™¡", "Ë­Ì¡Ìž(â—žâŽËƒá†ºË‚)â—žâ‚Žâ‚Ž=ÍŸÍŸÍžÍžâœ‰", "(Û¶à«ˆ Ûœ áµ’ÌŒâ–±à¹‹áµ’ÌŒ )Û¶à«ˆ=ÍŸÍŸÍžÍž âŒ¨`ãƒ¯Â°)ãƒ»;â€™.",
                   "â•°( ^o^)â•®-=ï¾†=ä¸€ï¼ä¸‰", "ï¼ˆãƒŽ>_<ï¼‰ãƒŽã€€â‰¡â—", "â—~*âŒ’ ãƒ½(Â´ï½°ï½€ )", "!!(âŠƒ Ð”)âŠƒâ‰¡ï¾Ÿ ï¾Ÿ", "(â•¬â˜‰Ð´âŠ™)ï¼â—¯)à¹Ð´à¹))ï½¥;â€™.",
                   "(à´°Ì€â¨à´°Ì)Ùˆ Ì‘Ì‘à¼‰ Õ¬à¨• Ìà©­áƒ¯ à«…à©~É­ É¿â¢â¢", "Ë­Ì¡Ìž(â—žâŽËƒá†ºË‚)â—žâ‚Žâ‚Ž=ÍŸÍŸÍžÍžË³Ëšà¥°Â°â‚’à§¹à¹", "à«®(ê‚§á·†âº«ê‚§á·‡)áƒ=ÍŸÍŸÍžÍžêŠž",
                   "ãƒ½ï¼»ãƒ»âˆ€ãƒ»ï¼½ï¾‰(((((((((â—ï½ž*", "ï¾|ï½¥âˆ€ï½¥|ï¾‰*~â—", "(*ï¾‰ï¾Ÿâ–½ï¾Ÿ)ï¾‰ âŒ’((((â—", "(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ à¸ªà¹‡à¹‡à¹‡à¹‡à¹‡à¹‡à¹‡à¸ª", "âŒ¨ â–ˆâ–¬â–¬â—Ÿ(`ï®§Â´ â—Ÿ )",
                   "â—‹ä¸‰ã€€ï¼¼(ï¿£^ï¿£ï¼¼ï¼‰", ",,,,,,,,((*ï¿£(ï½´)ï¿£)ï¾‰ âŒ’â˜† o*ï¼¿(x)_)", "(Û¶à«ˆâ€¡â–¼ç›Šâ–¼)Û¶à«ˆ=ÍŸÍŸÍžÍž âŒ¨", "(ãƒŽÏ‰ãƒ»)ãƒŽâŒ’ã‚›â—†",
                   "(Û¶à«ˆ Ûœ áµ’ÌŒâ–±à¹‹áµ’ÌŒ )Û¶à«ˆ=ÍŸÍŸÍžÍž âŒ¨", "(Û¶à«ˆ áµ’ÌŒ Ð”áµ’ÌŒ)Û¶à«ˆ=ÍŸÍŸÍžÍž âŒ¨", "â˜†(ï¾‰^o^)ï¾‰â€¥â€¥â€¥â€¦â”â”â”â”ã€‡(^~^)",
                   "( ã¤â€¢Ì€Ï‰â€¢Ì)ã¤ãƒ»ãƒ»*:ãƒ»:ãƒ»ã‚œ:==â‰¡â‰¡Î£=ÍŸÍŸÍžÍž(âœ¡)`Ð”Â´ï¼‰"],
    "flipsList": ["( ã¤â€¢Ì€Ï‰â€¢Ì)ã¤","(âˆ¿Â°â—‹Â°)âˆ¿","(Û¶à«ˆâ€¡â–¼ç›Šâ–¼)Û¶", "â—Ÿ(`ï®§Â´ â—Ÿ )","(â•¯Â°à¨ŠÂ°)â•¯ï¸µ", "(ã¥à²¥à¨Šà²¥)ã¥ï¸µ", "(ã¥à¹‘Ê–à¹‘)â”›ï¸µ"],
    "doubleflipsList": ["â•°(*ï¾Ÿxï¾Ÿâ€‹*)â•¯","ï¼¼(ï½€Ð´Â´)ï¼","ï¸µâ•°(ã‚œç›Šã‚œ)â•¯ï¸µ ","â•°(Â«â—‹Â»ç›ŠÂ«â—‹Â»)â•¯","ï¸µâ•°(ã‚œÐ”ã‚œ)â•¯ï¸µ"],
    "untablesList": ["â”¬â”€â”¬ ãƒŽ( ^_^ãƒŽ)", "â”¬â”€â”€â”¬â—¡ï¾‰(Â° -Â°ï¾‰)", "â”¬â”â”¬ ãƒŽ( ã‚œÂ¸ã‚œãƒŽ)", "â”¬â”â”¬ ãƒŽ( ã‚œ-ã‚œãƒŽ)", "â”³â”â”³ ãƒ½à¼¼à² Ù„Íœà² à¼½ï¾‰",
                     "â”¬â”€â”€â”¬ Â¯\\\_(ãƒ„)",
                     "â”¬â”€â”€â”¬ ãƒŽ( ã‚œ-ã‚œãƒŽ)", "(ãƒ˜ï½¥_ï½¥)ãƒ˜â”³â”â”³", "â”»o(ï¼´ï¼¿ï¼´ )ãƒŸ( ï¼›ï¼¿ï¼›)oâ”¯", "â”£ï¾(â‰§âˆ‡â‰¦ï¾)â€¦ (â‰§âˆ‡â‰¦)/â”³â”â”³",
                     "â”£ï¾(^â–½^ï¾)Îž(ï¾Ÿâ–½ï¾Ÿ*)ï¾‰â”³â”â”³",
                     ],
    "iceCreamList": [
        "http://www.daytonaradio.com/wkro/wp-content/uploads/sites/4/2015/07/ice-cream.jpg"],
    "sushiList": [
        "http://www.shopbelmontmarket.com/wp-content/uploads/page_img_sushi_01.jpg",
        "http://www.jim.fr/e-docs/00/02/66/5C/carac_photo_1.jpg"],
    "gunsList": ["(Ò‚â€¾ â–µâ€¾)ï¸»ãƒ‡â•ä¸€ (Ëšâ–½Ëšâ€™!)/",
                 "Ì¿â€™ Ì¿â€™\\\ÌµÍ‡Ì¿Ì¿\\\Ð·=(à²¥Ð”à²¥)=Îµ/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿",
                 "( ã†-Â´)ã¥ï¸»â•¦ÌµÌµÌ¿â•¤â”€â”€ \\\(Ëšâ˜Ëšâ€)/",
                 "(âŒâ– _â– )â€“ï¸»â•¦â•¤â”€",
                 "Ì¿Ì¿ Ì¿Ì¿ Ì¿â€™Ì¿â€™ÌµÍ‡Ì¿Ì¿Ð·=à¼¼ â–€Ì¿Ì¿Ä¹Ì¯Ì¿Ì¿â–€Ì¿ Ì¿ à¼½	",
                 "â”â•¤ãƒ‡â•¦ï¸»(â–€Ì¿Ì¿Ä¹Ì¯Ì¿Ì¿â–€Ì¿ Ì¿)",
                 "â•¾â”â•¤ãƒ‡â•¦ï¸»	â–„ï¸»Ì·Ì¿â”»Ì¿â•â”ä¸€", "ï¸»â•¦ÌµÌµÍ‡Ì¿Ì¿Ì¿Ì¿â•â•â•¤â”€",
                 "à¼¼ à² Ù„ÍŸà² à¼½ Ì¿ Ì¿ Ì¿ Ì¿â€™Ì¿â€™ÌµÐ·=à¼¼àºˆÙ„Íœàºˆà¼½ï¾‰",
                 "Ì¿â€™ Ì¿â€™\\\ÌµÍ‡Ì¿Ì¿\\\Ð·=(à²¡Ù„ÍŸà²¡)=Îµ/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿",
                 "ï¿¢o(ï¿£-ï¿£ï¾’)", "(Ò‚`Ð·Â´).ã£ï¸»ãƒ‡â•ä¸€",
                 "á••â• Í¡áµ” â€¸ Í¡áµ” â•Ùˆï¸»Ì·â”»Ì¿â•â”ä¸€", "âŒâ•¦â•¦â•â”€",
                 "(ï¾Ÿçš¿ï¾Ÿ)ï½’â”â”³ï¼ï¼ï¼ï¼Š",
                 "ãƒ»-/(ã€‚â–¡ã€‚;/)â€”-â”³â”“y(-_ãƒ» )", "(ï¾’â–¼â–¼)â”)ï¾Ÿoï¾Ÿ)",
                 "[ï¾‰à² à³ƒà² ]ï¸»Ì·â”»Ì¿â•â”ä¸€", "â€¦â€¦â”³â”“o(â–¼â–¼ï½·)",
                 "(ï½·â–¼â–¼)oâ”â”³â€¦â€¦", "(ï¾’â–¼çš¿â–¼)â”³*â€“",
                 "Ì¿Ì¿â€™Ì¿â€™\\\ÌµÍ‡Ì¿Ì¿\\\=(â€¢Ìªâ—)=/ÌµÍ‡Ì¿Ì¿/â€™Ì¿Ì¿ Ì¿ Ì¿ Ì¿",
                 "ã€‘ï¾ŸÐ”ï¾Ÿ)â”³â€”-ï¾Ÿ~:;â€™:;Ï‰*:;â€™;â€”-",
                 "Î¾(âœ¿ â›â€¿â›)Î¾â–„ï¸»â”»â”³â•ä¸€	",
                 "âž ã¤: â€¢Ì€ âŒ‚ â€¢Ì : âž-ï¸»â•¦ÌµÌµÍ‡Ì¿Ì¿Ì¿Ì¿â•â•â•¤â”€",
                 "â•¾â”â•¤ãƒ‡â•¦ï¸»Ô…à¼ ï½¥à¸´ _Ê– ï½¥à¸´ à¼à¸‡",
                 "â€¦â€¦â”³â”“o(-ï½€Ð”Â´-ï¾’ )",
                 "â”Œ( ÍÂ° ÍœÊ–Í¡Â°)=Îµ/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿ Ì¿ â””à¼ à¹‘ _ à¹‘ à¼â”˜",
                 "(â€¥)â†ï¿¢~(â–¼â–¼#)~~",
                 "(à¸‡âŒâ–¡Ù„Íœâ–¡)ï¸»Ì·â”»Ì¿â•â”ä¸€",
                 "â€˜Ì¿â€™\\\ÌµÍ‡Ì¿Ì¿\\\=( `â—Ÿ ã€)=/ÌµÍ‡Ì¿Ì¿/â€™Ì¿Ì¿ Ì¿",
                 "à¼¼ ÂºÙ„ÍŸÂº à¼½ Ì¿ Ì¿ Ì¿ Ì¿â€™Ì¿â€™ÌµÐ·=à¼¼ â–€Ì¿Ä¹Ì¯â–€Ì¿ Ì¿ à¼½",
                 "(ã‚­â–¼â–¼)ï¼¿â”â”³â€¦â€¦",
                 "( Íà²  Ê– à² )=Îµ/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿ Ì¿",
                 "áƒš(~â€¢Ì€ï¸¿â€¢Ì~)ã¤ï¸»Ì·â”»Ì¿â•â”ä¸€",
                 "(à¸‡ Í Â° / ^ \\\ Â°)-/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿ Ì¿",
                 "(â€˜ÂºÙ„ÍŸÂº)ãƒŽâŒ’. Ì¿Ì¿ Ì¿Ì¿ Ì¿â€™Ì¿â€™ÌµÍ‡Ì¿Ì¿Ð·=à¼¼ â–€Ì¿Ì¿Ä¹Ì¯Ì¿Ì¿â–€Ì¿ Ì¿ à¼½",
                 "(â–€Ì¿Ì¿Ä¹Ì¯Ì¿Ì¿â–€Ì¿ Ì¿)â€¢ï¸»Ì·Ì¿â”»Ì¿â”»â•â”â”ãƒ½à¼¼àºˆç›Šàºˆà¼½ï¾‰",
                 "ãƒ¼â•â”»â”³ï¸»â–„Î¾(âœ¿ â›â€¿â›)Î¾â–„ï¸»â”»â”³â•ä¸€",
                 "ï¾(ToTï¾)))ã€€ãƒ»ã€€â€”ã€€ã€€Îµï¿¢(â–¼â–¼ãƒ¡)å‡¸",
                 "( ï¾’â–¼Ð”â–¼)â”â˜†====(((ï¼¿â—‡ï¼¿)======âŠƒ",
                 "!! ( ï¾’â–¼Ð”â–¼)â”â˜†====(((ï¼¿â—‡ï¼¿)======âŠƒ",
                 "!!(â˜…â–¼â–¼)oâ”³*â€”â€”â€”â€”â€”â€“â—));Â´ï¾›`))",
                 "!! ï¾(ToTï¾)))ã€€ãƒ»ã€€â€”ã€€ã€€Îµï¿¢(â–¼â–¼ãƒ¡)å‡¸",
                 "ãƒ½à¼¼àºˆç›Šàºˆà¼½_â€¢ï¸»Ì·Ì¿â”»Ì¿â•â”ä¸€|<â€”â€”â€” Ò‰ Ä¹Ì¯Ì¿Ì¿â–€Ì¿ Ì¿)",
                 "ãƒ½à¼¼xÙ„Íœxà¼½ï¾‰ <===== Ì¿â€™ Ì¿â€™\\\ÌµÍ‡Ì¿Ì¿\\\Ð·à¼¼àºˆÙ„Íœàºˆà¼½ Îµ/ÌµÍ‡Ì¿Ì¿/â€™Ì¿â€™Ì¿ =====> ãƒ½à¼¼xÙ„Íœxà¼½ï¾‰",
                 "áƒš[â˜‰ï¸¿Û)à¥­)à¥­ï¸»Ì·â”»Ì¿â•â”ä¸€ï¸»Ì·â”»Ì¿â•â”ä¸€",
                 "( Ï†_<)râ”¬ â”â”â”â”â”â”â€¦=>"],
    "owners": ["113953", "135450", "24986","117922","128263"]
}


def handleActivity(activity):
    # log("ping", "activity.txt", verbose=False)
    if "e" in activity:
        for item in activity["e"]:
            if item["user_id"] == 200207:  # bot's user
                continue
            # 1: message, 2: edit, 3: user enters, 4: user leaves
            if item['event_type'] == 1:  # message posted
                handleMessages(item)

dailyQuestionThread=None
def sendDailyQuestion(roomId):
    currentDailyQuestionThread=dailyQuestionThread
    while currentDailyQuestionThread==dailyQuestionThread: # send daily random network question
        questions=chatbot.getSavedData("questions_interesting_10",roomId)
        if questions is False:
            questions=chatbot.getNetworkQuestions(roomId,10,1000)
        chatbot.sendMessage(random.choice(questions),roomId)
        time.sleep(3600*24)

def handleMessages(message):
    global dailyQuestionThread
    Mcontent = message["content"].replace('<div>', '').replace('</div>', '').replace( #encode("utf-8").
        "<div class='full'>", '')
    MuserName = message['user_name'].encode("utf-8")
    MchatRoom = message['room_name'].encode("utf-8")
    MroomId = str(message['room_id'])  # int
    noDelete = Mcontent.find('!!!') >= 0
    tempDataPath = MroomId + '//temp//'
    chatbot.log(MuserName + ' : ' + Mcontent, name=MroomId + '//log.txt', verbose=False)
    print(MchatRoom + " | " + MuserName + ' : ' + Mcontent)
    if  Mcontent.find('!!')>0 and random.randint(1, 1000) == 133:
        chatbot.sendMessage(u"__ðŸŽºðŸŽºðŸŽº AND HIS NAME IS JOHN CENA ðŸŽºðŸŽºðŸŽº__", MroomId)
    Mcontent, McontentCase = Mcontent.lower(), Mcontent
    if Mcontent.find('!!img/') >= 0:
        id = chatbot.sendMessage(
            "Hold tight, I'm processing your request ... " + random.choice(coolTables["tablesList"]), MroomId,
            noDelete=noDelete)
        molec = McontentCase[Mcontent.find('img/') + len('img/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '').replace('&#39;', "'")
        reqUrl = "http://www.chemspider.com/Search.aspx?q=" + molec
        answ = session.get(reqUrl).text
        pos=answ.find('<a href="/Chemical-Structure.')
        if answ.find('Found 0 results')>=0 and pos<0:
            chatbot.editMessage("No result found.", id, MroomId)
            return
        molecId=0
        if answ.find('<span>Names and Synonyms</span>')<0:
            molecId=answ[pos+len('<a href="/Chemical-Structure.'):answ.find('.',pos+len('<a href="/Chemical-Structure.')+1)]
        else:
            pos=answ.find('ChemSpider ID</span>')
            molecId=answ[pos+len('ChemSpider ID</span>'):answ.find('</li>',pos)]

        imgUrl='http://www.chemspider.com/ImagesHandler.ashx?id='+molecId+'&w=150&h=150'
        print(imgUrl)
        molecImg = session.get(imgUrl, stream=True)

        with open(tempDataPath + 'mol.gif', 'wb') as out_file:
            shutil.copyfileobj(molecImg.raw, out_file)
        try:
            Image.open(tempDataPath + 'mol.gif').save(tempDataPath + 'mol.png')
        except Exception as e:
            chatbot.editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        del molecImg
        removeUselessSpace('mol.png', tempDataPath)
        ans = ""
        try:
            ans = clientImg.upload_from_path(tempDataPath + 'cropped_mol.png')
        except Exception as e:
            chatbot.editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        answUrl = ans['link']
        chatbot.editMessage(answUrl, id, MroomId)
    if Mcontent.find('!!wiki/') >= 0:
        article = McontentCase[Mcontent.find('wiki/') + len('wiki/'):].replace(' ', '_').replace('</div>',
                                                                                                 '').replace('\n', '')
        id = chatbot.sendMessage("https://en.wikipedia.org/wiki/" + article, MroomId, noDelete=noDelete)
    if Mcontent.find('!!xkcd') >= 0:
        number=""
        if Mcontent.find('xkcd/')>0:
            number = McontentCase[Mcontent.find('xkcd/') + len('xkcd/'):].replace(' ', '_').replace('</div>',
                                                                                                 '').replace('\n', '')
        answ=session.get("http://xkcd.com/"+number).text
        if answ.find("404 - Not Found")>0:
            chatbot.sendMessage("Invalid ID", MroomId, noDelete=noDelete)
            return
        chatbot.sendMessage("http://xkcd.com/"+number, MroomId, noDelete=noDelete)
    if Mcontent.find('!!flip') >= 0:
        p=Mcontent.find('flip/')+len("flip/")
        if p>=len("flip/"):
            chatbot.sendMessage(random.choice(coolTables["flipsList"])+upsidedown.transform(McontentCase[p:])[::-1], MroomId, noDelete=noDelete)
        else:
            chatbot.sendMessage(random.choice(coolTables["tablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!doubleflip') >= 0:
        p = Mcontent.find('doubleflip/') + len("doubleflip/")
        if p >= len("doubleflip/"):
            sss=upsidedown.transform(McontentCase[p:])
            chatbot.sendMessage(sss+random.choice(coolTables["doubleflipsList"]) + sss[::-1], MroomId,
                                noDelete=noDelete)
        else:
            chatbot.sendMessage(random.choice(coolTables["tablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!untable') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["untablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!gun') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["gunsList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!beer') >= 0:
        #
        chatbot.sendMessage("http://www.mandevillebeergarden.com/wp-content/uploads/2015/02/Beer-Slide-Background.jpg",
                            MroomId, noDelete=noDelete)
    if Mcontent.find('!!tea') >= 0:
        #
        chatbot.sendMessage("https://pixabay.com/static/uploads/photo/2015/07/02/20/57/chamomile-829538_960_720.jpg",
                            MroomId, noDelete=noDelete)
    if Mcontent.find('!!spam') >= 0:
        #
        chatbot.sendMessage("https://upload.wikimedia.org/wikipedia/commons/0/09/Spam_can.png", MroomId,
                            noDelete=noDelete)
    if Mcontent.find('!!coffee') >= 0:
        #
        chatbot.sendMessage(
            "http://res.freestockphotos.biz/pictures/10/10641-a-cup-of-coffee-on-a-bean-background-pv.jpg",
            MroomId)
    if Mcontent.find('!!sushi') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["sushiList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!ice cream') >= 0:
        #
        chatbot.sendMessage(random.choice(coolTables["iceCreamList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!test') >= 0:
        id = chatbot.sendMessage("a test !!", MroomId, noDelete=noDelete)
        time.sleep(1)
        chatbot.editMessage("edited !", id, MroomId)
    if Mcontent.find('!!help') >= 0:
        helpString = """Hi! I'm the almighty bot of ChemistrySE's main chatroom. /!\ If you find me annoying, you can ignore me by clicking on my profile image and chosing "ignore this user" /!\ You can find my documentation [here](http://meta.chemistry.stackexchange.com/a/3198/5591)."""
        chatbot.sendMessage(helpString, MroomId, noDelete=noDelete)
    if Mcontent.find('!!doi/') >= 0:
        doi = McontentCase[Mcontent.find('doi/') + len('doi/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '')
        r = chatbot.sendRequest("http://pubs.acs.org/doi/abs/" + doi).text
        if r.find('Your request resulted in an error') > 0:
            chatbot.sendMessage("Could not find the requested DOI : " + doi, MroomId, noDelete=noDelete)
        else:
            try:
                p = r.find('dc.Title" content="') + len('dc.Title" content="')
                title = r[p:r.find('" />', p)]

                p = r.find('dc.Creator" content="') + len('dc.Creator" content="')
                author1 = r[p:r.find('" />', p)]

                chatbot.sendMessage("DOI " + doi + ' :\n"' + title + '"\nFirst author : ' + author1, MroomId,
                                    noDelete=noDelete)
            except Exception as e:
                chatbot.sendMessage("An error occured :" + str(e), MroomId, noDelete=noDelete)
    if Mcontent.find('!!scholar/') >= 0:
        search = McontentCase[Mcontent.find('scholar/') + len('scholar/'):].replace(' ', '%20').replace('</div>',
                                                                                                        '').replace(
            '\n', '')
        reqUrl = 'http://scholar.google.fr/scholar?hl=en&q=' + urllib.quote(search.replace(" ", "+")).replace("%2520",
                                                                                                              "+")
        r = chatbot.sendRequest(reqUrl,
                                "get")  # encode it, get best result, display * best result * requests's link * list of 3 next results
        r = r.text

        numArticles = 2
        articles = []
        art, p = 0, r.find('<h3 class="gs_rt"><a href="')
        while p >= 0 and art < numArticles:
            p += len('<h3 class="gs_rt"><a href="')
            url = r[p:r.find('"', p)]
            p = r.find('">', p) + len('">')
            title = r[p:r.find('</a>', p)].replace("<b>", "").replace("</b>", "")
            art += 1
            articles.append({"title": title, "url": url})
            p = r.find('<h3 class="gs_rt"><a href="', p + 1)
        fullMsg = "[Link to the request](" + reqUrl + "). Top links : "
        for i in articles:
            fullMsg += '[' + i["title"] + "](" + i['url'] + ") | "
        chatbot.sendMessage(fullMsg, MroomId, noDelete=noDelete)
    w = """if Mcontent.find('!!nogreet') >= 0:
        noGreet=getSavedData("noGreet.json")
        if not str(message['user_id']) in noGreet:
            noGreet[message['user_id']] = MuserName
            setSavedData("noGreet.json",noGreet)
            chatbot.sendMessage(MuserName + " was added to the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was added to the noGreet list.")
        else:
            chatbot.sendMessage("You are already in the noGreet list.", MroomId, noDelete=noDelete)
    if Mcontent.find('!!greet') >= 0:
        noGreet = getSavedData("noGreet.json")
        if str(message['user_id']) in noGreet:
            noGreet.pop(str(message['user_id']))
            setSavedData("noGreet.json", noGreet)
            chatbot.sendMessage(MuserName + " was removed from the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was removed from the noGreet list.")
        else:
            chatbot.sendMessage("You are not in the noGreet list.", MroomId, noDelete=noDelete)
    """
    if Mcontent.find('!!greet/') >= 0:
        user = McontentCase[Mcontent.find('greet/') + len('greet/'):].replace('%20', ' ').replace('</div>', '').replace(
            '\n', '')
        id = 0
        try:
            id = int(user)
        except Exception:
            pass
        uName = user
        if id is not None and id > 0:
            r = chatbot.sendRequest("http://chat.stackexchange.com/users/" + user).text
            p = r.find("<title>User ") + len("<title>User ")
            uName = r[p:r.find(" |", p)]
        chatbot.sendMessage(
            "Welcome to The Periodic Table " + uName + "! [Here](http://meta.chemistry.stackexchange.com/q/2723/) are our chat guidelines and it's recommended that you read them. If you want to turn Mathjax on, follow the instructions [in this answer](http://meta.stackexchange.com/a/220976/). Happy chatting!",
            MroomId)
    #** Owners only
    if Mcontent.find('!!sleep/') >= 0:
        if str(message['user_id']) in coolTables["owners"]:
            timeSleep = McontentCase[Mcontent.find('sleep/') + len('sleep/'):].replace(' ', '%20').replace('</div>',
                                                                                                           '').replace(
                '\n', '')
            try:
                timeSleep = float(timeSleep) * 60
                chatbot.sendMessage("See you in " + str(timeSleep / 60.) + " minutes !", MroomId, noDelete=noDelete)
                time.sleep(timeSleep)
            except Exception:
                chatbot.sendMessage("invalid time", MroomId, noDelete=noDelete)
    if Mcontent.find('!!reload') >= 0:
        if str(message['user_id']) in coolTables["owners"]:
            try:
                newCode=chatbot.sendRequest("https://raw.githubusercontent.com/gauthierhaas/SE_Bot/master/updater.py").text
                exec(newCode, globals())
                chatbot.sendMessage("Success !",MchatRoom)
            except Exception as e:
                chatbot.log("Error : "+str(e))
    if Mcontent.find('!!daily') >= 0:
        if str(message['user_id']) in coolTables["owners"]:
            try:
                dailyQuestionThread=threading.Thread(target=sendDailyQuestion, args={MroomId})
                dailyQuestionThread.start()
            except Exception as e:
                chatbot.log("Error : " + str(e))


chatbot.joinRooms({"25323": handleActivity, "3229": handleActivity, "26060": handleActivity, "38172": handleActivity,
                   "1": handleActivity})  # 10121 : test, 3229 : chemistry, 26060 : g-block, 38172 : chemobot, 1: sandbox

chatbot.enableControl(3229)

