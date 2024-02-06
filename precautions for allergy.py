def check_rain_symptoms():
    weather_condition = input("Is it raining? (yes/no): ")
    if weather_condition == "yes":
        allergy_symptoms = input("Do you experience allergy symptoms in the rain? (yes/no): ")
        if allergy_symptoms == "yes":
            print("There's a possibility that your allergy symptoms may worsen due to the rain. Take necessary precautions.")
        else:
            print("It's raining, but if you don't experience allergy symptoms, you should be fine.")
    elif weather_condition == "no":
        print("No rain, so your allergy symptoms may not worsen.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

check_rain_symptoms()
