# ────────────────────────────────────────────────────────────────

# ✅ THIS PROJECT IS DEVELOPED AND MAINTAINED BY @trinityXmods (TELEGRAM)
# 🚫 DO NOT REMOVE OR ALTER THIS CREDIT LINE UNDER ANY CIRCUMSTANCES.

# ⭐ FOR MORE HIGH-QUALITY OPEN-SOURCE BOTS, FOLLOW US ON GITHUB.
# 🔗 OFFICIAL GITHUB: https://github.com/Trinity-Mods
# 📩 NEED HELP OR HAVE QUESTIONS? REACH OUT VIA TELEGRAM: @velvetexams

# ────────────────────────────────────────────────────────────────

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("FileSharingBot_v1")

# ────────────────────────────────────────────────────────────────

# ✅ THIS PROJECT IS DEVELOPED AND MAINTAINED BY @trinityXmods (TELEGRAM)
# 🚫 DO NOT REMOVE OR ALTER THIS CREDIT LINE UNDER ANY CIRCUMSTANCES.

# ⭐ FOR MORE HIGH-QUALITY OPEN-SOURCE BOTS, FOLLOW US ON GITHUB.
# 🔗 OFFICIAL GITHUB: https://github.com/Trinity-Mods
# 📩 NEED HELP OR HAVE QUESTIONS? REACH OUT VIA TELEGRAM: @velvetexams

# ────────────────────────────────────────────────────────────────

