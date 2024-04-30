# PUMPING LEMMA Report:
## Authors: Samarth Kumar, Davis Leeth, Jacob Munroe, and Nikhil Patel

### 4.a. 
For the Git Hook, we utilized the following line to implement it:\

`bandit -r  ./ -f csv -o scans/"$(date +"%Y_%m_%d_%I_%M_%p").csv"`\

The output location for the code is in the home directory under the '/scans' folder where the CSV files are named in the format YYYY_MM_DD_HH_MM_AM/PM.csv in order to keep track of the scans as they are taken.\

Upon implementation we have been able to learn the importance of not only seeing the security vulnerabilities that can arise in code, but also the importance of seeing this before you commit code in order to allow for remediation.\

By tracking these vulnerabilities as they happen, one can also identify patterns that may occur in the way that they or their organization develops code with vulnerabilities along for them to analyze and fix issues from persisting.\

Below is an example of the output that we received:\

### 4.c.
We integrated forensics by adding logging into 5 methods in the empirical folder.
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

Fuzzing:

1. We chose to fuzz the following 5 methods:
    - reportDensity (empirical/report.py)
    - reportProp (empirical/report.py)
    - reportEventDensity (empirical/frequency.py)
    - checkPythonFile (mining/mining.py)
    - getPythonFileCount (mining/mining.py)
      
2. We then created the 'fuzz.py' script to test the methods with random values.
    <img width="704" alt="Screenshot 2024-04-29 at 2 36 56 PM" src="https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/e682548e-e38b-4ca7-a96e-64c7c83ba919">

3. We used 'fuzz.yaml' to configure the workflow, which runs 'fuzz.py' every time a push is made.
   <img width="406" alt="Screenshot 2024-04-29 at 2 40 09 PM" src="https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/810fcd30-bd1e-43ee-8c16-ec806483af5f">

4. Now testing the commits.
   ![Screenshot 2024-04-29 at 2 46 45 PM](https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/2afbd3eb-4022-4b33-a9eb-5be55d88a929)
