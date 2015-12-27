# HadoopMapReduce
Hadoop Mapper and Reducer for Coursera Big Data/Hadoop project

Your Task: Implement the following join request in Map/Reduce:
What is the total number of viewers for shows on ABC?

The show-to-channel relationship is Many-to-Many. In other words, each show might appear on many channels, and each channel might broadcast many shows.

In pseudo-SQL it might be something like:

select sum( viewer count) from File A, File B where FileA.TV show = FileB.TV show and FileB.Channel='ABC' grouped by TV show
