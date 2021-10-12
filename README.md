# indonesia-fish-production
This repository will give us information about the latest total marine fish production in Indonesia. 
Data will be collected from PIPP (Pusat Informasi Pelabuhan Perikanan). The Name of the fish is written in Indonesian.
The total production is in Kg.

## How it work?
This repository will scrape from [PIPP](http://pipp.djpt.kkp.go.id/produksi_harga) to get the latest marine fish production in Indonesia.

This repository will use BeautifulSoup4 and Request, to produce output in the form of JSON. This package is ready to be used in web or mobile applications.

## How to use
    import produksiikan

    if __name__ == '__main__':
        print('Aplikasi Utama')
        result = produksiikan.data_extraction()
        produksiikan.show_data(result)
        
# Author
mizan toyyibun