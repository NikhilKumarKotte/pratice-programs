from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Win money now",
    "Free prize waiting",
    "Congratulations you won",
    "Hello how are you",
    "Let's meet tomorrow",
    "Can you send the notes"
]

# 1 = Spam
# 0 = Normal
labels = [1, 1, 1, 0, 0, 0]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(messages)

model = MultinomialNB()

model.fit(X, labels)

new_message = ["Congratulations you won money"]

new_X = vectorizer.transform(new_message)

prediction = model.predict(new_X)

if prediction[0] == 1:
    print("🚨 Spam")
else:
    print("✅ Not Spam")