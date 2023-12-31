# Data Crawling and Cleaning

This repository contains code and instructions for data crawling and cleaning tasks. The tasks are divided into three exercises: Data Crawling, Data Cleaning, and Hadoop implementation on Hadoop Data.

## Exercise 1: Data Crawling

1. Install required packages:
   ```
   pip install requests beautifulsoup4 lxml
   ```

2. Writing the crawler:
   - Right-click on any Wiki CFP page and click on "Inspect Element".
   - Observe that header rows have `bgcolor` set to `#bbbbbb`, while conference rows have `bgcolor` set to either `#f6f6f6` or `#e6e6e6`.
   - Each entry has two consecutive rows. The first row contains acronym and name, and the second row contains date and location.
   - Use the provided information to fetch the desired values.

After running the above code, a file named "data.tsv" will be created.

## Exercise 2: Data Cleaning

1. Download and install OpenRefine from [https://openrefine.org/download.html](https://openrefine.org/download.html).

2. Extract the OpenRefine folder using the following command:
   ```
   tar -xzf openrefine-<version>.tar.gz
   ```

3. Open OpenRefine by running the "refine" script from the extracted directory.

4. A browser will open the OpenRefine homepage.

5. Load the TSV file generated by the crawler.

6. After selecting the file, click on the "Next" button.

7. Ensure the following settings match for parsing options:
   - Separator: Tab
   - Has header lines: Checked
   - Charset: UTF-8

8. Click on "Create Project".

9. Split the location to extract cities:
   - Click on the arrow button next to `con_location`.
   - Select "Split into several columns".

10. Split the cells using separators like ",", "()", and "-". This will generate multiple columns.

11. Sort each generated column alphabetically.

12. Manually review and edit each cell in the newly generated columns to extract only the cities. To edit a cell, hover over it and click the edit button that appears.

13. Delete rows that do not have valid cities (e.g., online, hybrid, etc.):
    - Click on the dropdown button as shown.
    - Select "Facet".
    - Enter the following regular expression: `(\bBook Chapter\b|\bco\b|\bCyberspace\b|\bHybrid\b|\bIEEE Computer Magazine\b|\bIEEE Computer Special Issue\b|\blive online\b|\bMadhav Institute of Technology & Science\b|\bMathematical Biosciences and Engineering\b|\bMDPI\b|\bonline\b|\bonline event\b|\bonline streaming\b|\bOnline Virtual Training\b|\bSouth Asian University\b|\bqatar\b|\bspain\b|\bTBA\b|\bTBD\b|\bvirtual\b|\bN/A\b|\bTUNISIA\b|\bCyprus\b)`.
    - Click on "OK".

14. Click on the "All" column, select "Edit Rows," and then click on "Remove matching rows".

15. Remove the filter by clicking on the cross button near `con_location 1`.

16. Similarly, remove rows that do not have valid dates/years using the regex "N/A".

17. Remove the extra columns that were created.

18. Rename `con_location 1` to `con_location`.

19. Remove duplicate conferences and empty cells:
    - Sort `con_name`.
    - Reorder the rows permanently.
    - Click on "Blank Down" to empty duplicate cells.

20. Delete rows with blank/empty cells.

21. Include the blank cell by selecting "true".

22. Remove matching rows.

23. Delete the facet.

24. Export the cleaned data as a TSV file.

## Exercise 3: Hadoop implementation on Hadoop Data

1. Make sure the following libraries are installed: Plotly, Kaleido, and Pandas.

2. Create a new directory for this project in Hadoop:
   ```
   hadoop fs -mkdir -p /user/your/path/conferences
   ```

   Confirm that the new directory is created.

### Question 1: Compute and plot the number of conferences per city.

1. Create a folder for the input in the conferences directory:
   ```
   hadoop fs -mkdir -p /user/your/path/conferences/ques1/input
   ```

2. Copy the cleaned data generated from OpenRefine into this folder:
   ```
   hadoop fs -put /your/path/to/data.tsv /user/your/path/conferences/ques1/input
   ```

3. Mapper.py: Code in respective folders

4. Reducer.py: Code in respective folders

5. Execute the MapReduce job:
   ```
   hadoop jar share/Hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -input /user/your/path/conferences/ques1/input/data.tsv -output /user/your/path/conferences/ques1/output
   ```

6. Download the output file to a local directory.

7. Plot the graph using Plot.py: (Code not provided)

### Question 2: List of conferences per city

1. Create the input folder:
   ```
   hadoop fs -mkdir -p /user/your/path/conferences/ques2/input
   ```

2. Put the cleaned data file in the input folder:
   ```
   hadoop fs -put /your/path/to/data.tsv /user/your/path/conferences/ques2/input
   ```

3. Mapper.py: Code in respective folders

4. Reducer.py: Code in respective folders

5. Run the MapReduce job:
   ```
   hadoop jar share/Hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -input /user/your/path/conferences/ques2/input/data.tsv -output /user/your/path/conferences/ques2/output
   ```

6. Fetch the output files to view the results.

### Question 3: List of cities for each category

1. Make the input directory:
   ```
   hadoop fs -mkdir -p /user/your/path/conferences/ques3/input
   ```

2. Put the cleaned data file in the input directory:
   ```
   hadoop fs -put /your/path/to/data.tsv /user/your/path/conferences/ques3/input
   ```

3. Mapper.py: Code in respective folders

4. Reducer.py: Code in respective folders

5. Run the MapReduce job:
   ```
   hadoop jar share/Hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -input /user/your/path/conferences/ques3/input/data.tsv -output /user/your/path/conferences/ques3/output

6. Get the output files and check the results:
   ```
   hadoop fs -get /user/your/path/conferences/ques3/output
   ```

### Question 4: Time series plot

1. Create the input directory and put the data file into it:
   ```
   hadoop fs -mkdir -p /user/your/path/conferences/ques4/input
   hadoop fs -put /your/path/to/data.tsv /user/your/path/conferences/ques4/input
   ```

2. Mapper.py: Code in respective folders

3. Reducer.py: Code in respective folders

4. Execute the MapReduce job:
   ```
   hadoop jar share/Hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -input /user/your/path/conferences/ques4/input/data.tsv -output /user/your/path/conferences/ques4/output
   ```

5. Fetch the output files and check the results:
   ```
   hadoop fs -get /user/your/path/conferences/ques4/output
   ```

6. Plot the time series graph using Plot.py: (Code not provided)

Please refer to the individual exercise folders for more specific instructions, code, and additional files.

