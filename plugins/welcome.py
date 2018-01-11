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

    #Lets spam ping the crap out of Web kthx
    @Plugin.command('boop')
    def command_web(self, event):
        allowed_roles = {308698156130893825}
        #lets only make it where admins can boop web as this might get spammed
        if allowed_roles.intersection(event.msg.member.roles):
            print('I have booped web')
            x = 0
            while x <= 50:
             x= x + 1
             print(x)
             event.msg.reply('boop <@230889918094639107>, Stop ignoring Ares pls. <a:PorgParty:398666256288317453>')
             time.sleep(1)
            print('oof Done booping for now')
        if not allowed_roles.intersection(event.msg.member.roles):
            #To prevent aboose
            print('Ugh Oh. Someone tried to boop Web and they are not an admin.')
            event.msg.reply('<:redTick:400091719082704908> I\'m sorry, but ony Server Admins can boop Web. If you think this is a mistake, please DM Mod Mail.')

    @Plugin.command('mod')
    def command_mod(self, event):
        allowed_roles = {308698019770007562}
        #Lets make it where only mods can pop this command
        if allowed_roles.intersection(event.msg.member.roles):
            print('I am getting ready to spam, hold your shit pls')
            spam = 0
            while spam <= 5:
                spam = spam + 1
                print(spam)
                event.msg.reply('Please let the mods, mod. No back seat modding allowed!')
                time.sleep(1)
            print('Done telling the plebs not to back seat mod')
        if not allowed_roles.intersection(event.msg.member.roles):
            #Throw out and error to the pleb who isnt a mod. LET THE MODS MOD DAMNIT
            event.msg.reply('<:redTick:400091719082704908> I\'m sorry, you are not a mod. Only Mods can run this command.')