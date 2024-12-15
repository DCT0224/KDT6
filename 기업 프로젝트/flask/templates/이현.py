from flask import Flask, render_template, request
import mysql.connector
from database_connection import get_database_connection
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the list of models
    model_dir = 'models'
    models = os.listdir(model_dir) if os.path.exists(model_dir) else []
    return render_template('가로로 다시 만들기블랙.html', models=models)

@app.route('/filter-data', methods=['POST'])
def filter_data():
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')

    # Database connection and query
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT c_temp_pv, k_rpm_pv, n_temp_pv, scale_pv, s_temp_pv 
        FROM total_refill_rf_time 
        WHERE date_only BETWEEN %s AND %s
    """
    cursor.execute(query, (start_date, end_date))
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    if not result:
        models = os.listdir('models') if os.path.exists('models') else []
        return render_template('가로로 다시 만들기블랙.html', mse=None, model_name=None, models=models)

    # Convert result to DataFrame
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    import pickle
    import os

    df = pd.DataFrame(result)

    # Train the model (assuming 'scale_pv' is the target column)
    X = df.drop(columns=['scale_pv'])
    y = df['scale_pv']
    model = RandomForestRegressor()
    model.fit(X, y)

    # Calculate MSE
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)

    # Save the model
    model_name = f"RF_{start_date}_to_{end_date}_mae{mae}.pkl"
    model_path = os.path.join('models', model_name)
    os.makedirs('models', exist_ok=True)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

    # Get updated list of models
    models = os.listdir('models') if os.path.exists('models') else []

    return render_template('가로로 다시 만들기블랙.html', mae=mae, model_name=model_name, models=models)


if __name__ == '__main__':
    app.run(debug=True)






#-------------------0-----------------------------------밑에꺼 삭제 하는 버튼





from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from database_connection import get_database_connection
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle
import os

app = Flask(__name__)

# 모델 디렉토리
MODEL_DIR = 'models'

@app.route('/')
def index():
    # 모델 목록 가져오기
    models = os.listdir(MODEL_DIR) if os.path.exists(MODEL_DIR) else []
    return render_template('가로로 다시 만들기블랙.html', models=models)

@app.route('/filter-data', methods=['POST'])
def filter_data():
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')

    # 데이터베이스 연결 및 쿼리 실행
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT c_temp_pv, k_rpm_pv, n_temp_pv, scale_pv, s_temp_pv 
        FROM total_refill_rf_time 
        WHERE date_only BETWEEN %s AND %s
    """
    cursor.execute(query, (start_date, end_date))
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    if not result:
        models = os.listdir(MODEL_DIR) if os.path.exists(MODEL_DIR) else []
        return render_template('가로로 다시 만들기블랙.html', mse=None, model_name=None, models=models)

    # 결과를 DataFrame으로 변환
    df = pd.DataFrame(result)

    # 모델 학습 ('scale_pv'를 타겟 열로 가정)
    X = df.drop(columns=['scale_pv'])
    y = df['scale_pv']
    model = RandomForestRegressor()
    model.fit(X, y)

    # MSE 계산
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)

    # 모델 저장
    model_name = f"RF_{start_date}_to_{end_date}_mse{mse}.pkl"
    model_path = os.path.join(MODEL_DIR, model_name)
    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

    # 업데이트된 모델 목록 가져오기
    models = os.listdir(MODEL_DIR) if os.path.exists(MODEL_DIR) else []

    return render_template('가로로 다시 만들기블랙.html', mse=mse, model_name=model_name, models=models)

@app.route('/delete-model', methods=['POST'])
def delete_model():
    model_name = request.form.get('model_name')
    model_path = os.path.join(MODEL_DIR, model_name)

    if os.path.exists(model_path):
        os.remove(model_path)  # 모델 파일 삭제
        print(f"Deleted model: {model_path}")
    else:
        print(f"Model file not found: {model_path}")

    # 삭제 후 모델 목록 페이지로 리다이렉트
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
