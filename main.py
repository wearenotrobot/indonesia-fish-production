"""
Total fish production in Indonesia
Data collected from KKP.go.id
"""
import produksiikan

if __name__ == '__main__':
    print('Apikasi Utama')
    result = produksiikan.data_extraction()
    produksiikan.show_data(result)
