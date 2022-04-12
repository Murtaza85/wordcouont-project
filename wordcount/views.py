from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is Engr Shani'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext, 'counts':len(wordlist), 'worddictionary':worddictionary.items()})



def aboutus(request):
    return render(request, 'aboutus.html')



