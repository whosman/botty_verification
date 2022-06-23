
# botty_verification ✔️

Button verification with periodic username keyword search & join scan to cleanup bots!

## Install Requirements:  
```
git clone https://github.com/whosman/botty_verification
cd /botty_verification
pip install -r requirements.txt
git clone https://github.com/Pycord-Development/pycord
cd pycord
pip install -U .[voice]
```
## Setting up the Discord Bot
1. Navigate to the Discord Developer Portal  
2. Select “New Application” then name accordingly  
4. Select “Bot” on the list of settings to the left  
6. Select “Reset Token”, copy-paste this string into the “token” variable near the top of the python script  
7. Set a cool icon + username underneath “Build-A-Bot”  
8. Toggle off “Public Bot”  
9. Scroll down a bit - Toggle on “PRESENCE INTENT”, “SERVER MEMBERS INTENT” and “MESSAGE CONTENT INTENT”  
10. SAVE CHANGES  
11. Select “OAuth2” on the list of settings to the left then select URL generator underneath  
12. Under SCOPES, enable “bot” and “applications.commands”  
13. Under “BOT PERMISSIONS”, enable:  
      - Manage Roles  
      - Kick members  
      - Ban members  
      - Read Messages/View Channels  
      - Send Messages  
      - Use Slash Commands  
14. Copy the generated URL at the bottom and paste into a browser  
15. Go through the prompts to add the bot into the server  
16. In Discord, navigate to server settings -> roles and move the bot role on top by hovering to the left of the grey shield icon and drag it up.  
17. SAVE CHANGES  
18. Click the triple dots near the right side and copy the role ID of the verification role - paste this into the `role_id` variable in the python script  
   
   <img width="707" alt="screencap" src="https://user-images.githubusercontent.com/33681794/175198287-af79cfbe-d6f1-466a-a3fb-50cec0a207c6.png">
  
19. Escape - right click on the verification channel and “Copy ID” - paste this into the `channel_id` variable in the python script  
20. Fill the `keywordban` list array in the python script with more entries. (caution, if any of these words are in someones username it will instantly ban them)  

## Usage
1. Host & run this externally for reliable 24/7 usage
2. Python output from the script should just be "Logged in as xxx#xx" (your discord bot username)
3. In the verification channel (id of which matches `channel_id` in main.py), send ">>>postbutton" to trigger the bot to post the verification button
