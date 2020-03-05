# -*- coding: utf-8 -*-
import asyncio
from AsyncLine import *
from boost_random.rd import choice
from random import sample
import traceback
import codecs
import json
loop = asyncio.get_event_loop()
tar = set()
with open("bot.txt") as f:
    l = [s.strip() for s in f.readlines()]
cl = Client('chrome')
cl.login(name="asyncline",token=l[17])
print(1)
kb = Client('chrome')
kb.login(name="asyncline",token=l[21])
print(2)
kc = Client('chrome')
kc.login(name="asyncline",token=l[18])
print(3)
kd = Client('chrome')
kd.login(name="asyncline",token=l[19])
print(4)
ke = Client('chrome')
ke.login(name="asyncline",token=l[20])
print(5)
kf = Client('chrome')
kf.login(name="asyncline",token=l[16])
print(6)
kg = Client('chrome')
kg.login(name="asyncline",token=l[22])
print(7)
kh = Client('chrome')
kh.login(name="asyncline",token=l[23])
print(8)
ki = Client('chrome')
ki.login(name="asyncline",token=l[24])
print(9)
kj = Client('chrome')
kj.login(name="asyncline",token=l[25])
print(10)
kk = Client('chrome')
kk.login(name="asyncline",token=l[26])
print(11)
kl = Client('chrome')
kl.login(name="asyncline",token=l[1])
print(12)
km = Client('chrome')
km.login(name="asyncline",token=l[2])
print(13)
kn = Client('chrome')
kn.login(name="asyncline",token=l[3])
print(14)
ko = Client('chrome')
ko.login(name="asyncline",token=l[4])
print(15)
kp = Client('chrome')
kp.login(name="asyncline",token=l[5])
print(16)
kq = Client('chrome')
kq.login(name="asyncline",token=l[6])
print(17)
kr = Client('chrome')
kr.login(name="asyncline",token=l[7])
print(18)
ks = Client('chrome')
ks.login(name="asyncline",token=l[8])
print(19)
kt = Client('chrome')
kt.login(name="asyncline",token=l[9])
print(20)
ku = Client('chrome')
ku.login(name="asyncline",token=l[10])
#ky = Client('chrome')
#ky.login(name="asyncline",token=l[24])
#kz = Client('chrome')
#kz.login(name="asyncline",token=l[25])
#ka = Client('chrome')
#ka.login(name="asyncline",token=l[26])

run = asyncio.ensure_future

mode = {}
black = {}
run(cl.talk.sendMessage("ubfb4168f1ca929d20a9eefe5b797021f", "起動"))
#json
f=codecs.open('admins.json', 'r', 'utf-8')
admins = json.load(f)
f.close()
f=codecs.open('ad1.json', 'r', 'utf-8')
ad1 = json.load(f)
f.close()
f=codecs.open('kick.json', 'r', 'utf-8')
protect = json.load(f)
f.close()

f=codecs.open('url.json','r','utf-8')
prourl = json.load(f)
f.close()

f=codecs.open('inv.json','r','utf-8')
proinv = json.load(f)
f.close()
haveP = {}
haveP.update(admins)
haveP.update(ad1)

boo = [cl,kb,kc,kd,ke,kf,kg,kh,ki,kj,kk,kl,km,kn,ko,kp,kq,kr,ks,kt,ku]
kick = [kb,kc,kd,ke,kf,kg,kh,ki,kj,kk,kl,km,kn,ko,kp,kq,kr,ks,kt,ku]

#get
length = len(kick)

#kicker
Ki = set(kick)
bots = set(boo)
bo = [x.profile.mid for x in bots]
ki = [x.profile.mid for x in kick]
kmid = set(ki)
cmid = set(bo)

#いらないものの削除
del bo
del boo

#関数群
def get_kicked_info():
    _max = length - 1
    return {
        ki[i]: kick[1] if i == _max else kick[i+1]
        for i in range(length)
    }
kicked_info = get_kicked_info()

async def notified_kick(param1, param2, param3):
  for a in "a":
    try:
        kicker = kicked_info[param3]
        group = await kicker.talk.getCompactGroup(param1)
        mids = set(c.mid for c in group.members)
        if group.preventedJoinByTicket:
            group.preventedJoinByTicket = False
            await kicker.talk.updateGroup(group)
        run(kicker.talk.kickoutFromGroup(param1, [param2]))
        preference = group.groupPreference
        if preference.invitationTicket:
            ticket = preference.invitationTicket
        else:
            ticket = await kicker.talk.reissueGroupTicket(param1)
        await asyncio.gather(*[line.talk.acceptGroupInvitationByTicket(param1, ticket) for line in bots if line.profile.mid not in mids])
    except:
        continue
    finally:
            black[param2] = True
    
async def notified_accept(param1, param2):
    kicker = choice(kick)
    group = await kicker.talk.getGroupWithoutMembers(param1)
    if group.preventedJoinByTicket:
        if len(group.name) > 50:
            group.name = "AtwoBotの提供"
        group.preventedJoinByTicket = False
        await kicker.talk.updateGroup(group)
    try:
        run(kicker.talk.kickoutFromGroup(param1, [param2]))
    except:
        print("failed kick")
async def notified_update(param1, param2):
  try:
    kicker = choice(kick)
    group = await kicker.talk.getGroupWithoutMembers(param1)
    if group.preventedJoinByTicket:
        if len(group.name) > 50:
           group.name = "AtwoBotの提供"
        group.preventedJoinByTicket = False
        await kicker.talk.updateGroup(group)
    try:
        run(kicker.talk.kickoutFromGroup(param1, [param2]))
    except:
        print("failed kick")
  finally:
      black[param2] = True
async def async_kick(param1, param2):
    for a in "a":
        try:
            await choice(kick).talk.kickoutFromGroup(param1,[param2])
        except:
            print("failed kick")
        

def shorturl(url):
        '''URL$BC;=L(B($B%H!<%/%sITMW(B)'''
        r = requests.get("http://tinyurl.com/api-create.php?url=%s" % url)
        return r.text

def ojichat(name,emojiLevel=9,punctiuationLevel=3):
        '''$BJ8;zNs$r$*$8$5$sIw$K(B'''
        payload = {'name': name, 'emoji_level': emojiLevel, "punctiuation_level": punctiuationLevel}
        r = requests.post("https://ojichat.appspot.com/post", data=payload)
        data = r.json()
        return data['message']

#Polling処理
async def polling(op):
  if op.type == 19:
    if op.param2 in kmid:
        return
    elif op.param3 in cmid:
        await notified_kick(op.param1, op.param2, op.param3)

    elif op.param3 in haveP:
        for a in "a":
            try:
                x = choice(kick)
                x.talk.findAndAddContactsByMid(op.param3)
                x.talk.inviteIntoGroup(op.param1, op.param3)
                break
            except:
                continue
    elif op.param1 in protect:
        await async_kick(op.param1, op.param2)


  if op.type == 11:
    if op.param2 in cmid:
        return
    elif op.param1 in mode or op.param1 in prourl:
        await notified_update(op.param1, op.param2)
  if op.type == 26:
    msg = op.message
    text = msg.text
    if msg.from_ in haveP: 
      if text == "help":
          await cl.talk.sendMessage(msg.to, """Atwo's Fighter
#main
hello
speed

#war!war!
.start
.stop

#protect
prokick:on/off
prourl:on/off
proinv:on/off

#groupurl
.ourl
.curl
.ticket
.join
.bye

#bot
cname:

#kick
.mk:
.kickall
tadd:
skick
limit

#admins
adminadd:
admindel:

#other
oji:
short:
exec:
""")
      elif text == ".ourl":
          bot = choice(kick)
          G = await bot.talk.getGroupWithoutMembers(msg.to)
          if G.preventedJoinByTicket:
              G.preventedJoinByTicket = False
              await bot.talk.updateGroup(G)
          await cl.talk.sendMessage(msg.to, "done")
      elif text == ".curl":
          bot = choice(kick)
          G = await bot.talk.getGroupWithoutMembers(msg.to)
          if G.preventedJoinByTicket == False:
              G.preventedJoinByTicket = True
              await bot.talk.updateGroup(G)
          await cl.talk.sendMessage(msg.to, "done")
      elif text == ".ticket":
          bot = choice(kick)
          g = await bot.talk.getGroupWithoutMembers(msg.to)
          if g.preventedJoinByTicket == True:
              g.preventedJoinByTicket = False
              await bot.talk.updateGroup(g)
          gurl = await bot.talk.reissueGroupTicket(msg.to)
          await cl.talk.sendMessage(msg.to,"line://ti/g/" + gurl)      
      elif "cname:" in text:
        if msg.from_ in admins:
          _name = text.replace("cname:","")
          for c, x in enumerate(bots):
              x.profile.displayName = _name + str(c)
              await x.talk.updateProfile(x.profile)
          await cl.talk.sendMessage(msg.to, "完了しね")
      elif "oji:" in text:
          _name = text.replace("oji:","")
          await cl.talk.sendMessage(msg.to, str(ojichat(_name)))
      elif "short:" in text:
          _name = text.replace("short:","")
          await cl.talk.sendMessage(msg.to, str(shorturl(_name)))
      elif text == "limit":
        if msg.from_ in admins:
          text = ' Kickers Limit\n'
          for c, x in enumerate(bots):
              try:
                  await x.talk.kickoutFromGroup(msg.to, [x.profile.mid])
                  text += 'No.%s Good\n' % c
              except:
                  text += 'No.%s fuck!\n' % c
          await cl.talk.sendMessage(msg.to, text[:-1])
      elif "prokick:on" == text:
          if msg.to in protect:
              await cl.talk.sendMessage(msg.to, "already on")
          else:
              protect[msg.to] = True
              await cl.talk.sendMessage(msg.to, "ok")
              f=codecs.open('kick.json','w','utf-8')
              json.dump(protect, f, sort_keys=False, indent=4,ensure_ascii=False)
              f.close()
      elif "prokick:off" == text:
          if msg.to in protect:
              await cl.talk.sendMessage(msg.to, "ok")
              del protect[msg.to]
              f=codecs.open('kick.json','w','utf-8')
              json.dump(protect, f, sort_keys=False, indent=4,ensure_ascii=False)
              f.close()
          else:
              await cl.talk.sendMessage(msg.to, "already off")
      elif "proinv:on" == text:
          if msg.to in protect:
              await cl.talk.sendMessage(msg.to, "already on")
          else:
              proinv[msg.to] = True
              await cl.talk.sendMessage(msg.to, "ok")
              f=codecs.open('inv.json','w','utf-8')
              json.dump(proinv, f, sort_keys=False, indent=4,ensure_ascii=False)
              f.close()
      elif "proinv:off" == text:
          if msg.to in protect:
              await cl.talk.sendMessage(msg.to, "ok")
              del proinv[msg.to]
              f=codecs.open('inv.json','w','utf-8')
              json.dump(proinv, f, sort_keys=False, indent=4,ensure_ascii=False)
              f.close()
          else:
              await cl.talk.sendMessage(msg.to, "already off")

      elif "prourl:on" == text:
          if msg.to in prourl:
              await cl.talk.sendMessage(msg.to, "already on")
          else:
              prourl[msg.to] = True
              await cl.talk.sendMessage(msg.to, "ok")
              f=codecs.open('url.json','w','utf-8')
              json.dump(prourl, f, sort_keys=False, indent=4, ensure_ascii=False)
              f.close()
      elif "prourl:off" == text:
          if msg.to in prourl:
              await cl.talk.sendMessage(msg.to, "ok")
              del prourl[msg.to]
              f=codecs.open('url.json','w','utf-8')
              json.dump(prourl, f, sort_keys=False, indent=4, ensure_ascii=False)
              f.close()
          else:
              await cl.talk.sendMessage(msg.to, "already off")
      elif "adminadd:" in text:
          if msg.from_ in admins:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = [x["M"] for x in key["MENTIONEES"]]
                for target in targets:
                    try:
                        ad1[target] = True
                        await cl.talk.sendMessage(msg.to, "done")
                    except:
                        await cl.talk.sendMessage(msg.to, "Error")
                f=codecs.open('ad1.json','w','utf-8')
                json.dump(ad1, f, sort_keys=False, indent=4, ensure_ascii=False)
                f.close()

      elif "admindel:" in text:
          if msg.from_ in admins:
              key = eval(msg.contentMetadata["MENTION"])
              key["MENTIONEES"][0]["M"]
              targets = [x["M"] for x in key["MENTIONEES"]]
              for target in targets:
                  try:
                      del ad1[target]
                      await cl.talk.sendMessage(msg.to, "done")
                  except:
                      await cl.talk.sendMessage(msg.to, "Error")
              f=codecs.open('ad1.json','w','utf-8')
              json.dump(ad1, f, sort_keys=False, indent=4, ensure_ascii=False)
              f.close()
             
      elif ".mk:" in text:
        if msg.from_ in admins:
          key = eval(msg.contentMetadata["MENTION"])
          key["MENTIONEES"][0]["M"]
          targets = set(x["M"] for x in key["MENTIONEES"])
          await asyncio.gather(*[choice(kick).talk.kickoutFromGroup(msg.to, [x]) for x in targets])
      elif "tadd:" in text:
        if msg.from_ in admins:
          key = eval(msg.contentMetadata["MENTION"])
          key["MENTIONEES"][0]["M"]
          for x in key["MENTIONEES"]:
              tar.add(x["M"])
          run(cl.talk.sendMessage(msg.to, "okok"))
      elif "skick" == text:
        if msg.from_ in admins:
          g = await cl.talk.getCompactGroup(msg.to)
          mids = set(c.mid for c in g.members)
          await cl.talk.sendMessage(msg.to, "Let's go!")
          await asyncio.gather(*[choice(kick).talk.kickoutFromGroup(msg.to, [target]) for target in tar if target in mids])
      elif text == ".start":
          mode[msg.to] = True
          await cl.talk.sendMessage(msg.to,"war!war!")

      elif text == ".stop":
          del mode[msg.to]
          await cl.talk.sendMessage(msg.to,"see you.")

      elif text == "hello":
          await cl.talk.sendReply(msg.id, msg.to, "Client ok")
          task = asyncio.gather(*[x.talk.sendReply(msg.id, msg.to, "LineBot by AsyncLine") for x in Ki])
          await task

      elif "exec:" in text:
        if msg.from_ in admins:
          _name = text.replace("exec:","")
          try:
              exec(_name)
          except Exception as e:
              await cl.talk.sendMessage(msg.to, str(e))

      elif text == "speed":
          start = time.time()
          await cl.talk.sendMessage(msg.to,"start")
          elapsed_time = time.time() - start
          s = time.time()
          await asyncio.gather(*[cl.talk.noop() for _ in range(1000)])
          e = time.time() - s
          await cl.talk.sendMessage(msg.to, "send>>" + str(elapsed_time)+ "\nnoop>>" + str(e/1000))

      elif text == ".join":
          G = await cl.talk.getCompactGroup(msg.to)
          if G.preventedJoinByTicket:
              G.preventedJoinByTicket = False
              await cl.talk.updateGroup(G)
          Ticket = await cl.talk.reissueGroupTicket(msg.to)
          mids= set(c.mid for c in G.members)
          task = asyncio.wait([bot.talk.acceptGroupInvitationByTicket(msg.to, Ticket) for bot in kick if bot.profile.mid not in mids])
          await task
          

      elif text == ".bye":
          await cl.talk.sendMessage(msg.to, "ば〜い")
          await asyncio.gather(*[x.talk.leaveGroup(msg.to) for x in bots])

      elif text == ".kickall":
        if msg.from_ in admins:
          group = await cl.talk.getCompactGroup(msg.to)
          mids= set(c.mid for c in group.members)
          mids_remove = mids.remove
          for x in bo:
              if x in mids:
                  mids_remove(x)
          for x in admins:
              if x in mids:
                  mids_remove(x)
          await asyncio.gather(*[choice(kick).talk.kickoutFromGroup(msg.to, [x]) for x in mids])

  if op.type == 17:
      if op.param2 in black:
        await async_kick(op.param1, op.param2)

  if op.type == 13:
    if op.param2 in cmid:
        return
    elif cl.profile.mid in op.param3:
        if op.param2 in haveP:
            await cl.talk.acceptGroupInvitation(op.param1)
            G = await cl.talk.getCompactGroup(op.param1)
            if G.preventedJoinByTicket:
                G.preventedJoinByTicket = False
                await cl.talk.updateGroup(G)
            Ti=await cl.talk.reissueGroupTicket(op.param1)
            mids= set(c.mid for c in G.members)
            await asyncio.gather(*[bot.talk.acceptGroupInvitationByTicket(op.param1, Ti) for bot in kick if bot.profile.mid not in mids])
            await cl.talk.sendMessage(op.param1, "Thank you for using!\nGood bye!")
    else:
      if op.param1 in mode or op.param1 in proinv:
        if op.param2 not in haveP:
          for a in "a":
            try:
                bot = choice(kick)
                await bot.talk.kickoutFromGroup(op.param1, [op.param2])
                run(bot.talk.cancelGroupInvitation(op.param1, [op.param3]))
                break
            except:
                continue
oplist = [19,11,26,13,17]
loop.run_until_complete(cl.poll.trace(polling, set(oplist)))



