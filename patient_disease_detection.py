import pandas as pd
# Load dataset
data = pd.read_csv(r"C:\5th_sem_projects\ML_unit1\PROJECT 2 Disease_symptom_and_patient_profile_dataset.csv")

# Display the dataset
print("Dataset:\n", data)

# Extract attributes and target
attributes = data.columns[:-1]  # All columns except target
target = data.columns[-1]       # Last column as target

# Step 1: Find first positive example
def find_s_algorithm(df):
    # Only consider positive examples (e.g., 'Yes')
    positive_examples = df[df[target] == 'Yes'].reset_index(drop=True)
    
    if positive_examples.empty:
        print("No positive examples found.")
        return None

    # Initialize hypothesis with the first positive example
    hypothesis = list(positive_examples.loc[0][:-1])

    # Iterate through remaining positive examples
    for i in range(1, len(positive_examples)):
        for j in range(len(hypothesis)):
            if hypothesis[j] != positive_examples.loc[i][j]:
                hypothesis[j] = "?"  # Replace different attributes with '?'

    return hypothesis

# Run Find-S
final_hypothesis = find_s_algorithm(data)

# Display result
print("\nFinal Hypothesis (Specific boundary):")
print(final_hypothesis)
