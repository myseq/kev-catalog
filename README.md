# Known Exploited Vulnerabilities (KEV) Catalog
A simple tool 

# kev-catalog Description
The is a simple tool written in Python to shows the top-N vendors and the top-N vulnerable products found in the CISA's KEV. It also can search a specific CVE or keyword in the KEV json file. 

## Usage
`
$ kev-catalog -h
$ kev-catalog -v 
$ kev-catalog -i 10
$ kev-catalog -l 8 
$ kev-catalog -e 2017-0143
$ kev-catalog -s keep
`

# MySeq Blog
https://myseq.blogspot.com/2022/03/cisa-known-exploited-vuln-catalog.html

# References
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- [csv] https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv
- [json] https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
