#Source Code

from urllib import request
from win10toast import ToastNotifier

#Getting responce from the given webpage

resp=request.urlopen("https://www.indiatoday.in/world")
resp=resp.read()               #Reading the source code of the webpage.
string=str(resp)               #Source code of teh webpage is of type 'bytes'...so converting it into string and Storing it.
i=string.find("<h2")           #Finding the index of the starting of the first heading in the HTML file i.e <h2.
i+=20                          # i+=20 because usefull required information lies from the 20th index from the starting index of the heading.
news=''                        #Empty string.

# Recieving the first news headline

while string[i] != '"':
    news += string[i]
    i += 1


#Showing the notification

notify=ToastNotifier()
notify.show_toast("Top News Headline of The Day",news+"\n\nhttps://www.indiatoday.in/world")
