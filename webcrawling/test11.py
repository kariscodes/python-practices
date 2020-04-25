#Failed

import google

# to search
query = "Geeksforgeeks"

for j in google.doGoogleSearch(query, 0, 10, 1):

        #(query, tld="co.in", num=10, stop=1, pause=2):
    print(j)