import nextcord
from nextcord.ext import commands, ipc

class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ipc = ipc.Server(self, secret_key="my/bots/secret/key") # create the IPC Server
        
    async def on_ready(self):
        """ The bot READY event """
        print("[ BOT ] is connected to Discord...")
        
    async def on_ipc_ready(self):
        """ The IPC Server being ready """
        print("IPC server connected...")
        
    async def on_ipc_error(self, endpoint, error):
        """ Listening to the errors being raised within an IPC route """
        print(endpoint, "raised", error)
        
client = Client(commands_prefix="$", intents=nextcord.Intents.all())

@client.ipc.route()
async def get_member_count(data):
    guild = client.get_guild(data.guild_id) # get the guild object using parsed guild_id
    
    return guild.member_count

if __name__ == "__main__":
    client.ipc.start() # start the IPC Server
    client.run("TOKEN")