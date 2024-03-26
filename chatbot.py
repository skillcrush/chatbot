from openai import OpenAI

client = OpenAI()

# accepts a preferred model and a list of messages
# makes chat completions API call
# returns the response message content
def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content

# prompt the user to ask a question
# user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

# only the first two paragraphs are shown but your code should have the entire plot description
plot_description = """
In the heart of the bustling metropolis of Astoria, the old Henderson House stands 
as a silent sentinel, its imposing facade a stark contrast to the modern skyscrapers 
that surround it. Once a grand mansion, it now sits abandoned, its windows broken, 
its once-luxurious gardens now a tangle of weeds and ivy. The house is said to be 
haunted, its halls echoing with the whispers of a tragic past.

When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately 
drawn to the mystery of the old house. Despite the warnings of her new friends, Mia 
becomes determined to uncover the truth behind the rumors that surround it.
"""

plot_prompt = f"""
Summarize the book plot below between < and > in 100 words or less.

<{plot_description}>

Make the summary exciting, this will be used for an email to announce the book release.
"""

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": plot_prompt}
]

book_summary = get_api_chat_response_message(model, messages)

# only the first two reviews are shown but your code should have the entire list of reviews
book_reviews ={
    "I read The Forgotten House and found it to be average. The writing was decent, and the plot was somewhat engaging, but it didn't leave a lasting impression on me.",
    "I found The Forgotten House to be predictable and lacking in originality. The plot felt formulaic, and the characters were one-dimensional. Overall, a disappointing read."
}

book_reviews_with_sentiments = []

# get the sentiment for each review and build the book_reviews_with_sentiments list
for review in book_reviews:
    review_prompt = f"""Give me the sentiment of {review} as one word, "positive" or "negative"."""

    review_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": review_prompt}
    ]

    sentiment = get_api_chat_response_message(model, review_messages)

    book_reviews_with_sentiments.append({
        "review": review,
        "sentiment": sentiment
    })

print("\n\n" + book_summary + "\n\n")
print(book_reviews_with_sentiments)
