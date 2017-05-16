# -*- coding: utf-8 -*-
import chatbot, random, shutil, time, urllib, sys, upsidedown, threading
from PIL import Image
from imgurpython import ImgurClient
from html.parser import HTMLParser
HTMLparser = HTMLParser()

client_id = 'fb1b922cb86bb0f'  # Imgur module setup
client_secret = 'cffaf5da440289a8923f9be60c22b26e25675d3d'
#clientImg = ImgurClient(client_id, client_secret)

# Initialization

session = chatbot.login()


# Utility

def removeUselessSpace(name, path=''):
	image = Image.open(path + name)

	image=image.crop(image.getbbox())

	image.save(path + 'cropped_' + name)


#


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
				   "┻━┻ ヘ╰( •̀ε•́ ╰)", "(ノ｀Д´)ノ~┻━┻", "(ﾉ｀△´)ﾉ~┻━┻", "(⑅ノ-_-)ノ~┻━┻	", "(╯ ･ ᗜ ･ )╯︵ ┻━┻  ",
				   "(ノ ﾟДﾟ)ノ　＝＝＝＝　┻━━┻", "!!!!|┛*｀Д´|┛・・~~┻━┻　┳━┳", "(/#-_-)/~┻┻〃", "(/ToT)/ ~┻┻", "（ノ－＿－）ノ･･･~┻┻	",
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
				   "(ノ｀m´)ノ ~┻━┻ (/o＼)", "(ﾉ`Д´)ﾉ.:･┻┻)｀з゜)･:ﾞ;	", "(ノ￣▽￣)ノ┻━┻☆)*￣□)ノ))", "(ノ￣◇￣)ノ~┻━┻/(×。×)",
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
		"http://www.jim.fr/e-docs/00/02/66/5C/carac_photo_1.jpg"],
	"cakeList": [
		"https://s-media-cache-ak0.pinimg.com/736x/d7/e8/29/d7e8295cc27143127d735bdaaa9fa314.jpg",
		"http://cdn001.cakecentral.com/gallery/2015/03/900_804210qttE_chemistry-cake.jpg",
		"https://s-media-cache-ak0.pinimg.com/originals/de/a7/7e/dea77e272ff71bee9925890163bfe82e.jpg",
		],
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
	Mcontent = HTMLparser.unescape(message["content"].replace('<div>', '').replace('</div>', '').replace( #encode("utf-8").
		"<div class='full'>", ''))
	MuserName = message['user_name']
	MchatRoom = message['room_name']
	MroomId = str(message['room_id'])  # int
	noDelete = Mcontent.find('!!!') >= 0
	tempDataPath = MroomId + '//temp//'
	chatbot.log(MuserName + ' : ' + Mcontent, name=MroomId + '//log.txt', verbose=False)
	print(MchatRoom + " | " + MuserName + ' : ' + Mcontent)
	if  Mcontent.find('!!')>0 and random.randint(1, 1000) == 133:
		chatbot.sendMessage(u"__🎺🎺🎺 AND HIS NAME IS JOHN CENA 🎺🎺🎺__", MroomId)
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
		chatbot.sendMessage("http://www.cherryhillgourmet.net/img/Tea/tea2.jpg",
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
	if Mcontent.find('!!cake') >= 0:
		#
		chatbot.sendMessage(random.choice(coolTables["cakeList"]), MroomId, noDelete=noDelete)
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
		art, p = 0, r.find('<h3 class="gs_rt">')
		with open("temp.txt","w") as f:
			f.write(r)
		while p >= 0 and art < numArticles:
			p += len('<h3 class="gs_rt">')
			p=r.find('"',p)
			url = r[p:r.find('"', p)]
			print(url)
			p = r.find('">', p) + len('">')
			title = r[p:r.find('</a>', p)].replace("<b>", "").replace("</b>", "")
			art += 1
			articles.append({"title": title, "url": url})
			p = r.find('<h3 class="gs_rt">', p + 1)
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


chatbot.joinRooms({"1": handleActivity,"1098m": handleActivity})  # 3229 : chemistry, 26060 : g-block, 1: sandbox

chatbot.enableControl("1")
