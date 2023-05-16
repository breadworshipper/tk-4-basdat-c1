from django.shortcuts import render
import psycopg2

# Create your views here.

def daftar_stadium(request):
    context = {}
    db_connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Inipasswordsaya12."
    )
    cursor = db_connection.cursor()
    
    cursor.execute("set search_path to babadu")
    cursor.execute("select * from stadium")
    context['stadium'] = cursor.fetchall()
    db_connection.close()
    return render(request, 'daftar_stadium.html', context=context)