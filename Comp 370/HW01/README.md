# COMP 370 - Mini Data Science Project: Homework 1

---

### Overview
This individual assignment focuses on hands-on experience with data analysis. The task involves analyzing tweets produced by Russian trolls during the 2016 US election, specifically assessing the frequency of tweets mentioning "Trump" by name.

### Key Learning Objectives
- Conduct data collection and preprocessing.
- Implement data annotation to identify specific features in the dataset.
- Perform statistical analysis to compute the percentage of tweets mentioning Trump.

### Assignment Tasks
1. **Data Collection**: 
   - Download and preprocess the raw tweet data from `IRAhandle_tweets_1.csv`.
   - Filter the first 10,000 tweets based on specific criteria (English language, non-questions).

2. **Data Annotation**: 
   - Annotate the data to include a new feature: `trump_mention`, a Boolean indicating whether the tweet mentions "Trump".

3. **Analysis**: 
   - Compute the statistic: percentage of tweets mentioning Trump.
   - Identify and resolve any issues in counting the tweets.

### Submission Files
- `README.md`: Brief explanation of the counting problem identified in the analysis.
- `dataset.tsv`: Output of the Data Annotation phase. The file should include columns: tweet_id, publish_date, content, and trump_mention.
- `results.tsv`: Contains the calculated statistic for the fraction of Trump mentions.

---

*This repository documents my work for Homework 1 in COMP 370. For any questions or discussions, feel free to reach out.*
