import cohere
from cohere.classify import Example

api_key = '1Gru5QNGbr2sBuoeLjzocxSGdVMWZsIR01V6qx5b'

co = cohere.Client(api_key)

from cohere.classify import Example

examples=[
  Example("Thank you for applying to our Industrial Placement 2023 role.", "negative"), 
  Example("Thank you for expressing an interest in career opportunities with Company.", "negative"),
  Example("Thank you for applying for the Software Development Engineer - Intern position here at Company. ", "negative"),
  Example("Thanks for your recent application to the programme - we’re delighted that you’ve been connected with Company and we hope you are too.", "positive"),
  Example("We will not be moving forward with your application, but we appreciate your time and wish you the best in your search.", "negative"),
  Example("Thanks for taking the time to talk to us, and for being flexible enough to get through our process before the end of the year.", "positive"),
  Example("Company would like to proceed with your application. ", "positive"),
]

inputs=[
  "Thank you for your brilliant application!",
  "Thank you for taking the time to interview with us.",
  "We first want to thank you for applying to this role.",
  "Company would like to congratulate you for progressing to the next round!"
]

response = co.classify(
  model='medium',
  inputs=inputs,
  examples=examples,
)

print(response.classifications)


