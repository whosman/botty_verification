import discord
from discord.ext import commands, tasks

keywordbanlist = ["captcha", "scammerbot"]  # keyword list of banned words in usernames
role_id = 123  # role id of verified users
channel_id = 123  # verification channel id
token = "xxx" # from the discord developer panel -> bot section 

class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, custom_id="persistent_view:verify")
    async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
        message = interaction.message
        member = message.guild.get_member(interaction.user.id)
        role = message.guild.get_role(role_id)
        baddy = False
        for items in keywordbanlist:
            if items in member.name.lower():
                await member.ban(reason="baddy")
                baddy = True
        if baddy == False:
            if role not in member.roles:
                await interaction.response.send_message("Verified!", ephemeral=True)
                await member.add_roles(role)
            else:
                await interaction.response.send_message("Already Verified.", ephemeral=True)
        else:
            print("baddy detected")

class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(">>>"), intents=intents)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistentView())
            self.persistent_views_added = True
        if not usercheck.is_running():
            usercheck.start()

        print(f"Logged in as {self.user} (ID: {self.user.id})")

bot = PersistentViewBot()

@bot.command()
async def postbutton(ctx: commands.Context):
    await ctx.send("Verify that you are (probably) human.", view=PersistentView())

@bot.event
async def on_member_join(member):
    for items in keywordbanlist:
        if items in member.name.lower():
            print("banning: " + member.name)
            await member.ban(reason="bot")

@tasks.loop(seconds=10)
async def usercheck():
    channel = bot.get_channel(channel_id)
    users = channel.members
    for members in users:
        for items in keywordbanlist:
            if items in members.name.lower():
                print("banning: " + members.name)
                await members.ban(reason="bot")

bot.run(token)
