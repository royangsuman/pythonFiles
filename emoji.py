message = input ("Enter your message ")
words = message.split(' ')
emoji = {
    ":)" : "hehe",
    ":(" : "WoooooHHHH"
}
out = ""
for ch in words:
    out += emoji.get(ch,ch) + " "

print(out)