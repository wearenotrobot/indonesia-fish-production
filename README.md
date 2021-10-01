# indonesia-fish-production
This Repository will give us information about the total fish production in Indonesia. Data will be collected from PIPP (Pusat Informasi Pelabuhan Perikanan).

## How it work?
This package will scrape from [PIPP](http://pipp.djpt.kkp.go.id/produksi_harga) to get the latest fish production in Indonesia.

This package will use BeautifulSoup4 and Request, to produce output in the form of JSON. This package is ready to be used in web or mobile applications.

## How to use
    import produksiikan

    if __name__ == '__main__':
        print('Aplikasi Utama')
        result = produksiikan.data_extraction()
        produksiikan.show_data(result)
        
# Author
mizan toyyibun