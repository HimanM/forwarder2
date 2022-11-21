import telethon
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import asyncio,requests,re


async def one():
    print("Logger Bot1 Started")
    #---------------------------Configuration---------------------------------------------------
    api_id = '19084340'                                                         #uberge ekk dapn
    api_hash = 'ddea16f6eecce0a0276c611086ff50f8'                               #uberge ekk dapn
    bt = '5009768358:AAGNbzEfUldjFUvAeyhwpO07BnuJx1b58L4'                        #ube botage lbba dapn

    LOG_GROUP = -1001653373835          #me apey log grp ekt thiyn eka
    CC_GET = 1846373843             #uber CC adinne meken ara heckerge grp eka 
    #----------------------------iwarai---------------------------------------------------------


    #uda thiyn okkoma wenas krpn uber meke okkoma thiynna adala nathi huttwal


    bot = TelegramClient('name', api_id, api_hash).start(bot_token=bt)
    await bot.start()
    def req(msg_id,id):
        api = f"https://api.telegram.org/bot{bt}/copyMessage?chat_id={LOG_GROUP}&message_id={msg_id}&from_chat_id={id}"
        r = requests.get(api)

    @bot.on(events.NewMessage(chats=CC_GET,outgoing=False))
    async def handler(event):
        # if event.media == None:
        #     return
        #meka uncomment krnna EPAAAAAAAAAAAA 
        msg_id =  event.id
        id =  event.chat_id
        req (msg_id,id)
    
    await bot.run_until_disconnected()

async def two():
    SESSION = '1BVtsOJwBuwZcD0ZAs4HzuviR_Y4q_qKRqMgd2CkUhCWuL_XCCh3dAc9-4cBbM08ovg1XGaAxrS70m0cZg5yGg_4bExITqCINxs0B-qVs3Wd27xuHuZaJfHs1bXTjdBuoqIiVIJP_1Hdyt-hwB5GVuD5Y7vmVMZi8riqcrEIz8irGhAv71sXWJDJWoeMdK0W2vfVYO1xETPmnzOOxt_sECch0yuKFHfWnUwb4Piua0xNl7dBbU0-EvGF5to_4nQJ0olVFmMOJp3oLJhQBlZo07aZ5s7_v_pAADD3D9OUx_u2Xl4dYU3efa9LKMgEQhLJ_W-vSMu46lznFc4boA2mM4EDW9DRxpeg='
    API_ID = '18038640'
    API_HASH = '3ae4443659d90734fb72985526b7a422'
    bot2 = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await bot2.start()
    CC_LOG = -1001653373835
    LOG_CCSEL = -1001783292066
    @bot2.on(events.NewMessage(chats= CC_LOG))
    async def runner(e):
        msg = e.message.message
        if re.search ('\d{12,}', msg):
            mention = "@USERID_null Possible CC found"
            await bot2.send_message(LOG_CCSEL,mention)
            await bot2.send_message(LOG_CCSEL,msg)
    print("Logger Bot2 Started")
    await bot2.run_until_disconnected()

async def main():
    f1 = loop.create_task(one())
    f2 = loop.create_task(two())
    await asyncio.wait([f1, f2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


    