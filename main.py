"""
Total fish production in Indonesia
Data collected from KKP.go.id
"""

def data_extraction():
    hasil = dict()
    hasil['nama_jenis_ikan'] = 'Total Produksi (Kg)'
    hasil['cakalang_[SKJ]'] = '70.031.295,89'
    hasil['layang_benggol'] = '34.311.048,90'
    hasil['madidihang_[YFT]'] = '34.071.561,50'
    hasil['cumi-cumi'] = '29.018.893,30'
    hasil['layang_deles'] = '16.432.081,10'
    hasil['swanggi'] = '13.538.254,47'
    hasil['lemuru'] = '13.470.370,00'
    hasil['tongkol_pisang-cerutu_[BLT]'] = '11.465.453,02'
    hasil['siro'] = '7.362.794,00'
    hasil['tongkol_pisang-balaki_[FRI]'] = '6.977.063,31'
    print(hasil)
    return hasil


def show_data(result):
    print('INDONESIA FISH PRODUCTION IN 2021')
    print(f"Nama Jenis Ikan {result['nama_jenis_ikan']}")
    print(f"Cakalang [SKJ] {result['cakalang_[SKJ]']}")
    print(f"layang_benggol {result['layang_benggol']}")
    print(f"Madidihang [YFT] {result['madidihang_[YFT]']}")
    print(f"Cumi-Cumi {result['cumi-cumi']}")
    print(f"Layang Deles {result['layang_deles']}")
    print(f"Swanggi {result['swanggi']}")
    print(f"Lemuru {result['lemuru']}")
    print(f"Tongkol Pisang-Cerutu [BLT] {result['tongkol_pisang-cerutu_[BLT]']}")
    print(f"Siro {result['swanggi']}")
    print(f"Tongkol Pisang-Balaki [FRI] {result['tongkol_pisang-balaki_[FRI]']}")


if __name__ == '__main__':
    print('Apikasi Utama')
    result = data_extraction()
    show_data(result)
