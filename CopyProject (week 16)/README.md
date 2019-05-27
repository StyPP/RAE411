The goal of this project is to display in a graph the time to copy files with different sizes.

A script allows to create files with differents sizes, these files are copyied and then deleted.
The number of files size can be determined in the variable end, it begins to 1Mb to the end.
Then, it's better to have an average of the time, so, we can determined the number of times these files will be created, copied and deleted.
All times are put in a file called time. A python script allows to get his times and displays the average of these times in a graph.

Through the network, files are passed to a receiver from a server. I have used netcat to do this action. The times is computed and then put in a file. Then the python script draw graphs. 

I have had some problems because at the beginninig I have done this project on AWS and then on my computer, on Ubuntu. The bash script write with AWS didn't work in my computer. So I have solved this problem.

To use the network copying, the script "scriptreceiver" has to be run and then the script "scriptserver". Files from different sizes are created, send and removed from both sides. But the file timersever has been completed and then the script python can be runned. 

It was intereting to practice a practrical with netcat. I only known in the course, this semester.
