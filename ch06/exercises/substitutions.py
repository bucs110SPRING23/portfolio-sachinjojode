import json

def main():
    text = open("news.txt").read().lower()
    sub_fptr = open("subs.json", "r")
    subs = json.load(sub_fptr)
    print(subs, type(subs))
    
    #use one list to modify another list
    #which list should you loop trough?
    for k,v in subs.items():
        text = text.replace(k,v)
        
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()
    
main()