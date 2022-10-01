print('hello world')

client = commands.Bot(command_prefix = '!',intents=intents)
status_loop = cycle(['Valorant', 'With my own life'])
print('yolo')
print('yahooo!!')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')
