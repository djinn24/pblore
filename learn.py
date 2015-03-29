import createds
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# get data set
review = createds.ex_dataset()

#tokenize
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(review.data[:450])

#transform
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#train
clf = MultinomialNB().fit(X_train_tfidf, review.target[:450])

#predict
#rev_new = ['worst']
rev_new = review.data[450:500]
X_new_counts = count_vect.transform(rev_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)

i=450

a=b=c=0
for t in review.target:
  if t==0:
    a+=1
  elif t==1:
    b+=1
  else:
    c+=1 
   
print a,b,c


for rev, res in zip(rev_new, predicted):
  if res == review.target[i]:
    print 'correct',
  else:
    print 'incorrect',
  print res,review.target[i]
  i+=1

