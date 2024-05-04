from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def translate(request):
    text = request.GET.get('text')
    source_lang = request.GET.get('source_lang')
    target_lang = request.GET.get('target_lang')

    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}"
    response = requests.get(url)

    if response.status_code == 200:
        translated_text = response.json()[0][0][0]
        return JsonResponse({'translated_text': translated_text})
    else:
        return JsonResponse({'error': 'Translation failed'}, status=500)
