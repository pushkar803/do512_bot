# do512_bot

1 required python 3.X
2 extract project
3 pip install -r requirements.txt

4 create folder anywhere with any name 
5 then go to chrome installation folder usually (C:\Program Files (x86)\Google\Chrome\Application) and open cmd there and type following command, instead of c:\selenium\prof1\  give path of folder that u created in step 4
chrome.exe --user-data-dir=c:\selenium\prof1\   

6 create a shortcut of newly created chrome profile and then open chrome by that shortcut
7 install anticapcha plugin in this chrome profile  (follow https://antcpt.com/eng/download/google-chrome-options/manual-crx.html) registory file and extention file is in project folder 
anticapcha key this u need to put inanticapcha extention settings

8 after this type python create_users.py to run script this will create input given number of users on do512
9 and to upvode and downvote type python vote.py (input action i.e. upvote or downvote)
