#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up
hindi_dict = {
    "नमस्ते": "Hello",
    "नमस्कार": "Hello",
    "अलविदा": "Goodbye",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "हाँ": "Yes",
    "नहीं": "No",
    "माफ़ कीजिए": "Sorry",
    "मैं": "I",
    "आप": "You",
    "घर": "Home",
    "पानी": "Water",
    "खाना": "Food",
    "दोस्त": "Friend",
    "किताब": "Book"
}

def lookup_translation(word):
    word = word.strip().lower()
    for hindi, english in hindi_dict.items():
        if hindi.lower() == word:
            return english
    return "Translation not found. Try again!"

print("Hindi to English Dictionary (type 'quit' to exit)")
while True:
    try:
        user_input = input("\nEnter Hindi word: ")
        if user_input.lower() == 'quit':
            print("धन्यवाद! Thanks!")
            break
        result = lookup_translation(user_input)
        print(f"→ {result}")
    except KeyboardInterrupt:
        print("\nExiting...")
        break
