from bs4 import BeautifulSoup
import requests
import time

url = ["http://www.wikicfp.com/cfp/call?conference=big%20data&page=",
       "http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=", 
       "http://www.wikicfp.com/cfp/call?conference=data%20mining&page="]

output_data = open("data.tsv","w+")

output_data.write("con_acronym\tcon_name\tcon_date\tcon_location\tcon_category\n")
j=0
all_Conference = ["Big Data", "Machine Learning", "Data Mining"]

for current_url in url:

    current_page_number = 1
    current_conference = all_Conference[j]
    j+=1

    while current_page_number <21:
        current_page_url = current_url+str(current_page_number)
        crawled_data = requests.get(current_page_url)

        if crawled_data.status_code !=200:
            print("Failed at", current_page_url)

        parsed_data = BeautifulSoup(crawled_data.text, features="lxml")

        temp_acronym = ""
        temp_name =""
        temp_date = ""
        temp_location = ""
        i=0
        total_entries =0
        for rows in parsed_data.body.find_all("tr",attrs={"bgcolor" : ["#f6f6f6","#e6e6e6"]}):
            for data in rows.find_all("td"):
                if i==0:
                    
                    temp_acronym = data.a.text.strip()
                    

                elif i==1:
                    temp_name = data.text.strip()
                    

                elif i==3:
                    temp_date = data.text.strip()
                    if temp_date != 'N/A':
                        dates = temp_date.split('-')
                        year = dates[0].split(',')[1].strip()
                        date = year
                    

                elif i ==4:
                    temp_location = data.next.strip()
                    

                elif i ==5:
                    combined_Data = temp_acronym+'\t'+temp_name+'\t'+temp_date+'\t'+temp_location+'\t'+ current_conference+"\n"
                    output_data.write(combined_Data)
                    temp_acronym = ""
                    temp_name =""
                    temp_date = ""
                    temp_location = ""
                    i=0
                    total_entries +=1
                    break

                i+=1


        print("done with url",current_page_url)
        print("Total entries", total_entries)
        current_page_number+=1            


            

        time.sleep(10)

