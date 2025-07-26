import secrets
import string
import pyperclip

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """
    Generate a secure random password with customizable complexity.
    
    Args:
        length (int): Desired password length (8-32)
        use_upper (bool): Include uppercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters
        
    Returns:
        str: Generated password
    """
    # Character pool creation
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Validate at least one character set is selected
    if len(chars) == 0:
        print("Warning: No character sets selected. Using default (a-z, 0-9).")
        chars = string.ascii_lowercase + string.digits
    
    # Secure random selection
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    print("\n=== Secure Password Generator ===")
    print("This tool creates cryptographically secure random passwords.\n")
    
    try:
        # Get password length with validation
        while True:
            try:
                length = int(input("Enter password length (8-32): "))
                if 8 <= length <= 32:
                    break
                print("Please enter a value between 8 and 32.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get character set preferences
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate password
        password = generate_password(length, use_upper, use_digits, use_special)
        
        # Display results
        print("\n=== Generated Password ===")
        print(f"Password: {password}")
        print(f"Length: {len(password)} characters")
        
        # Clipboard option
        if input("\nCopy password to clipboard? (y/n): ").lower() == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard!")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")
    
    print("\nThank you for using the Secure Password Generator!")

if __name__ == "__main__":
    main()