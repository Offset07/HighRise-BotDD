from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
)
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
)
from asyncio import run as arun
from webserver import keep_alive
import requests
import random
import asyncio
import os
import importlib

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class Bot(BaseBot):
    
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(10., 1., .19, "FrontLeft"))
            await self.highrise.chat("يتم التحميل...")
        except Exception as e:
            print(f"خطأ: {e}")
          

    async def on_user_join(self, user: User) -> None:
        try:
            print(f"{user.username} انضم إلى الغرفة.")
            wm = [
            'مرحبًا بك عزيزي!',
            'مرحبًا بك في الغرفة!',
            'انضم وتحدث أو اضغط على الدعم 🥹',
            'ماذا تريد؟',
            'مرحبًا، من هنا القوة!',
            'مرحبًا بك!',
            ]
            rwm = random.choice(wm)
            await self.highrise.send_whisper(user.id, f"مرحبًا {user.username}\n{rwm}")
            await self.highrise.send_whisper(user.id, f"\n[📢] للأوامر اكتب مساعده")
            face = ["FrontRight","FrontLeft"]
            fp = random.choice(face)
            # قم بتغيير الإحداثيات حسب غرفتك 
            
            __ = random.choice(_)
            await self.highrise.teleport(user.id, __)
        except Exception as e:
            print(f"خطأ: {e}")

  
    async def on_chat(self, user: User, message: str):
        try:
            _bid = "64de1e1136b643cc318000c1" # معرف المستخدم للبوت هنا
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"
            _rid = "63d3ef349e94d65aef81bac0" # معرف الغرفة هنا
            if message.lower().lstrip().startswith(("!invite", "-invite")):
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, "\nاستخدام: !invite <@اسم المستخدم> أو -invite <@اسم المستخدم> هذا الأمر سيقوم بإرسال دعوة الغرفة المستهدفة إلى اسم المستخدم المعني. تحقق مما إذا كنت قد تفاعلت مع البوت في الماضي أم لا.\n • مثال: !invite @rainox")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, f"شكل المستخدم غير صالح. يرجى استخدام '@اسم المستخدم'.")
                    return

                url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
                response = requests.get(url)
                data = response.json()
                users = data['users']
                
                for user in users:
                    user_id = user['user_id']
                    __id = f"1_on_1:{_bid}:{user_id}"
                    __idx = f"1_on_1:{user_id}:{_bid}"
                    __rid = "63d3ef349e94d65aef81bac0" # معرف الغرفة هنا
                    try:
                        await self.highrise.send_message(__id, "انضم إلى الغرفة", "invite", __rid)
                    except:
                        await self.highrise.send_message(__idx, "انضم إلى الغرفة", "invite", __rid)

            if message.lower().lstrip().startswith(("-مساعده", "مساعد")):
                await self.highrise.chat(f"الأوامر المتاحة:\n • !emote أو -emote\n • !invite أو -invite\n • !feedback\n • أوامر لزوجين/أصدقاء\n !punk @اسم المستخدم\n !fight @اسم المستخدم \n !uwu @اسم المستخدم \n مثال: !punk @rainox")


          
            if message.lower().lstrip().startswith("!feedback"):
                try:
                    await self.highrise.send_message(_id, "• [ إرسال ملاحظات ]\nشكرًا لانضمامك إلى الغرفة! نحن نهتم بآرائك. الرجاء مشاركة ملاحظاتك/اقتراحاتك مع @rainox لمساعدتنا على تطوير بيئتنا. مساهماتك مهمة وستساعد في تطويرنا.", "text")
                except:
                    await self.highrise.send_message(_idx, "• [ إرسال ملاحظات ]\nشكرًا لانضمامك إلى الغرفة! نحن نهتم بآرائك. الرجاء مشاركة ملاحظاتك/اقتراحاتك مع @rainox لمساعدتنا على تطوير بيئتنا. مساهماتك مهمة وستساعد في تطويرنا.")
            if message.lower().lstrip().startswith(("-emote", "!emote")):
                await self.highrise.send_whisper(user.id, "\nيمكن استخدام Emote في غرفتنا فقط بكتابة اسم الـ EMOTE فقط. إليك استخدامات Emote:\n\nعاطفي\nمدمن للأزياء\nيستحم\n\nوجميع العبارات الأخرى، يجب على أي شخص في الغرفة فقط أن يذكر اسمها.")
                await self.highrise.send_whisper(user.id, "\n• يرجى ملاحظة أن هذه الأوامر تعمل فقط في غرفة 🏫AŞK OKULU🏫. بسبب القيود، قد لا تعمل بعض العبارات.")

            if message.lstrip().startswith(("!fight", "!uwu", "!punk")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]
        
                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"استخدام: !{parts[0]} <@اسم المستخدم>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, f"شكل المستخدم غير صالح. يرجى استخدام '@اسم المستخدم'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} ليس في الغرفة.")
                    return
        
                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"المستخدم {args[0][1:]} غير موجود")
                    return
        
                try:
                    if message.startswith("!fight"):
                        await self.highrise.chat(f"\n🥷 @{user.username} و@{args[0][1:]} في معركة")
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)
                    elif message.startswith("!uwu"):
                        await self.highrise.chat(f"\n @{user.username} و@{args[0][1:]} جميلان جداً")
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await this.highrise.send_emote("idle-uwu", user_id)
                    elif message.startswith("!punk"):
                        await self.highrise.chat(f"\n مرحبًا @{user.username} و@{args[0][1:]}، هم جميلون")
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)
                except Exception as e:
                    print(f"حدث استثناء [بسبب {parts[0][1:]}]: {e}")

            if message == "kj":
                shirt = ["shirt-n_starteritems2019tankwhite", "shirt-n_starteritems2019tankblack", "shirt-n_starteritems2019raglanwhite", "shirt-n_starteritems2019raglanblack", "shirt-n_starteritems2019pulloverwhite", "shirt-n_starteritems2019pulloverblack", "shirt-n_starteritems2019maletshirtwhite", "shirt-n_starteritems2019maletshirtblack", "shirt-n_starteritems2019femtshirtwhite", "shirt-n_starteritems2019femtshirtblack", "shirt-n_room32019slouchyredtrackjacket", "shirt-n_room32019malepuffyjacketgreen", "shirt-n_room32019longlineteesweatshirtgrey", "shirt-n_room32019jerseywhite", "shirt-n_room32019hoodiered", "shirt-n_room32019femalepuffyjacketgreen", "shirt-n_room32019denimjackethoodie", "shirt-n_room32019croppedspaghettitankblack", "shirt-n_room22109plaidjacket", "shirt-n_room22109denimjacket", "shirt-n_room22019tuckedtstripes", "shirt-n_room22019overalltop", "shirt-n_room22019denimdress", "shirt-n_room22019bratoppink", "shirt-n_room12019sweaterwithbuttondowngrey", "shirt-n_room12019cropsweaterwhite", "shirt-n_room12019cropsweaterblack", "shirt-n_room12019buttondownblack", "shirt-n_philippineday2019filipinotop", "shirt-n_flashysuit", "shirt-n_SCSpring2018flowershirt", "shirt-n_2016fallblacklayeredbomber", "shirt-n_2016fallblackkknottedtee", "shirt-f_skullsweaterblack", "shirt-f_plaidtiedshirtred", "shirt-f_marchingband"]
                pant = ["shorts-f_pantyhoseshortsnavy", "pants-n_starteritems2019mensshortswhite", "pants-n_starteritems2019mensshortsblue", "pants-n_starteritems2019mensshortsblack", "pants-n_starteritems2019cuffedshortswhite", "pants-n_starteritems2019cuffedshortsblue", "pants-n_starteritems2019cuffedshortsblack", "pants-n_starteritems2019cuffedjeanswhite", "pants-n_starteritems2019cuffedjeansblue", "pants-n_starteritems2019cuffedjeansblack", "pants-n_room32019rippedpantswhite", "pants-n_room32019rippedpantsblue", "pants-n_room32019longtrackshortscamo", "pants-n_room32019longshortswithsocksgrey", "pants-n_room32019longshortswithsocksblack", "pants-n_room32019highwasittrackshortsblack", "pants-n_room32019baggytrackpantsred", "pants-n_room32019baggytrackpantsgreycamo", "pants-n_room22019undiespink", "pants-n_room22019undiesblack", "pants-n_room22019techpantscamo", "pants-n_room22019shortcutoffsdenim", "pants-n_room22019longcutoffsdenim", "pants-n_room12019rippedpantsblue", "pants-n_room12019rippedpantsblack", "pants-n_room12019formalslackskhaki", "pants-n_room12019formalslacksblack", "pants-n_room12019blackacidwashjeans", "pants-n_2016fallgreyacidwashjeans"]
                item_top = random.choice(shirt)
                item_bottom = random.choice(pant)
                xox = await self.highrise.set_outfit(outfit=[
                        Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=65),
                        Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),

                        Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='glasses-n_room12019circleframes', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='mouth-basic2018downturnedthinround', account_bound=False, active_palette=0),
                        Item(type='clothing', amount=1, id='hair_front-n_malenew07', account_bound=False, active_palette=1),
                        Item(type='clothing', amount=1, id='hair_back-n_malenew07', account_bound=False, active_palette=1),
                        Item(type='clothing', amount=1, id='bag-n_room12019backpack', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='eye-n_basic2018zanyeyes', account_bound=False, active_palette=-1),
                        Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows09', account_bound=False, active_palette=-1)
                ])
                await self.highrise.chat(f"{xox}")
          
            if message.lower().strip() == "1":
                await self.highrise.send_emote("emote-superpose", user.id)
            elif message.lower().strip() == "2":
                await self.highrise.send_emote("dance-tiktok10", user.id)
            elif message.lower().strip() == "3":
                await self.highrise.send_emote("dance-weird", user.id)
            elif message.lower().strip() == "4":
                await self.highrise.send_emote("emote-sumo", user.id)
            elif message.lower().strip() == "5":
                await self.highrise.send_emote("emote-charging", user.id)
            elif message.lower().strip() == "6":
                await self.highrise.send_emote("emote-ninjarun", user.id)
            elif message.lower().strip() == "7":
                await self.highrise.send_emote("emote-proposing", user.id)
            elif message.lower().strip() == "8":
                await self.highrise.send_emote("emote-ropepull", user.id)
            elif message.lower().strip() == "9":
                await self.highrise.send_emote("10", user.id)
            elif message.lower().strip() == "11":
                await self.highrise.send_emote("emote-elbowbump", user.id)
            elif message.lower().strip() == "12":
                await self.highrise.send_emote("emote-baseball", user.id)
            elif message.lower().strip() == "13":
                await self.highrise.send_emote("idle-floorsleeping2", user.id)
            elif message.lower().strip() == "14":
                await self.highrise.send_emote("emote-hug", user.id)
            elif message.lower().strip() == "15":
                await self.highrise.send_emote("idle-floorsleeping", user.id)
            elif message.lower().strip() == "16":
                await self.highrise.send_emote("emote-hugyourself", user.id)
            elif message.lower().strip() == "17":
                await self.highrise.send_emote("emote-snowball", user.id)
            elif message.lower().strip() == "18":
                await self.highrise.send_emote("emote-hot", user.id)
            elif message.lower().strip() == "19":
                await self.highrise.send_emote("emote-levelup", user.id)
            elif message.lower().strip() == "20":
                await self.highrise.send_emote("emote-snowangel", user.id)
            elif message.lower().strip() == "21":
                await self.highrise.send_emote("idle-posh", user.id)
            elif message.lower().strip() == "22":
                await self.highrise.send_emote("emote-apart", user.id)
            elif message.lower().strip() == "23":
                await self.highrise.send_emote("idle-sad", user.id)
            elif message.lower().strip() == "24":
                await self.highrise.send_emote("idle-angry", user.id)
            elif message.lower().strip() == "25":
                await self.highrise.send_emote("emote-hero", user.id)
            elif message.lower().strip() == "26":
                await self.highrise.send_emote("idle-hero", user.id)
            elif message.lower().strip() == "27":
                await self.highrise.send_emote("dance-russian", user.id)
            elif message.lower().strip() == "28":
                await self.highrise.send_emote("emote-curtsy", user.id)
            elif message.lower().strip() == "29":
                await self.highrise.send_emote("emote-bow", user.id)
            elif message.lower().strip() == "30":
                await self.highrise.send_emote("idle-lookup", user.id)
            elif message.lower().strip() == "31":
                await self.highrise.send_emote("emote-headball", user.id)
            elif message.lower().strip() == "32":
                await self.highrise.send_emote("emote-fail2", user.id)
            elif message.lower().strip() == "33":
                await self.highrise.send_emote("emote-fail1", user.id)
            elif message.lower().strip() == "34":
                await self.highrise.send_emote("dance-pennywise", user.id)
            elif message.lower().strip() == "35":
                await self.highrise.send_emote("emote-boo", user.id)
            elif message.lower().strip() == "36":
                await self.highrise.send_emote("emote-wings", user.id)
            elif message.lower().strip() == "37":
                await self.highrise.send_emote("dance-floss", user.id)
            elif message.lower().strip() == "38":
                await self.highrise.send_emote("dance-blackpink", user.id)
            elif message.lower().strip() == "39":
                await self.highrise.send_emote("emote-model", user.id)
            elif message.lower().strip() == "40":
                await self.highrise.send_emote("emote-theatrical", user.id)
            elif message.lower().strip() == "41":
                await self.highrise.send_emote("emote-laughing2", user.id)
            elif message.lower().strip() == "42":
                await self.highrise.send_emote("emote-jetpack", user.id)
            elif message.lower().strip() == "43":
                await self.highrise.send_emote("emote-bunnyhop", user.id)
            elif message.lower().strip() == "44":
                await self.highrise.send_emote("Idle_zombie", user.id)
            elif message.lower().strip() == "45":
                await self.highrise.send_emote("emote-death2", user.id)
            elif message.lower().strip() == "46":
                await self.highrise.send_emote("emote-death", user.id)
            elif message.lower().strip() == "47":
                await self.highrise.send_emote("emote-disco", user.id)
            elif message.lower().strip() == "48":
                await self.highrise.send_emote("idle_relaxed", user.id)
            elif message.lower().strip() == "49":
                await self.highrise.send_emote("idle_layingdown", user.id)
            elif message.lower().strip() == "50":
                await self.highrise.send_emote("emote-faint", user.id)
            elif message.lower().strip() == "51":
                await self.highrise.send_emote("emote-cold", user.id)
            elif message.lower().strip() == "52":
                await self.highrise.send_emote("idle-sleep", user.id)
            elif message.lower().strip() == "53":
                await self.highrise.send_emote("emote-handstand", user.id)
            elif message.lower().strip() == "54":
                await self.highrise.send_emote("emote-ghost-idle", user.id)
            elif message.lower().strip() == "55":
                await self.highrise.send_emote("emoji-ghost", user.id)
            elif message.lower().strip() == "56":
                await self.highrise.send_emote("emote-splitsdrop", user.id)
            elif message.lower().strip() == "57":
                await self.highrise.send_emote("dance-spiritual", user.id)
            elif message.lower().strip() == "58":
                await self.highrise.send_emote("dance-smoothwalk", user.id)
            elif message.lower().strip() == "59":
                await self.highrise.send_emote("dance-singleladies", user.id)
            elif message.lower().strip() == "60":
                await self.highrise.send_emote("emoji-sick", user.id)
            elif message.lower().strip() == "61":
                await self.highrise.send_emote("dance-sexy", user.id)
            elif message.lower().strip() == "62":
                await self.highrise.send_emote("dance-robotic", user.id)
            elif message.lower().strip() == "63":
                await self.highrise.send_emote("emoji-naughty", user.id)
            elif message.lower().strip() == "64":
                await self.highrise.send_emote("emoji-pray", user.id)
            elif message.lower().strip() == "65":
                await self.highrise.send_emote("dance-duckwalk", user.id)
            elif message.lower().strip() == "66":
                await self.highrise.send_emote("emote-deathdrop", user.id)
            elif message.lower().strip() == "67":
                await self.highrise.send_emote("dance-voguehands", user.id)
            elif message.lower().strip() == "68":
                await self.highrise.send_emote("dance-orangejustice", user.id)
            elif message.lower().strip() == "69":
                await self.highrise.send_emote("dance-tiktok8", user.id)
            elif message.lower().strip() == "70":
                await self.highrise.send_emote("emote-heartfingers", user.id)
            elif message.lower().strip() == "71":
                await self.highrise.send_emote("emote-heartshape", user.id)
            elif message.lower().strip() == "72":
                await self.highrise.send_emote("emoji-halo", user.id)
            elif message.lower().strip() == "73":
                await self.highrise.send_emote("emoji-sneeze", user.id)
            elif message.lower().strip() == "74":
                await self.highrise.send_emote("dance-tiktok2", user.id)
            elif message.lower().strip() == "75":
                await self.highrise.send_emote("dance-metal", user.id)
            elif message.lower().strip() == "76":
                await self.highrise.send_emote("dance-aerobics", user.id)
            elif message.lower().strip() == "77":
                await self.highrise.send_emote("dance-martial-artist", user.id)
            elif message.lower().strip() == "78":
                await self.highrise.send_emote("dance-macarena", user.id)
            elif message.lower().strip() == "79":
                await self.highrise.send_emote("dance-handsup", user.id)
            elif message.lower().strip() == "80":
                await self.highrise.send_emote("dance-breakdance", user.id)
            elif message.lower().strip() == "90":
                await self.highrise.send_emote("emoji-hadoken", user.id)
            elif message.lower().strip() == "91":
                await self.highrise.send_emote("emoji-arrogance", user.id)
            elif message.lower().strip() == "92":
                await self.highrise.send_emote("emoji-smirking", user.id)
            elif message.lower().strip() == "93":
                await self.highrise.send_emote("emoji-lying", user.id)
            elif message.lower().strip() == "94":
                await self.highrise.send_emote("emoji-give-up", user.id)
            elif message.lower().strip() == "95":
                await self.highrise.send_emote("emoji-punch", user.id)
            elif message.lower().strip() == "96":
                await self.highrise.send_emote("emoji-poop", user.id)
            elif message.lower().strip() == "97":
                await self.highrise.send_emote("emoji-there", user.id)
            elif message.lower().strip() == "98":
                await self.highrise.send_emote("idle-loop-annoyed", user.id)
            elif message.lower().strip() == "99":
                await self.highrise.send_emote("idle-loop-tapdance", user.id)
            elif message.lower().strip() == "100":
                await self.highrise.send_emote("idle-loop-sad", user.id)
            elif message.lower().strip() == "101":
                await self.highrise.send_emote("idle-loop-happy", user.id)
            elif message.lower().strip() == "102":
                await self.highrise.send_emote("idle-loop-aerobics", user.id)
            elif message.lower().strip() == "103":
                await self.highrise.send_emote("idle-dance-swinging", user.id)
            elif message.lower().strip() == "104":
                await self.highrise.send_emote("emote-think", user.id)
            elif message.lower().strip() == "105":
                await self.highrise.send_emote("emote-disappear", user.id)
            elif message.lower().strip() == "106":
                await self.highrise.send_emote("emoji-scared", user.id)
            elif message.lower().strip() == "107":
                await self.highrise.send_emote("emoji-eyeroll", user.id)
            elif message.lower().strip() == "108":
                await self.highrise.send_emote("emoji-crying", user.id)
            elif message.lower().strip() == "109":
                await self.highrise.send_emote("emote-frollicking", user.id)
            elif message.lower().strip() == "110":
                await self.highrise.send_emote("emote-graceful", user.id)
            elif message.lower().strip() == "111":
                await self.highrise.send_emote("sit-idle-cute", user.id)
            elif message.lower().strip() == "112":
                await self.highrise.send_emote("emote-lust", user.id)
            elif message.lower().strip() == "113":
                await self.highrise.send_emote("idle-loop-tired", user.id)
            elif message.lower().strip() == "114":
                await self.highrise.send_emote("emoji-gagging", user.id)
            elif message.lower().strip() == "115":
                await self.highrise.send_emote("emoji-flex", user.id)
            elif message.lower().strip() == "116":
                await self.highrise.send_emote("emoji-celebrate", user.id)
            elif message.lower().strip() == "117":
                await self.highrise.send_emote("emoji-cursing", user.id)
            elif message.lower().strip() == "118":
                await self.highrise.send_emote("emoji-dizzy", user.id)
            elif message.lower().strip() == "119":
                await self.highrise.send_emote("emote-mindblown", user.id)
            elif message.lower().strip() == "120":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "121":
                await self.highrise.send_emote("idle-loop-sitfloor", user.id)
            elif message.lower().strip() == "122":
                await self.highrise.send_emote("emote-thumbsup", user.id)
            elif message.lower().strip() == "123":
                await self.highrise.send_emote("emote-clap", user.id)
            elif message.lower().strip() == "124":
                await self.highrise.send_emote("emote-mad", user.id)
            elif message.lower().strip() == "125":
                await self.highrise.send_emote("emote-sleepy", user.id)
            elif message.lower().strip() == "126":
                await self.highrise.send_emote("emote-thewave", user.id)
            elif message.lower().strip() == "127":
                await self.highrise.send_emote("emote-suckthumb", user.id)
            elif message.lower().strip() == "128":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "129":
                await self.highrise.send_emote("emote-peace", user.id)
            elif message.lower().strip() == "130":
                await self.highrise.send_emote("emote-panic", user.id)
            elif message.lower().strip() == "131":
                await self.highrise.send_emote("emote-jumpb", user.id)
            elif message.lower().strip() == "132":
                await self.highrise.send_emote("emote-hearteyes", user.id)
            elif message.lower().strip() == "133":
                await self.highrise.send_emote("emote-exasperated", user.id)
            elif message.lower().strip() == "134":
                await self.highrise.send_emote("emote-exasperatedb", user.id)
            elif message.lower().strip() == "135":
                await self.highrise.send_emote("emote-dab", user.id)
            elif message.lower().strip() == "136":
                await self.highrise.send_emote("emote-gangnam", user.id)
            elif message.lower().strip() == "137":
                await self.highrise.send_emote("emote-harlemshake", user.id)
            elif message.lower().strip() == "138":
                await self.highrise.send_emote("emote-tapdance", user.id)
            elif message.lower().strip() == "139":
                await self.highrise.send_emote("emote-yes", user.id)
            elif message.lower().strip() == "140":
                await self.highrise.send_emote("emote-sad", user.id)
            elif message.lower().strip() == "141":
                await self.highrise.send_emote("emote-robot", user.id)
            elif message.lower().strip() == "142":
                await self.highrise.send_emote("emote-rainbow", user.id)
            elif message.lower().strip() == "143":
                await self.highrise.send_emote("emote-no", user.id)
            elif message.lower().strip() == "144":
                await self.highrise.send_emote("emote-nightfever", user.id)
            elif message.lower().strip() == "145":
                await self.highrise.send_emote("emote-laughing", user.id)
            elif message.lower().strip() == "146":
                await self.highrise.send_emote("emote-kiss", user.id)
            elif message.lower().strip() == "147":
                await self.highrise.send_emote("emote-judochop", user.id)
            elif message.lower().strip() == "148":
                await self.highrise.send_emote("emote-hello", user.id)
            elif message.lower().strip() == "149":
                await self.highrise.send_emote("emote-happy", user.id)
            elif message.lower().strip() == "150":
                await self.highrise.send_emote("emote-gordonshuffle", user.id)
            elif message.lower().strip() == "151":
                await self.highrise.send_emote("emote-zombierun", user.id)
            elif message.lower().strip() == "152":
                await self.highrise.send_emote("emote-pose8", user.id)
            elif message.lower().strip() == "153":
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "154":
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "155":
                await self.highrise.send_emote("emote-pose5", user.id)
            elif message.lower().strip() == "156":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "157":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "158":
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.lower().strip() == "159":
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.lower().strip() == "160":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "161":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "162":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "163":
                await self.highrise.send_emote("emote-cutey", user.id)
            elif message.lower().strip() == "164":
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.lower().strip() == "165":
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.lower().strip() == "166":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "167":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "168":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "169":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "170":
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "171":
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "172":
                 await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "173":
                await self.highrise.send_emote("dance-icecream", user.id)
            elif message.lower().strip() == "174":
                await self.highrise.send_emote("emote-gravity", user.id)
            elif message.lower().strip() == "fashionista":
                await self.highrise.send_emote("emote-fashionista", user.id)
            elif message.lower().strip() == "175":
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.lower().strip() == "176":
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.lower().strip() == "177":
                await self.highrise.send_emote("dance-wrong", user.id)
            elif message.lower().strip() == "179":
                await self.highrise.send_emote("dance-wrong", user.id)
        except Exception as e:
            print(f"Error : {e}")


    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)

keep_alive()
if __name__ == "__main__":
    room_id = "63d3ef349e94d65aef81bac0"
    token = "aa6fdb51f49ccde5fddb2b846aa47e614845628f6a3df8eed85a48c456405add"
    arun(Bot().run(room_id, token))
