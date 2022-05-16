# -*- coding: utf-8 -*-

# dataset1: Scrape all tweets with keyword "BeijingOlympics"
import snscrape.modules.twitter as sntwitter
import pandas as pd
import warnings
import itertools

def get_first_dataset():
    warnings.filterwarnings('ignore')
    proxy = None
    kw = 'BeijingOlympics'
    start = "2022-02-04"
    end = "2022-02-20"
    item_num=int(10e10)
    query = '"{kw}" until:{end} since:{start}'.format(kw=kw, end=end, start=start)
    print("looking for: ", query)
    scraper = sntwitter.TwitterSearchScraper(query)
    scraper._session.proxies = {'https': proxy, 'http': proxy}
    tmp_res = scraper.get_items()  # qurey
    res_details = itertools.islice(tmp_res, item_num)  # details, maximum 10e10 records
    df = pd.DataFrame(res_details)
    print("records found: ", df.shape[0], query)
    df.to_csv("datasource1.csv", index=None)
    return df

# dataset2: Scrape all tweets with keyword "BoycottBeijingOlympics"
def get_second_dataset():
    warnings.filterwarnings('ignore')
    proxy = None
    kw = 'BoycottBeijingOlympics'
    start = "2022-02-04"
    end = "2022-02-20"
    item_num=int(10e10)
    query = '"{kw}" until:{end} since:{start}'.format(kw=kw, end=end, start=start)
    print("looking for: ", query)
    scraper = sntwitter.TwitterSearchScraper(query)
    scraper._session.proxies = {'https': proxy, 'http': proxy}
    tmp_res = scraper.get_items()  # qurey
    res_details = itertools.islice(tmp_res, item_num)  # details, maximum 10e10 records
    df = pd.DataFrame(res_details)
    print("records found: ", df.shape[0], query)
    df.to_csv("datasource2.csv", index=None)
    return df

# Scrape all comments from Reddit as dataset3
import praw
def get_third_dataset():
    reddit_read_only = praw.Reddit(client_id="PlE2KRbFbJuh7abkxcL-0w",     
                                   client_secret="QZ0JWkWBlfyCbhpGYaZ7EBXgo805FQ", 
                                   user_agent="ChloeZhang")        # your user agent
    # URL of the post
    url = "https://www.reddit.com/r/AskAnAmerican/comments/m5yj40/would_you_support_a_boycott_of_the_2022_beijing/"
    # Creating a submission object
    submission = reddit_read_only.submission(url=url)

    from praw.models import MoreComments

    post_comments = []

    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
        post_comments.append(comment.body)
    #creating a dataframe
    comments_df = pd.DataFrame(post_comments, columns=['comment'])
    comments_df.to_csv('datasource3.csv')
    return comments_df

# execute program in command line
import sys
if __name__ == "__main__":
    l = list(sys.argv)
    d = {"data1":[],"data2":[],"data3":[]}
    dataset = pd.DataFrame(data=d)
    if len(l)==2 and l[1]=='--scrape':
        dataset1 = get_first_dataset()
        print("Dataset1:the first five rows are:\n",dataset1[:5])
        dataset2 = get_first_dataset()
        print("Dataset2: the first five rows are:\n",dataset2[:5])
        dataset3 = get_first_dataset()
        print("Dataset3: the first five rows are:\n",dataset3[:5])
        
    elif len(l)==3 and l[1]=='--static': # Print all the rows of the dataset (by loading from the stored CSV file)
        path = l[2]
        df = pd.read_csv(path)
        print(df)
        
    elif len(l)==1:
        dataset1 = get_first_dataset()
        content1 = dataset1['content']
        dataset["data1"] = content1
        dataset2 = get_second_dataset()
        content2 = dataset2['content']
        dataset["data2"] = content2
        dataset3 = get_third_dataset()
        content3 = dataset3['comment']
        dataset["data3"] =content3
        dataset.to_csv('combined_datasource.csv')
        print(dataset)

    else:
        print("The arguments do not match the requirements. Please refer README.md for understanding the requirements")

