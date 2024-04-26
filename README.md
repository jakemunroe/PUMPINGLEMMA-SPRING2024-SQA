Team Pumping Lemma

Members:
Davis Leeth,
Jake Munroe,
Samarth Kumar,
Nikhil Patel

Report (make separate file?):

4.c. We integrated forensics by adding logging into 5 methods in the empirical folder.
The logging was used in methods that had files or dataframes as input as the data in these files can be poisoned and it is good practice to routinely check it.

Also, a myLogger.py file was added to facilitate the logging actions.

Edited methods:

report.py:
reportDensity( res_file )

frequency.py:
reportEventDensity(res_file, output_file)
reportProportion( res_file, output_file )

dataset.stats.py:
getFileLength(file_)
getAllFileCount(df_)
