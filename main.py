# -*- coding: utf-8 -*-
# Imports and initialization
import requests, codecs, time, random, shutil, urllib, json, getpass, thread
import numpy as np
from PIL import Image
from imgurpython import ImgurClient  # Communicate with Imgur

# os.chdir("C:/Users/Hippa/PycharmProjects/CSE_chatbot")  # Change to script's directory. Will store images and logs here.

client_id = 'fb1b922cb86bb0f'  # Imgur module setup
client_secret = 'cffaf5da440289a8923f9be60c22b26e25675d3d'
clientImg = ImgurClient(client_id, client_secret)

email = getpass.getpass("Email ? ")  # SE email and username. Don't leave them as plain text.
password = getpass.getpass("Password ? ")

session = requests.Session()  # main session for POST/GET requests

Todo = """

"""

# Variables
globalVars = {
    "roomsJoined": {},  # List of rooms joined : {roomId1:timestamp1,roomId2:timestamp2}
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
    "untablesList": ["┬─┬ ノ( ^_^ノ)", "┬──┬◡ﾉ(° -°ﾉ)", "┬━┬ ノ( ゜¸゜ノ)", "┬━┬ ノ( ゜-゜ノ)", "┳━┳ ヽ༼ಠل͜ಠ༽ﾉ", "┬──┬ ¯\\\_(ツ)",
                     "┬──┬ ノ( ゜-゜ノ)", "(ヘ･_･)ヘ┳━┳", "┻o(Ｔ＿Ｔ )ミ( ；＿；)o┯", "┣ﾍ(≧∇≦ﾍ)… (≧∇≦)/┳━┳", "┣ﾍ(^▽^ﾍ)Ξ(ﾟ▽ﾟ*)ﾉ┳━┳",
                     ],
    "iceCreamList": ["http://www.daytonaradio.com/wkro/wp-content/uploads/sites/4/2015/07/ice-cream.jpg"],
    "sushiCreamList": ["http://www.shopbelmontmarket.com/wp-content/uploads/page_img_sushi_01.jpg",
                       "http://www.jim.fr/e-docs/00/02/66/5C/carac_photo_1.jpg",
                       "http://www.harusushi.com/images/gallery/hires/Sushi-and-Sashimi-for-Two_1024.jpg"],
    "gunsList": ["(҂‾ ▵‾)︻デ═一 (˚▽˚’!)/", "̿’ ̿’\\\̵͇̿̿\\\з=(ಥДಥ)=ε/̵͇̿̿/’̿’̿", "( う-´)づ︻╦̵̵̿╤── \\\(˚☐˚”)/",
                 "(⌐■_■)–︻╦╤─",
                 "̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽	", "━╤デ╦︻(▀̿̿Ĺ̯̿̿▀̿ ̿)", "╾━╤デ╦︻	▄︻̷̿┻̿═━一", "︻╦̵̵͇̿̿̿̿══╤─",
                 "༼ ಠل͟ಠ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ຈل͜ຈ༽ﾉ", "̿’ ̿’\\\̵͇̿̿\\\з=(ಡل͟ಡ)=ε/̵͇̿̿/’̿’̿", "￢o(￣-￣ﾒ)", "(҂`з´).っ︻デ═一",
                 "ᕕ╏ ͡ᵔ ‸ ͡ᵔ ╏و︻̷┻̿═━一", "⌐╦╦═─", "(ﾟ皿ﾟ)ｒ┏┳－－－＊", "・-/(。□。;/)—-┳┓y(-_・ )", "(ﾒ▼▼)┏)ﾟoﾟ)",
                 "[ﾉಠೃಠ]︻̷┻̿═━一", "……┳┓o(▼▼ｷ)", "(ｷ▼▼)o┏┳……", "(ﾒ▼皿▼)┳*–", "̿̿’̿’\\\̵͇̿̿\\\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿",
                 "】ﾟДﾟ)┳—-ﾟ~:;’:;ω*:;’;—-", "ξ(✿ ❛‿❛)ξ▄︻┻┳═一	", "⁞ つ: •̀ ⌂ •́ : ⁞-︻╦̵̵͇̿̿̿̿══╤─",
                 "╾━╤デ╦︻ԅ། ･ิ _ʖ ･ิ །ง", "……┳┓o(-｀Д´-ﾒ )", "┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ └། ๑ _ ๑ །┘", "(‥)←￢~(▼▼#)~~",
                 "(ง⌐□ل͜□)︻̷┻̿═━一", "‘̿’\\\̵͇̿̿\\\=( `◟ 、)=/̵͇̿̿/’̿̿ ̿", "༼ ºل͟º ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ ▀̿Ĺ̯▀̿ ̿ ༽",
                 "(キ▼▼)＿┏┳……",
                 "( ͝ಠ ʖ ಠ)=ε/̵͇̿̿/’̿’̿ ̿", "ლ(~•̀︿•́~)つ︻̷┻̿═━一", "(ง ͠° / ^ \\\ °)-/̵͇̿̿/’̿’̿ ̿",
                 "(‘ºل͟º)ノ⌒. ̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽", "(▀̿̿Ĺ̯̿̿▀̿ ̿)•︻̷̿┻̿┻═━━ヽ༼ຈ益ຈ༽ﾉ",
                 "ー═┻┳︻▄ξ(✿ ❛‿❛)ξ▄︻┻┳═一", "ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸", "( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃",
                 "!! ( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃", "!!(★▼▼)o┳*—————–●));´ﾛ`))", "!! ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸",
                 "ヽ༼ຈ益ຈ༽_•︻̷̿┻̿═━一|<——— ҉ Ĺ̯̿̿▀̿ ̿)",
                 "ヽ༼xل͜x༽ﾉ <===== ̿’ ̿’\\\̵͇̿̿\\\з༼ຈل͜ຈ༽ ε/̵͇̿̿/’̿’̿ =====> ヽ༼xل͜x༽ﾉ",
                 "ლ[☉︿۝)७)७︻̷┻̿═━一︻̷┻̿═━一", "( φ_<)r┬ ━━━━━━…=>"],
    "owners": ["113953", "135450", "24986", "117922"]
}


def sendRandom(L):
    t = list(L)
    random.shuffle(t)
    return t[0]


def setGlobalVars(field, value):
    global globalsVars
    globalVars[field] = value


# Utility
def logFile(r,
            name="logFile.html"):  # logs the string in the file <name>. Will overwrite previous data. Will be improved later on.
    with codecs.open(name, "w", encoding="utf-8") as f:
        f.write(str(r))


def log(r, name="log.txt", verbose=True):  # Appends <r> to the log <name> and prints it.
    r = str(r)
    with codecs.open(name, "a", encoding="utf-8") as f:
        timeStr = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        f.write(timeStr + ' ' + r + '\n')
        if verbose: print('<Log> ' + r)


def error(msg="", logFileStr=""):  # Prints the error *and breaks the script !!* Will be improved later on.
    log('ERROR : ' + msg)
    if logFileStr != "":
        logFile(logFileStr)
    breakErrorHere()


def sendRequest(url, typeR="get", payload={}, headers={}):
    r = ""
    successful, tries = False, 0
    while successful == False:
        try:
            if typeR == "get":
                r = session.get(url, data=payload, headers=headers)
            elif typeR == "post":
                r = session.post(url, data=payload, headers=headers)
            else:
                error("Invalid request type :" + str(typeR))
            successful = True
        except Exception as e:
            time.sleep(1)
            if tries > 4:
                if type(r) != type(""):  # string or request object ?
                    r = r.text
                error("The request failed : " + str(e), r)
            tries += 1
    return r


def getSavedData(name):
    name = "savedData//" + name
    with open(name) as json_file:
        data = json.load(json_file)
    return data


def setSavedData(name, data):
    name = "savedData/" + name
    with open(name, 'w') as outfile:
        json.dump(data, outfile)

def removeUselessSpace(path):
    image=Image.open(path)
    image.load()

    imageBox = image.getbbox()
    cropped=image.crop(imageBox)
    cropped.save('cropped_'+path)

# Login

def login():
    log("--- NEW LOGIN ---")
    """ logs in to all the necessary channels"""

    def getField(field, url="", r=""):
        """gets the hidden field <field> from string <r> ELSE url <url>"""
        if r == "":
            r = sendRequest(url, 'get').text
            r.encode('utf-8')
        p = r.find('name="' + field)
        if p <= 0:
            error("No field <" + field + "> found", r)
        p = r.find('value="', p) + len('value="')
        key = r[p:r.find('"', p + 1)]
        return key

    # Login to OpenId
    payload = {"email": email, "password": password,
               "fkey": getField("fkey", "https://openid.stackexchange.com/account/login")}
    r = sendRequest("https://openid.stackexchange.com/account/login/submit", "post", payload).text
    if r.find('<a href="/account/logout" >Logout</a>') <= 0:
        error("OpenId login failed", r)
    log("Login to OpenId successful")

    # Login to StackExchange
    payload = {'oauth_version': '', 'oauth_server': '', 'openid_identifier': 'https://openid.stackexchange.com/',
               "fkey": getField("fkey", "https://stackexchange.com/users/login?returnurl%20=%20%2f")}
    r = sendRequest("http://stackexchange.com/users/authenticate", "post", payload).text
    if r.find('<span class="hidden-text">Inbox</span>') <= 0:
        error("StackExchange login failed", r)
    log("Login to StackExchange successful")

    # Login to SE Chat
    sendRequest("http://stackexchange.com/users/chat-login", "post")
    r = sendRequest("http://chat.stackexchange.com/chats/join/favorite", "get").text
    setGlobalVars("masterFkey", getField("fkey", r=r))
    log("Got master fkey : " + globalVars["masterFkey"])
    log("Login to the SE chat successful")


# Chat Functions

def sendMessage(msg, roomId="10121", noDelete=False):  # 10121 : test, 3229 : chemistry
    roomId = str(roomId)
    payload = {"fkey": globalVars["masterFkey"], "text": msg}
    r = sendRequest("http://chat.stackexchange.com/chats/" + roomId + "/messages/new", "post", payload)
    if r.text.find("You can perform this action again") >= 0:
        time.sleep(3)
        sendMessage(msg, roomId)
    else:
        if r.text.find("The message is too long") >= 0:
            log("Message too long : " + msg)
            return
        r = r.json()

        if noDelete: # noDelete actually deletes the message ;_;
            thread.start_new_thread(deleteMessage, (r["id"], roomId, 60*1.7))
        return r["id"]

def editMessage(msg, id, roomId):
    roomId = str(roomId)
    id = str(id)
    payload = {"fkey": globalVars["masterFkey"], "text": msg}
    headers = {'Referer': "http://chat.stackexchange.com/rooms/" + roomId}
    r = sendRequest("http://chat.stackexchange.com/messages/" + id, "post", payload, headers).text
    if r.find("You can perform this action again") >= 0:
        time.sleep(3)
        editMessage(msg, id, roomId)

def deleteMessage(id, roomId, waitTime=0):
    time.sleep(waitTime)
    roomId = str(roomId)
    id = str(id)
    payload = {"fkey": globalVars["masterFkey"]}
    headers = {'Referer': "http://chat.stackexchange.com/rooms/" + roomId}
    r = sendRequest("http://chat.stackexchange.com/messages/" + id + "/delete", "post", payload, headers).text
    if r.find("You can perform this action again") >= 0:
        time.sleep(3)
        deleteMessage(id, roomId)

def joinRooms(roomsDict):
    """
    roomsTable is a dict {str(roomId):activityActionFunction}
    The ActivityActionFunction is triggred every time some activity related to that room is recorded.
    """
    payload = {"fkey": globalVars["masterFkey"], 'since': 0, 'mode': 'Messages', 'msgCount': 100}
    for key in roomsDict.keys():
        roomId = str(key)
        r = sendRequest("http://chat.stackexchange.com/chats/" + roomId + "/events", "post", payload).json()
        t = globalVars["roomsJoined"]
        t[roomId] = {"eventtime": r['time']}

        r = sendRequest("http://chat.stackexchange.com/rooms/info/" + roomId, "post", payload).text  # get room info
        roomName = ""
        try:
            p = r.find("all time messages in ")
            roomName = r[p + len("all time messages in "):r.find('"', p)]
        except Exception:
            log("Failed to scrape metadata for room : " + roomId)
        t[roomId]["roomName"] = roomName
        t[roomId]["usersGreeted"] = []

        setGlobalVars("roomsJoined", t)  # update global table
        log("Joined room : " + roomName + " / id: " + roomId)
    while True:
        for key in globalVars["roomsJoined"]:
            room = globalVars["roomsJoined"][key]
            roomId = key
            lastTime = room["eventtime"]
            payload = {"fkey": globalVars["masterFkey"], 'r' + roomId: lastTime}
            activity = sendRequest("http://chat.stackexchange.com/events", "post", payload).json()
            roomResult = {}
            try:  # update eventtime
                roomResult = activity['r' + roomId]
                eventtime = roomResult['t']
                t = globalVars["roomsJoined"]
                t[roomId]["eventtime"] = eventtime
                setGlobalVars("roomsJoined", t)
            except KeyError as ex:
                pass  # no updated time from room
            activityHandler = roomsDict[key]
            try:
                activityHandler(roomResult)  # send activity to designated function
            except Exception as e:
                log("Error occured while sending event <" + str(roomResult) + "> : " + str(e))
        time.sleep(5)


def handleActivity(activity):
    #log("ping", "activity.txt", verbose=False)
    if "e" in activity:
        for item in activity["e"]:
            if item["user_id"] == 200207:  # bot's user
                continue
            # 1: message, 2: edit, 3: user enters, 4: user leaves
            if item['event_type'] == 1:  # message posted
                handleMessages(item)
            noGreet = getSavedData("noGreet.json")


def handleMessages(message):
    Mcontent = str(message["content"].encode("utf-8"))
    MuserName = str(message['user_name'].encode("utf-8"))
    MchatRoom = str(message['room_name'].encode("utf-8"))
    MroomId = str(message['room_id'])
    noDelete=Mcontent.find('!!!')>=0
    print(MchatRoom + " | " + MuserName + ' : ' + Mcontent)
    Mcontent, McontentCase = Mcontent.lower(), Mcontent
    if Mcontent.find('!!img/') >= 0:
        id = sendMessage("Hold tight, I'm processing your request ... " + sendRandom(globalVars["tablesList"]), MroomId, noDelete=noDelete)
        molec = McontentCase[Mcontent.find('img/') + len('img/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '').replace('&#39;', "'")
        reqUrl = "http://cactus.nci.nih.gov/chemical/structure/" + molec + "/image"
        print(reqUrl)
        # print(molec, reqUrl)
        molecImg = session.get(reqUrl, stream=True)
        with open('mol.gif', 'wb') as out_file:
            shutil.copyfileobj(molecImg.raw, out_file)
        try:
            Image.open('mol.gif').save('mol.png')
        except Exception as e:
            editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        del molecImg
        removeUselessSpace('mol.png')
        ans = ""
        try:
            ans = clientImg.upload_from_path('cropped_mol.png')
        except Exception as e:
            editMessage("<An error occured : " + str(e) + ". Check your molecule's name.>", id, MroomId)
            return
        url = ans['link']
        editMessage(url, id, MroomId)
    if Mcontent.find('!!wiki/') >= 0:
        article = McontentCase[Mcontent.find('wiki/') + len('wiki/'):].replace(' ', '_').replace('</div>',
                                                                                                 '').replace('\n', '')
        id = sendMessage("https://en.wikipedia.org/wiki/" + article, MroomId, noDelete=noDelete)
    if Mcontent.find('!!table') >= 0:
        #
        sendMessage(sendRandom(globalVars["tablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!untable') >= 0:
        #
        sendMessage(sendRandom(globalVars["untablesList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!gun') >= 0:
        #
        sendMessage(sendRandom(globalVars["gunsList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!beer') >= 0:
        #
        sendMessage("http://www.mandevillebeergarden.com/wp-content/uploads/2015/02/Beer-Slide-Background.jpg", MroomId, noDelete=noDelete)
    if Mcontent.find('!!spam') >= 0:
        #
        sendMessage("https://upload.wikimedia.org/wikipedia/commons/0/09/Spam_can.png", MroomId,
                    noDelete=noDelete)
    if Mcontent.find('!!coffee') >= 0:
        #
        sendMessage("http://res.freestockphotos.biz/pictures/10/10641-a-cup-of-coffee-on-a-bean-background-pv.jpg",
                    MroomId)
    if Mcontent.find('!!sushi') >= 0:
        #
        sendMessage(sendRandom(globalVars["sushiCreamList"]), MroomId, noDelete=noDelete)
    if Mcontent.find('!!ice cream') >= 0:
        #
        sendMessage(sendRandom(globalVars["iceCreamList"]), MroomId, noDelete=noDelete)
    if False and Mcontent.find('!!changelog') >= 0:
        changelog = """3/22/16 - Created the bot.
        3/23/16 - Added the <help> command - the bot now edits its message to save space - the bot now welcomes entering users
        3/24/16 - Added the <changelog> command - updated <help> - refactored the whole code, rewrote the bot from scratch - moved host to Cloud9 - added support for multiple chatrooms at once - added the <wiki> command
        3/25/16 - Added the <doi> command - bot no longer greets users if it has seen them earlier - added the <scholar> command
        3/26/16 - Bot no longer pings people when they enter.
        """
        sendMessage(changelog, MroomId, noDelete=noDelete)
    if Mcontent.find('!!test') >= 0:
        id = sendMessage("a test", MroomId, noDelete=noDelete)
        time.sleep(1)
        editMessage("edited", id, MroomId)
    if Mcontent.find('!!help') >= 0:
        helpString = """Hi! I'm the (for now) unofficial bot of ChemistrySE's main chatroom. __If you find me annoying, you can ignore me by clicking on my profile image and chosing "ignore this user"__
            Here are the useful commands I provide : (don't add the brackets)
            * img/[molecule's name] -> I will try and upload an image corresponding to your molecule. You can give its name, formula, SMILES, or any common identifier. When using complex InChI, use img/InChI=1/[molecule's InChI]
            * help -> displays this message
            * wiki/[article] -> returns a link to wikiedia's page n <article> if I can find it
            * doi/[DOI] -> gives metadata on the requested DOI
            * scholar/[requests] -> executes the request on Google Scholar
            ~ Syntax : !!!commandName/[arguments] for temporary messages, !!commandName/[arguments] for permanent ones ~
            I also greet new users, and have a few more less useful commands for fun.
            Example : !!img/3-(carboxymethyl)-12-ethyl-8,13,17-trimethyl- 21H,23H-porphine-2,7,18-tripropanoic acid
            """
        sendMessage(helpString, MroomId, noDelete=noDelete)
    if Mcontent.find('!!doi/') >= 0:
        doi = McontentCase[Mcontent.find('doi/') + len('doi/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '')
        r = sendRequest("http://pubs.acs.org/doi/abs/" + doi).text
        if r.find('Your request resulted in an error') > 0:
            sendMessage("Could not find the requested DOI : " + doi, MroomId, noDelete=noDelete)
        else:
            try:
                p = r.find('dc.Title" content="') + len('dc.Title" content="')
                title = r[p:r.find('" />', p)]

                p = r.find('dc.Creator" content="') + len('dc.Creator" content="')
                author1 = r[p:r.find('" />', p)]

                sendMessage("DOI " + doi + ' :\n"' + title + '"\nFirst author : ' + author1, MroomId, noDelete=noDelete)
            except Exception as e:
                sendMessage("An error occured :" + str(e), MroomId, noDelete=noDelete)
    if Mcontent.find('!!scholar/') >= 0:
        search = McontentCase[Mcontent.find('scholar/') + len('scholar/'):].replace(' ', '%20').replace('</div>',
                                                                                                        '').replace(
            '\n', '')
        reqUrl = 'http://scholar.google.fr/scholar?hl=en&q=' + urllib.quote(search.replace(" ", "+")).replace("%2520",
                                                                                                              "+")
        r = sendRequest(reqUrl,
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
        sendMessage(fullMsg, MroomId, noDelete=noDelete)
    w = """if Mcontent.find('!!nogreet') >= 0:
        noGreet=getSavedData("noGreet.json")
        if not str(message['user_id']) in noGreet:
            noGreet[message['user_id']] = MuserName
            setSavedData("noGreet.json",noGreet)
            sendMessage(MuserName + " was added to the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was added to the noGreet list.")
        else:
            sendMessage("You are already in the noGreet list.", MroomId, noDelete=noDelete)
    if Mcontent.find('!!greet') >= 0:
        noGreet = getSavedData("noGreet.json")
        if str(message['user_id']) in noGreet:
            noGreet.pop(str(message['user_id']))
            setSavedData("noGreet.json", noGreet)
            sendMessage(MuserName + " was removed from the noGreet list.", MroomId, noDelete=noDelete)
            log(MuserName + " was removed from the noGreet list.")
        else:
            sendMessage("You are not in the noGreet list.", MroomId, noDelete=noDelete)
    """
    if Mcontent.find('!!greet') >= 0:
        user = McontentCase[Mcontent.find('greet/') + len('greet/'):].replace(' ', '%20').replace('</div>', '').replace(
            '\n', '')
        id = 0
        try:
            id = int(user)
        except Exception:
            pass
        uName = user
        if id != None and id > 0:
            r = sendRequest("http://chat.stackexchange.com/users/" + user).text
            p = r.find("<title>User ") + len("<title>User ")
            uName = r[p:r.find(" |", p)]
        sendMessage(
            "Welcome to The Periodic Table " + uName + "! [Here](http://meta.chemistry.stackexchange.com/q/2723/7448) are our chat guidelines and it's recommended that you read them. If you want to turn Mathjax on, make a bookmark of [the link in this answer](http://meta.chemistry.stackexchange.com/a/1668/7448). Happy chatting!",
            MroomId)
    if Mcontent.find('!!sleep') >= 0:
        if str(message['user_id']) in globalVars["owners"]:
            timeSleep = McontentCase[Mcontent.find('sleep/') + len('sleep/'):].replace(' ', '%20').replace('</div>',
                                                                                                           '').replace(
                '\n', '')
            try:
                timeSleep = float(timeSleep) * 60
                sendMessage("See you in " + str(timeSleep / 60.) + " minutes !", MroomId, noDelete=noDelete)
                time.sleep(timeSleep)
            except Exception:
                sendMessage("invalid time", MroomId, noDelete=noDelete)


# Main Loop
login()
joinRooms({"25323": handleActivity, "3229": handleActivity, "26060": handleActivity, "38172": handleActivity})  # 10121 : test, 3229 : chemistry, 26060 : g-block, 38172 : chemobot
