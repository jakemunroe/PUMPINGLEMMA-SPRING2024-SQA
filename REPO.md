# PUMPING LEMMA Report:
### Authors: Samarth Kumar, Davis Leeth, Jacob Munroe, and Nikhil Patel

## 4.a. 
For the Git Hook, we utilized the following line to implement it:

`bandit -r  ./ -f csv -o scans/"$(date +"%Y_%m_%d_%I_%M_%p").csv"`

The output location for the code is in the home directory under the **'/scans'** folder where the CSV files are named in the format **YYYY_MM_DD_HH_MM_AM/PM.csv** in order to keep track of the scans as they are taken.

Upon implementation we have been able to learn the importance of not only seeing the security vulnerabilities that can arise in code, but also the importance of seeing this before you commit code in order to allow for remediation.

By tracking these vulnerabilities as they happen, one can also identify patterns that may occur in the way that they or their organization develops code with vulnerabilities along for them to analyze and fix issues from persisting.

Below is an example of the output that we received:

![image](https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/72417111/1bb60ccd-330b-4d37-b0cd-e81adbdee232)


## 4.b.
**Fuzzing:**

1. We chose to fuzz the following 5 methods:
    - **reportDensity (empirical/report.py)**
    - **reportProp (empirical/report.py)**
    - **reportEventDensity (empirical/frequency.py)**
    - **checkPythonFile (mining/mining.py)**
    - **getPythonFileCount (mining/mining.py)**
      
2. We then created the **'fuzz.py'** script to test the methods with random values.
    <img width="704" alt="Screenshot 2024-04-29 at 2 36 56 PM" src="https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/e682548e-e38b-4ca7-a96e-64c7c83ba919">

3. We used **'fuzz.yaml'** to configure the workflow, which runs **'fuzz.py'** every time a push is made.
   <img width="406" alt="Screenshot 2024-04-29 at 2 40 09 PM" src="https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/810fcd30-bd1e-43ee-8c16-ec806483af5f">

4. Now testing the commits.
   ![Screenshot 2024-04-29 at 2 46 45 PM](https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/144175666/2afbd3eb-4022-4b33-a9eb-5be55d88a929)

5. Lessons Learned:
   
   Fuzzing involves bombarding software with randomized or unexpected inputs to find vulnerabilities. This technique can be used to detect vulnerabilities that could
   cause crashes or expose security flaws. When completing this project, we learned how to select the appropriate methods for fuzzing as well as how the workflow of the process
   works.
   
## 4.c.
We integrated forensics by adding logging into 5 methods in the empirical folder.
The logging was used in methods that had files or dataframes as input as the data in these files can be poisoned and it is good practice to routinely check it. Logging is crucial in the software quality assurance world because it provides detailed insights into the application’s behavior, facilitating effective debugging and issue resolution. It allows teams to monitor the system in real time and understand the circumstances surrounding any failures or anomalies, thereby enhancing the overall reliability and performance of the software.
We learned that by incorporating logging into critical methods, especially those handling external data, we could preemptively identify and mitigate issues that might corrupt the system or degrade its performance.

Also, a **'myLogger.py' (/MLForensics/MLForensics-farzana/empirical/myLogger.py)** file was added to facilitate the logging actions.

Edited methods:

**report.py:\
*reportDensity( res_file )***

**frequency.py:\
*reportEventDensity(res_file, output_file)*\
*reportProportion( res_file, output_file )***

**dataset.stats.py:\
*getFileLength(file_)*\
*getAllFileCount(df_)***


## 4.d.
Continuous integration was implemented via GitHub Actions using [Codacy Analysis CLI](https://github.com/codacy/codacy-analysis-cli/tree/master). Using this technique, we were able to see how such a process is able to automate the arduous task that is integrating code.

A tool such as [Codacy Analysis](https://github.com/codacy/codacy-analysis-cli/tree/master), give plenty of output for us to analyze possible errors or issues that may exist in our code. This can go from anything in terms of unit testing our code to formatting that might not meet the requirments of an organization. Below is the code for the workflow file (also found in **'/.github/workflows/codacy-analysis.yaml'**):

```
name: Codacy Analysis CLI

on: ["push"]

jobs:
  codacy-analysis-cli:
    name: Codacy Analysis CLI
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@main

      - name: Run Codacy Analysis CLI
        uses: codacy/codacy-analysis-cli-action@master
```

GitHub Actions has also proven to be very useful as it is a central location to host the tool as it allows for not just one person to have access to a tool that might need to be applicable across an organization. Having these workflows available in such a way allows for standardization and formatting to be more centralized and controlled across even large organizations.

Below are a few examples of what such output looks like:

![image](https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/72417111/9aea10fc-7959-487e-89eb-77c132a5a116)

![image](https://github.com/jakemunroe/PUMPINGLEMMA-SPRING2024-SQA/assets/72417111/f56c51d0-4846-4e4a-8a26-ec46eb77d866)

