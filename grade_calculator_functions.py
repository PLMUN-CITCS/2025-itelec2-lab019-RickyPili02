def get_student_score():
    """
    Handles user input to obtain the student's score.

    Returns:
        float: The validated student score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))  
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(score):
    """
    Determines the letter grade based on the given score.

    Args:
        score (float): The student's numerical score.

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
    print("Your Grade is:", grade)

if __name__ == "__main__":
    main()