from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	wordcountdic = {}

	for word in wordlist:
		if word in wordcountdic:
			#Increase
			wordcountdic[word] += 1
		else:
			#add to dictoinary
			wordcountdic[word] = 1

	sortedword = sorted(wordcountdic.items(), key=operator.itemgetter(1), reverse=True)


	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedword': sortedword})

def about(request):
	return render(request, 'about.html')