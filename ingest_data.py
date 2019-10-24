import feedparser
from bs4 import BeautifulSoup
from bs4.element import Comment
import numpy as np

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)




data = {}
data['dttm'] = []
data['title'] = []
data['title_id'] = []
data['summary_text'] = []
data['link'] = []
data['author'] = []
data['author_id'] = []
data['subreddit'] = []
data['subreddit_id'] = []
tid = 0
aid = 0
sid = 0
while len(data['title'])<400:
    a_reddit_rss_url = 'http://www.reddit.com/new/.rss?sort=new'
    feed = feedparser.parse( a_reddit_rss_url )
    if (feed['bozo'] == 1):
        print("Error Reading/Parsing Feed XML Data")    
    else:
        for item in feed[ "items" ]:
            if item['title'] not in data['title']:
                data['dttm'].append(item[ "date" ][:10] + ' ' + item["date"][12:19])
                data['title'].append(item[ "title" ])
                data['title_id'].append(tid)
                data['summary_text'].append(text_from_html(item[ "summary" ]).split('/u')[0].strip())
                data['link'].append(item[ "link" ])
                
                #get author name and test if it exists in our data already
                #if so, get previous id number, if not generate a new one
                data['author'].append(item['author'])
                if data['author'][-1] in data['author'][0:-1]:
                    data['author_id'].append(data['author_id'][
                                    np.where([data['author'][-1]==i for i in data['author'][0:-1]])[0][0]])
                else:
                    data['author_id'].append(aid)
                    aid += 1
                    
                #get subreddit name and test if it exists in our data already
                #if so, get previous id number, if not generate a new one   
                data['subreddit'].append(item['tags'][0]['term'])
                if data['subreddit'][-1] in data['subreddit'][0:-1]:
                    data['subreddit_id'].append(data['subreddit_id'][
                                    np.where([data['subreddit'][-1]==i for i in data['subreddit'][:-1]])[0][0]])
                else:
                    data['subreddit_id'].append(sid)
                    sid += 1
                tid += 1

    subreddits = ['funny','datascience','python','statistics','dataisbeautiful','politics','NoSQL','MachineLearning']
    for sub in subreddits:
        a_reddit_rss_url = 'http://www.reddit.com/r/'+ sub + '/.rss?sort=new'
        feed = feedparser.parse( a_reddit_rss_url )
        if (feed['bozo'] == 1):
            print("Error Reading/Parsing Feed XML Data")    
        else:
            for item in feed[ "items" ]:
                if item['title'] not in data['title']: #eliminate duplicates (assuming titles are unique)
                    data['dttm'].append(item[ "date" ][:10] + ' ' + item["date"][12:19])
                    data['title'].append(item[ "title" ])
                    data['title_id'].append(tid)
                    data['summary_text'].append(text_from_html(item[ "summary" ]).split('/u')[0].strip())
                    data['link'].append(item[ "link" ])
                    
                    #get author name and test if it exists in our data already
                    #if so, get previous id number, if not generate a new one
                    data['author'].append(item['author'])
                    if data['author'][-1] in data['author'][0:-1]:
                        data['author_id'].append(data['author_id'][
                                        np.where([data['author'][-1]==i for i in data['author'][:-1]])[0][0]])
                    else:
                        data['author_id'].append(aid)
                        aid += 1
                        
                    #get subreddit name and test if it exists in our data already
                    #if so, get previous id number, if not generate a new one
                    data['subreddit'].append(item['tags'][0]['term'])
                    if data['subreddit'][-1] in data['subreddit'][0:-1]:
                        data['subreddit_id'].append(data['subreddit_id'][
                                        np.where([data['subreddit'][-1]==i for i in data['subreddit'][:-1]])[0][0]])
                    else:
                        data['subreddit_id'].append(sid)
                        sid += 1
                    tid += 1
