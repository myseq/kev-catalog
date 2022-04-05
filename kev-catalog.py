#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, argparse
from argparse import RawTextHelpFormatter
from timeit import default_timer as timer
import json
import requests

from datetime import date
from datetime import datetime, timedelta
from collections import Counter
from colorama import init, Fore, Back, Style
import pyfiglet


description = f'CISA\'s Known Exploited Vulns (KEV) Catalog'
banner = f"""
   Zzzzz   |\      _,,,---,,_
           /,`.-'`'    -.  ;-;;,_   __author__ : [ zd ]
          |,4-  ) )-,_..;\ (  `'-'  __year__   : [ 2022.03 ]
         '---''(_/--'  `-'\_)       __file__   : [ {__file__} ]

         [ {description} ]
    """

url = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
verberos = False
count = 0

def cg(x): return (f'{Fore.GREEN}{x}{Style.RESET_ALL}')
def cy(x): return (f'{Fore.YELLOW}{x}{Style.RESET_ALL}')

def Search_CVE(cisa, cveid):

    for vuln in cisa["vulnerabilities"]:
        cve = vuln["cveID"].strip('CVE-')
        if cve == cveid:
            print(f'')
            print(f'  [*] CVE-ID         : {vuln["cveID"]} [ {vuln["vulnerabilityName"]} ]')
            print(f'  [*] Date_Added     : {vuln["dateAdded"]}')
            print(f'  [*] Description    : {vuln["shortDescription"]}')
            print(f'')
            print(f'      [**] Vendor/Product : {vuln["vendorProject"]} / {vuln["product"]}')
            print(f'      [**] Remediation    : {vuln["requiredAction"]}')
            print(f'      [**] Overdue        : {vuln["dueDate"]}')
            print(f'')
    else:
        print(f'')


def Search_String(cisa, searchstring):

    vcount = 0
    for vuln in cisa["vulnerabilities"]:
        vcve = vuln["cveID"]
        vname = vuln["vulnerabilityName"]
        vdesc = vuln["shortDescription"]
        vadded = vuln["dateAdded"]
        vdue = vuln["dueDate"]
        vaction = vuln["requiredAction"]
        vproduct = f'{vuln["vendorProject"]} / {vuln["product"]}'

        if (vname.lower().find(searchstring.lower()) != -1 or vdesc.lower().find(searchstring.lower()) != -1):
            vcount = vcount + 1
            print(f'')
            print(f'  [*] CVE-ID         : {vcve} [ {vname} ]')
            print(f'  [*] Date_Added/Due : {vadded} / {vdue}')
            print(f'  [*] Vendor/Prod    : {vproduct}')
            print(f'  [*] Description    : {vdesc}')
            print(f'')
    else:
        print(f'')
        print(f'    [**] Found          : {cg(vcount)} [ {searchstring} ] ')
        print(f'')


def main():
    """ main() function """
    g = globals()

    parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

    parser.add_argument('-i', dest='mostcommon', metavar='<n>', default=5, type=int,  help='Specifying most common vendor/product. Default is top 5.')
    parser.add_argument('-j', dest='jsonfile', metavar='<file.json>', help='Specifying local JSON file')
    parser.add_argument('-l', dest='lastdays', metavar='<N>', default=2, type=int,  help='Specifying latest N-cve. Default is last 2.')
    parser.add_argument('-v', action='store_true', help='verbose output')

    searching = parser.add_argument_group('Search in Catalog')
    searching.add_argument('-e', dest='cve', metavar='<cve>', help='Search a CVE within Known Exploited Vulnerabilities catalog.')
    searching.add_argument('-s', dest='searchstring', metavar='<string>', help='Search a string within Known Exploited Vulnerabilities catalog.')

    args = parser.parse_args()
    g['verbose'] = True if args.v else False

    init(autoreset=True)
    print(f'')
    word = pyfiglet.figlet_format("KEV Catalog", font="slant")
    print(Fore.RED + word)
         
    if args.jsonfile:
        try:
            fh = open(args.jsonfile, 'r')
            cisa = json.load(fh)
        except:
            print(f' [*] FAIL to open the {args.jsonfile}')
            return
    else:
        resp = requests.get(url)
        if resp.ok:
            cisa = resp.json()
        else:
            print(f' [*] FAIL to access the JSON file at {url}')
            return
    
    print(f'\n{cisa["title"]} [ {cg(cisa["catalogVersion"])}/{cy(cisa["count"])} ]\n')

    if args.cve:
        Search_CVE(cisa, args.cve)
        return

    if args.searchstring:
        Search_String(cisa, args.searchstring)
        return

    pastNdays = args.lastdays
    pDate = date.today() - timedelta(days=pastNdays)

    today = datetime.today()
    cveOverdue = []
    cveFuture = []
    vulnlist = []
    vendors = []
    products = []

    newAdded = {}
    newVulnList = [] 
    newAdded = { "vuln" : newVulnList }

    for vuln in cisa["vulnerabilities"]:
        cve = vuln["cveID"].strip('CVE-')
        vulnlist.append(cve)
        duedate = datetime.strptime(vuln["dueDate"], '%Y-%m-%d')
        if duedate <= today: 
            cveOverdue.append(cve)
        else:
            cveFuture.append(cve)
        vendors.append(vuln["vendorProject"].strip())
        products.append(vuln["product"].strip())
        
        cveAddedDate = datetime.strptime(vuln["dateAdded"], '%Y-%m-%d').date()

        if cveAddedDate >= pDate:
            newVuln = { "cveID" : vuln["cveID"], "dateAdded" : vuln["dateAdded"], "name" : vuln["vulnerabilityName"], "dueDate" : vuln["dueDate"] }
            newAdded["vuln"].append(newVuln)


    qstr = ' OR '.join(vulnlist)
    qstr_overdue = ' OR '.join(cveOverdue)
    qstr_future = ' OR '.join(cveFuture)

    c_vendor = Counter(vendors)
    c_product = Counter(products)
    top = args.mostcommon

    c_vendor_out = ''
    for k,v in c_vendor.most_common(top):
        c_vendor_out = f'{c_vendor_out}  "{k}"/({v})'
    
    c_product_out = ''
    for k,v in c_product.most_common(top):
        c_product_out = f'{c_product_out}  "{k}"/({v})'

    print(f'')
    title_vendor = f'Top {top} vendors '
    print(f' [*] {cg(title_vendor)}  : {c_vendor_out}')
    print(f'')
    title_product = f'Top {top} products '
    print(f' [*] {cy(title_product)} : {c_product_out}')
    print(f'')

    if args.v: 
        print(f' [*] There are {cy(len(newAdded["vuln"]))} newly added Known Exploited vulnerabilities since {cg(pastNdays)} days ago ({pDate.isoformat()}).')
        for v in newAdded["vuln"]:
            days = datetime.strptime(v["dueDate"], "%Y-%m-%d").date() - date.today()
            print(f'     [**] {v["dateAdded"]} : {v["cveID"]} / {v["name"]} [ {cg(v["dueDate"])} / {cy(days.days)}d ]')
    else:
        print(f' [*] There are {cy(len(newAdded["vuln"]))} newly added Known Exploited vulnerabilities since {cg(pastNdays)} days ago.')
    print(f'')

    if args.v:
        vendors = list(dict.fromkeys(vendors))
        products = list(dict.fromkeys(products))
        print(f'  [*] Total vendors  : {len(vendors)}')
        print(f'  [*] Total products : {len(products)}')
        print(f'  [*] Total CVEs     : {len(vulnlist)}')
        print(f'  [*] Overdue CVE    : {cy(len(cveOverdue))}')
        print(f'  [*] Upcoming CVE   : {cg(len(cveFuture))}')

    

if __name__ == "__main__":

    if sys.version_info.major == 2:
        print('This script needs Python 3.')
        exit()

    start = timer()
    main()
    end = timer()

    print(f'')
    print(f'\n [{date.today()}] Completed within [{end-start:.2f} sec].\n')


