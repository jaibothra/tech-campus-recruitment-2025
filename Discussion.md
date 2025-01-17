Solutions Considered: 

Using mmap to reduce the time taken to filter through a 1TB logfile was my first intuition. mmap (memory mapping) allows you to map a file directly into memory instead of reading it line by line. This can be much faster because it reduces the overhead of file I/O. It works by creating a memory region that behaves like the file itself, allowing you to access parts of the file as if they were in memory, rather than physically loading each piece into memory one at a time.

I implemented this approach in my first version of the code, which is saved as test.py. The idea was to use mmap to read the file all at once and search for lines starting with the target date. While it seemed like a good solution for handling large files, it ended up being slower than expected for my use case. I ditched that approach considering that I needed the program to return results as quickly as possible.

Final Solution Summary:

After realizing that mmap wasn’t giving me the response time I had for, I decided to switch strategies. Instead of using mmap, I opted for a simpler and more efficient approach to process the file line by line. In this new strategy, I opened the log file and checked each line individually to see if it started with the target date. If it did, I wrote that line to the output file.
This strategy turned out to be much faster and more efficient for my needs, and I uploaded this final version of the code as extract_logs.py.

Steps to Run: 

Simply run the command along with the select date you are searching for -> python extract_logs.py 2024-12-01
