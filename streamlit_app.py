import streamlit as st
import pandas as pd

def main():

    st.image("https://i.pinimg.com/originals/c8/66/ee/c866ee95bd42e0c8cb3e9d40c53550e2.jpg")

    st.title("Данные пассажиров Титаника")

    df = pd.read_csv('titanic_train.csv')

    sibsp_choice = st.selectbox(
        "Выберите количество братьев и сестер:",
        ["0", "1-2", "больше 2"]
    )

    results = filter_and_analyze_data(df, sibsp_choice)

    st.subheader(f"Доля выживших (SibSp = {sibsp_choice})")
    st.table(results)
    

def filter_and_analyze_data(df, sibsp_choice):

    if sibsp_choice == "0":
        filtered_df = df[df['SibSp'] == 0]
    elif sibsp_choice == "1-2":
        filtered_df = df[(df['SibSp'] >= 1) & (df['SibSp'] <= 2)]
    else:
        filtered_df = df[df['SibSp'] > 2]


    results = []
    for sex in filtered_df['Sex'].unique():
        sex_data = filtered_df[filtered_df['Sex'] == sex]
        total = len(sex_data)
        survived = sex_data['Survived'].sum()
        survival_rate = (survived / total * 100) if total > 0 else 0
        
        sex = "Мужчины" if sex == 'male' else "Женщины"
        
        results.append({
            'Пол': sex,
            'Доля выживших': f"{survival_rate:.1f}%",
            'Выжило/Всего': f"{survived}/{total}"
        })
        
    return results

if __name__ == "__main__":
    main()