from django.shortcuts import render
import psycopg2
import locale
locale.setlocale(locale.LC_ALL, '')

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

def daftar_event(request, nama_stadium):
    db_connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Inipasswordsaya12."
    )
    cursor = db_connection.cursor()
    cursor.execute("set search_path to babadu")
    event_list = get_event_in_stadium(nama_stadium, cursor)
    context = {"daftar_event": event_list}
    return render(request, 'daftar_event.html', context=context)

def daftar_partai(request, nama_stadium, nama_event, tahun_event):
    return render(request, 'daftar_partai.html')

def get_event_in_stadium(nama_stadium, cursor):
    query_get_event = """
    SELECT E.nama_event, E.Total_hadiah, E.Tgl_mulai, E.Kategori_Superseries
    FROM EVENT E
    WHERE E.nama_stadium = %s
    AND E.Tgl_Mulai > CURRENT_DATE
    """
    event_list = cursor.execute(query_get_event, (nama_stadium,))
    event_list = cursor.fetchall()
    event_list = [(event[0], locale.currency(event[1], grouping=True), 
                   event[2].strftime('%d-%m-%Y'), event[3]) for event in event_list]
                   
    return event_list