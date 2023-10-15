import lxml.etree
import requests
import csv
import pymysql

try:
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='priority', database='introdase')
    cursor = db.cursor()
except Exception as e:
    print(e)
    exit()

# fp = 'spider_spec_cfp2017.csv'
# with open(fp, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Test Sponsor', 'System Name', 'Paralled', 'Base Threads', 'Enabled Cores', 'Enabled Chips', 'Threads/Core', 'Base Results', 'Peak Results']) # write header

urls = ['https://www.spec.org/cpu2017/results/cfp2017.html']
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}
for url in urls:
    html = requests.get(url, headers=headers)
    selector = lxml.etree.HTML(html.text)
    infos = selector.xpath("//tbody")
    
    for info in infos:
        for n in range(1, 100):
            try:
                path = 'tr[{}]/td[1]/text()'.format(n) 
                test_sponsor = info.xpath(path)[0]
                system_name = info.xpath('tr[{}]/td[2]/text()'.format(n))[0]
                parallel = info.xpath('tr[{}]/td[3]/text()'.format(n))[0]
                base_threads = info.xpath('tr[{}]/td[4]/text()'.format(n))[0]
                enable_cores = info.xpath('tr[{}]/td[5]/text()'.format(n))[0]
                enable_chips = info.xpath('tr[{}]/td[6]/text()'.format(n))[0]
                threads_core = info.xpath('tr[{}]/td[7]/text()'.format(n))[0]
                base_results = info.xpath('tr[{}]/td[8]/text()'.format(n))[0]
                peak_results = info.xpath('tr[{}]/td[9]/text()'.format(n))[0]
                #print (test_sponsor, system_name, parallel, base_threads, enable_cores,enable_chips, threads_core, base_results, peak_results)
                # with open(fp, 'a', newline='') as file:
                #     writer = csv.writer(file)
                #     writer.writerow([test_sponsor, system_name, parallel, base_threads, enable_cores, enable_chips, threads_core, base_results, peak_results])

                try:
                    sql = "INSERT INTO introdase.spec(testsponsor, systemname, baseresult) values('%s', '%s', '%s')" % (test_sponsor, system_name, base_results)
                    cursor.execute(sql)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    print(e)
                    continue
            except:
                db.rollback()
                continue
        
cursor.close()
db.close()