# TiltShield

When you play online games, you're inevitably going to get horrible matches at some point. If you're left in a situation where the enemy team is cheating, your own side is full of verbally abusive children, or any another unenjoyable circumstance, at a certain point it's better to just pull the plug and just try to play on your own. After one too many games with toxic teammates, I noticed that most of the time, I would play the round, die, then turn up my music until the next round started. I decided that automating this process would be a worthwhile project to tackle, and TiltShield was born. 

## How does it work?

CSGO has a very robust [Game State Integration](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration) system that you can leverage to do all kinds of cool stuff. For example, it's how they do the fancy effects at LAN events (when those existed, anyways...). All you have to do is have an HTTP server that accepts POST requests and give CSGO a `.cfg` file that tells it where to send the data. In essence, TiltShield simply receives POST data and turns media on/off in response to changes in game state.

## Installation

Still in progress!
