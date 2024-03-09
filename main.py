import requests

# Conectar a API
response = requests.get('https://randomuser.me/api')


def check_api():
    status_code = response.status_code

    return "Sorry, but cannot connect to the api!Try again later!" if status_code != 200 else "Connected to the API!"


def print_user(first_name: str, last_name: str, age: str, gender: str):
    return f"Name: {first_name} {last_name}\nAge: {age}\nGender: {gender}"


def main():
    print("===== WELCOME TO THE USER GENERATOR =====")
    print(check_api())
    choices = ("g", "q")

    while True:
        print("\ng - Generate User\nq - Quit")
        choice: str = str(input(""))
        if choice.lower().strip() in choices:
            break
        else:
            print("\nChoose a valid option!")

    if choice.lower().strip() == choices[0]:
        print(print_user(response.json()['results'][0]['name']['first'],
                         response.json()['results'][0]['name']['last'],
                         response.json()['results'][0]['registered']['age'],
                         response.json()['results'][0]['gender']))
        print("\nBye!")
    elif choice.lower().strip() == choices[1]:
        print("\nBye!")


if __name__ == "__main__":
    main()

