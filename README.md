# MapReduce_Project

It is the final project of udacity Hadoop Course.

###Part 1 Students and Posting Time on Forums
We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.
Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

Mapper: [student_posting_time_mapper.py](https://github.com/LuqiY/MapReduce_Project/blob/master/student_posting_time_mapper.py) 

Reducer: [student_posting_time_reducer.py](https://github.com/LuqiY/MapReduce_Project/blob/master/student_posting_time_reducer.py)

###Part 2 Post and Answer Length
We are interested to see if there is a correlation between the length of a post and the length of answers.
Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

Mapper: [post_answer_length_mapper.py](https://github.com/LuqiY/MapReduce_Project/blob/master/post_answer_length_mapper.py)

Reducer:[post_answer_length_reducer.py](https://github.com/LuqiY/MapReduce_Project/blob/master/post_answer_length_reducer.py)

###Part 3 Top Tags
We are interested seeing what are the top tags used in posts.
Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
For an extra challenge you can think about how to get a top 10 list of tags, where they are ordered by some weighted score of your choice. If you decide to do this, then please submit your solution to the regular problem and then also submit this extra challenge problem in separate files as described on the instruction page.

Mapper: [top_tags_mapper.py](https://github.com/LuqiY/MapReduce_Project/blob/master/top_tags_mapper.py)

Reducer: [top_tags_reducer.py](https://github.com/LuqiY/MapReduce_Project/blob/master/top_tags_reducer.py)

###Part 4 Study Groups
We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

Mapper: [study_groups_mapper.py](https://github.com/LuqiY/MapReduce_Project/blob/master/study_groups_mapper.py)

Reducer: [study_groups_reducer.py](https://github.com/LuqiY/MapReduce_Project/blob/master/study_groups_reducer.py)
