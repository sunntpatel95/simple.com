import telebot
from PIL import Image, ImageDraw, ImageFont
import random
import sys
import os

allowed_users = [928040182,]

def is_allowed(user_id):
    return user_id in allowed_users


Tokan = "7408137663:AAFij-0o6kvr3RlvXY3Ai3nmzZs9-G6iivE"
Api = "sk-JEi4Yh-nfIp0C4gEiJnC1U2siyMyaCWH80BrlNOWlfT3BlbkFJuqn7NSSp-eTbBHOmuev5rtG_v72DR9g0H1JnFnB3kA"


print("Bot Started . . . !")
bot = telebot.TeleBot(Tokan)

@bot.message_handler(['start'])
def start(message): 
    bot.reply_to(message,"""
\nᴡᴇʟᴄᴏᴍᴇ ʙᴜᴅᴅʏ 😃

ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ? 
» ɪ ʜᴏᴘᴇ ʏᴏᴜ ᴀʀᴇ ꜰɪɴᴇ

ᴀᴅᴅ ᴍᴇ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 
ᴀɴᴅ ᴇɴᴊᴏʏ . . . 😗😉
                 
/command - all commands
    """)

@bot.message_handler(['botowner'])
def owner(message):
    bot.reply_to(message,"""
          \n𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓑𝔂 >>  @IntRoO_x  

    """)

@bot.message_handler(['command'])
def command(message):
    bot.reply_to(message,"""
           ᴄᴏᴍᴍᴀɴᴅꜱ
                 
/start - start
/help  - help
/command - all commands
/botowner - bot owner
/txt - text convert into sticter page 
         e.x >> /txt Hello WOrld !`
/pfp - send a random pics for pfp
/join - join any group
/couple - make custome couple using user id
/funnytag - with username to funny comment

    """)
@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"Help -> @EmOvRtTtzZ")


@bot.message_handler(['join'])
def join(message):
    bot.reply_to(message,"""
   \n 𝓳𝓸𝓲𝓷 𝓖𝓻𝓸𝓾𝓹
                 \nhttps://t.me/+HfNpHLYnVopiM2Nl
                 \n

    """)


@bot.message_handler(['txt'])
def txt(message):
    if is_allowed(message.from_user.id):
        try:
            # Get user input
            text = message.text.replace('/txt ', '')

            # Set image dimensions
            width, height = 512, 500

            # Create a new image
            #img = Image.new('RGB', (width, height), color=(255, 255, 255, 0))
            img = Image.new('RGBA', (512, 512), (255, 255, 255, 0))            
            # Set font
            font = ImageFont.truetype('arial.ttf', 40)

            # Initialize text position
            x, y = 10, 10

            # Split text into lines
            lines = []
            for i in range(0, len(text), 14):
                lines.append(text[i:i+14])

            # Draw text
            for line in lines:
                d = ImageDraw.Draw(img)
                d.text((x, y), line, font=font, fill=(255, 0, 0))
                y += 100  # Move to next line

            # Save image
            img.save('sticker.webp', 'webp')

            # Send sticker
            bot.send_sticker(message.chat.id, open('sticker.webp', 'rb'))
        except Exception as e:
            bot.reply_to(message, str(e))
    else:
        bot.reply_to(message, "You are not allowed to use this command, contact authontication support ")



@bot.message_handler(['funnytag'])
def funnytag(message):
    if is_allowed(message.from_user.id):
        try:
            # Get user input
            args = message.text.split()
            username = args[1].replace('@', '')
            text = ' '.join(args[2:])

            # Generate a funny comment about the tagged user
            funny_comment = get_funny_comment(username)

            # Send the message with the funny comment
            bot.send_message(message.chat.id, f"{funny_comment} {text} 😊")
        except Exception as e:
            bot.reply_to(message, str(e))
    else:
        bot.reply_to(message, "You are not allowed to use this command, contact authontication support ")

def get_funny_comment(username):
    # Generate a random funny comment about the tagged user
    funny_comments = [
        f"@{username} is you brainless cutie",
        f"@{username} पहले अपनी सकल देख लिया कर 😁😲",
        f"@{username} चल पहली फुरसत में निकल 👉",
        f"@{username} is a Cute Monkey🐵",
        f"@{username} is a idiot!😇",
        f"@{username} इतना स्मार्ट है, वे आंखों पर पट्टी बांधकर रूबिक क्यूब को भी हल कर सकते हैं ... उनके सपनों 😴 में ",
        f"@{username} इतना एथलेटिक है, वे मैराथन दौड़ सकते हैं ... अपने सोफे पर, वीडियो गेम खेलते समय ",
        f"@{username} इतना आलसी है, वे स्लॉथ को ऐसे दिखते हैं जैसे वे स्टेरॉयड 😂 पर हैं ",
        f"@{username} खाना पकाने में इतना बुरा है, वे पानी जला सकते हैं ... और फिर चूल्हे 🍳 को दोष देते हैं ",
        f"@{username} इतना अनाड़ी है, वे हवा पर यात्रा कर सकते हैं ... और फिर फर्श 😂 को दोष दें ",
        f"@{username} निंजा की तरह डरपोक है, लेकिन केवल जब पिज्जा 🍕 का आखिरी टुकड़ा खाने की बात आती है ",
        f"@{username} द फ्लैश जितना तेज़ है, लेकिन केवल जब जिम्मेदारियों 💨 से भागने की बात आती है ",
        f"@{username} हल्क की तरह मजबूत है, लेकिन केवल जब उनके मुंह 🍴 में कांटा उठाने की बात आती है ",
        f"@{username} बहाने बनाने में पीएचडी है, वे कुछ भी 🎓 नहीं करने का एक कारण के साथ आ सकते हैं ",
        f"@{username} के पास एक महाशक्ति है, वे कहीं भी, कभी भी सो सकते हैं ... यहां तक कि एक बैठक 😴 में ",
    ]
    return random.choice(funny_comments)








@bot.message_handler(['pfp'])
def pfp(message):
    bot.send_photo(message.chat.id, random.choice(PFP))



PFP = [
    "https://t.me/unique_piczz/458",
    "https://t.me/unique_piczz/460",
    "https://t.me/unique_piczz/459",
    "https://t.me/unique_piczz/457",
    "https://t.me/unique_piczz/456"
    "https://t.me/unique_piczz/455",
    "https://t.me/unique_piczz/454",
    "https://t.me/unique_piczz/453",
    "https://t.me/unique_piczz/452",
    "https://t.me/unique_piczz/451",
    "https://t.me/unique_piczz/450",
    "https://t.me/unique_piczz/449",
    "https://t.me/unique_piczz/448",
    "https://t.me/unique_piczz/447",
    "https://t.me/unique_piczz/446",
    "https://t.me/unique_piczz/4",
"https://t.me/unique_piczz/5",
"https://t.me/unique_piczz/6",
"https://t.me/unique_piczz/7",
"https://t.me/unique_piczz/8",
"https://t.me/unique_piczz/9",
"https://t.me/unique_piczz/10",
"https://t.me/unique_piczz/11",
"https://t.me/unique_piczz/12",
"https://t.me/unique_piczz/13",
"https://t.me/unique_piczz/14",
"https://t.me/unique_piczz/15",
"https://t.me/unique_piczz/16",
"https://t.me/unique_piczz/17",
"https://t.me/unique_piczz/18",
"https://t.me/unique_piczz/19",
"https://t.me/unique_piczz/20",
"https://t.me/unique_piczz/21",
"https://t.me/unique_piczz/22",
"https://t.me/unique_piczz/23",
"https://t.me/unique_piczz/24",
"https://t.me/unique_piczz/25",
"https://t.me/unique_piczz/26",
"https://t.me/unique_piczz/27",
"https://t.me/unique_piczz/28",
"https://t.me/unique_piczz/29",
"https://t.me/unique_piczz/30",
"https://t.me/unique_piczz/31",
"https://t.me/unique_piczz/32",
"https://t.me/unique_piczz/33",
"https://t.me/unique_piczz/34",
"https://t.me/unique_piczz/35",
"https://t.me/unique_piczz/36",
"https://t.me/unique_piczz/37",
"https://t.me/unique_piczz/38",
"https://t.me/unique_piczz/39",
"https://t.me/unique_piczz/40",
"https://t.me/unique_piczz/41",
"https://t.me/unique_piczz/42",
"https://t.me/unique_piczz/43",
"https://t.me/unique_piczz/44",
"https://t.me/unique_piczz/45",
"https://t.me/unique_piczz/46",
"https://t.me/unique_piczz/47",
"https://t.me/unique_piczz/48",
"https://t.me/unique_piczz/49",
"https://t.me/unique_piczz/50",
"https://t.me/unique_piczz/51",
"https://t.me/unique_piczz/52",
"https://t.me/unique_piczz/53",
"https://t.me/unique_piczz/54",
"https://t.me/unique_piczz/55",
"https://t.me/unique_piczz/56",
"https://t.me/unique_piczz/57",
"https://t.me/unique_piczz/58",
"https://t.me/unique_piczz/59",
"https://t.me/unique_piczz/60",
"https://t.me/unique_piczz/61",
"https://t.me/unique_piczz/62",
"https://t.me/unique_piczz/63",
"https://t.me/unique_piczz/64",
"https://t.me/unique_piczz/65",
"https://t.me/unique_piczz/66",
"https://t.me/unique_piczz/67",
"https://t.me/unique_piczz/68",
"https://t.me/unique_piczz/69",
"https://t.me/unique_piczz/70",
"https://t.me/unique_piczz/71",
"https://t.me/unique_piczz/72",
"https://t.me/unique_piczz/73",
"https://t.me/unique_piczz/74",
"https://t.me/unique_piczz/75",
"https://t.me/unique_piczz/76",
"https://t.me/unique_piczz/77",
"https://t.me/unique_piczz/78",
"https://t.me/unique_piczz/79",
"https://t.me/unique_piczz/80",
"https://t.me/unique_piczz/81",
"https://t.me/unique_piczz/82",
"https://t.me/unique_piczz/83",
"https://t.me/unique_piczz/84",
"https://t.me/unique_piczz/85",
"https://t.me/unique_piczz/86",
"https://t.me/unique_piczz/87",
"https://t.me/unique_piczz/88",
"https://t.me/unique_piczz/89",
"https://t.me/unique_piczz/90",
"https://t.me/unique_piczz/91",
"https://t.me/unique_piczz/92",
"https://t.me/unique_piczz/93",
"https://t.me/unique_piczz/94",
"https://t.me/unique_piczz/95",
"https://t.me/unique_piczz/96",
"https://t.me/unique_piczz/97",
"https://t.me/unique_piczz/98",
"https://t.me/unique_piczz/99",
"https://t.me/unique_piczz/100",
"https://t.me/unique_piczz/101",
"https://t.me/unique_piczz/102",
"https://t.me/unique_piczz/103",
"https://t.me/unique_piczz/104",
"https://t.me/unique_piczz/105",
"https://t.me/unique_piczz/106",
"https://t.me/unique_piczz/107",
"https://t.me/unique_piczz/108",
"https://t.me/unique_piczz/109",
"https://t.me/unique_piczz/110",
"https://t.me/unique_piczz/111",
"https://t.me/unique_piczz/112",
"https://t.me/unique_piczz/113",
"https://t.me/unique_piczz/114",
"https://t.me/unique_piczz/115",
"https://t.me/unique_piczz/116",
"https://t.me/unique_piczz/117",
"https://t.me/unique_piczz/118",
"https://t.me/unique_piczz/119",
"https://t.me/unique_piczz/120",
"https://t.me/unique_piczz/121",
"https://t.me/unique_piczz/122",
"https://t.me/unique_piczz/123",
"https://t.me/unique_piczz/124",
"https://t.me/unique_piczz/125",
"https://t.me/unique_piczz/126",
"https://t.me/unique_piczz/127",
"https://t.me/unique_piczz/128",
"https://t.me/unique_piczz/129",
"https://t.me/unique_piczz/130",
"https://t.me/unique_piczz/131",
"https://t.me/unique_piczz/132",
"https://t.me/unique_piczz/133",
"https://t.me/unique_piczz/134",
"https://t.me/unique_piczz/135",
"https://t.me/unique_piczz/136",
"https://t.me/unique_piczz/137",
"https://t.me/unique_piczz/138",
"https://t.me/unique_piczz/139",
"https://t.me/unique_piczz/140",
"https://t.me/unique_piczz/141",
"https://t.me/unique_piczz/142",
"https://t.me/unique_piczz/143",
"https://t.me/unique_piczz/144",
"https://t.me/unique_piczz/145",
"https://t.me/unique_piczz/146",
"https://t.me/unique_piczz/147",
"https://t.me/unique_piczz/148",
"https://t.me/unique_piczz/149",
"https://t.me/unique_piczz/150",
"https://t.me/unique_piczz/151",
"https://t.me/unique_piczz/152",
"https://t.me/unique_piczz/153",
"https://t.me/unique_piczz/154",
"https://t.me/unique_piczz/155",
"https://t.me/unique_piczz/156",
"https://t.me/unique_piczz/157",
"https://t.me/unique_piczz/158",
"https://t.me/unique_piczz/159",
"https://t.me/unique_piczz/160",
"https://t.me/unique_piczz/161",
"https://t.me/unique_piczz/162",
"https://t.me/unique_piczz/163",
"https://t.me/unique_piczz/164",
"https://t.me/unique_piczz/165",
"https://t.me/unique_piczz/166",
"https://t.me/unique_piczz/167",
"https://t.me/unique_piczz/168",
"https://t.me/unique_piczz/169",
"https://t.me/unique_piczz/170",
"https://t.me/unique_piczz/171",
"https://t.me/unique_piczz/172",
"https://t.me/unique_piczz/173",
"https://t.me/unique_piczz/174",
"https://t.me/unique_piczz/175",
"https://t.me/unique_piczz/176",
"https://t.me/unique_piczz/177",
"https://t.me/unique_piczz/178",
"https://t.me/unique_piczz/179",
"https://t.me/unique_piczz/180",
"https://t.me/unique_piczz/181",
"https://t.me/unique_piczz/182",
"https://t.me/unique_piczz/183",
"https://t.me/unique_piczz/184",
"https://t.me/unique_piczz/185",
"https://t.me/unique_piczz/186",
"https://t.me/unique_piczz/187",
"https://t.me/unique_piczz/188",
"https://t.me/unique_piczz/189",
"https://t.me/unique_piczz/190",
"https://t.me/unique_piczz/191",
"https://t.me/unique_piczz/192",
"https://t.me/unique_piczz/193",
"https://t.me/unique_piczz/194",
"https://t.me/unique_piczz/195",
"https://t.me/unique_piczz/196",
"https://t.me/unique_piczz/197",
"https://t.me/unique_piczz/198",
"https://t.me/unique_piczz/199",
"https://t.me/unique_piczz/200",
"https://t.me/unique_piczz/201",
"https://t.me/unique_piczz/202",
"https://t.me/unique_piczz/203",
"https://t.me/unique_piczz/204",
"https://t.me/unique_piczz/205",
"https://t.me/unique_piczz/206",
"https://t.me/unique_piczz/207",
"https://t.me/unique_piczz/208",
"https://t.me/unique_piczz/209",
"https://t.me/unique_piczz/210",
"https://t.me/unique_piczz/211",
"https://t.me/unique_piczz/212",
"https://t.me/unique_piczz/213",
"https://t.me/unique_piczz/214",
"https://t.me/unique_piczz/215",
"https://t.me/unique_piczz/216",
"https://t.me/unique_piczz/217",
"https://t.me/unique_piczz/218",
"https://t.me/unique_piczz/219",
"https://t.me/unique_piczz/220",
"https://t.me/unique_piczz/221",
"https://t.me/unique_piczz/222",
"https://t.me/unique_piczz/223",
"https://t.me/unique_piczz/224",
"https://t.me/unique_piczz/225",
"https://t.me/unique_piczz/226",
"https://t.me/unique_piczz/227",
"https://t.me/unique_piczz/228",
"https://t.me/unique_piczz/229",
"https://t.me/unique_piczz/230",
"https://t.me/unique_piczz/231",
"https://t.me/unique_piczz/232",
"https://t.me/unique_piczz/233",
"https://t.me/unique_piczz/234",
"https://t.me/unique_piczz/235",
"https://t.me/unique_piczz/236",
"https://t.me/unique_piczz/237",
"https://t.me/unique_piczz/238",
"https://t.me/unique_piczz/239",
"https://t.me/unique_piczz/240",
"https://t.me/unique_piczz/241",
"https://t.me/unique_piczz/242",
"https://t.me/unique_piczz/243",
"https://t.me/unique_piczz/244",
"https://t.me/unique_piczz/245",
"https://t.me/unique_piczz/246",
"https://t.me/unique_piczz/247",
"https://t.me/unique_piczz/248",
"https://t.me/unique_piczz/249",
"https://t.me/unique_piczz/250",
"https://t.me/unique_piczz/251",
"https://t.me/unique_piczz/252",
"https://t.me/unique_piczz/253",
"https://t.me/unique_piczz/254",
"https://t.me/unique_piczz/255",
"https://t.me/unique_piczz/256",
"https://t.me/unique_piczz/257",
"https://t.me/unique_piczz/258",
"https://t.me/unique_piczz/259",
"https://t.me/unique_piczz/260",
"https://t.me/unique_piczz/261",
"https://t.me/unique_piczz/262",
"https://t.me/unique_piczz/263",
"https://t.me/unique_piczz/264",
"https://t.me/unique_piczz/265",
"https://t.me/unique_piczz/266",
"https://t.me/unique_piczz/267",
"https://t.me/unique_piczz/268",
"https://t.me/unique_piczz/269",
"https://t.me/unique_piczz/270",
"https://t.me/unique_piczz/271",
"https://t.me/unique_piczz/272",
"https://t.me/unique_piczz/273",
"https://t.me/unique_piczz/274",
"https://t.me/unique_piczz/275",
"https://t.me/unique_piczz/276",
"https://t.me/unique_piczz/277",
"https://t.me/unique_piczz/278",
"https://t.me/unique_piczz/279",
"https://t.me/unique_piczz/280",
"https://t.me/unique_piczz/281",
"https://t.me/unique_piczz/282",
"https://t.me/unique_piczz/283",
"https://t.me/unique_piczz/284",
"https://t.me/unique_piczz/285",
"https://t.me/unique_piczz/286",
"https://t.me/unique_piczz/287",
"https://t.me/unique_piczz/288",
"https://t.me/unique_piczz/289",
"https://t.me/unique_piczz/290",
"https://t.me/unique_piczz/291",
"https://t.me/unique_piczz/292",
"https://t.me/unique_piczz/293",
"https://t.me/unique_piczz/294",
"https://t.me/unique_piczz/295",
"https://t.me/unique_piczz/296",
"https://t.me/unique_piczz/297",
"https://t.me/unique_piczz/298",
"https://t.me/unique_piczz/299",
"https://t.me/unique_piczz/300",
"https://t.me/unique_piczz/301",
"https://t.me/unique_piczz/302",
"https://t.me/unique_piczz/303",
"https://t.me/unique_piczz/304",
"https://t.me/unique_piczz/305",
"https://t.me/unique_piczz/306",
"https://t.me/unique_piczz/307",
"https://t.me/unique_piczz/308",
"https://t.me/unique_piczz/309",
"https://t.me/unique_piczz/310",
"https://t.me/unique_piczz/311",
"https://t.me/unique_piczz/312",
"https://t.me/unique_piczz/313",
"https://t.me/unique_piczz/314",
"https://t.me/unique_piczz/315",
"https://t.me/unique_piczz/316",
"https://t.me/unique_piczz/317",
"https://t.me/unique_piczz/318",
"https://t.me/unique_piczz/319",
"https://t.me/unique_piczz/320",
"https://t.me/unique_piczz/321",
"https://t.me/unique_piczz/322",
"https://t.me/unique_piczz/323",
"https://t.me/unique_piczz/324",
"https://t.me/unique_piczz/325",
"https://t.me/unique_piczz/326",
"https://t.me/unique_piczz/327",
"https://t.me/unique_piczz/328",
"https://t.me/unique_piczz/329",
"https://t.me/unique_piczz/330",
"https://t.me/unique_piczz/331",
"https://t.me/unique_piczz/332",
"https://t.me/unique_piczz/333",
"https://t.me/unique_piczz/334",
"https://t.me/unique_piczz/335",
"https://t.me/unique_piczz/336",
"https://t.me/unique_piczz/337",
"https://t.me/unique_piczz/338",
"https://t.me/unique_piczz/339",
"https://t.me/unique_piczz/340",
"https://t.me/unique_piczz/341",
"https://t.me/unique_piczz/342",
"https://t.me/unique_piczz/343",
"https://t.me/unique_piczz/344",
"https://t.me/unique_piczz/345",
"https://t.me/unique_piczz/346",
"https://t.me/unique_piczz/347",
"https://t.me/unique_piczz/348",
"https://t.me/unique_piczz/349",
"https://t.me/unique_piczz/350",
"https://t.me/unique_piczz/351",
"https://t.me/unique_piczz/352",
"https://t.me/unique_piczz/353",
"https://t.me/unique_piczz/354",
"https://t.me/unique_piczz/355",
"https://t.me/unique_piczz/356",
"https://t.me/unique_piczz/357",
"https://t.me/unique_piczz/358",
"https://t.me/unique_piczz/359",
"https://t.me/unique_piczz/360",
"https://t.me/unique_piczz/361",
"https://t.me/unique_piczz/362",
"https://t.me/unique_piczz/363",
"https://t.me/unique_piczz/364",
"https://t.me/unique_piczz/365",
"https://t.me/unique_piczz/366",
"https://t.me/unique_piczz/367",
"https://t.me/unique_piczz/368",
"https://t.me/unique_piczz/369",
"https://t.me/unique_piczz/370",
"https://t.me/unique_piczz/371",
"https://t.me/unique_piczz/372",
"https://t.me/unique_piczz/373",
"https://t.me/unique_piczz/374",
"https://t.me/unique_piczz/375",
"https://t.me/unique_piczz/376",
"https://t.me/unique_piczz/377",
"https://t.me/unique_piczz/378",
"https://t.me/unique_piczz/379",
"https://t.me/unique_piczz/380",
"https://t.me/unique_piczz/381",
"https://t.me/unique_piczz/382",
"https://t.me/unique_piczz/383",
"https://t.me/unique_piczz/384",
"https://t.me/unique_piczz/385",
"https://t.me/unique_piczz/386",
"https://t.me/unique_piczz/387",
"https://t.me/unique_piczz/388",
"https://t.me/unique_piczz/389",
"https://t.me/unique_piczz/390",
"https://t.me/unique_piczz/391",
"https://t.me/unique_piczz/392",
"https://t.me/unique_piczz/393",
"https://t.me/unique_piczz/394",
"https://t.me/unique_piczz/395",
"https://t.me/unique_piczz/396",
"https://t.me/unique_piczz/397",
"https://t.me/unique_piczz/398",
"https://t.me/unique_piczz/399",
"https://t.me/unique_piczz/400",
"https://t.me/unique_piczz/401",
"https://t.me/unique_piczz/402",
"https://t.me/unique_piczz/403",
"https://t.me/unique_piczz/404",
"https://t.me/unique_piczz/405",
"https://t.me/unique_piczz/406",
"https://t.me/unique_piczz/407",
"https://t.me/unique_piczz/408",
"https://t.me/unique_piczz/409",
"https://t.me/unique_piczz/410",
"https://t.me/unique_piczz/411",
"https://t.me/unique_piczz/412",
"https://t.me/unique_piczz/413",
"https://t.me/unique_piczz/414",
"https://t.me/unique_piczz/415",
"https://t.me/unique_piczz/416",
"https://t.me/unique_piczz/417",
"https://t.me/unique_piczz/418",
"https://t.me/unique_piczz/419",
"https://t.me/unique_piczz/420",
"https://t.me/unique_piczz/421",
"https://t.me/unique_piczz/422",
"https://t.me/unique_piczz/423",
"https://t.me/unique_piczz/424",
"https://t.me/unique_piczz/425",
"https://t.me/unique_piczz/426",
"https://t.me/unique_piczz/427",
"https://t.me/unique_piczz/428",
"https://t.me/unique_piczz/429",


]

@bot.message_handler(commands=['couple'])
def couple(message):
 if is_allowed(message.from_user.id):   
    chat_id = message.chat.id
    args = message.text.split()[1:]

    if len(args) % 2 != 0:
        bot.reply_to(message, "Please specify an even number of member user IDs.")
        return

    # List of member user IDs
    members = args

    # Get the names of the members
    member_names = []
    for member in members:
        user = bot.get_chat_member(chat_id, member)
        member_names.append(user.user.first_name)

    # Shuffle the list of members
    random.shuffle(member_names)

    # Pair up the members
    couples = [(member_names[i], member_names[i+1]) for i in range(0, len(member_names), 2)]

    # Create a couple string
    couple_string = "💞Couples of the day 👇\n"
    for couple in couples:
        couple_string += f"{couple[0]}\n 💝 🫶 💌 \n{couple[1]}\n"

    # Send the couple string to the chat
    bot.send_message(chat_id, couple_string)

    # Delete the original command message
    bot.delete_message(chat_id, message.id)
 else:
        bot.reply_to(message, "You are not allowed to use this command, contact authontication support ")


@bot.message_handler(commands=['off'])
def off():
    bot.stop_polling()

bot.polling()

try:
    bot.polling()
except Exception as e:
    print(f"An error occurred: {e}")
    os.execv(__file__, sys.argv)