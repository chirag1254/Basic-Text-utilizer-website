# i created this file

from django.http import HttpResponse
from django.shortcuts import render





def home(request):

    return render(request, 'home.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    test = djtext
    analyzed_text = ''
    
    

        
    if test =='' :
        
        return HttpResponse("Error")

    #Remove Punctuations
    if removepunc == 'on':
        punctuations = '''!()-[]{;:}'"\,<>./?@#$%^&*_~'''
        
        for j in test:
            if j not in punctuations:
                
                analyzed_text = analyzed_text+j
                
        test = analyzed_text

    # Uppercase The text            
    if uppercase == 'on':
        analyzed_text = ''
        for char in test:
            analyzed_text = analyzed_text+char.upper()
        test = analyzed_text

     # Capitalize text       
    if capitalize == 'on':
        analyzed_text = ''
        analyzed_text = test.capitalize()
        test = analyzed_text
    
    #New line remover
    if newlineremover == 'on':
        analyzed_text = ''
        for char in test:
            if char != "\n" and char!="\r":
                analyzed_text = analyzed_text + char
                
        test = analyzed_text
    
    #Extra Space remover
    if extraspaceremover == 'on':
        analyzed_text = ''
        for index,char in enumerate(test):
            
            if not(test[index]==' ' and test[index+1]==' '):
                
                analyzed_text = analyzed_text + char
        test = analyzed_text


    
    #Char count of input and output text

    CharInput = len(djtext)
    CharOutput = len(test)


    params = {'analyzed_text':test,'CharInput':CharInput,'CharOutput':CharOutput}
    return render(request,'analyze.html',params)

    
    
    
   
        
            


    
    
    

    
