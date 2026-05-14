from datetime import datetime, timedelta

KAPASITAS_GEROBAK = 15
KAPASITAS_TRUK = 200

JAM_MULAI_GEROBAK = 6
JAM_SELESAI_GEROBAK = 15

JAM_MULAI_TRUK = 8
JAM_SELESAI_TRUK = 17

def buat_waktu(jam):
    return datetime(2026, 1, 1, jam, 0, 0)

def tambah_menit(waktu, menit):
    return waktu + timedelta(minutes=menit)

def format_waktu(waktu):
    return waktu.strftime("%H:%M")

def hitung_waktu_jalan_gerobak(jarak):
    return jarak * 3

def hitung_waktu_loading_gerobak(sampah):
    return sampah * 2

def hitung_waktu_jalan_truk(jarak):
    return (jarak / 5) * 3

def hitung_waktu_loading_truk(sampah):
    return (sampah / 10) * 2

def hitung_waktu_transfer(sampah):
    return sampah * 2

def transfer_ke_truk(muatan_gerobak, kapasitas_truk_tersisa):
    sampah_ditransfer = min(muatan_gerobak, kapasitas_truk_tersisa)
    sisa_gerobak = muatan_gerobak - sampah_ditransfer
    return sampah_ditransfer, sisa_gerobak

def unload_ke_tps(muatan_truk, kapasitas_tps):
    sampah_dibuang = min(muatan_truk, kapasitas_tps)
    sisa_muatan = muatan_truk - sampah_dibuang
    return sampah_dibuang, sisa_muatan

def simulasi_gerobak(
    rute,
    total_jarak,
    kapasitas_truk_tersisa=KAPASITAS_TRUK,
    id_gerobak=1
):
    waktu_sekarang = buat_waktu(JAM_MULAI_GEROBAK)
    batas_operasi = buat_waktu(JAM_SELESAI_GEROBAK)

    muatan_gerobak = 0
    total_waktu = 0
    total_sampah_terangkut = 0

    report = []
    sisa_rumah = []

    report.append({
        "waktu": format_waktu(waktu_sekarang),
        "aktivitas": "Mulai operasional"
    })

    for i in range(1, len(rute)):
        rumah = rute[i]
        rumah_sebelumnya = rute[i - 1]

        dx = rumah["x"] - rumah_sebelumnya["x"]
        dy = rumah["y"] - rumah_sebelumnya["y"]
        jarak = (dx ** 2 + dy ** 2) ** 0.5
        sampah = rumah["sampah"]

        waktu_jalan = hitung_waktu_jalan_gerobak(jarak)
        estimasi_jalan = tambah_menit(waktu_sekarang, waktu_jalan)

        if estimasi_jalan > batas_operasi:
            for j in range(i, len(rute)):
                sisa_rumah.append({
                    "rumah_id": rute[j]["id"],
                    "sisa_sampah": rute[j]["sampah"]
                })
            report.append({
                "waktu": format_waktu(batas_operasi),
                "aktivitas": "Waktu habis saat perjalanan"
            })
            waktu_sekarang = batas_operasi
            break

        waktu_sekarang = estimasi_jalan
        total_waktu += waktu_jalan

        report.append({
            "waktu": format_waktu(waktu_sekarang),
            "aktivitas": f"Tiba di rumah {rumah['id']}"
        })

        if muatan_gerobak + sampah > KAPASITAS_GEROBAK:
            sampah_ditransfer, sisa_gerobak = transfer_ke_truk(
                muatan_gerobak,
                kapasitas_truk_tersisa
            )

            if sampah_ditransfer == 0:
                report.append({
                    "waktu": format_waktu(waktu_sekarang),
                    "aktivitas": "Truk penuh, operasional berhenti"
                })
                for j in range(i, len(rute)):
                    sisa_rumah.append({
                        "rumah_id": rute[j]["id"],
                        "sisa_sampah": rute[j]["sampah"]
                    })
                break

            waktu_transfer = hitung_waktu_transfer(sampah_ditransfer)
            estimasi_transfer = tambah_menit(waktu_sekarang, waktu_transfer)

            if estimasi_transfer > batas_operasi:
                report.append({
                    "waktu": format_waktu(batas_operasi),
                    "aktivitas": "Waktu habis saat transfer"
                })
                waktu_sekarang = batas_operasi
                break

            waktu_sekarang = estimasi_transfer
            total_waktu += waktu_transfer
            kapasitas_truk_tersisa -= sampah_ditransfer
            muatan_gerobak = sisa_gerobak

            report.append({
                "waktu": format_waktu(waktu_sekarang),
                "aktivitas": "Transfer ke truk",
                "jumlah_transfer": sampah_ditransfer,
                "sisa_muatan_gerobak": muatan_gerobak
            })

        waktu_loading = hitung_waktu_loading_gerobak(sampah)
        estimasi_loading = tambah_menit(waktu_sekarang, waktu_loading)

        if estimasi_loading > batas_operasi:
            sisa_rumah.append({
                "rumah_id": rumah["id"],
                "sisa_sampah": sampah
            })
            report.append({
                "waktu": format_waktu(batas_operasi),
                "aktivitas": "Waktu habis saat loading"
            })
            waktu_sekarang = batas_operasi
            break

        waktu_sekarang = estimasi_loading
        total_waktu += waktu_loading
        muatan_gerobak += sampah
        total_sampah_terangkut += sampah

        report.append({
            "waktu": format_waktu(waktu_sekarang),
            "rumah": rumah["id"],
            "ambil_sampah": sampah,
            "muatan_gerobak": muatan_gerobak
        })

    return {
        "id_gerobak": id_gerobak,
        "total_jarak": round(total_jarak, 2),
        "total_waktu": round(total_waktu, 2),
        "total_sampah_terangkut": total_sampah_terangkut,
        "sisa_muatan_gerobak": muatan_gerobak,
        "sisa_sampah_rumah": sisa_rumah,
        "kapasitas_truk_tersisa": kapasitas_truk_tersisa,
        "jam_selesai": format_waktu(waktu_sekarang),
        "report": report
    }

def simulasi_truk(
    total_sampah,
    total_jarak,
    kapasitas_tps=500,
    id_truk=1
):
    waktu_sekarang = buat_waktu(JAM_MULAI_TRUK)
    batas_operasi = buat_waktu(JAM_SELESAI_TRUK)

    muatan_truk = min(total_sampah, KAPASITAS_TRUK)
    sisa_sampah_truk = max(0, total_sampah - KAPASITAS_TRUK)
    total_waktu = 0

    report = []
    report.append({
        "waktu": format_waktu(waktu_sekarang),
        "aktivitas": "Mulai operasional"
    })

    waktu_jalan = hitung_waktu_jalan_truk(total_jarak)
    estimasi_jalan = tambah_menit(waktu_sekarang, waktu_jalan)

    if estimasi_jalan > batas_operasi:
        return {
            "id_truk": id_truk,
            "status": "Waktu habis saat perjalanan",
            "sisa_sampah_truk": total_sampah
        }

    waktu_sekarang = estimasi_jalan
    total_waktu += waktu_jalan

    report.append({
        "waktu": format_waktu(waktu_sekarang),
        "aktivitas": "Tiba di TPS"
    })

    waktu_loading = hitung_waktu_loading_truk(muatan_truk)
    estimasi_unload = tambah_menit(waktu_sekarang, waktu_loading)

    if estimasi_unload > batas_operasi:
        return {
            "id_truk": id_truk,
            "status": "Waktu habis saat unload TPS",
            "sisa_sampah_truk": total_sampah
        }

    waktu_sekarang = estimasi_unload
    total_waktu += waktu_loading

    sampah_dibuang, sisa_muatan = unload_ke_tps(muatan_truk, kapasitas_tps)

    report.append({
        "waktu": format_waktu(waktu_sekarang),
        "aktivitas": "Unload ke TPS",
        "jumlah_dibuang": sampah_dibuang,
        "sisa_muatan_truk": sisa_muatan
    })

    return {
        "id_truk": id_truk,
        "total_jarak": round(total_jarak, 2),
        "total_waktu": round(total_waktu, 2),
        "total_sampah_terangkut": muatan_truk,
        "sisa_sampah_truk": sisa_sampah_truk + sisa_muatan,
        "kapasitas_tps_tersisa": kapasitas_tps - sampah_dibuang,
        "jam_selesai": format_waktu(waktu_sekarang),
        "report": report
    }