# SNListSwiftCheck
Checks input csv of supernovae if each sn has been observed since 1 year after explosion year.

# Input CSV
In SwiftSNweblist - swiftgi17templates.csv, the file is formatted as follows: SNname, TargetID, SNRa, SNDec, Template Status

As of right now, the template status is useless.
SNname is the name of the supernova and is used to parse the year of each supernova, SNRa is the Right Ascension, SNDec is the Declination, and TargetID is the host galaxy. Ascencion and Declination are both to be in sexagesimal (ra in hours:minutes:seconds, dec in decimals:arcminutes:arcseconds) but the code can be modified to accept decimal.

# Output
The main output file is named OutputSN.csv. This will output the most recent year and either true or false in the last two columns. If the code outputs True, that means the SN has been observed since or on it's explosion year. If it outputs False, that means that the Supernova likely needs to be re-observed for new data as it hasnt been observed since explosion.

# Debugging
Currently I have an extra text file that gets generated from the Input list. This is simply to check the values that the code is using to pull observation information and make sure it is working properly. In a later release I will remove this from the code and make it use an array instead.
