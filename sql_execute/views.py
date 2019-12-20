# from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.db.utils import DatabaseError
from django.db import connection


def sql_execute(request):
    if request.user.is_staff:

        if request.method == 'GET':
            return render(request, 'sql.html')
        elif request.method == 'POST':
            query = request.POST['query']
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except DatabaseError as error:
                context = {'error': error.message,
                           'query': query, }
                return render(request, 'sql.html', context)
            data = cursor.fetchall()
            # cursor.execute(query)
            desc = cursor.description
            headers = [d[0] for d in desc]
            context = {'data': data,
                       'query': query,
                       'headers': headers}
            return render(request, 'sql.html', context)
    else:
        return HttpResponse('auth failed!')
