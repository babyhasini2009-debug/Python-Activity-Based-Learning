#Student Feedback Sentiment Scoring
feedback = input("Enter student feedback: ")
positive = 0
negative = 0
for word in feedback.lower().split():
    if word == "good" or word == "excellent" or word == "nice":
        positive = positive + 1
    elif word == "bad" or word == "poor" or word == "worst":
        negative = negative + 1

print("Positive Words:", positive)
print("Negative Words:", negative)
if positive > negative:
    print("Sentiment: Positive")
elif negative > positive:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
