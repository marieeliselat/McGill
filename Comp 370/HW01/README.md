# COMP 370 - Introduction to Data Science: Homework 1

---

### Overview
This assignment provides hands-on experience with data analysis. The task involves analyzing tweets produced by Russian trolls during the 2016 US election, with a specific focus on assessing the frequency of tweets mentioning "Trump" by name.

### Key Objectives
- Data Collection: Download and preprocess the first 10,000 tweets from the file `IRAhandle_tweets_1.csv`, focusing on English language tweets that do not contain a question.
- Data Annotation: Add a new Boolean feature `trump_mention` to indicate whether a tweet mentions "Trump" as a word.
- Analysis: Compute the percentage of tweets mentioning Trump and identify any issues in the counting process.

### Submission Files
- `dataset.tsv`: The annotated dataset in TSV format, containing columns `tweet_id`, `publish_date`, `content`, and `trump_mention`.
- `results.tsv`: The result for the fraction of Trump mentions in TSV format.

### Methodology
- Data was filtered based on language and content criteria and annotated for Trump mentions.
- Analysis involved computing the percentage of tweets with Trump mentions and troubleshooting any counting issues.

---

*This assignment was an individual effort as part of COMP 370. For questions or discussions regarding this work, feel free to contact me.*
