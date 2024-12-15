from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from database_connection import get_database_connection

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows의 경우
plt.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login_set.html')

@app.route('/manager_page')
def index():
    return render_template('manager_page.html')

@app.route('/manager_page/Day', methods=['GET'])
def day_plot():
    date = request.args.get('date')
    date_format = "%Y-%m-%d"
    nowdate = datetime.strptime(date, date_format)
    date_list = [(nowdate + timedelta(days=i)).strftime(date_format) for i in range(-3, 4)]
    conn = get_database_connection()
    cursor = conn.cursor()

    # Query data from ai_전_데이터
    query_before = "SELECT loss, quality FROM ai_전_데이터 WHERE date_only = %s"
    cursor.execute(query_before, (date,))
    data_before = cursor.fetchall()

    # Query data from ai_후_데이터
    query_after = "SELECT loss, quality FROM ai_후_데이터 WHERE date_only = %s"
    cursor.execute(query_after, (date,))
    data_after = cursor.fetchall()

    conn.close()

    if not data_before and not data_after:
        return render_template('manager_page.html', chart=None, stacked_chart=None, date=date)

    # Process data into lists
    losses_before = [row[0] for row in data_before]
    qualities_before = [row[1] for row in data_before]
    losses_after = [row[0] for row in data_after]
    qualities_after = [row[1] for row in data_after]

    # Cumulative loss data
    cumulative_before = round(sum(losses_before),3)
    cumulative_after = round(sum(losses_after),3)

    # Plot cumulative loss using matplotlib
    categories = ['Before', 'After']
    values = [cumulative_before, cumulative_after]

    plt.figure(figsize=(10, 6))
    color = 'blue'
    bars = plt.bar(categories, values,width=0.5, color=color, alpha=0.4)
    plt.xlim(-0.7, len(categories) - 1 + 0.7)
    # plt.title(f'Loss of {date}', fontsize=17)
    plt.xlabel('AI 모델 적용', fontsize=15)
    plt.ylabel('Cumulative Loss(g)', fontsize=15)
    plt.ylim(0, max(values) * 1.1)
    plt.xticks(fontsize=14)  # 글자 크기를 14로 설정
    plt.yticks(fontsize=13,weight='bold')
    for i, value in enumerate(values):     # 막대 위에 값 표시
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=12,fontweight='bold')
    

    chart_path = os.path.join(app.root_path, 'static', 'Day_Loss.png')
    plt.savefig(chart_path)
    plt.close()

    # Quality stacked bar chart
    qualities = ['A', 'B', 'C']
    be_quality_counts = pd.Series(qualities_before).value_counts()
    af_quality_counts = pd.Series(qualities_after).value_counts()

    # Prepare counts for plotting
    be_counts = [be_quality_counts.get(q, 0) for q in qualities]
    af_counts = [af_quality_counts.get(q, 0) for q in qualities]

    # X-axis labels
    x_labels = ['Before', 'After']
    width = 0.4
    counts = {quality: [be_counts[i], af_counts[i]] for i, quality in enumerate(qualities)}

    # Plot stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(len(x_labels))
    colors = ['green', 'orange', 'red']

    
    for i, quality in enumerate(qualities):
        p = ax.bar(x_labels, counts[quality], width=0.4, label=quality, color=colors[i], bottom=bottom, alpha=0.5)
        bottom += counts[quality]

        # Add bar labels only if the value is 200 or more
        labels = [str(val) if val >= 200 else '' for val in counts[quality]]
        ax.bar_label(p, labels=labels, label_type='center',fontweight='bold')


    # Configure chart
    max_value = sum(max(counts[key]) for key in counts.keys())/2
    ax.set_xlim(-0.7, len(categories) - 1 + 0.7)
    ax.set_ylim(0, max_value * 1.1)
    # ax.set_title(f'Quality of {date}', fontsize=17)
    ax.set_xlabel('AI 모델 적용', fontsize=15)
    ax.set_ylabel('Counts', fontsize=15)
    plt.yticks(fontsize=13,weight='bold')
    ax.set_xticklabels(x_labels, fontsize=13)  # 글자 크기를 14로 설정

    plt.legend(fontsize=13)  # 범례 글씨 크기



    stacked_chart_path = os.path.join(app.root_path, 'static', 'Day_quality.png')
    plt.savefig(stacked_chart_path)
    plt.close()

    return render_template('Day.html', date_list=date_list, chart=url_for('static', filename='Day_Loss.png'), stacked_chart=url_for('static', filename='Day_quality.png'), date=date)


@app.route('/manager_page/Month', methods=['GET'])
def month_plot():
    year_month = request.args.get('month')
    if year_month:
        # 연도와 월 분리
        date = list(map(int,year_month.split('-')))
        year = date[0]
        month = date[1]
    else:
        # 데이터가 없는 경우 기본 값 처리
        return "Invalid date format. Please provide a valid month.", 400
    year = 0 if year < 0 else year
    date_list = []
    for i in range(-3, 4):
        pyear = year + ((month+i) // 13)
        pmonth = (month + i -1 ) % 12 + 1
        date_list.append(f'{pyear}-{pmonth}')

    conn = get_database_connection()
    cursor = conn.cursor()

    # Query data from ai_전_데이터
    query_before = """
    SELECT loss, quality FROM ai_전_데이터 
    WHERE YEAR(date_only) = %s AND MONTH(date_only) = %s
    """
    cursor.execute(query_before, (year, month))
    data_before = cursor.fetchall()

    # Query data from ai_후_데이터
    query_after = """
    SELECT loss, quality FROM ai_후_데이터 
    WHERE YEAR(date_only) = %s AND MONTH(date_only) = %s
    """
    cursor.execute(query_after, (year, month))
    data_after = cursor.fetchall()

    conn.close()

    if not data_before and not data_after:
        return render_template('manager_page.html', chart=None, stacked_chart=None, year=year, month=month)

    # Process data into lists
    losses_before = [row[0] for row in data_before]
    qualities_before = [row[1] for row in data_before]
    losses_after = [row[0] for row in data_after]
    qualities_after = [row[1] for row in data_after]

    # Cumulative loss data
    cumulative_before = sum(losses_before)
    cumulative_after = sum(losses_after)

    # Plot cumulative loss using matplotlib
    categories = ['Before', 'After']
    values = [cumulative_before, cumulative_after]

    plt.figure(figsize=(10, 6))
    color = 'blue'
    bars = plt.bar(categories, values, width=0.4, color=color, alpha=0.4)

    plt.xlim(-0.7, len(categories) - 1 + 0.7)
    # plt.title(f'Loss for {year}-{month}', fontsize=16)
    plt.xlabel('AI 모델 적용', fontsize=15)
    plt.ylabel('Cumulative Loss(g)', fontsize=15)
    plt.ylim(0, max(values) * 1.1)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=13,weight='bold')

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 10, f'{int(height)}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    chart_path = os.path.join(app.root_path, 'static', 'Month_loss.png')
    plt.savefig(chart_path)
    plt.close()

    # Quality stacked bar chart
    qualities = ['A', 'B', 'C']
    be_quality_counts = pd.Series(qualities_before).value_counts()
    af_quality_counts = pd.Series(qualities_after).value_counts()

    # Prepare counts for plotting
    be_counts = [be_quality_counts.get(q, 0) for q in qualities]
    af_counts = [af_quality_counts.get(q, 0) for q in qualities]

    # X-axis labels
    x_labels = ['Before', 'After']
    counts = {quality: [be_counts[i], af_counts[i]] for i, quality in enumerate(qualities)}

    # Plot stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(len(x_labels))
    colors = ['green', 'orange', 'red']

    for i, quality in enumerate(qualities):
        p = ax.bar(x_labels, counts[quality], width=0.4, label=quality, color=colors[i], bottom=bottom, alpha=0.5)
        bottom += counts[quality]

        # Add bar labels only if the value is 200 or more
        labels = [str(val) if val >= 200 else '' for val in counts[quality]]
        ax.bar_label(p, labels=labels, label_type='center',fontweight='bold')

    # Configure chart
    max_value = sum(max(counts[key]) for key in counts.keys())

    ax.set_xlim(-0.7, len(categories) - 1 + 0.7)
    ax.set_ylim(0, af_quality_counts['A'] * 1.2)
    # ax.set_title(f'Quality for {year}-{month}', fontsize=16)
    ax.set_xlabel('AI 모델 적용', fontsize=15)
    ax.set_ylabel('Counts', fontsize=15)
    plt.legend(fontsize=13)  # 범례 글씨 크기
    plt.yticks(fontsize=13,weight='bold')
    ax.set_xticklabels(x_labels, fontsize=13)

    stacked_chart_path = os.path.join(app.root_path, 'static', 'Month_quality.png')
    plt.savefig(stacked_chart_path)
    plt.close()

    return render_template('Month.html',date_list=date_list, chart=url_for('static', filename='Month_loss.png'), stacked_chart=url_for('static', filename='Month_quality.png'), year=year, month=month)

if __name__ == '__main__':
    app.run(debug=True)
