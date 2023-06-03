from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import wordlist

array = [
    
]
@csrf_exempt
def study(request):
    return render(request, 'study.html')

@csrf_exempt
def word(request):
    if request.method == 'GET':
        # 표시할 단어 개수
        amount = request.GET['amount']   
        # 단어장 배열
        arrays = wordlist.objects.all()
        return render(request, 'words.html', 
                    #   {'wordlists',arrays}
                    )

@csrf_exempt
def test(request):
    return render(request, 'test.html')

@csrf_exempt
def vocabulary(request):
    return render(request, 'vocabulary.html')
