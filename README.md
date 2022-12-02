# application-response-analysis
A simple example of using Cohere's API to detect whether the first sentence of a response from a company indicates whether you are succesful or not.

#Results
On inputs where the emails would have been: `[positive, negative, negative, positive]` the model ended up returning `[Classification<prediction: "negative", confidence: 0.8578428>, Classification<prediction: "negative", confidence: 0.6063306>, Classification<prediction: "negative", confidence: 0.9652053>, Classification<prediction: "positive", confidence: 0.902598>]`.

As the training data in most cases has negative cases starting with 'Thank you' this shows why the model may have classified the first sentence as the beginning of a negative email, because it found this same pattern: >  "Thank you for your brilliant application!".
