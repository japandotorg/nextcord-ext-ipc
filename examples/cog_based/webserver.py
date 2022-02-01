from quart import Quart
from nextcord.ext import ipc

app = Quart(__name__)
ipc_client = ipc.Client(secret_key="my/bots/secret/key") # secret_key must be the same as your server

@app.route('/')
async def index():
    member_count = await ipc_client.request(
        "get_member_count",
        guild_id=123456789
    ) # get the member count of the server with ID 123456789
    
    return str(member_count) # display member count

if __name__ == "__main__":
    app.run()