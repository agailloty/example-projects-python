from tkinter import *
from joblib import load
model = load("model.joblib")


root = Tk()
#root.configure(background='light gray')
root.title("Impact étude & expérience sur salaire.")

root.geometry("500x200")
heading = Label(root, text="Déploiement Machine Learning")

years_study = Label(root, text="Années d'études")
experience = Label(root, text="Années d'expérience")

heading.grid(row=1, column=1)
years_study.grid(row=2, column=1)
experience.grid(row=3, column=1)


years_study_field = Entry(root)
experience_field = Entry(root)

years_study_field.grid(row=2, column=2, ipadx="50")
experience_field.grid(row=3, column=2, ipadx="50")

result_label = Label()
result_label.grid(row=12, column=1, columnspan=4)


def compute(years_study, years_experience):
    years_study = float(years_study)
    years_experience = float(years_experience)
    salary = model.predict([[years_study, years_experience]])
    result_label.config(
        text=f"Le salaire prédit pour {years_study} années d'études et {years_experience} années d'expérience est {salary}.")


predict = Button(root, text="Prédire salaire",
                 bg="Green", command=lambda: compute(years_study_field.get(), experience_field.get()))
predict.grid(row=8, column=3)

root.mainloop()
