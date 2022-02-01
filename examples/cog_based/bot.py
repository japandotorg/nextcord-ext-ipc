import nextcord
from nextcord.ext import commands, ipc


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="my/bots/secret/key")  # create our IPC Server

        self.load_extension("cogs.ipc")  # load the IPC Route cog

    async def on_ready(self):
        """ The bot READY event """
        print("Bot is ready.")

    async def on_ipc_ready(self):
        """ The IPC Server being ready """
        print("Ipc is ready.")

    async def on_ipc_error(self, endpoint, error):
        """ Listening to the errors being raised within an IPC route """
        print(endpoint, "raised", error)


client = Client(command_prefix="$", intents=nextcord.Intents.all())


if __name__ == "__main__":
    client.ipc.start()  # start the IPC Server
    client.run("TOKEN")