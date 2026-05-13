import math

def hitung_jarak(rumah1, rumah2):
    x1 = rumah1["x"]
    y1 = rumah1["y"]

    x2 = rumah2["x"]
    y2 = rumah2["y"]

    jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return round(jarak, 2)

def greedy_route(data_rumah, titik_awal):
    belum_dikunjungi = data_rumah.copy()

    rute = [titik_awal]
    total_jarak = 0

    current = titik_awal

    while belum_dikunjungi:
        rumah_terdekat = None
        jarak_terdekat = float('inf')

        for rumah in belum_dikunjungi:
            jarak = hitung_jarak(current, rumah)

            if jarak < jarak_terdekat:
                jarak_terdekat = jarak
                rumah_terdekat = rumah

        rute.append(rumah_terdekat)
        total_jarak += jarak_terdekat

        current = rumah_terdekat
        belum_dikunjungi.remove(rumah_terdekat)

    return rute, round(total_jarak, 2)

def tampilkan_output(rute, total_jarak):
    print("\n=== RUTE KENDARAAN ===")

    for rumah in rute:
        print(
            f"Rumah {rumah['id']} "
            f"-> ({rumah['x']}, {rumah['y']}) "
            f"Sampah: {rumah.get('sampah', 0)} Kg"
        )

    print("\n=== TOTAL JARAK ===")
    print(f"{total_jarak} satuan jarak")

# TEST
if __name__ == "__main__":

    titik_awal = {
        "id": 0,
        "x": 0,
        "y": 0,
        "sampah": 0
    }

    data_rumah = [
        {"id": 1, "x": 10, "y": 5, "sampah": 3},
        {"id": 2, "x": 3, "y": 7, "sampah": 2},
        {"id": 3, "x": 15, "y": 10, "sampah": 5},
        {"id": 4, "x": 6, "y": 2, "sampah": 1},
    ]

    rute, total_jarak = greedy_route(data_rumah, titik_awal)

    tampilkan_output(rute, total_jarak)