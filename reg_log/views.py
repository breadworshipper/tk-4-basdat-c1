from django.shortcuts import render, redirect
import psycopg2
import uuid
from django.contrib import messages

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_umpire(request):
    return render(request, 'umpire.html')

def register_athlete(request):
    if (request.method == 'POST'):
        db_connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Inipasswordsaya12."
        )
        
        cursor = db_connection.cursor()
        cursor.execute("set search_path to babadu")
        id_user = str(uuid.uuid4())
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        negara = request.POST.get('negara')
        tanggal_lahir = request.POST.get('tgl_lahir')
        play_type = parse_play_type(request.POST.get('play'))
        tinggi_badan = request.POST.get('tinggi_badan')
        jenis_kelamin = parse_play_type(request.POST.get('jenis_kelamin'))
        
        try:
            query_insert_member = """insert into member (id, name, email) 
            VALUES (%s, %s, %s)"""
            cursor.execute(query_insert_member, (id_user, nama, email))
            query_insert_atlet = """INSERT INTO atlet (id, tgl_lahir, negara_asal, play_right, height, world_rank, jenis_kelamin) 
            VALUES (%s, %s, %s, %s, %s, NULL, %s)"""
            cursor.execute(query_insert_atlet, (id_user, tanggal_lahir, negara, play_type, tinggi_badan , jenis_kelamin))
            db_connection.commit()
            # TODO: redirect ke suatu page
            db_connection.close()
        except Exception as e:
            db_connection.rollback()
            messages.error(request, e)
            redirect('reg_log:register-atlet')
    return render(request, 'athlete.html')

def register_coach(request):
    return render(request, 'coach.html')

def portal(request):
    return render(request, 'portal.html')

def parse_play_type(play_type: str) -> bool:
    return play_type == 'right'

def parse_kelamin(kelamin: str) -> bool:
    return kelamin == 'Laki-laki'