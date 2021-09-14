##### kaikki viety engine.py

from engine import hash, readwordlist, bruteforce



url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'hacker'
actual_password_hash = hash(actual_password)
 
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't crack your password. This is good news for you! You win (: ")
 