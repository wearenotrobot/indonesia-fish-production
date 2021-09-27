"""
Total fish production in Indonesia
Data collected from KKP.go.id
"""

import fishproduction

if __name__ == '__main__':
    print('Apikasi Utama')
    result = fishproduction.data_extraction()
    fishproduction.show_data(result)

