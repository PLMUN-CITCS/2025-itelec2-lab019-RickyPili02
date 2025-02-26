def get_student_score() -> float:
    """
    Prompts the user to enter their score and returns it as a float.
    Ensures that input is a valid numeric value.
    """
    while True:
        try:
            score = float(input("Enter your score: ")) 
            if 0 <= score <= 100:
                return score  
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid numeric score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the provided score.
    
    Args:
        score (float): The numerical score of the student.
    
    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """Main function to run the grade calculator."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()