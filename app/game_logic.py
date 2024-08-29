def get_game_data(level):
    # TODO: Define the game data for each level, including challenges, hints, and objectives
    levels = {
        1: {
            "objective": "Breach the Perimeter Firewall",
            "hint": "Download the file and decrypt the password using ROT13.",
            "question": "Download the file below and find the correct password.",
            "file_link": "/static/files/level1_password.txt",  # Link to the downloadable file
            "final_answer": "W!tp@$sw3rd"
        },
        2: {
            "level": 2,
            "objective": "Decode the Encryption",
            "hint": "Think about common encryption methods.",
            "question": "Decode the encrypted message: 'Uryyb Jbeyq!'"
        },
        # TODO: Add more levels with increasing complexity
    }
    return levels.get(level, {})

def process_level(level, player_input):
    # TODO: Implement the logic for checking the player's input against the correct answer]
    correct_answers = {
        1: "W!tp@$sw3rd",  # Final decrypted answer for Level 1
        2: "Hello World!",  # Example answer for Level 2 (ROT13 decoding)
        # TODO: Add more correct answers for additional levels
    }

    success = player_input == correct_answers.get(level)
    feedback = "Correct!" if success else "Try again. Remember the hint."
    return success, feedback
