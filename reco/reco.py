from joblib import load
import jieba

# 加载模型
cv = load('D:/Program/code/spam/reco/count_vectorizer.joblib')
tfidf = load('D:/Program/code/spam/reco/tfidf_transformer.joblib')
mnb = load('D:/Program/code/spam/reco/multinomial_nb_classifier.joblib')

# 加载停用词
with open('D:/Program/code/spam/reco/stopwords.txt', encoding='utf8') as file:
    stopword_list = file.read().split('\n')
def preprocess(email_content):

    # 使用jieba进行分词
    cut_words = jieba.lcut(email_content)

    # 移除停用词
    cut_words = [word for word in cut_words if word not in stopword_list]

    # 将分词结果转化为CountVectorizer能够处理的格式
    transformed_email_content = ' '.join(cut_words)

    # 使用CountVectorizer进行向量化
    email_counts = cv.transform([transformed_email_content])

    # 将向量化结果转化为TF-IDF特征
    email_tfidf = tfidf.transform(email_counts)

    # 使用分类器进行垃圾邮件预测
    is_spam = mnb.predict(email_tfidf)

    # 输出预测结果
    if is_spam[0] == 1:
        return False
    else:
        return True
    # print('This email is', 'spam.' if is_spam[0] == 1 else 'not spam.')