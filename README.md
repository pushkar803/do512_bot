# do512_bot

1 required python 3.X<br><br>
2 extract project<br><br>
3 pip install -r requirements.txt<br><br>

4 create folder anywhere with any name <br><br>
5 then go to chrome installation folder usually (C:\Program Files (x86)\Google\Chrome\Application) and open cmd there and type following command, instead of c:\selenium\prof1\  give path of folder that u created in step 4<br><br>
chrome.exe --user-data-dir=c:\selenium\prof1\   <br><br>

6 create a shortcut of newly created chrome profile and then open chrome by that shortcut<br><br>
7 install anticapcha plugin in this chrome profile  (follow https://antcpt.com/eng/download/google-chrome-options/manual-crx.html) registory file and extention file is in project folder <br><br>
anticapcha key this u need to put inanticapcha extention settings<br><br>

8 after this type python create_users.py to run script this will create input given number of users on do512<br><br>
9 and to upvode and downvote type python vote.py (input action i.e. upvote or downvote)<br><br>
