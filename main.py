import discord
from discord.ui import Button, View
from discord.ext import commands, tasks

role_id = 987450688051228733  # role of verified users
channel_id = 987452567288184874  # should be the verification channel
keywordbanlist = ["captcha", "scammerbot"]  # keyword list of banned words in usernames
# client secret 41105O1ntz3REgyJgTaU2jpCDNod58kF
token = 'OTg5MzEwNjMzNjU4OTQxNDYx.GGUrf_.vUBL4jiZFZNOMXsVX_Hy-veQfp7spcDiIk5GrA' # new new
# token = 'OTg3NDk0NTc3NjE3MzcxMTU4.G13lyq.qpB8frbMXHNqMLvIMptH5lPwirgLp_5G0ApwYI'
# token = 'OTg5MzEwNjMzNjU4OTQxNDYx.GRT_1i.ezjMIn7uz-_CB9SLsyE0ar-51XRuvsmXSSlM98'

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=">>>", intents=intents)


@bot.event
async def on_ready():
    print('Logged in as ' + str(bot.user))
    if not usercheck.is_running():
        usercheck.start()


@bot.event
async def on_member_join(member):
    for items in keywordbanlist:
        if items in member.name.lower():
            print("banning: " + member.name)
            await member.ban(reason="bot")


@bot.command()
async def postbutton(ctx):
    button = Button(label="Verify", style=discord.ButtonStyle.green, emoji="✔️")

    async def button_callback(interaction):
        message = interaction.message
        member = message.guild.get_member(interaction.user.id)
        role = message.guild.get_role(role_id)
        if "captcha" in member.name.lower():
            print("banning: " + member.name)
            await member.ban(reason="bot")
        try:
            await member.add_roles(role)
            await interaction.response.defer()
            await interaction.followup.send("Verified!", ephemeral=True)
        except:
            pass

    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.send("Click below to prove you are (probably) human.", view=view)


@tasks.loop(seconds=10)
async def usercheck():
    channel = bot.get_channel(channel_id)
    users = channel.members
    for members in users:
        if "captcha" in members.name.lower():
            print("banning: " + members.name)
            await members.ban(reason="bot")


bot.run(token)
