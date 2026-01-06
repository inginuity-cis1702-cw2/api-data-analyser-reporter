import json

def save_to_json(user_input: dict, user_log: dict, filename="output_json.json"):
    output = {
        "user_input": user_input,
        "user_log": user_log
    }

    with open('output_json.json', 'w') as f:
        json.dump(output, f, indent=4)
        print("Data saved to output_json.json.")
