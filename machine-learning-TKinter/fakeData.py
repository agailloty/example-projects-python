import numpy as np
import pandas as pd
experience_sample = np.linspace(0, 35, 70)  # 70 niveaux d'expériences
education = np.arange(15)
education_sample = np.random.choice(education, 70, True)  # Niveau d'éducation

salary = 1280 + 12.9 * education_sample + 30 * \
    experience_sample + experience_sample * education_sample * 10

data = pd.DataFrame({"education_years": education_sample,
                     "experience_years": experience_sample, "salary": salary})
data.to_csv("salary_data.csv", index=False)
