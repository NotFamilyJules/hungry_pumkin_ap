## Hungry Pumkin AP Setup

### What you need

Release page: https://github.com/NotFamilyJules/hungry_pumkin_ap/releases

- `HungryPumkinAP.apworld`
- `HungryPumkin.yaml`
- Access to an Archipelago installation version `0.6.6` or newer

### Host setup (if you're just playing, just ignore this)

1. Install `HungryPumkinAP.apworld` into your Archipelago by double clicking it after Archipelago is installed.
2. Copy the player's `HungryPumkin.yaml` to the Players folder.
3. Generate the multiworld.
4. Host the room normally through Archipelago.
5. Give the player the room page and address with the port. The tracker will probably be helpful.

### Player setup

1. Install `HungryPumkinAP.apworld` into your Archipelago by double clicking it (Archipelago must be installed, choose to open with Archipelago).
2. Open Archipelago Launcher.
3. Go to Misc on the left, and the click Generate Template Options.
4. A window will open and you can find "Hungry Pumkin.yaml"
5. Edit the file with Notepad or whatever. 
6. Find name: Player{number} and change Player to your name (I also recommend changing {number} to {NUMBER} so it doesn't add a number to your name.)
7. Turn deathlink on by putting 'false': 0 and 'true': 50. (lol)
8. Save, and send the poor bastard setting up the server this yaml file.

### It's time to play the game

1. Ask the server host nicely for the address and port after the game is generated. With please and thank you.
2. Open `https://hungrypumkin.com`.
3. Click the AP logo in the top-left corner of the game.
4. Enter:
   - the room address, `archipelago.gg:PORT`
   - your slot name
   - your password, if your room uses one
5. Click `Connect`.
6. You're now very hungry. Items should disappear from the shelf if done correctly.

### Notes

- The web client is intended to work like other browser-based Archipelago worlds.
- Website-hosted Archipelago rooms should work by entering the given `archipelago.gg:PORT` address directly.
- If someone hosts their own private Archipelago server, it must support secure browser connections to work from the HTTPS web client.

### Checks

- every `Correct` food answer
- every `Incorrect` food answer
