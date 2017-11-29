# -*- coding: utf-8 -*-
## V 3.0
"""
ChangeLog
- V3.0 -
Rewrote main.py to work with the new chatbot.py
Cleaned the code



"""
## Description
"""
A chatbot mainly for the ChemistryStackExchange chatroom
"""

# Imports and initialization
from chatbot import Chatbot, log # chatbot.py, the chatbot framework
import random # chose a random element from a table
import upsidedown # flips strings - non PIP library
import shutil # file manipulation (creating images from bytes)
from PIL import Image # check if images are valid / images format conversion
from imgurpython import ImgurClient # upload images to imgur
import time # sleeping

client_id = 'fb1b922cb86bb0f'  # Imgur module setup
client_secret = 'cffaf5da440289a8923f9be60c22b26e25675d3d'
clientImg = ImgurClient(client_id, client_secret)

## Initialization
# Create chatbot
chatbot=Chatbot()
# Login to SE
chatbot.login()

# useful vars
coolTables = {
    "tablesList": ["(╯°□°）╯︵ ┻━┻", "(ノಠ益ಠ)ノ彡┻━┻", "ʕノ•ᴥ•ʔノ ︵ ┻━┻", "(/¯◡ ‿ ◡)/¯ ~ ┻━┻", "(ノ-_-)ノ ~┻━┻", "(ﾉ；；)ﾉ~┻━┻",
                   "(ﾉ-_-)ﾉ ~┻━┻ ☆`", "(ノ-_-)ノ・・・~~┻━┻", "(ノ-_-)ノ~┻━┻", "ノ￣□￣)ノ ~┻━┻", "(ﾉꐦ ⊙曲ఠ)ﾉ彡┻━┻", "(ﾉ｀□´)ﾉ⌒┻━┻",
                   "(ﾉꐦ ๑´Д`๑)ﾉ彡┻━┻", "┻━┻ミ＼（≧ロ≦＼）", "(ﾉ￣□￣)ﾉ ~┻━┻", "（ノ♯｀△´）ノ~’┻━┻", "（ノT＿T)ノ ＾┻━┻", "(┛ಠДಠ)┛彡┻━┻",
                   "(ノ°▽°)ノ︵┻━┻", "(ﾉ*’ω’*)ﾉ彡┻━┻", "‎(ﾉಥ益ಥ）ﾉ ┻━┻", "(╯’□’)╯︵ ┻━┻", "(ﾉಥДಥ)ﾉ︵┻━┻･/", "(._.) ~ ︵ ┻━┻",
                   "┗[© ♒ ©]┛ ︵ ┻━┻", "┻━┻ ︵ ლ(⌒-⌒ლ)", "(ﾉ＾◡＾)ﾉ︵ ┻━┻", "༼ ᕤ ºل͟º ༽ᕤ ︵┻━┻", "ヽ༼ ツ ༽ﾉ ︵┻━┻",
                   "༼ ͠ຈ ͟ل͜ ͠ຈ༽ง︵┻━┻", "ヽ༼ຈل͜ຈ༽ﾉ︵┻━┻", "(╯ຈل͜ຈ) ╯︵ ┻━┻", "༼ノಠل͟ಠ༽ノ ︵ ┻━┻", "༼ﾉຈل͜ຈ༽ﾉ︵┻━┻",
                   "(╯ ͝° ͜ʖ͡°)╯︵ ┻━┻", "(つ☢益☢)つ︵┻━┻", "ヽ༼ຈل͜ຈ༽ﾉ︵ ┻━┻", "(┛◉Д◉)┛彡┻━┻", "(ﾉ≧∇≦)ﾉ ﾐ ┸━┸", "┻━┻ミ＼(≧ﾛ≦＼)",
                   "(ノ｀´)ノ ~┻━┻ ～", "ʕ ⊃･ ◡ ･ ʔ⊃︵┻━┻", "(ﾉ▼д▼)ﾉ ~┻━┻ ☆`", "(┛❍ᴥ❍)┛彡┻━┻", "(ʘ∇ʘ)ク 彡 ┻━┻",
                   "┻━┻ ︵ ლ(ಠ益ಠლ)", "(╯ಠ_ರೃ)╯︵ ┻━┻", "/(ò.ó)┛彡┻━┻", "(╯=▃=)╯︵┻━┻", "(ノ｀ー´)ノ・・・~~┻━┻", "(ﾉ｀◇´)ﾉ~┻━┻",
                   "┻━┻ ヘ╰( •̀ε•́ ╰)", "(ノ｀Д´)ノ~┻━┻", "(ﾉ｀△´)ﾉ~┻━┻", "(⑅ノ-_-)ノ~┻━┻    ", "(╯ ･ ᗜ ･ )╯︵ ┻━┻  ",
                   "(ノ ﾟДﾟ)ノ　＝＝＝＝　┻━━┻", "!!!!|┛*｀Д´|┛・・~~┻━┻　┳━┳", "(/#-_-)/~┻┻〃", "(/ToT)/ ~┻┻", "（ノ－＿－）ノ･･･~┻┻    ",
                   "(ﾉ*’‐’)ﾉ ﾐ ┸┸", "(ノ#-_-)ノ ミ　┴┴", "（ノ｀_´）ﾉ~~┴┴", "(ノ｀´）ノミ┻┻", "ノToT)ノ ~┻┻", "(ﾉ｀Д)ﾉ:・’∵:.┻┻",
                   "(ﾉToT)ﾉ ﾐ ┸┸", "(メ–)ノノ。。。┻┻", "(ﾉ≧∇≦)ﾉ ﾐ ┸┸", "(ノToT)ノ ~┻┻", "┳┳ヾ(T(エ)Tヽ)",
                   "(ﾉTwT)ﾉ ┫:･’.::･┻┻:･’.::･", "(ノ͡° ͜ʖ ͡°)ノ︵┻┻  ", "（ノ－＿－）ノ・・・~~~┻┻", "(ノ；o；)ノ ┫:･’.::･┻┻:･’.::･",
                   "(ノ；ω；)ノ ┫:･’.::･┻┻:･’.::･", "(ノToT)ノ ┫:・’.::・┻┻:・’.::・", "(ノTДT)ノ ┫:･’.::･┻┻:･’.::･",
                   "(ノToT)ノ　┫：･’.::･┻┻:･’.::･", "（ﾉ｀Д´）ﾉ－－－－－┻┻　-３-３", "（ノ￣＾￣）ノ　┳┳　┣　┻┻　┫　┳┳",
                   "(ﾉ´□｀)ﾉ ┫:･’∵:.┻┻:･’.:┣∵･:. ┳┳", "(ノ｀０)ノ ⌒┫：・’.：：・┻┻：・’.：：・", "(ﾉ｀⌒´)ﾉ ┫：・’.：：・┻┻：・’.：：・",
                   "(ノ｀⌒´)ノ ┫：・’.：：・┻┻：・’.：：・", "( ｀o)ﾉﾉ ┫", "( ﾉo|o)ﾉ ┫｡ﾟ:.:", "（；－－）ノノ ┫：・゜’", "(/-o-)/ ⌒ ┤",
                   "(/｀ο´)/ ⌒ ┫:’ﾟ:｡･,. 。゜", "(/ToT)/_┫・..", "(ノ－＿－）ノ　┫〝〟∵", "(ノ-0-)ノ　┫∵：．", "(ﾉ-ｏ-)ﾉ ~┫：・’.：：・",
                   "(ノ-o-)ノ⌒┳ ┫┻┣", "(ノ￣＿￣）ノ　┫〝〟∵", "(丿>ロ<)丿 ┤∵:.", "（ノ￣ー￣）ノ　┫：・’.::", "(ノ￣ー￣）ノ　┫〝〟∵",
                   "(ﾉ＝ﾟﾛﾟ)ﾉ ⌒┫:･’.::", "(ノ＞o＜)ノ ┫:･’.::", "（ノ≧∇≦）ノ　┫　゜・∵。", "（ノ≧ο≦）ノ　┫　゜・∵。", "（ノ○Д○）ノ＝＝＝┠",
                   "（ノー”ー）ノ　┫　゜・∵。", "(ノToT)ノ ┫:・’.::・", "((((ﾉ｀皿´)ﾉ ⌒┫:･┫┻┠’.", "(ﾉ*｀▽´*)ﾉ ⌒┫ ┻ ┣ ┳", "(ノ￣皿￣）ノ ⌒=== ┫",
                   "･.:ﾟ｡┣＼(’ﾛ´＼)", "(ﾉ#▼o▼)ﾉ ┫:･’.::･", "┣¨┣¨┣¨ヾ(゜Д゜ )ノ┣¨┣¨┣", "┣¨ ୧(๑ ⁼̴̀ᐜ⁼̴́๑)૭",
                   "((|||||┝＼(｀д´)／┥|||||))", "┝＼( ‘∇^*)^☆／┥  ", "(ﾉﾟ∀ﾟ)ﾉ ┫:｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆━━━!!!!",
                   "┻━┻ ︵ ¯\\\ (ツ)/¯ ︵ ┻━┻", "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻", "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻", "┻━┻ ︵ ¯\\\(ツ)/¯ ︵ ┻━┻",
                   "┫┻┠⌒ヾ(-_-ヾ 三 ﾉ-_-)ﾉ⌒┫:･┫┻", "（/＞□＜）/亠亠", "(ノ￣＿￣)ノ＼。:・゛。", "(ノÒ益Ó)ノ彡▔▔▏", "_|___|_ ╰(º o º╰)  ",
                   "(ノ￣￣∇￣￣)ノ~~~~~⌒━━┻━━┻━━", "⊂(ﾉ￣￣￣(工)￣￣￣)⊃ﾉ~~~~~━━━┻━━┻━━━", "(ノ-o-)ノ┸┸)`3゜)・;’.",
                   "(ノ-。-）ノ┻━┻☆(　　^)", "(ノ-_-)ノ ~┻━┻ (/o＼)", "(ノ#-◇-)ノ ~~~~┻━┻☆(x _ x)ノ", "(ノ｀０)ノ ⌒┫ ┻ ┣ ┳☆(x x)",
                   "(ノ｀m´)ノ ~┻━┻ (/o＼)", "(ﾉ`Д´)ﾉ.:･┻┻)｀з゜)･:ﾞ;    ", "(ノ￣▽￣)ノ┻━┻☆)*￣□)ノ))", "(ノ￣◇￣)ノ~┻━┻/(×。×)",
                   "(ﾉToT)ﾉ ┫:･’.::･＼┻┻(･_＼)", "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)", "(ノ^_^)ノ┻━┻ ┬─┬ ノ( ^_^ノ)", "ﾐ┻┻(ﾉ>｡<)ﾉ",
                   ".::･┻┻☆()ﾟOﾟ)", "(ﾉ｀A”)ﾉ ⌒┫ ┻ ┣ ┳☆(x x)", "(ノ｀m´)ノ ~┻━┻ (/o＼)", "⌒┫ ┻ ┣ ⌒┻☆)ﾟ⊿ﾟ)ﾉ",
                   "(ﾉ≧∇≦)ﾉ ﾐ ┸┸)`νﾟ)･;’.", "(ﾉToT)ﾉ ┫:･’.::･＼┻┻(･_＼)", "（ノ－ｏ－）ノ　”″┻━┻☆（>○<）",
                   "ミ(ノ￣^￣)ノ!≡≡≡≡≡━┳━☆()￣□￣)/", "（メ｀д´）┫～┻┻ ～┣～┳┳　　（。@ﾍ@。川", "ミ(ノ￣^￣)ノ≡≡≡≡≡━┳━☆()￣□￣)/",
                   "(╯°Д°）╯︵/(.□ . )", "(ノಠ ∩ಠ)ノ彡( o°o)", "/( .□.) ︵╰(゜益゜)╯︵ /(.□. /)",
                   "≡/( .-.)\\\ ︵╰(«○»益«○»)╯︵ /(.□. /)̨", "(/ .□.)\\\ ︵╰(゜Д゜)╯︵ /(.□. \\\)", "（╯°□°）╯︵( .o.)",
                   "(╯°□°）╯︵ (\\\ . 0 .)(/￣(ｴ)￣)/ ⌒ ○┼<", "(╯°□°）╯︵ /( ‿⌓‿ )ノ┬─┬ノ ︵ ( o°o)", "┬─┬ ︵ /(.□. \\\）",
                   "┬──┬╯︵ /(.□. \\\）", "┬──┬ ︵(╯。□。）╯", "ヘ(´° □°)ヘ┳━┳", "(╯°□°)╯︵ ʞooqǝɔɐℲ", "(╯°□°)╯︵ ɹǝʇʇıʍ⊥",
                   "(∿°○°)∿ ︵ ǝʌol", "(╯°□°)╯︵ ɯsıɥdɹoɯouǝʞs", "(╯°□°)╯︵ sɯɐxǝ", "(╯°□°)╯︵ ƃuıʎpnʇs", "(╯°□°)╯︵ ʞɹoʍ",
                   "(੭ ◕㉨◕)੭ =͟͟͞͞=͟͟͞͞三❆)’дº);,’:=͟͟͞͞", "(ﾉꐦ ◎曲◎)ﾉ=͟͟͞͞ ⌨", "(っ ºДº)っ ︵ ⌨", "(╯^□^)╯︵ ❄☃❄",
                   "(╯ `Д ́)╯︵ (฿)", "♡╰(*ﾟxﾟ​*)╯♡", "˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞✉", "(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨`ワ°)・;’.",
                   "╰( ^o^)╮-=ﾆ=一＝三", "（ノ>_<）ノ　≡●", "●~*⌒ ヽ(´ｰ｀ )", "!!(⊃ Д)⊃≡ﾟ ﾟ", "(╬☉д⊙)＝◯)๏д๏))･;’.",
                   "(ര̀⍨ര́)و ̑̑༉ լਕ ̏੭ჯ ૅੁ~ɭ ɿ❢❢", "˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞˳˚॰°ₒ৹๐", "૮(ꂧ᷆⺫ꂧ᷇)ა=͟͟͞͞ꊞ",
                   "ヽ［・∀・］ﾉ(((((((((●～*", "ﾍ|･∀･|ﾉ*~●", "(*ﾉﾟ▽ﾟ)ﾉ ⌒((((●", "(╯°□°）╯︵ ส็็็็็็็ส", "⌨ █▬▬◟(`ﮧ´ ◟ )",
                   "○三　＼(￣^￣＼）", ",,,,,,,,((*￣(ｴ)￣)ﾉ ⌒☆ o*＿(x)_)", "(۶ૈ‡▼益▼)۶ૈ=͟͟͞͞ ⌨", "(ノω・)ノ⌒゛◆",
                   "(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨", "(۶ૈ ᵒ̌ Дᵒ̌)۶ૈ=͟͟͞͞ ⌨", "☆(ﾉ^o^)ﾉ‥‥‥…━━━━〇(^~^)",
                   "( つ•̀ω•́)つ・・*:・:・゜:==≡≡Σ=͟͟͞͞(✡)`Д´）"],
    "flipsList": ["( つ•̀ω•́)つ","(∿°○°)∿","(۶ૈ‡▼益▼)۶", "◟(`ﮧ´ ◟ )","(╯°ਊ°)╯︵", "(づಥਊಥ)づ︵", "(づ๑ʖ๑)┛︵"],
    "doubleflipsList": ["╰(*ﾟxﾟ​*)╯","＼(｀д´)／","︵╰(゜益゜)╯︵ ","╰(«○»益«○»)╯","︵╰(゜Д゜)╯︵"],
    "untablesList": ["┬─┬ ノ( ^_^ノ)", "┬──┬◡ﾉ(° -°ﾉ)", "┬━┬ ノ( ゜¸゜ノ)", "┬━┬ ノ( ゜-゜ノ)", "┳━┳ ヽ༼ಠل͜ಠ༽ﾉ",
                     "┬──┬ ¯\\\_(ツ)",
                     "┬──┬ ノ( ゜-゜ノ)", "(ヘ･_･)ヘ┳━┳", "┻o(Ｔ＿Ｔ )ミ( ；＿；)o┯", "┣ﾍ(≧∇≦ﾍ)… (≧∇≦)/┳━┳",
                     "┣ﾍ(^▽^ﾍ)Ξ(ﾟ▽ﾟ*)ﾉ┳━┳",
                     ],
    "iceCreamList": [
        "http://www.daytonaradio.com/wkro/wp-content/uploads/sites/4/2015/07/ice-cream.jpg"],
    "sushiList": [
        "http://www.shopbelmontmarket.com/wp-content/uploads/page_img_sushi_01.jpg",
        "http://www.jim.fr/e-docs/00/02/66/5C/carac_photo_1.jpg",
        "https://u.tfstatic.com/restaurant_photos/503/250503/169/612/sushi-company-suggestie-van-de-chef-5fc05.jpg"],
    "gunsList": ["(҂‾ ▵‾)︻デ═一 (˚▽˚’!)/",
                 "̿’ ̿’\\\̵͇̿̿\\\з=(ಥДಥ)=ε/̵͇̿̿/’̿’̿",
                 "( う-´)づ︻╦̵̵̿╤── \\\(˚☐˚”)/",
                 "(⌐■_■)–︻╦╤─",
                 "̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽	",
                 "━╤デ╦︻(▀̿̿Ĺ̯̿̿▀̿ ̿)",
                 "╾━╤デ╦︻	▄︻̷̿┻̿═━一", "︻╦̵̵͇̿̿̿̿══╤─",
                 "༼ ಠل͟ಠ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ຈل͜ຈ༽ﾉ",
                 "̿’ ̿’\\\̵͇̿̿\\\з=(ಡل͟ಡ)=ε/̵͇̿̿/’̿’̿",
                 "￢o(￣-￣ﾒ)", "(҂`з´).っ︻デ═一",
                 "ᕕ╏ ͡ᵔ ‸ ͡ᵔ ╏و︻̷┻̿═━一", "⌐╦╦═─",
                 "(ﾟ皿ﾟ)ｒ┏┳－－－＊",
                 "・-/(。□。;/)—-┳┓y(-_・ )", "(ﾒ▼▼)┏)ﾟoﾟ)",
                 "[ﾉಠೃಠ]︻̷┻̿═━一", "……┳┓o(▼▼ｷ)",
                 "(ｷ▼▼)o┏┳……", "(ﾒ▼皿▼)┳*–",
                 "̿̿’̿’\\\̵͇̿̿\\\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿",
                 "】ﾟДﾟ)┳—-ﾟ~:;’:;ω*:;’;—-",
                 "ξ(✿ ❛‿❛)ξ▄︻┻┳═一	",
                 "⁞ つ: •̀ ⌂ •́ : ⁞-︻╦̵̵͇̿̿̿̿══╤─",
                 "╾━╤デ╦︻ԅ། ･ิ _ʖ ･ิ །ง",
                 "……┳┓o(-｀Д´-ﾒ )",
                 "┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ └། ๑ _ ๑ །┘",
                 "(‥)←￢~(▼▼#)~~",
                 "(ง⌐□ل͜□)︻̷┻̿═━一",
                 "‘̿’\\\̵͇̿̿\\\=( `◟ 、)=/̵͇̿̿/’̿̿ ̿",
                 "༼ ºل͟º ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ ▀̿Ĺ̯▀̿ ̿ ༽",
                 "(キ▼▼)＿┏┳……",
                 "( ͝ಠ ʖ ಠ)=ε/̵͇̿̿/’̿’̿ ̿",
                 "ლ(~•̀︿•́~)つ︻̷┻̿═━一",
                 "(ง ͠° / ^ \\\ °)-/̵͇̿̿/’̿’̿ ̿",
                 "(‘ºل͟º)ノ⌒. ̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽",
                 "(▀̿̿Ĺ̯̿̿▀̿ ̿)•︻̷̿┻̿┻═━━ヽ༼ຈ益ຈ༽ﾉ",
                 "ー═┻┳︻▄ξ(✿ ❛‿❛)ξ▄︻┻┳═一",
                 "ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸",
                 "( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃",
                 "!! ( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃",
                 "!!(★▼▼)o┳*—————–●));´ﾛ`))",
                 "!! ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸",
                 "ヽ༼ຈ益ຈ༽_•︻̷̿┻̿═━一|<——— ҉ Ĺ̯̿̿▀̿ ̿)",
                 "ヽ༼xل͜x༽ﾉ <===== ̿’ ̿’\\\̵͇̿̿\\\з༼ຈل͜ຈ༽ ε/̵͇̿̿/’̿’̿ =====> ヽ༼xل͜x༽ﾉ",
                 "ლ[☉︿۝)७)७︻̷┻̿═━一︻̷┻̿═━一",
                 "( φ_<)r┬ ━━━━━━…=>"],
    "owners": ["113953", "135450", "24986","117922"]
}

def handleEvents(room, event):
	if 'user_id' in event and event['user_id']==chatbot.bot_chat_id: return # don't consider events from the bot*
	if event['event_type']==1: # event: new message
		handleMessage(room, event)
	if event['event_type']==3: # event: user entered the room
		pass
	if event['event_type']==6: # event: change in the stars on a message
		pass
	if event['event_type']==10: # event: message deleted
		pass

commands={} #format :: {init : {cmd_msg : [func, sep]}, ...}
def addCommand(func, cmd_msg, init='!!', sep='/'):
	# adds commands following the following pattern
	# func(a,b,c) for message "!!cmd_msg/a/b/c"
	if not init in commands:
		commands[init]={}
	commands[init][cmd_msg]=[func, sep]

def initCommands():
	def exit(room, event, *args):
		if event['user_id']==117922: # Hippalectryon
			room.leave()
	def exit_all(room, event, *args):
		if event['user_id']==117922: # Hippalectryon
			chatbot.leaveAllRooms()
	def repeat(room, event, *args): # nope
		return
		s=args[0]
		room.sendMessage(s)
	def wiki(room, event, *args):
		article = args[0]
		room.sendMessage("https://en.wikipedia.org/wiki/{}".format(article))
	def flip(room, event, *args):
		if len(args)==0: # no args
			room.sendMessage(random.choice(coolTables["tablesList"]))
		else:
			msg=args[0]
			room.sendMessage(random.choice(coolTables["flipsList"])+upsidedown.transform(msg)[::-1])
	def molec_img(room, event, *args):
		def removeUselessSpace(name):
			image = Image.open(name)
			image.load()

			imageBox = image.getbbox()
			cropped = image.crop(imageBox)
			cropped.save(name)
		molec=args[0]
		id = room.sendMessage("Hold tight, I'm processing your request ... {}".format(random.choice(coolTables["tablesList"])))
		reqUrl = "http://cactus.nci.nih.gov/chemical/structure/{}/image".format(molec)
		molecImg = chatbot.session.get(reqUrl, stream=True)
		with open('{}/mol.gif'.format(room.temp_path), 'wb') as out_file:
			shutil.copyfileobj(molecImg.raw, out_file)
		try:
			Image.open('{}/mol.gif'.format(room.temp_path)).save('{}/mol.png'.format(room.temp_path))
		except Exception as e:
			room.editMessage("<An error occured : {}. Check your molecule's name>".format(e), id)
			return
		del molecImg
		removeUselessSpace('{}/mol.png'.format(room.temp_path))
		ans = ""
		try:
			ans = clientImg.upload_from_path('{}/mol.png'.format(room.temp_path))
		except Exception as e:
			room.editMessage("<An error occured : {}. Check your molecule's name>".format(e), id)
			return
		url = ans['link']
		room.editMessage(url, id)
	def doubleflip(room, event, *args):
		if len(args)==0: # no args
			room.sendMessage(random.choice(coolTables["tablesList"]))
		else:
			msg=args[0]
			sss=upsidedown.transform(msg)
			room.sendMessage("{}{}{}".format(sss,random.choice(coolTables["doubleflipsList"]),sss[::-1]))
	def untable(room, event, *args):
		room.sendMessage(random.choice(coolTables["untablesList"]))
	def gun(room, event, *args):
		room.sendMessage(random.choice(coolTables["gunsList"]))
	def beer(room, event, *args):
		room.sendMessage("http://www.mandevillebeergarden.com/wp-content/uploads/2015/02/Beer-Slide-Background.jpg")
	def tea(room, event, *args):
		room.sendMessage("https://www.drinkpreneur.com/wp-content/uploads/2017/02/drinkpreneur_health-benefits-of-rose-tea.jpg")
	def spam(room, event, *args):
		room.sendMessage("https://upload.wikimedia.org/wikipedia/commons/0/09/Spam_can.png")
	def coffee(room, event, *args):
		room.sendMessage("http://res.freestockphotos.biz/pictures/10/10641-a-cup-of-coffee-on-a-bean-background-pv.jpg")
	def sushi(room, event, *args):
		room.sendMessage(random.choice(coolTables["sushiList"]))
	def ice_cream(room, event, *args):
		room.sendMessage(random.choice(coolTables["iceCreamList"]))
	def test(room, event, *args):
		id=room.sendMessage("a test")
		time.sleep(1)
		room.editMessage("test - success !", id)
	def help(room, event, *args):
		helpString = """Hi! I'm the almighty bot of ChemistrySE's main chatroom. /!\ If you find me annoying, you can ignore me by clicking on my profile image and chosing "ignore this user" /!\ You can find my documentation [here](http://meta.chemistry.stackexchange.com/a/3198/5591)."""
		room.sendMessage(helpString)
	
	
	addCommand(exit, 'exit')
	addCommand(exit_all, 'exit!')
	addCommand(beer, 'beer')
	addCommand(tea, 'tea')
	addCommand(spam, 'spam')
	addCommand(coffee, 'coffee')
	addCommand(sushi, 'sushi')
	addCommand(ice_cream, 'ice cream')
	addCommand(repeat, 'repeat')
	addCommand(wiki, 'wiki')
	addCommand(flip, 'flip')
	addCommand(molec_img, 'img')
	addCommand(doubleflip, 'doubleflip')
	addCommand(untable, 'untable')
	addCommand(gun, 'gun')
	addCommand(test, 'test')
	addCommand(help, 'help')
initCommands()
	
def handleMessage(room, event):
	content = event["content"]
	user_name = event['user_name']
	user_id = event['user_id']
	chat_room_name = event['room_name']
	chat_room_id = event['room_id']
	log('[{} - {}] Got message "{}" from user {}, id={}'.format(chat_room_name, chat_room_id, content, user_name, user_id))
	
	for init in commands:
		if content.find(init)==0: # find if the init is registered
			content_=content[len(init):]
			for cmd_msg in commands[init]:
				if content_.find(cmd_msg)==0: # find if the command is registered
					func, sep=commands[init][cmd_msg]
					content_=content_[len(cmd_msg)+len(sep):]
					args=content_.split(sep)
					if args==['']: args=[]
					try:
						func(room, event, *args)
					except Exception as e:
						log("An error occured while launching function {} with args {} : {}".format(cmd_msg, args, e))
				
			

chatbot.joinRoom(1,handleEvents) # Sandbox
chatbot.joinRoom(3229,handleEvents) # The Periodic Table












































