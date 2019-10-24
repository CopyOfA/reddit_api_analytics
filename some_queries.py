##which user(s) post in more than 1 subreddit?
SQL = "SELECT reddit_authors.author, COUNT(*) FROM reddit_authors JOIN reddit_title_authors USING(author_id) "
SQL += "JOIN reddit_titles USING(title_id)"
SQL += "GROUP BY reddit_authors.author, reddit_titles.subreddit_id HAVING COUNT(*)>1 ORDER BY COUNT(*) DESC "

out = pd.read_sql(sql=SQL, con=connection)

print(out)


##how many unique subreddits are represented here?
sql = "SELECT reddit_subreddits.subreddit, COUNT(*) from reddit_subreddits JOIN reddit_titles USING(subreddit_id) "
sql += "GROUP BY reddit_subreddits.subreddit ORDER BY COUNT(*) DESC"

out = pd.read_sql(sql=sql, con=connection)
print(out)
#the result is heavily weighted by the fact that I gather from new (random sample) and then from 8 specified subreddit


##what time are most of the posts made?
sql = "SELECT DATE_PART('hour', reddit_titles.dttm), COUNT(*) FROM "
sql += "reddit_titles GROUP BY DATE_PART('hour', reddit_titles.dttm) "
sql += "ORDER BY DATE_PART('hour', reddit_titles.dttm)"

out = pd.read_sql(sql=sql, con=connection)
print(out)
#this result is also clearly weighted toward the time at which I get the data from the rss feed
