from django.http import HttpResponse
from django.shortcuts import render

def te(request):
    '''
    Helper for guesing output channel, basically if we know
    stat name then it is statfin, else nobody know yet...
    
    Params
        obj (str): abbr. of stat name
    
    Return
        information (dict): information about statfin output channel or
                            empty dict
    '''    
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'template.html')