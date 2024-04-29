Report:

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
