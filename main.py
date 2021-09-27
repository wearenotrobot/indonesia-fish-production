"""
Total fish production in Indonesia
Data collected from KKP.go.id
"""


def data_extraction():
    """
    PRODUKSI TAHUN 2021
    Nama Jenis Ikan	Total Produksi (Kg)
    Cakalang [SKJ]              : 70.031.295,89
    Layang Benggol              : 34.311.048,90
    Madidihang [YFT]            : 34.071.561,50
    Cumi-Cumi                   : 29.018.893,30
    Layang Deles                : 16.432.081,10
    Swanggi                     : 13.538.254,47
    Lemuru                      : 13.470.370,00
    Tongkol Pisang-Cerutu [BLT] : 11.465.453,02
    Siro                        : 7.362.794,00
    Tongkol Pisang-Balaki [FRI]	: 6.977.063,31
    :return:
    """
    hasil = dict()
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
    pass


if __name__ == '__main__':
    print('Apikasi Utama')
    result = data_extraction()
    show_data(result)
