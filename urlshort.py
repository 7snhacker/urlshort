# 7snhacker
def url():
    print("""            _     _                _   
 _   _ _ __| |___| |__   ___  _ __| |_ 
| | | | '__| / __| '_ \ / _ \| '__| __|
| |_| | |  | \__ \ | | | (_) | |  | |_ 
 \__,_|_|  |_|___/_| |_|\___/|_|   \__|
                                       """)
    url = input(" instagram / snapchat / facebook >> ")
    urlshort1 = input("ShortCut >> ").replace("https://", "")
    if url == "instagram":
        print("Success Link >> https://instagram.com-instagram@" + urlshort1)
        print("Thanks For Useing Script")
    elif url == "snapchat":
        print("Success Link >> https://snapchat.com-snapchat@" + urlshort1)
        print("Thanks For Useing Script") 
    elif url == "facebook":
        print("Success Link >> https://facebook.com-facebook@" + urlshort1)
        print("Thanks For Useing Script")
    else:
        print("Somthing Wrong try again [!]")
        print("Thanks For Useing Script")
    

url()

