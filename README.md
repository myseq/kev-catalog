# kev-catalog
A simple tool to query CISA's KEV catalog. This tool is written in Python to shows the top-N vendors and the top-N vulnerable products found in the CISA's KEV. It also can search a specific CVE or keyword in the KEV json file. 

## Usages
```
$ kev-catalog -h
$ kev-catalog -v 
$ kev-catalog -i 10
$ kev-catalog -l 8 
$ kev-catalog -e 2017-0143
$ kev-catalog -s keep
```


# References
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- Download [CSV link](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv)
- Download [JSON LINK](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)


# MySeq Blog
- https://myseq.blogspot.com/2022/03/cisa-known-exploited-vuln-catalog.html

