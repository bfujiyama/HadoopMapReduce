# HadoopMapReduce
Hadoop Mapper and Reducer for Coursera Big Data/Hadoop project

Your Task: Implement the following join request in Map/Reduce:
What is the total number of viewers for shows on ABC?

The show-to-channel relationship is Many-to-Many. In other words, each show might appear on many channels, and each channel might broadcast many shows.

In pseudo-SQL it might be something like:
select sum( viewer count) from File A, File B where FileA.TV show = FileB.TV show and FileB.Channel='ABC' grouped by TV show

Generate datasets using: 
sh make_data_join2.txt

To make the mapper and reducer executable:
> chmod +x join1_mapper.py   
> chmod +x join1_reducer.py  

After uploading all 6 files to HDFS and writing the mapper and reducer codes, use the following command to run the mapreduce:
> hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_join \   
   -mapper /home/cloudera/join1_mapper.py \   
   -reducer /home/cloudera/join1_reducer.py
   
Test/debug mapper using:  
   cat join2_gen*.txt | ./join1_mapper.py | sort  
   
Test/debug mapper and reducer using:  
   cat join2_gen*.txt | ./join1_mapper.py | sort | ./join1_reducer.py

Consider breaking down into the following parts to write the mapper and reducer:

    Make the mapper output 1 tv_show only (tv_shows, views)
    Make the reducer add up the views for 1 tv_show (tv_show, total_views)
    Make the mapper output 1 tv_show only (tv_shows, views) + (tv_shows, ABC)
    Make the reducer handle what happens when "ABC" occurs
    Make the mapper output all tv shows (tv_shows, views) + (tv_shows, ABC)
    Make the reducer handle what happens for multiple tv_shows

join2_mapper:  
read lines, and split lines into key & value  
if value is ABC or if value is a digit print it out  

join2_reducer:  
read lines and split lines into key & value  
if a key has changed (and it's not the first input)  
then check if ABC had been found and print out key and running total,  
if value is ABC then set some variable to mark that ABC was found (like abc_found = True)  
otherwise keep a running total of viewer counts

The first two lines of your output should be:  
Almost_Games 49237  
Almost_News 46592  
