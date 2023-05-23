from django.shortcuts import render, redirect
import psycopg2
import uuid
from django.contrib import messages


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_umpire(request):
    # TODO: Benerin connect kalo buat nanti PROD
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
        try:
            create_member(cursor, id_user, nama, email)

            create_umpire(cursor, id_user, negara)

            db_connection.commit()
            db_connection.close()
            # TODO: Redirect ke halaman setelah berhasil
        except Exception as e:
            db_connection.rollback()
            messages.error(
                request, 'Gagal mendaftar, mohon perika input anda dan coba lagi')
            db_connection.close()
            return redirect('reg_log:register-umpire')
    return render(request, 'umpire.html')


def register_athlete(request):
    # TODO: Benerin connect kalo buat nanti PROD
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
        jenis_kelamin = parse_kelamin(request.POST.get('jenis_kelamin'))

        try:
            create_member(cursor, id_user, nama, email)
            create_atlet(cursor, id_user, negara, tanggal_lahir, play_type,
                         tinggi_badan, jenis_kelamin)
            db_connection.commit()
            # TODO: redirect ke suatu page
            db_connection.close()
        except Exception as e:
            db_connection.rollback()
            messages.error(
                request, "Gagal mendaftar, mohon perika input anda dan coba lagi")
            db_connection.close()
            redirect('reg_log:register-atlet')
    return render(request, 'athlete.html')


def register_coach(request):
    if (request.method == 'POST'):
        # TODO: Benerin connect kalo nanti buat PROD
        db_connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Inipasswordsaya12."
        )
        try:
            cursor = db_connection.cursor()
            cursor.execute("set search_path to babadu")
            id_user = str(uuid.uuid4())
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            negara = request.POST.get('negara')
            kategori = request.POST.getlist('kategori')
            tanggal_mulai = request.POST.get('tanggal-mulai')

            create_member(cursor, id_user, nama, email)

            create_pelatih(cursor, id_user, kategori, tanggal_mulai)

            db_connection.commit()
            # TODO: Reditect ke suatu page
            db_connection.close()
        except Exception as e:
            db_connection.rollback()
            messages.error(
                request, "Gagal mendaftar, mohon perika input anda dan coba lagi")
            db_connection.close()
            redirect('reg_log:register-coach')
    return render(request, 'coach.html')


def portal(request):
    return render(request, 'portal.html')


def parse_play_type(play_type: str) -> bool:
    return play_type == 'right'


def parse_kelamin(kelamin: str) -> bool:
    return kelamin == 'Laki-laki'


def create_member(cursor, id_user: str, nama: str, email: str) -> None:
    query_insert_member = """insert into member (id, name, email) 
            VALUES (%s, %s, %s)"""
    cursor.execute(query_insert_member, (id_user, nama, email))


def create_atlet(cursor, id_user: str, negara: str, tanggal_lahir: str, play_type: str,
                 tinggi_badan: str, jenis_kelamin: str) -> None:
    query_insert_atlet = """INSERT INTO atlet (id, tgl_lahir, negara_asal, 
        play_right, height, world_rank, jenis_kelamin) VALUES (%s, %s, %s, %s, 
        %s, NULL, %s)"""
    cursor.execute(query_insert_atlet, (id_user, tanggal_lahir,
                                        negara, play_type, tinggi_badan,
                                        jenis_kelamin))


def get_spesialisasi(cursor) -> dict[str:str]:
    query_get_spesialisasi = """select * from spesialisasi"""
    cursor.execute(query_get_spesialisasi)
    result = cursor.fetchall()
    result = {nama: id for id, nama in result}
    return result


def create_pelatih(cursor, id_user: str, kategori: str, tanggal_mulai: str) -> None:
    query_insert_pelatih = """INSERT INTO pelatih (id, tanggal_mulai)
            VALUES (%s, %s)"""
    cursor.execute(query_insert_pelatih, (id_user, tanggal_mulai))

    create_spesialisasi_relasi(cursor, id_user, kategori)


def create_spesialisasi_relasi(cursor, id_user: str, kategori: str) -> None:
    spesialisasi_map = get_spesialisasi(cursor)
    query_inserti_pelatih_spesialisasi = """INSERT INTO pelatih_spesialisasi (id_pelatih, id_spesialisasi)
            VALUES (%s, %s)"""
    pelatih_spesialisasi_values = [
        (id_user, spesialisasi_map[kategori]) for kategori in kategori]
    cursor.executemany(query_inserti_pelatih_spesialisasi,
                       pelatih_spesialisasi_values)


def create_umpire(cursor, id_user: str, negara: str) -> None:
    query_create_umpire = "INSERT INTO umpire (id, negara) VALUES (%s, %s)"
    cursor.execute(query_create_umpire, (id_user, negara))
