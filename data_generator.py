import random

def generate_rumah(jumlah_rumah=100):
    rumah_list = []

    for i in range(1, jumlah_rumah + 1):
        rumah = {
            "id": i,
            "x": random.randint(1, 50),
            "y": random.randint(1, 50),
            "sampah": random.randint(0, 7)
        }

        rumah_list.append(rumah)

    return rumah_list


# TEST
if __name__ == "__main__":
    data_rumah = generate_rumah()

    for rumah in data_rumah[:5]:
        print(rumah)

        import math

