def run_battle(health_potion_amount, enemy_attack_power,enemy_health = 150, player_health = 100):

    query = "5"
    round_no = 0
    while player_health > 0:

        query = "5" 
        round_no += 1

        while query != "0" and query != "1":
            query = input(f"Round {round_no}, what would you like to do: press 1 for health potion, press 0 for attack: ")
            print("")

        if query == "1": # Health Potions
            if health_potion_amount <= 0:
                print("No more potions left, enemys turn now!")
                print("")
            else:
                player_health += 15
                if player_health > 100:
                    player_health = 100
                print(f"You have {health_potion_amount} health potions left!")
                print(f"Your health is {player_health} now! Time for enemys turn!")
                print("")
                health_potion_amount -= 1

        else: # Player Attacks
            player_attack_power = int(input("Choose your attack power (1-10): "))

            if player_attack_power >10 or player_attack_power <1:
                print("Invalid attack power, proceeding with enemy attack!")
                print("")
            else:
                enemy_health -= player_attack_power
                if enemy_health >0:
                    print(f"Nice shot, the enemy health is {enemy_health} now!")
                    print("")
                else:
                    print("The enemy's health is 0 now!")
                    print(f"You've defeated the enemy, GGS!")
                    print("")
                    break

        
        player_health -= enemy_attack_power #Enemy Counter-attacks
        if player_health >= 20:
            print("Oh no, you've got hit!")
            print(f"Your health is {player_health} now!")
            print("")
        elif player_health <20 and player_health > 0:
             print(f"Be cautious, your health is {player_health} now!")
             print("")
        else:
            print("Player defeated...")
            print("")
            break

enemy_power = 5 # You can choose enemy power to make the game harder/easier.
run_battle(5,enemy_power)
