def check_argument(arg):
    # Check if the argument is None or an empty string after stripping whitespace
    if not arg or not arg.strip():
        return True
    return False


# Examples
print(check_argument(""))  # True (empty string)
print(check_argument("    "))  # True (only whitespace)
print(check_argument("Hello"))  # False (contains text)
print(check_argument("  World  "))  # False (contains text with spaces around)
