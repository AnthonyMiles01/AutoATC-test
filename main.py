import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Dictionary to store callsigns, positions, and flight plans
callsigns = {}

def generate_atc_response(prompt):
    # Generate the ATC response using ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated ATC response
    atc_response = response.choices[0].text.strip()

    return atc_response

# Example usage
print("Welcome to the Automated Ticketing System!")

# Get user input for location
location = input("Please enter the location: ")

while True:
    # Get user input for flight information
    user_input = input("Please provide the flight information (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    # Split user input into callsign and message
    callsign, message = map(str.strip, user_input.split(",", maxsplit=1))

    # Retrieve previous position and flight plan for the callsign if available
    previous_position = callsigns.get(callsign, {}).get("position", "None")
    flight_plan = callsigns.get(callsign, {}).get("flight_plan", "None")

    # Update the current position for the callsign
    callsigns[callsign] = {
        "position": message,
        "flight_plan": flight_plan
    }

    # Construct prompt to inform the AI that it is an ATC and provide previous position and flight plan if available
    prompt = f"You are an Air Traffic Controller (ATC).\nATC: {callsign}, {message}\nLocation: {location}\nPrevious Position: {previous_position}\nFlight Plan: {flight_plan}\n"

    # Generate and display ATC response
    atc_response = generate_atc_response(prompt)

    # Filter out any responses that contain the callsign and remove the callsign prefix
    atc_response = atc_response.replace(callsign, "").strip()

    print("ATC Response:")
    print(atc_response)
    print()
