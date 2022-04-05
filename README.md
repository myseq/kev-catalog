# kev-catalog.py
A simple tool to query CISA's KEV catalog. This tool is written in Python to shows the top-N vendors and the top-N vulnerable products found in the CISA's KEV. It also can search a specific CVE or keyword in the KEV json file. 

You also can save the JSON file from CISA website, and perform local search with this tool.


## Setup
```console
$ pip3 install -r requirements.txt
```



## Usage
Run kev-catalog and show the verbose information.
```console
$ ./kev-catalog.py -h
usage: kev-catalog.py [-h] [-i <n>] [-j <file.json>] [-l <N>] [-v] [-e <cve>] [-s <string>]

   Zzzzz   |\      _,,,---,,_
           /,`.-'`'    -.  ;-;;,_   __author__ : [ zd ]
          |,4-  ) )-,_..;\ (  `'-'  __year__   : [ 2022.03 ]
         '---''(_/--'  `-'\_)       __file__   : [ kev-catalog.py ]

         [ CISA's Known Exploited Vulns (KEV) Catalog ]


optional arguments:
  -h, --help      show this help message and exit
  -i <n>          Specifying most common vendor/product. Default is top 5.
  -j <file.json>  Specifying local JSON file
  -l <N>          Specifying latest N-cve. Default is last 2.
  -v              verbose output

Search in Catalog:
  -e <cve>        Search a CVE within Known Exploited Vulnerabilities catalog.
  -s <string>     Search a string within Known Exploited Vulnerabilities catalog.
  
$ ./kev-catalog.py -v 
```
![kev-catalog.py -v](screenshot/kev-catalog_v.png)


Run kev-catalog and show the top 10 vendors and top 10 vulnerable products.
```console
$ ./kev-catalog.py -i 10
```
![kev-catalog.py -i 10 -l 7](screenshot/kev-catalog_i.png)


Run kev-catalog and show the last 8 days (inclusive) CVE.
```console
$ ./kev-catalog.py -l 8 
```


Run kev-catalog and search for a specific CVE (2017-0143 for wannacry)
```console
$ ./kev-catalog.py -e 2017-0143
```
![kev-catalog.py -e 2017-0143](screenshot/kev-catalog_e.png)


Run kev-catalog and search for a specific keyword, like keep or bluekeep.
```console
$ ./kev-catalog.py -s keep
```
![kev-catalog.py -s bluekeep](screenshot/kev-catalog_s.png)


Run kev-catalog and refer to a local JSON file.
```console
$ ./kev-catalog.py -j known_exploited_vulnerabilities_20220401.json 
```

# References
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- Download [JSON LINK](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- Download [CSV link](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)


# MySeq Blog
There is a hidden feature that cna show the Kenna query string. See in the blog post.
- https://myseq.blogspot.com/2022/04/publish-kev-catalog-on-github.html
- https://myseq.blogspot.com/2022/03/cisa-known-exploited-vuln-catalog.html

