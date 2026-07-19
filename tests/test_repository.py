from repository.repo_patient_visit_csv import repo_get_summary

dataframe = repo_get_summary()

print(dataframe.head())

print(dataframe.shape)