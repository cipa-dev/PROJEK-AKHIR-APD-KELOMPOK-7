from datetime import datetime

def hitung_hari_sewa(rent_date_str, return_date_str):
    rent_date = datetime.strptime(rent_date_str, "%Y-%m-%d") 
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    mid = return_date - rent_date
    selisih_hari = mid.days
    if selisih_hari <= 0:
        return 1 #minimal sewa 1 hari
    else:
        return selisih_hari

def hitung_hari_telat(tgl_batasSewa_str, return_date_str):
    tgl_batasSewa = datetime.strptime(tgl_batasSewa_str, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    kid = return_date - tgl_batasSewa
    selisih = kid.days
    if selisih < 0:
        return 0
    else:
        return selisih

def hitung_denda(hari_telat):
    denda_per_hari=10000
    return hari_telat * denda_per_hari