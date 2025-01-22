from yowsup.registration import WACodeRequest, WARegister

def request_code(phone_number, country_code):
    """
    Request a registration code from WhatsApp.
    """
    try:
        registration = WACodeRequest(phone=phone_number, cc=country_code)
        result = registration.send()

        if result.get("status") == "sent":
            print(f"Code sent successfully to {phone_number}. Check your SMS or call.")
            return True
        elif result.get("status") == "fail":
            print(f"Failed to send code: {result.get('reason')}")
        else:
            print(f"Unexpected response: {result}")
        return False
    except Exception as e:
        print(f"Error requesting code: {e}")
        return False

def register_number(phone_number, country_code):
    """
    Prompt user for the OTP and complete registration.
    """
    try:
        verification_code = input("Enter the OTP sent to your phone: ").strip()
        register = WARegister(phone=phone_number, cc=country_code, code=verification_code)
        result = register.send()

        if result.get("status") == "ok":
            print(f"Registration successful! Your password is: {result.get('pw')}")
        elif result.get("status") == "fail":
            print(f"Registration failed: {result.get('reason')}")
        else:
            print(f"Unexpected response: {result}")
    except Exception as e:
        print(f"Error during registration: {e}")

# Example Usage
phone_number = input("Enter your phone number (without country code): ").strip()
country_code = input("Enter your country code: ").strip()

if request_code(phone_number, country_code):
    register_number(phone_number, country_code)
