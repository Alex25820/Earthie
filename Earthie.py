import discord
from discord.ext import commands
import os
import random
from datetime import date

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
	print("Bot is ready.")

#Help
@client.command()
async def help (ctx):
	embed = discord.Embed(title = "Help", description = "Here is a list of all Earthie's commands.", color = 0x3cf03c)
	embed.add_field(name ="\u200b", value =".help - Shows this message.", inline = False)
	embed.add_field(name ="\u200b", value =".about - Shows information about this bot.", inline = False)
	embed.add_field(name ="\u200b", value =".github - Gives you a link to this bots github page.", inline = False)
	embed.add_field(name ="\u200b", value =".orgs - Shows a list of organizations that are dedicated to saving our planet.", inline = False)
	embed.add_field(name ="\u200b", value =".time_left - Shows a list of all time left commands.", inline = False)
	embed.add_field(name ="\u200b", value =".fact - Gives you a random fact about saving our planet.", inline = False)
	embed.add_field(name ="\u200b", value =".ice - Shows you how earth would look if all the ice melted.", inline = False)
	embed.add_field(name ="\u200b", value =".ping - Pong, shows you the bots ping.", inline = False)
	await ctx.send(embed = embed)

#About
@client.command()
async def about (ctx):
	embed = discord.Embed(title = "About", description = "Earthie is a discord bot dedicated to informing you about the state of our planet. Earthie was created by Alex25820#8116 as a submition for the first ever discord hack week.", color = 0x18abf5)
	embed.add_field(name ="\u200b", value ="Use .github to get a link to Earthie's github page where you can report bugs.", inline = False)
	embed.add_field(name ="\u200b", value ="Use .help to get a list of all Earthie's commands.", inline = False)
	await ctx.send(embed = embed)

#Github
@client.command()
async def github (ctx):
	embed = discord.Embed(title = "Github", description = "Here is a link to Earthie's github page. If you have found any bugs please report them here.", color = 0xffffff)
	embed.add_field(name ="\u200b", value ="Link: https://github.com/Alex25820/Earthie", inline = False)
	await ctx.send(embed = embed)

#Orgs
@client.command()
async def orgs (ctx):
	embed = discord.Embed(title = "Orgs", description = "Here are some organizations that are dedicated to saving our planet.", color = 0xeb57ff)
	embed.add_field(name ="United Nations", value ="https://www.un.org/en/", inline = False)
	embed.add_field(name ="WWF", value ="https://www.worldwildlife.org", inline = False)
	embed.add_field(name ="Bill & Melinda Gates Foundation", value ="https://www.gatesfoundation.org", inline = False)
	embed.add_field(name ="Union of Concerned Scientists", value ="https://www.ucsusa.org", inline = False)
	embed.add_field(name ="4Ocean", value ="https://4ocean.com", inline = False)
	await ctx.send(embed = embed)

#Time left
@client.command()
async def time_left (ctx):
	embed = discord.Embed(title = "Time left commands", description = "Here are all the time left commands.", color = 0xe34242)
	embed.add_field(name ="\u200b", value =".oil - Shows how many days until the oil runs out.", inline = False)
	embed.add_field(name ="\u200b", value =".ccirreversible - Shows how many days we have left to prevent irreversible damage from climate change.", inline = False)
	embed.add_field(name ="\u200b", value =".naturalgas - Shows how many days until the natural gas runs out.", inline = False)
	embed.add_field(name ="\u200b", value =".coal - Shows how many days until the coal runs out.", inline = False)
	await ctx.send(embed = embed)
		
#Oil
@client.command()
async def oil (ctx):
	runout_date = date(2063, 6, 23)
	current_date = date.today()
	days_left1 = runout_date - current_date
	days_left2 = days_left1.days
	embed = discord.Embed(title ="Oil", description =f"There is {days_left2} days until the oil runs out.", color = 0x000000)
	embed.set_footer(text = "Source: Worldometers.info")
	await ctx.send(embed = embed)

#Climate change irreversible
@client.command()
async def ccirreversible (ctx):
	runout_date = date(2030, 3, 28)
	current_date = date.today()
	days_left1 = runout_date - current_date
	days_left2 = days_left1.days
	embed = discord.Embed(title ="Irreversible damage", description =f"There is {days_left2} days until climate change has caused irreversible damage.", color = 0xe34242)
	embed.set_footer(text = "Source: United Nations")
	await ctx.send(embed = embed)
	
#Natural gas
@client.command()
async def naturalgas (ctx):
	runout_date = date(2177, 6, 26)
	current_date = date.today()
	days_left1 = runout_date - current_date
	days_left2 = days_left1.days
	embed = discord.Embed(title ="Natural gas", description =f"There is {days_left2} days until the natural gas runs out.", color = 0x73a82d)
	embed.set_footer(text = "Source: Worldometers.info")
	await ctx.send(embed = embed)

#Coal
@client.command()
async def coal (ctx):
	runout_date = date(2427, 6, 26)
	current_date = date.today()
	days_left1 = runout_date - current_date
	days_left2 = days_left1.days
	embed = discord.Embed(title ="Coal", description =f"There is {days_left2} days until the coal runs out.", color = 0x000000)
	embed.set_footer(text = "Source: Worldometers.info")
	await ctx.send(embed = embed)

#Random fact
desc_list = ["Ireland is ranked worst in the EU for performance on climate change action", "Rainforest destruction is a major cause of carbon dioxide releases", "Average sea level is expected to rise between 0.5 and 1.5 metres before the end of the century", "The United States is the second largest contributor to carbon dioxide (CO2) in our atmosphere", "Global temperatures have increased by about 1° Celsius in the past century", "The average temperature of the Earth is determined by the greenhouse effect", "Most of the increase in global temperatures since 1950 has been caused by human activity", "195 countries signed the 2015 Paris Agreement, agreeing to limit global warming and adapt to climate change, partly by protecting nature", "Tropical forests are incredibly effective at storing carbon providing at least 30% of action needed to prevent the worst climate change scenarios. Yet nature-based solutions receive only 2% of all climate funding", "An area of coastal ecosystems larger than New York City is destroyed every year, removing an important buffer from extreme weather for coastal communities and releasing carbon dioxide into the atmosphere", "Eleven percent of the world’s population is currently vulnerable to climate change impacts such as droughts, floods, heat waves, extreme weather events and sea-level rise", "The concentration of carbon dioxide (CO2)​​​​​​​ in our atmosphere, as of 2018, is the highest it has been in 3 million years", "By maintaining the current rate of progress, poverty should reach its target eradication around 2025-2030", "Some 54 percent of Americans are considered to be living below the poverty line", "About 30 percent of the world’s extremely poor live in India", "One frappuccino at Starbucks costs more than the median income for people in the developing world ($3 a day)", "According to an Oxfam report, if the world’s 100 richest people pooled their collective earnings in 2012, they could have ended extreme world poverty four times over", "In 2011, about 800 children under the age of five died every hour", "A quarter of humanity, 1.6 billion people, lives without electricity", "The average income of extreme poverty in a developing world rose from 74 cents to 87 cents per day from 1981 to 2010", "Global poverty has decreased by half over the last decade however, 71 percent of the population still live in low-income or poor ($10 a day) conditions", "A third of all poor in developing countries are children aged zero to 12", "There are 2.2 billion children in the world, and 1 billion of them live in poverty", "Nearly 22,000 children die each day due to living in poverty", "Scientists believe that pollution, land clearing, and overfishing might drive half of the planet’s existing land and marine species to extinction by 2100", "Among the most famous species driven to extinction by humans is the dodo", "A quarter of mammals is at risk of extinction", "Our big cats, including tigers, leopards, and cheetahs are in critical decline, and many will become extinct in the next decade", "The American Bison once numbered in the millions and roamed from Alaska to Mexico. They now occupy less than one percent of their original habitat", "Lizard populations are especially vulnerable to climate change. A recent study projects that if the current decline in lizard populations continues, 40% of all lizard species will be extinct by 2080", "40% of the world’s bird species are in decline and 1 in 8 is threatened with global extinction", "Worldwide, more than 650,000 marine mammals are caught or seriously injured by fishing gear annually"]
source_list = ["Spunout.ie", "Spunout.ie", "Spunout.ie", "Spunout.ie", "Spunout.ie", "Spunout.ie", "Spunout.ie", "Conservation.org", "Conservation.org", "Conservation.org", "Conservation.org", "Conservation.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "Borgenproject.org", "National Geographic", "National Geographic", "National Geographic", "Earthday.org", "Earthday.org", "Earthday.org", "Earthday.org", "Earthday.org"]
	
@client.command()
async def fact (ctx):
	global desc_list
	global source_list
	random_number = random.randint(0, ((len(desc_list))-1))
	desc = (desc_list[random_number])
	source = (source_list[random_number])
	embed = discord.Embed(description = f"{desc}.", color = 0x73c773)
	embed.set_footer(text = f"Source: {source}")
	await ctx.send(embed = embed)
	
#Ice
@client.command()
async def ice (ctx):
	embed = discord.Embed(title = "Ice", description = "Here is what the world would look like if all the ice melted.", color = 0xffffff)
	embed.add_field(name = "North America", value = "https://bit.ly/2IN2gIE", inline = True)
	embed.add_field(name = "South America", value = "https://bit.ly/2X5PUPE", inline = True)
	embed.add_field(name = "Europe", value = "https://bit.ly/2X9zg6E", inline = True)
	embed.add_field(name = "Asia", value = "https://bit.ly/2X4EyLE", inline = True)
	embed.add_field(name = "Africa", value = "https://bit.ly/31VyIjy", inline = True)
	embed.add_field(name = "Australia", value = "https://bit.ly/2XAqD4o", inline = True)
	embed.add_field(name = "Antarctica", value = "https://bit.ly/2ZMAT78", inline = True)
	embed.set_footer(text = "Source: National Geographic")
	await ctx.send(embed = embed)

	
#Ping
@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! The ping of the bot is {round(client.latency * 1000)} ms.")

client.run(os.environ['TOKEN'])
