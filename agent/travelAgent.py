import groq

def get_travel_recommendation(destination, duration, budget, interests):
    """
    Generates a simple travel recommendation using Groq's API.

    Args:
        destination: The desired travel destination.
        duration: The length of the trip (e.g., "7 days", "weekend").
        budget: The approximate budget (e.g., "low", "medium", "high").
        interests: A list of interests (e.g., ["beaches", "hiking", "museums"]).

    Returns:
        A string containing a travel recommendation.
    """

    client = groq.Groq(api_key="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")  # Replace with your actual API key.

    prompt = f"""
    You are a helpful travel agent. Provide a travel recommendation based on the following:

    Destination: {destination}
    Duration: {duration}
    Budget: {budget}
    Interests: {', '.join(interests)}

    Recommendation:
    """

    try:
        chat_completion = client.chat.completions.create(
            model="mixtral-8x7b-32768", # or your preferred model
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        recommendation = chat_completion.choices[0].message.content.strip()
        return recommendation

    except groq.APIError as e:
        print(f"Groq API Error: {e}")
        return "Sorry, I couldn't generate a recommendation at this time."

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, I couldn't generate a recommendation due to an internal error."

# Example usage:
if __name__ == "__main__":
    destination = "Tokyo"
    duration = "10 days"
    budget = "medium"
    interests = ["food", "culture", "technology"]

    recommendation = get_travel_recommendation(destination, duration, budget, interests)
    print(recommendation)

    destination2 = "Paris"
    duration2 = "weekend"
    budget2 = "high"
    interests2 = ["art", "food", "sightseeing"]

    recommendation2 = get_travel_recommendation(destination2, duration2, budget2, interests2)
    print(recommendation2)