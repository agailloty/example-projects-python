import numpy as np
experience_sample = np.linspace(0, 35, 70)  # 70 niveaux d'expériences
education = np.arange(15)
education_sample = np.random.choice(education, 70, True)  # Niveau d'éducation

print(education_sample)
