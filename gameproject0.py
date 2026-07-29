import random

def play_game():
    """Παίζει μια παρτίδα Πέτρα, Ψαλίδι, Χαρτί."""

    choices = ["πετρα", "ψαλιδι", "χαρτι"]
    
    print("Παρακαλώ διάλεξε: πετρα, ψαλιδι, ή χαρτι;")
    user_choice = input("> ").lower()
    
    while user_choice not in choices:
        print("Μη έγκυρη επιλογή. Διάλεξε ξανά: πετρα, ψαλιδι, ή χαρτι.")
        user_choice = input("> ").lower()
        
    computer_choice = random.choice(choices)
    
    print(f"\nΗ επιλογή σου: **{user_choice.capitalize()}**")
    print(f"Η επιλογή του υπολογιστή: **{computer_choice.capitalize()}**\n")
    
    if user_choice == computer_choice:
        print("🤝 Ισοπαλία!")
        
    elif (user_choice == "πετρα" and computer_choice == "ψαλιδι") or \
        (user_choice == "ψαλιδι" and computer_choice == "χαρτι") or \
        (user_choice == "χαρτι" and computer_choice == "πετρα"):
        print("🎉 Συγχαρητήρια! **Κέρδισες!**")
        
    else:
        print("😞 Δυστυχώς **έχασε** ο παίκτης.")

if __name__ == "__main__":
    while True:
        play_game()
        
        play_again = input("\nΘέλεις να ξαναπαίξεις; (ναι/οχι): ").lower()
        while play_again not in ['ναι', 'οχι']:
            print("Παρακαλω, επιλέξτε ναι η οχι")
            play_again = input("Θελεις να ξαναπαιξεις; (ναι/οχι): ").lower()

        if play_again == 'οχι':
            print("Ευχαριστουμε που επαιξες! Αντιο!")
            break