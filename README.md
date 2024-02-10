# Hawkeye Bot
Official Discord bot of the Dundoody Hawks.
Hawkeye bot itself is restricted to the Hawks Discord, 
but with minor tweaks the code will work for any bot in any server.

## Features
Hawkeye features the following commands:

- Purge (Number)
 - Deletes specified number of messages from the channel
 - Usable by those with `manage_messages` permission
- Kick (User, Reason)
 - Kicks specified user from server with specified reason
 - Usable by those with `kick_members` permission
- Ban (User, Reason)
 - Bans specified user from server with specified reason
 - Usable by those with `ban_members` permission

Hawkeye also listens for any message containing a Discord server invite.
The bot owner must set the `promoChannel` and `logChannel` values to the channel ID's of the channels where the bot should
allow invites to be posted, and log deleted invites respectively. Failure to set these values will cause errors, so do it!

### Bug Reports
If you encounter a bug or any problem with the bot, feel free
to create an Issue on GitHub, DM me on Discord (.flyx), or [join my Discord server](https://discord.gg/flyx) and notify me there.