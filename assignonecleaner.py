import csv

# Open our input and output files
csvfile = open('cleanme.csv', 'r')
outfile = open('clean-cleanme.csv', 'w')

#Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

#Write headers
writer.writeheader()

#clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['city'] = row['city'].replace("&nbsp", " ")
    if int(row['amount']) >= 1000: 
        print type(row['amount'])
        print row
        writer.writerow(row)
