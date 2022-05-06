from unittest import result
import discord
from discord.ext import commands
import asyncio
import random
from discord.ui import Button, View
from discord.utils import get
import time
import os

name = "" #info[0]
money = 0 #info[1]
Enter_bank = "N" #info[2]
Bank_number = 0 #info[3]
Bank_name = None
Bank_coin = 0 #info[4]
quit_number = "N" #info[5]

front_command = "$"


beginner = " " + str(50000) + " " + Enter_bank + " " + str(Bank_number) + " " + str(Bank_coin) + " " + quit_number #처음 등록하는 틀

checknumber = 0 #파일에 계정이 있는지 체크
info = [] # 파일을 배열로 담은 값에서 하나하나 분리하기 위한 배열
ebd = "" #은행 임베드

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents = intents)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("게임 연구"))

@bot.event
async def on_message(message):
    # await bot.process_commands(message)
    if message.author.bot:
        return

    if message.content.startswith(front_command+"명령어"):
        embed=discord.Embed(title="명령어",color=0x00ff56)
        embed.add_field(name=">등록", value="봇 서비스에 등록합니다.", inline=False)
        embed.add_field(name=">탈퇴", value="봇 서비스에서 탈퇴합니다.", inline=False)
        embed.add_field(name=">내정보", value="내정보를 확인할 수 있습니다.", inline=False)
        embed.add_field(name=">도박", value="도박 관련 명령어를 확인할 수 있습니다.", inline=False)
        embed.add_field(name=">통장", value="통장 관련 명령어를 확인할 수 있습니다.", inline=False)
        embed.add_field(name=">송금", value="송금 관련 명령어를 확인할 수 있습니다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(front_command+"내정보"):
        global checknumber
        with open('user.txt') as temp_f:
            datafile = temp_f.readlines()
        for i in range(len(datafile)):
            if message.author.name in datafile[i]:
                checknumber = 1
                info = datafile[i].split()

                if info[5] == "Y":
                    await message.channel.send("탈퇴한 계정은 내정보를 확인할 수 없습니다.")
                    break

                if info[5] == "N":
                    if int(info[3]) == 1:
                        Bank_name = "미니은행"
                    
                    elif int(info[3]) == 2:
                        Bank_name = "단풍은행"

                    else:
                        Bank_name = None

                    embed=discord.Embed(title="내정보", description = message.author.name+"님의 정보입니다.",color=0x00ff56)
                    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/954248874757865482/954249016730853376/coins.png")
                    embed.add_field(name="맨션", value="<@!"+str(message.author.id)+">", inline=True)
                    embed.add_field(name="지닌 돈", value=str(format(int(info[1]), ',d')), inline=True)
                    embed.add_field(name="탈퇴 여부", value=info[5], inline=True)
                    embed.add_field(name="통장 개설 여부", value=info[2], inline=True)
                    embed.add_field(name="통장", value=Bank_name, inline=True)
                    embed.add_field(name="저금한 금액", value=str(format(int(info[4]), ',d')), inline=True)
                    await message.channel.send(embed=embed)
                    break

                else:
                    await message.channel.send("에러코드 : NOT QUIT STR 1")
                    break

        if checknumber == 0:
          await message.channel.send("아직 계정을 등록하지 않았습니다. >등록으로 계정을 등록해주세요!")
        checknumber = 0
    
    if message.content.startswith(front_command+"도박"):
        number = 0
        percent = 0
        if "도움말" in message.content:
            embed=discord.Embed(title="도박 도움말", color=0x00ff56)
            embed.add_field(name="도박 서비스를 이용해보세요", value="""
            미니게임 봇의 가장 중요한 기능이라고 할 수 있는 도박 서비스를 이용해보세요!
            """, inline=False)
            embed.add_field(name="올인 도박", value="""
            올인으로 지니고 있는 모든 돈을 걸 수 있어요
            올인을 하게되면 성공 확률은 0.1%로 상금은 배팅한 돈 * 10000을 받을 수 있어요
            0.1%의 확률로 인생역전을 노려보세요!
            >도박 올인
            """, inline=False)
            embed.add_field(name="도박 확률", value="""
            도박의 확률은 10% ~ 100%까지 있어요
            확률마다 돈의 최대 배수도 0% ~ 10000%까지 있어요
            자세한 확률표는 ">도박 확률"을 확인해주세요!
            """, inline=False)
            embed.add_field(name="도박 명령어", value="""
            >도박 도움말 -> 도박 관련 도움말을 확인할 수 있습니다.
            >도박 확률 -> 도박 확률에 대해 자세한 내용을 확인합니다.
            >도박 올인 -> 지니고 있는 돈 전부를 도박에 배팅합니다
            >도박 [숫자] -> 숫자만큼 배팅합니다.
            """, inline=False)
            await message.channel.send(embed=embed)
        elif "확률" in message.content:
            embed=discord.Embed(title="도박 확률", color=0x00ff56)
            embed.add_field(name="도박 확률", value="""
            도박의 확률은 고정적 확률이에요.
            건 돈은 회수하고, 돈은 원금 * (배수)로 받을 수 있어요.
            35% 0배
            20% 0.5배
            20% 1.5배
            15% 2배
            7% 3배
            2% 5배
            0.988% 10배
            0.01% 100배
            0.001% 1000배
            0.001% 파산 (저금한 돈을 제외한 모든 돈이 0이 됩니다.)
            """, inline=False)
            await message.channel.send(embed=embed)

        elif "올인" in message.content:
            i = 0
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            k = 0
            while(k < len(datafile)):
              if datafile[k] == "\n":
                del datafile[k]
              k = k + 1
            for j in range(len(datafile)):
                if message.author.name in datafile[j]:
                    info = datafile[j].split()
                    i = j
            
                    if int(info[1]) == 0:
                      await message.channel.send("0원 이하는 배팅할 수 없습니다.")
                      break

                    else:
                        temp_f.close()
                        number = random.choices(range(1,3), weights=[0.1, 99.9])
                        if str(number) == "[1]":
                            temp_f = open("user.txt","w")
                            datafile[i] = info[0] + " " + str(int(info[1]) * 10000) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                            temp_f.write('\n'.join(datafile))
                            embed=discord.Embed(title="축하합니다!",color=0x00ff56)
                            embed.add_field(name="배팅한 돈", value=str(format(int(info[1]), ',d'))+ "원", inline=False)
                            embed.add_field(name="얻은 돈", value=str(format(int(int(info[1]) * 10000), ',d')) + "원", inline=False)
                            embed.add_field(name="최종 배수", value="10,000배", inline=False)
                            await message.channel.send(embed=embed)
                            break
    
                        elif str(number) == "[2]":
                            embed=discord.Embed(title="아깝습니다..",color=0x00ff56)
                            temp_f = open("user.txt","w")
                            datafile[i] = info[0] + " " + "0" + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                            temp_f.write('\n'.join(datafile))
                            
                            embed.add_field(name="배팅한 돈", value=str(format(int(info[1]), ',d'))+ "원", inline=False)
                            embed.add_field(name="잃은 돈", value=str(format(int(info[1]), ',d')) + "원", inline=False)
                            embed.add_field(name="최종 배수", value="0배", inline=False)
                            await message.channel.send(embed=embed)
                            break
                
            temp_f.close()


        else:
            i = 0
            check_int = message.content.replace(front_command+"도박", "")
            if check_int.isdecimal():
                embed=discord.Embed(title="띄어쓰기 오류",color=0x00ff56)
                embed.add_field(name="걸 돈과 도박 명령어를 띄어쓰기가 있어야 해요!", value="EX) >도박 1000", inline=False)
                await message.channel.send(embed=embed)

            elif check_int[1:].isdecimal():
                temp_f = open("user.txt","r")
                datafile = temp_f.readlines()
                k = 0
                while(k < len(datafile)):
                  if datafile[k] == "\n":
                    del datafile[k]
                  k = k + 1
                for j in range(len(datafile)):
                    if message.author.name in datafile[j]:
                        info = datafile[j].split()
                        i = j

                        temp_f.close()
                
                        if int(check_int[1:]) == 0:
                            await message.channel.send("0원 이하는 배팅할 수 없습니다.")
                            break
                        
                        elif int(info[1]) < int(check_int[1:]):
                            await message.channel.send("현재 가진 돈보다 많은 돈을 배팅할 수 없습니다.")
                            break

                        else:
                            percent = 0
                            number = random.choices(range(1,11), weights=[35, 20, 20, 15, 7, 2, 0.988, 0.01, 0.001, 0.001]) #고정확률

                            if str(number) == "[1]":
                                temp_f = open("user.txt","w")
                                datafile[i] = info[0] + " " + str(int(info[1]) - int(check_int[1:])) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                              
                                temp_f.write('\n'.join(datafile))
                                
                                  
                                embed=discord.Embed(title="아깝습니다..",color=0x00ff56)
                                embed.add_field(name="배팅한 돈", value=str(format(int(check_int[1:]), ',d'))+ "원", inline=False)
                                embed.add_field(name="잃은 돈", value=str(format(int(check_int[1:]), ',d')) + "원", inline=False)
                                embed.add_field(name="최종 배수", value=str(percent) + "배", inline=False)
                                await message.channel.send(embed=embed)
                                break

                            elif str(number) == "[2]":
                                temp_f = open("user.txt","w")
                                datafile[i] = info[0] + " " + str(int(info[1]) - int(check_int[1:]) + int((int(check_int[1:]) * 0.5))) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                                temp_f.write('\n'.join(datafile)) 
                                embed=discord.Embed(title="아쉽습니다..",color=0x00ff56)
                                embed.add_field(name="배팅한 돈", value=str(format(int(check_int[1:]), ',d'))+ "원", inline=False)
                                embed.add_field(name="잃은 돈", value=str(format(int(int(check_int[1:]) * 0.5), ',d')) + "원", inline=False)
                                embed.add_field(name="최종 배수", value=str(0.5) + "배", inline=False)
                                await message.channel.send(embed=embed)  
                                break

                            elif str(number) == "[3]":
                                percent = 1.5 #20%
                            elif str(number) == "[4]":
                                percent = 2 #15%
                            elif str(number) == "[5]":
                                percent = 3 #7%
                            elif str(number) == "[6]":
                                percent = 5 #2%
                            elif str(number) == "[7]":
                                percent = 10 #0.988%
                            elif str(number) == "[8]":
                                percent = 100 #0.01%
                            elif str(number) == "[9]":
                                percent = 1000 #0.001%
                            elif str(number) == "[10]":
                              #파산
                              temp_f = open("user.txt","w")
                              datafile[i] = info[0] + " " + str(0) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                              temp_f.write('\n'.join(datafile)) 
                              embed=discord.Embed(title="희박한 확률을 뚫고 파산했습니다..",color=0x00ff56)
                              embed.add_field(name="배팅한 돈", value=str(format(int(check_int[1:]), ',d'))+ "원", inline=False)
                              embed.add_field(name="잃은 돈", value=str(format(int(int(check_int[1:])), ',d')) + "원", inline=False)
                              embed.add_field(name="최종 배수", value=str(0.5) + "배", inline=False)
                              await message.channel.send(embed=embed)  
                              break
                            
                                
                            temp_f = open("user.txt","w")
                            datafile[i] = info[0] + " " + str(int(info[1]) - int(check_int[1:]) + int((int(check_int[1:]) * percent))) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                            temp_f.write('\n'.join(datafile)) 
                            embed=discord.Embed(title="축하합니다!",color=0x00ff56)
                            embed.add_field(name="배팅한 돈", value=str(format(int(check_int[1:]), ',d'))+ "원", inline=False)
                            embed.add_field(name="얻은 돈", value=str(format(int(int(check_int[1:]) * percent), ',d')) + "원", inline=False)
                            embed.add_field(name="최종 배수", value=str(percent) + "배", inline=False)
                            await message.channel.send(embed=embed)     

                            if int(info[3]) == 1: #미니은행 이자
                              number = random.choices(range(1,3), weights=[20, 80])
                              if str(number) == "[1]":
                                  temp_f.close()
                                  temp_f = open("user.txt","w")
                                  datafile[i] = info[0] + " " + str(round(int(info[1]) + (int(check_int[1:]) * percent * 0.7))) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                                  temp_f.write('\n'.join(datafile))
                          
                              
                                  embed=discord.Embed(title="미니은행 이자",color=0x00ff56)
                                  embed.add_field(name="이자 환수", value="이자로 " +str(round(int(check_int[1:]) * percent * 0.7))+ "원을 추가로 받았습니다.", inline=False)
                                  await message.channel.send(embed=embed)

                            elif int(info[3]) == 2: #단풍은행 이자
                              number = random.choices(range(1,3), weights=[70, 30])
                              if str(number) == "[1]":
                                  temp_f.close()
                                  temp_f = open("user.txt","w")
                                  datafile[i] = info[0] + " " + str(round(int(info[1]) + (int(check_int[1:]) * percent * 0.05))) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "N"
                                  k = 0
                                  while(k < len(datafile)):
                                      if datafile[k] == "\n":
                                          del datafile[k]
                                      k = k + 1
                                  temp_f.write('\n'.join(datafile))
                                  embed=discord.Embed(title="단풍은행 이자",color=0x00ff56)
                                  embed.add_field(name="이자 환수", value="이자로 " +str(round(int(check_int[1:]) * percent * 0.05)) + "원을 추가로 받았습니다.", inline=False)
                                  await message.channel.send(embed=embed)
                    

                temp_f.close()

            else:
                embed=discord.Embed(title="도박 관련 명령어",color=0x00ff56)
                embed.add_field(name=">도박 도움말 ", value="도박 관련 도움말을 확인할 수 있습니다.", inline=False)
                embed.add_field(name=">도박 확률", value="도박 확률에 대해 자세한 내용을 확인할 수 있습니다.", inline=False)
                embed.add_field(name=">도박 올인 ", value="지니고 있는 돈 전부를 도박에 배팅합니다.", inline=False)
                embed.add_field(name=">도박 [숫자] ", value="[숫자]만큼 도박에 배팅합니다.", inline=False)
                await message.channel.send(embed=embed)

    if message.content.startswith(front_command+"등록"):
        global beginner
        temp_f = open("user.txt","r")
        datafile = temp_f.readlines()
        if len(datafile) == 0:
            temp_f.close()
            temp_f = open("user.txt","w")
            temp_f.write(message.author.name + beginner + "\n")
            await message.channel.send("계정이 정상적으로 등록되었습니다. " + message.author.name +"님 안녕하세요 :) 등록지원금으로 50000원이 증정되었습니다!")
        else:
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    checknumber = 1
                    await message.channel.send("이미 등록된 계정입니다. 봇 이용이 안되면 관리자를 불러주세요!")
                    break
            
            if checknumber == 0:
                temp_f.close()
                temp_f = open("user.txt","a")
                if datafile[int(len(datafile)) - 2] == " ":
                  temp_f.write(message.author.name + beginner)
                else:
                  temp_f.write("\n" + message.author.name + beginner)
                await message.channel.send("계정이 정상적으로 등록되었습니다. " + message.author.name + "님 안녕하세요 :) 등록지원금으로 50000원이 증정되었습니다!")

        checknumber = 0


        temp_f.close()

    if message.content.startswith(front_command+"탈퇴"):
        temp_f = open("user.txt","r")
        datafile = temp_f.readlines()
        if len(datafile) == 0:
            await message.channel.send("등록된 계정이 없습니다.")
        else:
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    if info[5] == "Y":
                        checknumber = 1
                        await message.channel.send("이미 탈퇴된 계정입니다. 탈퇴 번복은 관리자에게 문의하세요.")
                        break
                    elif info[5] == "N":
                        temp_f.close()
                        temp_f = open("user.txt","w")
                        datafile[i] = info[0] + " " + str(info[1]) + " " + info[2] + " " + str(info[3]) + " " + str(info[4]) + " " + "Y"
                        temp_f.write('\n'.join(datafile))
                        checknumber = 1
                        await message.channel.send("탈퇴가 정상적으로 진행되었습니다. 서비스를 이용해주셔서 감사합니다 :)")
                        break
                    else:
                        await message.channel.send("에러코드 : NOT QUIT STR 1")
                        break
                      
            if checknumber == 0:
              await message.channel.send("등록된 계정이 없습니다.")
        checknumber = 0
        temp_f.close()


    if message.content.startswith(front_command+"통장"):
        if "도움말" in message.content:
            embed=discord.Embed(title="통장 도움말", color=0x00ff56)
            embed.add_field(name="통장은 서비스를 이용하는데 아주 많은 도움을 줍니다!", value="""
            1. 송금 기능을 사용할 수 있어요
            2. 도박을 통해 돈을 얻을 때마다 은행 이자로 돈을 추가로 받을 수 있어요
            """, inline=False)
            embed.add_field(name="통장을 개설하면 이자를 받을 수 있는데요", value="""
            이자는 5% ~ 50%까지 다양하고,
            이자율도 1% ~ 90%까지 확률이 다양해요
            """, inline=False)
            embed.add_field(name="개설할 수 있는 통장은 두 곳이에요", value="""
            1. 미니은행
            2. 단풍은행
            """, inline=False)
            embed.add_field(name="은행마다 효과가 달라요", value="""
            1. 미니은행에 경우, 이자율이 높은 대신 이자를 얻을 확률이 낮아요 (이자율 최대 70%, 이자 확률 최대 20%)
            2. 단풍은행에 경우, 이자율이 낮은 대신 이자를 얻을 확률이 높아요 (이자율 최대 5%, 이자 확률 최대 70%)
            """, inline=False)
            
            await message.channel.send(embed=embed)

        elif "개설" in message.content:
            global ebd
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    if str(info[5]) == "Y":
                        await message.channel.send("탈퇴한 계정은 통장을 개설할 수 없습니다.")
                        break

                    else:
                        if str(info[2]) == "N":
                            if int(info[3]) == 0:
                                mini_bank_button = Button(label="1. 미니은행", style = discord.ButtonStyle.grey)
                                maple_bank_button = Button(label="2. 단풍은행", style = discord.ButtonStyle.grey)

                                async def mini_bank_button_callback(interaction):
                                  global ebd
                                  temp_f = open("user.txt","r")
                                  datafile = temp_f.readlines()
                                  k = 0
                                  while(k < len(datafile)):
                                      if datafile[k] == "\n":
                                          del datafile[k]
                                      k = k + 1
                                      for i in range(len(datafile)):
                                          if interaction.user.name in datafile[i]:
                                            info = datafile[i].split()
                                            temp_f.close()
                                            temp_f = open("user.txt","w")
                                            datafile[i] = str(info[0]) + " " + str(info[1]) + " " + "Y" + " " + str(1) + " " + str(0) + " " + "N"
                                            temp_f.write('\n'.join(datafile))
                                            embed=discord.Embed(title="통장 개설 완료",color=0x00ff56)
                                            embed.add_field(name="통장 이름", value="미니은행", inline=False)
                                            embed.add_field(name="통장 개설자", value=str(interaction.user.name), inline=False)
                                            view.clear_items()
                                            await ebd.edit(embed=embed, view = view)
                                            break

                                  temp_f.close()
                                async def maple_bank_button_callback(interaction):
                                  global ebd
                                  temp_f = open("user.txt","r")
                                  datafile = temp_f.readlines()
                                  k = 0
                                  while(k < len(datafile)):
                                      if datafile[k] == "\n":
                                          del datafile[k]
                                      k = k + 1
                                      for i in range(len(datafile)):
                                          if interaction.user.name in datafile[i]:
                                            info = datafile[i].split()
                                            temp_f.close()
                                            temp_f = open("user.txt","w")
                                            datafile[i] = str(info[0]) + " " + str(info[1]) + " " + "Y" + " " + str(2) + " " + str(0) + " " + "N"
                                            temp_f.write('\n'.join(datafile))
                                            
                                            embed=discord.Embed(title="통장 개설 완료",color=0x00ff56)
                                            embed.add_field(name="통장 이름", value="단풍은행", inline=False)
                                            embed.add_field(name="통장 개설자", value=str(interaction.user.name), inline=False)
                                            view.clear_items()
                                            await ebd.edit(embed=embed, view = view)
                                            break

                                      temp_f.close()
                                      

                                mini_bank_button.callback = mini_bank_button_callback
                                maple_bank_button.callback = maple_bank_button_callback

                                view = View()
                                view.clear_items()
                                view.add_item(mini_bank_button)
                                view.add_item(maple_bank_button)

                                embed=discord.Embed(title="개설할 통장을 선택해주세요.",color=0x00ff56)
                                embed.add_field(name="1. 미니은행 ", value="이자율이 높은 대신 이자를 얻을 확률이 낮아요 (이자율 최대 70%, 이자 확률 최대 20%)", inline=False)
                                embed.add_field(name="2. 단풍은행", value="이자율이 낮은 대신 이자를 얻을 확률이 높아요. (이자율 최대 5%, 이자 확률 최대 70%)", inline=False)
                                ebd = await message.channel.send(embed=embed, view = view)
                                # await ebd.add_reaction("\U00000031\U0000FE0F\U000020E3") #미니은행
                                # await ebd.add_reaction("\U00000032\U0000FE0F\U000020E3") #단풍은행
                                break

                            else:
                                if int(info[3]) == 1:
                                    await message.channel.send("이미 미니은행에 가입했습니다.")
                                elif int(info[3]) == 2:
                                    await message.channel.send("이미 단풍은행에 가입했습니다.")
                                else:
                                    await message.channel.send("에러코드 : NOT BANK INT 1")

                                break
                        
                        else:
                            await message.channel.send("통장을 이미 개설했습니다.")
                            break
    
            temp_f.close()
        elif "출금" in message.content:
            global out_money
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            k = 0
            while(k < len(datafile)):
              if datafile[k] == "\n":
                del datafile[k]
              k = k + 1
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    out_money = 0
                    if info[3] == 0 or info[5] == "Y":
                        await message.channel.send("통장이 개설되지 않았습니다.")
                        break
                    else:
                        await message.channel.send("얼마를 출금하시겠습니까?")

                        def check(msg):
                          global out_money
                          money = msg.content
                          if money.isdecimal():
                              out_money = int(msg.content)
                              return msg.author == message.author and msg.channel == message.channel
                          else:
                              return msg.author == message.author and msg.channel == message.channel

                        try:
                            msg = await bot.wait_for('message', timeout = 30.0, check=check)
                            money = msg.content
                            if money.isdecimal():
                              if int(info[4]) < int(out_money):
                                  await message.channel.send("출금 실패 (통장에 있는 돈보다 많은 출금)")
                                  break
                              else:
                                  temp_f.close()
                                  temp_f = open("user.txt","w")
                                  datafile[i] = info[0] + " " + str(int(info[1]) + out_money) + " " + info[2] + " " + str(info[3]) + " " + str(int(info[4]) - out_money) + " " + "N"
                                  temp_f.write('\n'.join(datafile))
                                    
                                  if int(info[3]) == 1:
                                      Bank_name = "미니은행"
                                  
                                  elif int(info[3]) == 2:
                                      Bank_name = "단풍은행"
  
                                  else:
                                      Bank_name = None
                                  await message.channel.send(str(out_money) + "원이 " + Bank_name + "에서 정상적으로 출금되었습니다.")
                                  break
                            else:
                              await message.channel.send("입금 실패 (숫자만 입력해주세요.)")
                        except asyncio.TimeoutError:
                            await message.channel.send("출금 실패 (시간초과)")
                            break

            temp_f.close()

        elif "입금" in message.content:
            global in_money
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            k = 0
            while(k < len(datafile)):
              if datafile[k] == "\n":
                del datafile[k]
              k = k + 1
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    in_money = 0
                    if info[3] == 0 or info[5] == "Y":
                        await message.channel.send("통장이 개설되지 않았습니다.")
                        break
                    else:
                        await message.channel.send("얼마를 입금하시겠습니까?")

                        def check(msg):
                            global in_money
                            money = msg.content
                            if money.isdecimal():
                                in_money = int(msg.content)
                                return msg.author == message.author and msg.channel == message.channel
                            else:
                                return msg.author == message.author and msg.channel == message.channel

                        try:
                            msg = await bot.wait_for('message', timeout = 30.0, check=check)
                            money = msg.content
                            if money.isdecimal():
                              if int(info[1]) < int(in_money):
                                  await message.channel.send("입금 실패 (지니고 있는 돈보다 많은 입금)")
                                  break
                                
                              else:
                                  temp_f.close()
                                  temp_f = open("user.txt","w")
                                  datafile[i] = info[0] + " " + str(int(info[1]) - in_money) + " " + info[2] + " " + str(info[3]) + " " + str(int(info[4]) + in_money) + " " + "N"
                                  temp_f.write('\n'.join(datafile))
                                    
                                  if int(info[3]) == 1:
                                      Bank_name = "미니은행"
                                  
                                  elif int(info[3]) == 2:
                                      Bank_name = "단풍은행"
  
                                  else:
                                      Bank_name = None
                                  await message.channel.send(str(in_money) + "원이 " + Bank_name + "에서 정상적으로 입금되었습니다.")
                                  break
                            else:
                              await message.channel.send("입금 실패 (숫자만 입력해주세요.)")
                        except asyncio.TimeoutError:
                            await message.channel.send("입금 실패 (시간초과)")
                            break

            temp_f.close()


        elif "정보" in message.content:
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    if int(info[3]) == 1:
                        Bank_name = "미니은행"
                    
                    elif int(info[3]) == 2:
                        Bank_name = "단풍은행"

                    else:
                        Bank_name = None
                    embed=discord.Embed(title="통장 정보",color=0x00ff56)
                    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/954248874757865482/956138538687152178/bank.png")
                    embed.add_field(name="통장 개설 여부", value=str(info[2]), inline=True)
                    embed.add_field(name="통장 이름", value=Bank_name, inline=True)
                    embed.add_field(name="저금한 금액", value=str(int(info[4])), inline=True)
                    await message.channel.send(embed=embed)
                    break

        else:
            embed=discord.Embed(title="통장 관련 명령어",color=0x00ff56)
            embed.add_field(name=">통장 도움말 ", value="통장 관련 도움말을 확인할 수 있습니다.", inline=False)
            embed.add_field(name=">통장 개설", value="통장을 개설할 수 있습니다. 개설할 수 있는 통장은 도움말을 확인해주세요!", inline=False)
            embed.add_field(name=">통장 정보", value="통장 정보를 확인할 수 있습니다.", inline=False)
            embed.add_field(name=">통장 출금", value="통장에 있는 돈을 출금할 수 있습니다.", inline=False)
            embed.add_field(name=">통장 입금", value="통장에 돈을 입금할 수 있습니다.", inline=False)
            # embed.add_field(name=">입출금내역", value="통장 입출금내역을 확인할 수 있습니다. 날짜는 가입한 날부터 기록됩니다.", inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith(front_command+"복권"):
        if "구매" in message.content:
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            k = 0
            while(k < len(datafile)):
              if datafile[k] == "\n":
                del datafile[k]
              k = k + 1
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()

                    if int(info[1]) < 5000:
                        await message.channel.send("가진 돈이 5000원 미만이라 복권을 구매할 수 없습니다.")
                        break
                        
                    elif info[5] == "Y":
                        await message.channel.send("탈퇴한 계정은 복권 기능을 이용할 수 없습니다.")
                        break

                    else:
                        result_list = []
                        emoji = ['♥️', '💬', '🔔', '🎵', '♻️', '🎁', '🎉', '🎲', '🍉', '🔊', '⌛', '🎀', '💡', '🔍', '🍜', '🔑', '📚', '🍁', '💎', '🎈', '🗺️', '🚀', '✈️', '⚽', '🥇', '🏆', '🎯', '🎨', '🍖']
                        number = random.choices(range(0, 6), weights=[41, 33, 20, 5, 0.075, 0.025])
                        percent_name = ['5,000원', '10,000원', '50,000원', '2,000만원', '5억']
                        number = 1

                        random.shuffle(emoji)

                        if number == 1:
                            first_picture = ""
                            second_picture = ""
                            win_price = ""

                            for i in range(0, 3):
                                while number in result_list:
                                    number = random.choices(range(1,7), weights=[41, 33, 20, 5, 0.075, 0.025])
                                result_list.append(number)

                                result_list.sort()

                            first_picture = emoji[0] + "\n\n" + emoji[1] + emoji[2] + "\n\n" + emoji[3]
                            second_picture = emoji[5] + "\n\n" + emoji[6] + emoji[7] + "\n\n" + emoji[8]
                            win_price = percent_name[result_list[0] - 1] + "\n\n" + percent_name[result_list[1] - 1] + "\n\n" + percent_name[result_list[2] - 1] + "\n\n" + percent_name[result_list[3] - 1]

                            embed=discord.Embed(title="복권", description = "최대 5억원 획득 기회!",color=0x00ff56)
                            embed.add_field(name="첫번째 그림", value = first_picture, inline=True)
                            embed.add_field(name="두번째 그림", value = second_picture, inline=True)
                            embed.add_field(name="당첨 금액", value = win_price, inline=True)
                            # embed.add_field(name=">입출금내역", value="통장 입출금내역을 확인할 수 있습니다. 날짜는 가입한 날부터 기록됩니다.", inline=True)
                            await message.channel.send(embed=embed)


                        else:
                            result_list.append(number)
                            for i in range(0, 3):
                                while number in list:
                                    number = random.choices(range(1,7), weights=[41, 33, 20, 5, 0.075, 0.025])
                                result_list.append(number)

                                result_list.sort()

                            


        elif "확률" in message.content:
            embed=discord.Embed(title="복권 확률", color=0x00ff56)
            embed.add_field(name="복권 확률", value="""
            복권의 확률은 고정적 확률이에요.
            41% 꽝 (0배)
            33% 5,000원 (1배)
            20% 10,000원 (2배)
            5% 50,000원 (10배)
            0.075% 2000만원 (4,000배)
            0.025% 5억원 (100,000배)
            """, inline=False)
            await message.channel.send(embed=embed)

        elif "도움말" in message.content:
            embed=discord.Embed(title="복권 도움말", color=0x00ff56)
            embed.add_field(name="복권으로 인생역전을 노려보세요!", value="""
            최대 5억원까지 나올 수 있는 복권, 인생역전을 노려보세요!
            """, inline=False)
            embed.add_field(name="복권 사용 방법", value="""
            복권은 1매당 5,000원으로,
            복권은 구매 즉시 자동으로 사용되는 상품이에요.
            검은색으로 가려져있는 부분을 긁어 상품을 확인하고
            복권 밑 버튼으로 돈을 받으세요!
            """, inline=False)
            embed.add_field(name="당첨 확인 방법", value="""
            연속된 두 그림 혹은 숫자가 일치하는 경우 해당된 금액이 당첨이 되는 방식이에요.
            일치하는 그림이 하나도 없으면 아쉽지만 당첨되지 않은 꽝이에요. 
            """, inline=False)
            embed.add_field(name="복권 확률", value="""
            도박의 확률은 41% ~ 0.025%까지 다양하게 분포되어 있어요.
            자세한건 >복권 확률을 통해 확인하세요!
            """, inline=False)
            
            await message.channel.send(embed=embed)

        else:
            embed=discord.Embed(title="복권 관련 명령어",color=0x00ff56)
            embed.add_field(name=">복권 구매 ", value="복권을 한장 구매합니다. 복권은 구매 후 바로 사용됩니다.", inline=False)
            embed.add_field(name=">복권 확률", value="복권 확률에 대해 자세한 내용을 확인할 수 있습니다.", inline=False)
            embed.add_field(name=">복권 도움말", value="복권 관련 도움말을 확인할 수 있습니다.", inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith(front_command+"송금"):
        global send_money
        send_check = 0
        user_check = message.content.replace(">송금", "")
        if user_check == "":
            embed=discord.Embed(title="송금 관련 명령어",color=0x00ff56)
            embed.add_field(name=">송금 도움말 ", value="송금 관련 도움말을 확인할 수 있습니다.", inline=False)
            embed.add_field(name=">송금 [유저이름]", value="[유저이름]에게 돈을 보냅니다. 돈은 따로 입력합니다.", inline=False)
            await message.channel.send(embed=embed)
        elif "도움말" in message.content:
            embed=discord.Embed(title="송금 도움말", color=0x00ff56)
            embed.add_field(name="송금 기능을 사용해보세요!", value="""
            통장에 있는 돈을 다른 유저에게 보낼 수 있어요.
            """, inline=False)
            embed.add_field(name="송금은 조건이 필요해요", value="""
            1. 개설된 통장이 있어야 해요
            2. 보낼 유저는 등록된 유저여야해요
            """, inline=False)
            embed.add_field(name="송금의 장점", value="""
            1. 수수료가 없어요
            2. 돈을 안전하게 보낼 수 있어요
            """, inline=False)
            embed.add_field(name="명령어", value="""
            >송금 [유저이름] : 유저에게 돈을 송금해요
            >송금 도움말 : 송금 관련 도움말을 확인해요
            """, inline=False)
            await message.channel.send(embed = embed)
        else:
            temp_f = open("user.txt","r")
            datafile = temp_f.readlines()
            k = 0
            while(k < len(datafile)):
              if datafile[k] == "\n":
                del datafile[k]
              k = k + 1
            for i in range(len(datafile)):
                if message.author.name in datafile[i]:
                    info = datafile[i].split()
                    send_check = 1
                    send_user = info[0]
                    send_money = 0
                    check_money = info[4]
                    user_data = info[0] + " " + str(info[1]) + " " + info[2] + " " + str(info[3]) + " "
                    if info[2] == "N":
                        await message.channel.send("통장을 개설하지 않아 송금기능을 사용할 수 없습니다.")
                        break
                    else:
                        if info[5] == "Y":
                            await message.channel.send("탈퇴한 계정은 송금 기능을 사용할 수 없습니다.")
                            break
                        else:
                            for j in range(len(datafile)):
                                if user_check[1:] in datafile[j]:
                                    info = datafile[j].split()
                                    checknumber = 1
                                    if info[2] == "N":
                                        await message.channel.send(user_check[1:]+"님이 통장을 개설하지 않아 송금기능을 사용할 수 없습니다.")
                                        break
                                    elif info[5] == "Y":
                                        await message.channel.send(user_check[1:]+"님이 탈퇴해 송금 기능을 사용할 수 없습니다.")
                                        break
                                    elif str(user_check[1:]) == str(send_user):
                                        await message.channel.send("본인에게는 송금 기능을 사용할 수 없습니다.")
                                        break
                                    else:
                                        await message.channel.send(user_check[1:]+"님에게 얼마를 보내시겠습니까? (숫자만 입력)")

                                        def check(msg):
                                          global send_money
                                          money = msg.content
                                          if money.isdecimal():
                                              send_money = int(msg.content)
                                              return msg.author == message.author and msg.channel == message.channel
                                          else:
                                              return msg.author == message.author and msg.channel == message.channel
                                        try:
                                            msg = await bot.wait_for('message', timeout = 30.0, check=check)
                                            money = msg.content
                                            if money.isdecimal():
                                              if int(check_money) < int(send_money):
                                                  await message.channel.send("송금 실패 (통장에 있는 돈보다 많은 송금)")
                                              else:
                                                  temp_f.close()
                                                  temp_f = open("user.txt","w")
                                                  datafile[i] = user_data + str(int(check_money)-int(send_money)) + " " + "N"
                                                  datafile[j] = info[0] + " " + str(info[1]) + " " + info[2] + " " + str(info[3]) + " " + str(int(info[4]) + send_money) + " " + "N"
                                                  temp_f.write('\n'.join(datafile))
                                                  
                                                  await message.channel.send(user_check[1:] + "님에게 " + str(send_money) + "원을 정상적으로 보냈습니다.")
                                            else:
                                              await message.channel.send("입금 실패 (숫자만 입력해주세요.)")
                                        except asyncio.TimeoutError:
                                            await message.channel.send("송금 실패 (시간초과)")
                    

                        if checknumber == 0:
                            await message.channel.send("송금할 유저를 찾을 수 없습니다")
                            break
                
            if send_check == 0:
                await message.channel.send("등록하지 않아 송금 서비스를 사용할 수 없습니다. >등록 후 사용해주세요!")
    
            checknumber = 0

bot.run('Nzg4MzU4MzM0MDIxNTAwOTI5.X9iV6Q.G8MNj1Rj0r9fidh5IWl805osE9g')



 
