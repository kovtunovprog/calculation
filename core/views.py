import json

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import CalculateResults


@csrf_exempt
def index(request):
    if request.method == 'GET':
        template_name = 'index.html'
        return render(request, template_name)
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        nums = body['nums']
        result = 0
        for i in nums:
            if i == '':
                return HttpResponse(json.dumps({'num': 'Вы ввели не все числа'}), status=500)
            try:
                if int(i) < 0:
                    result += 1
            except ValueError:
                try:
                    if float(i) < 0:
                        result += 1
                except ValueError:
                    return HttpResponse(json.dumps({'num': 'Вы должны были ввести число'}))
        return HttpResponse(json.dumps({'num': f'{result}'}), content_type='application/json')


@csrf_exempt
def api_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        num = CalculateResults(result_num=body['num'], input_a=body['input_a'], input_b=body['input_b'],
                               input_c=body['input_c'], username=request.user.username)
        num.save()
        return HttpResponse(json.dumps({'text': 'Success'}))

    if request.method == 'GET':
        results = CalculateResults.objects.filter(username=request.user.username).order_by('-date_result')[:5]
        results_list = []
        for num in results:
            results_list.append({'date': num.date_result.strftime("%d/%m/%Y at %I:%M %p"),
                                 'num': num.result_num,
                                 'input_a': num.input_a,
                                 'input_b': num.input_b,
                                 'input_c': num.input_c,
                                 'id': num.pk
                                 })
        return HttpResponse(json.dumps({'results': results_list}), content_type='application/json')

    if request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        pk = body['id']
        CalculateResults.objects.filter(pk=pk).delete()
        return HttpResponse(json.dumps({'success': 'deleted'}))
