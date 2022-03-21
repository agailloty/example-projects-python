from datetime import datetime

welcome_msg = """
Bienvenue dans Misc-App, un programme utilitaire qui vous permet de faire plein de choses. 
Taper : 
1: Pour convertir votre âge en jours 
2: Pour avoir des informations sur votre jour de naissance
3: 
"""


def birthday_to_days(birthday):
    date_naissance = datetime.fromisoformat(birthday)
    return (datetime.now() - date_naissance).days


def birthday_info(birthday):
    date_naissance = datetime.fromisoformat(birthday)
    return f"""
    Vous êtes né(e) un {date_naissance.strftime("%A")} 
    C'était la {date_naissance.strftime("%V")}e semaine de cette année
    """


def main():
    print(welcome_msg)
    choix = input("Votre choix : ")
    if choix == "1":
        print("Vous avez choisi 1, veuillez entrer votre date de naissance au format AAAA-MM-JJ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        days = birthday_to_days(date_naissance)
        print(f"Vous avez {days} jours sur terre !")
    elif choix == "2":
        date_naissance = input(
            "Vous avez choisi 2, Veuillez entrer votre date de naissance (AAAA-MM-JJ): ")
        print(birthday_info(date_naissance))


main()
