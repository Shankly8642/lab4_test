import pandas as pd
from streamlit_app import filter_and_analyze_data
     
#Тест 1: Проверка формата вывода
def test_output_format():
    test_data = pd.DataFrame({
        'SibSp': [0, 0],
        'Sex': ['male', 'female'],
        'Survived': [1, 1]
    })
    
    result = filter_and_analyze_data(test_data, "0")
    
    for item in result:
        assert 'Доля выживших' in item
        assert 'Выжило/Всего' in item
        assert item['Доля выживших'].endswith('%')
        assert 'Пол' in item
        
# Тест 2: Проверка вычисления доли выживших для SibSp = 0
def test_basic_sibsp_zero():
    test_data = pd.DataFrame({
        'SibSp': [0, 0, 1, 0],
        'Sex': ['male', 'female', 'male', 'female'],
        'Survived': [0, 1, 1, 1]
    })
    
    result = filter_and_analyze_data(test_data, "0")
    
    assert len(result) == 2
    male_data = next(item for item in result if item['Пол'] == 'Мужчины')
    female_data = next(item for item in result if item['Пол'] == 'Женщины')
    
    assert male_data['Доля выживших'] == '0.0%'
    assert female_data['Доля выживших'] == '100.0%'

# Тест 3: Проверка вычисления доли выживших для SibSp = 1-2
def test_sibsp_one_two():
    test_data = pd.DataFrame({
        'SibSp': [1, 2, 3, 1],
        'Sex': ['male', 'female', 'male', 'female'],
        'Survived': [1, 0, 1, 1]
    })
    
    result = filter_and_analyze_data(test_data, "1-2")
    
    male_data = next(item for item in result if item['Пол'] == 'Мужчины')
    female_data = next(item for item in result if item['Пол'] == 'Женщины')
    
    assert male_data['Доля выживших'] == '100.0%'
    assert female_data['Доля выживших'] == '50.0%'

# Тест 4: Проверка вычисления доли выживших для SibSp > 2
def test_sibsp_more_than_two():
    test_data = pd.DataFrame({
        'SibSp': [3, 4, 1, 2],
        'Sex': ['male', 'female', 'male', 'female'],
        'Survived': [1, 0, 1, 1]
    })
    
    result = filter_and_analyze_data(test_data, "больше 2")
    
    male_data = next(item for item in result if item['Пол'] == 'Мужчины')
    female_data = next(item for item in result if item['Пол'] == 'Женщины')
    
    assert male_data['Доля выживших'] == '100.0%'
    assert female_data['Доля выживших'] == '0.0%'
