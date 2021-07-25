from io import BytesIO

import discord
from PIL import Image
from discord.ext import commands
from quickchart import QuickChart

description = '''An example bot to showcase the use of QuickChart with discord.py module.'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def graph(ctx):
    qc = QuickChart()
    qc.width = 600
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = {
        "type": "bar",
        "data": {
            "labels": ["Hello world", "Test"],
            "datasets": [{
                "label": "Foo",
                "data": [1, 2]
            }]
        }
    }
    with Image.open(BytesIO(qc.get_bytes())) as chat_sample:
        output_buffer = BytesIO()  # By using BytesIO we don't have to save the file in our system.
        chat_sample.save(output_buffer, "png")
        output_buffer.seek(0)
    await ctx.send(file=discord.File(fp=output_buffer, filename="chart_sample.png"))  # Change the file name accordingly.


@graph.before_invoke
async def before_test_invoke(ctx):
    await ctx.trigger_typing()  # Take time to render and send graph so triggering typing to reflect bot action.

bot.run('token')
