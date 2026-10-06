import pandas as pd
import os

file_path = 'Advertising.csv'

def load_data():
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print("Error: Advertising.csv not found.")
        return None

while True:
    df = load_data()
    if df is None: break

    print("\n--- Project Menu: Data Management ---")
    print("1. Ajouter une ligne (Add Row)")
    print("2. Afficher la deuxième colonne (Display Radio)")
    print("3. Rechercher une donnée (Search Sales)")
    print("4. Modifier une donnée (Update Row)")
    print("5. Supprimer une donnée (Delete Row)")
    print("6. Quitter (Quit)")
    
    choice = input("Select an option (1-6): ")

    if choice == '1':
        tv = float(input("Enter TV budget: "))
        radio = float(input("Enter Radio budget: "))
        news = float(input("Enter Newspaper budget: "))
        sales = float(input("Enter Sales: "))
        new_row = pd.DataFrame({'TV': [tv], 'Radio': [radio], 'Newspaper': [news], 'Sales': [sales]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file_path, index=False)
        print("Row added successfully.")

    elif choice == '2':
        print("\nDisplaying 'Radio' Column:")
        print(df.iloc[:, 1]) 

    elif choice == '3':
        val = float(input("Enter Sales value to search: "))
        print(df[df['Sales'] == val])

    elif choice == '4':
        idx = int(input("Enter row index to modify: "))
        col = input("Enter column (TV, Radio, Newspaper, Sales): ")
        new_val = float(input("Enter new value: "))
        df.at[idx, col] = new_val
        df.to_csv(file_path, index=False)
        print("Value updated.")

    elif choice == '5':
        idx = int(input("Enter row index to delete: "))
        df = df.drop(idx).reset_index(drop=True)
        df.to_csv(file_path, index=False)
        print("Row deleted.")

    elif choice == '6':
        print("Exiting Management...")
        break