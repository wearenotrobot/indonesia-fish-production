"""
Total fish production in Indonesia
Data collected from http://pipp.djpt.kkp.go.id/produksi_harga
"""
import produksiikan

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = produksiikan.data_extraction()
    produksiikan.show_data(result)
