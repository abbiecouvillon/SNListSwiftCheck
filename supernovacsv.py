from swifttools.swift_too import Swift_ObsQuery
from swifttools.swift_too import Swift_TOO
from astropy.coordinates import SkyCoord
import astropy.units as u
import ast as a

# Initiate the Swift_TOO class
too = Swift_TOO()

# Username and secret key
too.username, too.shared_secret = 'anonymous', 'anonymous'


snlist = []
snfile = open('snlist.txt', 'w')
filename = 'SwiftSNweblist - swiftgi17templates.csv'
# CSV formatting: SNname,targetids,SNra,SNdec,template status

with open(filename, 'r') as f:
    file = f.read().split("\n")
    for k in range(len(file)):
        file[k] = file[k].split(",")
        if k != 0:
            c = SkyCoord(file[k][2] + " " + file[k][3], unit=(u.hourangle, u.deg))
            # SNra at line k turned into degrees, SNdec at line k turned into degrees
            file[k][2], file[k][3] = c.ra.degree, c.dec.degree
            # SNname at line k, 4 digit year in the SNname at line k
            name, year = file[k][0], file[k][0][2:6]
            snfile.write(str(file[k]))
            snfile.write('\n')
snfile.close()

output = open('outputsn.csv', 'w')
# snlist.txt is basically just a txt file where each line is a list. I reformatted the data in the csv in the above
# and wrote it to the text file to make my life easier when checking if the code was wrong.
with open('snlist.txt', 'r') as f:
    file = f.read().split('\n')
    output.write(f'SNName,RA(deg),DEC(deg),observed,yearchecked\n')

    for k in range(len(file) - 1):
        query = Swift_ObsQuery()
        obj = a.literal_eval(file[k])
        name = obj[0]
        year = obj[0][2:6]
        query.ra, query.dec, query.radius = float(obj[2]), float(obj[3]), 6 / 60  # 6 arcminutes
        if query.submit():
            print(f"Query succeeded for {obj[0]}")
        else:
            print(f"Query failed for {obj[0]}")
        listsn = str(query).split('\n')
        querylist = []
        for k in range(len(listsn)):
            if listsn[k].startswith("|"):
                c = listsn[k].split('|')
                for k in range(len(c)):
                    c[k] = c[k].strip()
                querylist.append(c)
        found = False
        print(query)
        latestobv = 0
        for k in range(len(querylist)):
            if k != 0:
                #print(querylist[k])
                if int(querylist[k][2][0:4]) >= int(year) + 1:  # int(year) + number is the minimum year looking past.
                    found = True
                if int(querylist[k][2][0:4]) >= latestobv:
                    latestobv = int(querylist[k][2][0:4])
        print(f"{obj[0]} observed within year range boolean = {found} with a latest obv of {latestobv}")
        output.write(f'{name},{float(obj[2])},{float(obj[3])},{found},{year}\n')

output.close()
print("closed")
