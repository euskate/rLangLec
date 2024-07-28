# Twitter API 인증 및 데이터 수집
import tweepy
import pandas as pd

# Twitter API 인증 정보 설정
API_KEY = 'YOUR_CONSUMER_KEY'
API_SECRET_KEY = 'YOUR_CONSUMER_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# 인증 및 API 객체 생성
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# 트윗 수집 함수 정의
def collect_tweets(query, max_tweets=1000):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(max_tweets):
        tweets.append({
            'tweet_id': tweet.id,
            'created_at': tweet.created_at,
            'user': tweet.user.screen_name,
            'text': tweet.full_text
        })
    return pd.DataFrame(tweets)

# "data science" 관련 트윗 수집
df_tweets = collect_tweets('data science', max_tweets=1000)
print(df_tweets.head())


# 데이터 전처리: 텍스트 정제 및 변환 - 수집한 트윗 데이터를 분석하기 위해 텍스트를 정제하고 변환합니다.
# 텍스트 정제 및 전처리
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# NLTK 자원 다운로드 (한 번만 실행)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# 텍스트 전처리 함수 정의
def preprocess_text(text):
    # 소문자 변환
    text = text.lower()
    # URL 제거
    text = re.sub(r'http\S+', '', text)
    # 사용자명 및 해시태그 제거
    text = re.sub(r'@\w+|#\w+', '', text)
    # 특수문자 및 숫자 제거
    text = re.sub(r'[^a-z\s]', '', text)
    # 토큰화
    tokens = word_tokenize(text)
    # 불용어 제거 및 어간 추출
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = [ps.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# 트윗 데이터 전처리
df_tweets['clean_text'] = df_tweets['text'].apply(preprocess_text)
print(df_tweets[['text', 'clean_text']].head())


# 데이터 분석: 감정 분석 및 트렌드 추출 - 감정 분석을 통해 트윗의 긍정, 부정, 중립을 판별합니다. VADER 감정 분석기를 사용하여 트윗의 감정을 분석할 수 있습니다.
# 감정 분석
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# VADER 감정 분석기 초기화
analyzer = SentimentIntensityAnalyzer()

# 감정 분석 함수 정의
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

# 감정 분석 수행
df_tweets['sentiment_score'] = df_tweets['clean_text'].apply(analyze_sentiment)
df_tweets['sentiment'] = df_tweets['sentiment_score'].apply(
    lambda score: 'positive' if score > 0.05 else ('negative' if score < -0.05 else 'neutral')
)
print(df_tweets[['text', 'sentiment_score', 'sentiment']].head())


# 트렌드 분석 : 트렌드를 분석하기 위해, 트윗에서 자주 사용된 단어를 추출합니다.
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 단어 구름 생성
text = ' '.join(df_tweets['clean_text'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 단어 구름 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Tweets')
plt.show()


# 감정 분포 시각화
import seaborn as sns

# 감정 분포 시각화
plt.figure(figsize=(10, 6))
sns.countplot(data=df_tweets, x='sentiment', palette='viridis')
plt.title('Sentiment Distribution of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()


# 트윗 타임라인 분석 : 트윗의 시간에 따른 분포를 분석합니다.
# 시간대별 트윗 수 계산
df_tweets['hour'] = df_tweets['created_at'].dt.hour
tweets_per_hour = df_tweets.groupby('hour').size()

# 시간대별 트윗 수 시각화
plt.figure(figsize=(10, 6))
tweets_per_hour.plot(kind='bar', color='skyblue')
plt.title('Number of Tweets per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Tweets')
plt.show()
