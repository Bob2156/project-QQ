import os
from aiohttp import web
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Webhook endpoint to handle events
async def handle(request):
    data = await request.json()
    if "message" in data and data["message"].startswith("!ping"):
        # Respond to the webhook
        return web.json_response({"response": "Pong!"})

    return web.Response(text="Bot is running", status=200)

# Create aiohttp application
app = web.Application()
app.router.add_post("/", handle)

if __name__ == "__main__":
    web.run_app(app, port=3000)
