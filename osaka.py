import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta
from typing import Optional

Token = ''  # Token for the bot

intents = discord.Intents.default()
intents.message_content = True
    

class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()   # Sync slash commands with Discord

bot = MyBot(command_prefix="!", intents=intents)

#Bot commands

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Slash command

@bot.tree.command(name="hello", description="Say hello!") #say hello
@app_commands.default_permissions(send_messages=True)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@bot.tree.command(name="ping", description="Check bot latency") #ping
@app_commands.default_permissions(send_messages=True)
async def ping(interaction: discord.Interaction):      
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms", ephemeral=True)

@bot.tree.command(name="say", description="say a message") #say message
@app_commands.describe(message="The message to say")
@app_commands.default_permissions(send_messages=True)
async def say(interaction: discord.Interaction, message:str):   
    if message:
        await interaction.response.send_message(message)
    if not message:
        await interaction.response.send_message("**you must select message** ⚠️", ephemeral=True)


@bot.tree.command(name="clear-channel", description="Clear all messages in the channel") #delete channel messages
@app_commands.default_permissions(manage_messages=True)
async def clear_channel(interaction: discord.Interaction):
    await interaction.channel.purge(limit=None)
    await interaction.response.send_message('**channel has been cleared** ✅', ephemeral=True)


@bot.tree.command(name="kick", description="Kick a user from the server") #kick user
@app_commands.describe(user="The user to kick")
@app_commands.default_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, user: discord.Member):
    if user:
        await user.kick(reason="womp womp :)")
        await interaction.response.send_message(f"**you kicked the {user} ✅**", ephemeral=True)
    if not user:
        await interaction.response.send_message("**you must select a user** ⚠️", ephemeral=True)

@bot.tree.command(name="ban") #ban user
@app_commands.describe(user="The user to ban")
@app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, user: discord.Member):
    if user:
        await user.ban(reason="womp womp :)")
        await interaction.response.send_message(f"**you banned the {user} ✅**", ephemeral=True)
    if not user:
        await interaction.response.send_message("**you must select a user** ⚠️", ephemeral=True)
        
@bot.tree.command(name="unban") #unban user
@app_commands.describe(user="The user to unban")
@app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, user: discord.Member):
    if user:
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"**you unbanned the {user} ✅**", ephemeral=True)
    if not user:
        await interaction.response.send_message("**you must select a user** ⚠️", ephemeral=True)

@bot.tree.command(name="timeout") #timeout user
@app_commands.describe(user="The user to timeout")
@app_commands.default_permissions(moderate_members=True)
async def timeout(interaction: discord.Interaction, user: discord.Member, minutes: int):
    if user:
        await user.timeout(timedelta(minutes=minutes), reason="womp womp :)")
        await interaction.response.send_message(f"**you timeout the {user} ✅**", ephemeral=True)
    if not user:
        await interaction.response.send_message("**you must select a user** ⚠️", ephemeral=True)
        
@bot.tree.command(name="untimeout") #untimeout user
@app_commands.describe(user="The user to  untimeout")
@app_commands.default_permissions(moderate_members=True)
async def timeout(interaction: discord.Interaction, user: discord.Member, minutes: int):
    if user:
        await user.timeout(None)
        await interaction.response.send_message(f"**you untimeout the {user} ✅**", ephemeral=True)
    if not user:
        await interaction.response.send_message("**you must select a user** ⚠️", ephemeral=True)

@bot.tree.command(name="channel-delete") #delete channel
@app_commands.describe(tchannel="The text channel to delete", vchannel="The voice channel to delete")
@app_commands.default_permissions(manage_channels=True)
async def channeldel(interaction: discord.Interaction, tchannel: Optional[discord.TextChannel] = None, vchannel: Optional[discord.VoiceChannel] = None):
    if tchannel:
        await tchannel.delete()
        await interaction.response.send_message(f"channel {tchannel} deleter :)", ephemeral=True)
    elif vchannel:
        await vchannel.delete()
        await interaction.response.send_message(f"channel {vchannel} deleter :)", ephemeral=True)
    
    await interaction.response.send_message("**you must select a channel** ⚠️", ephemeral=True)

@bot.tree.command(name="server-info") #server info
@app_commands.default_permissions(send_message=True,use_commands=True)
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title =f"📊 server info: {guild.name}"color discord.color.blurple())
    
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="🆔 server ID", value=guild.id, inline=True)
    embed.add_field(name="👑 Owner", value=guild.owner, inline=True)
    embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
    embed.add_field(name="📁 Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="📅 Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
    
    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(name="user-info") #user info
@app_commands.describe(member="The member to get info about")
@app_commands.default_permissions(send_message=True,use_commands=True)
async def user_info(interaction: discord.Interaction,member: discord.Member | None = None):
    member = member or interaction.user

    embed = discord.Embed(title=f"👤 User Info: {member}", color=member.color)
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)

    embed.add_field(name="🆔 User ID", value=member.id, inline=True)
    embed.add_field(name="🤖 Bot", value=member.bot, inline=True)
    embed.add_field(name="📛 Nickname", value=member.nick or "None", inline=True)

    embed.add_field(name="📅 Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="📥 Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="⏳ Timed Out", value=member.is_timed_out(), inline=True)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="lock", description="Lock a text or voice channel")
@app_commands.describe(channel="The channel to lock")
@app_commands.default_permissions(manage_channels=True)
async def lock(interaction: discord.Interaction,channel: Optional[discord.abc.GuildChannel] = None):
    
    channel = channel or interaction.channel
    everyone = interaction.guild.default_role
    overwrite = channel.overwrite_for(every one)
    
    if isinstance(channel, discord.TextChannel):
        overwrite.send_messages = False
    if isinstance(channel, discord.VoiceChannelChannel):
        overwrite.connect = False
    else:
        return await interaction.response.send_message("❌ Unsupported channel type", ephemeral=True)
        
    await channel.set_permissions(everyone, overwrite=overwrite)
    await interaction.response.send_message(f"🔒 **{channel.mention} has been locked**", ephemeral=True)
    
@bot.tree.command(name="unlock", description="Unlock a text or voice channel")
@app_commands.describe(channel="The channel to unlock")
@app_commands.default_permissions(manage_channels=True)   
    
    channel = channel or interaction.channel
    everyone = interaction.guild.default_role
    overwrite = channel.overwrites_for(everyone)

    if isinstance(channel, discord.TextChannel):
        overwrite.send_messages = True
    elif isinstance(channel, discord.VoiceChannel):
        overwrite.connect = True
    else:
        return await interaction.response.send_message("❌ Unsupported channel type", ephemeral=True)

    await channel.set_permissions(everyone, overwrite=overwrite)
    await interaction.response.send_message(f"🔒 **{channel.mention} has been unlocked**", ephemeral=True)

bot.run(Token)