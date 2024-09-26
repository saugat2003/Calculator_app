from django.shortcuts import render
from django.http import JsonResponse
import re

# Create your views here.

def index(request):
    return render(request, 'calculator/index.html')

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')

        # Basic validation to prevent code injection (only allow numbers, operators, parentheses)
        if not re.match(r'^[\d\+\-\*/\.\(\) ]+$', expression):
            return JsonResponse({'error': 'Invalid input'})

        try:
            result = eval(expression)  # Using eval here but in a production app, avoid this for security reasons.
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': 'Error in calculation'})

    return JsonResponse({'error': 'Invalid request method'})
