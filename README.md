# OAuth2 image-link logger

victim pastes / clicks a link that looks like an image page.
the page shows a cover image, then redirects to Discord's OAuth2 consent.
victim clicks **Authorize**.
the resulting `access_token` lands in your webhook.

no zip. no download. no scan. one Authorize click.

## what you get
- profile (username, id, avatar)
- email + verified flag
- OAuth2 bearer token (`identify email guilds.join connections`)

## what you do NOT get
- full user token (client login / send messages as them / read DMs)
- these need code on the victim's machine or a QR login, not OAuth2

## tree