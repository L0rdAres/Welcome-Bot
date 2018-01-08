from disco.bot import Plugin
import time

class WelcomePlugin(Plugin):
    @Plugin.listen('GuildMemberAdd')
    def listen_server(self, event):
        #Looks like we have a new user!
        member = event.member.user
        print(event.member.guild_id)
        if event.member.guild_id == 308697555359760384:
            print('New member dected! Begin Sending DM')
            #This sends the DM to the new user as it should hopefully
            member.open_dm().send_message('Hello {}, \nWe Welcome you to **Game Center Central**! \n'.format(member.username) +
                                         'Before you start chatting, we need to go over a few rules. \n**1.)** Show respect to other members including Server Admins, Mods, Partnered Streamers, and regular members.\n**2.)** Fire off role commands in <#325424576043679754> - This is to help to prevent <#325409734792445952> from getting spammed with bot commands. \n**3.)** When getting tech support always remain calm and try rebooting your computer.\n**4.)** Please do not ping the whole Mod role, if you are needing help please DM <@343849499455913994> ,that will get you in contact with a mod faster than pinging them.\n**5.)** Try not to ping Ares when he is DND, or Offline. Chances is that he is doing something super important. \n**6.)** When going to grab food always go for Chicken nuggets and fries. \n**7.)** Follow Discord ToS and Guidelines.\n**8.)** No Discord Invite Links.\n'+
                                         '**Discord`s Terms and Serivces and Guildelines** \nhttps://discordapp.com/terms \nhttps://discordapp.com/guidelines \nIf you need any help at anytime, please feel free to contact the mods!')
            print('DM Sent! Now waiting for new members!')

    @Plugin.command('ping')
    def command_ping(self, event):
        print('Am I alive?')
        event.msg.reply('pong')