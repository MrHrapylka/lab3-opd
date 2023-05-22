from flask import Flask, render_template, request

app = Flask(__name__)  # Создание экземпляра приложения Flask

@app.route('/')  # Декоратор маршрута для главной страницы
def index():
    return render_template('index.html')  # Возвращает шаблон 'index.html'

@app.route('/calculate', methods=['POST'])  # Декоратор маршрута для обработки формы
def calculate():
    shape = request.form['shape']  # Получение значения 's
    # hape' из формы
    precision = int(request.form['precision'])  # Получение значения 'precision' из формы и преобразование в целое число

    if shape == 'cube':  # Если выбрана форма куба
        side = float(request.form['side'])  # Получение значения 'side' из формы и преобразование в число с плавающей точкой
        if precision == 0:
            volume = int(side ** 3)  # Расчет объема куба
        else:
            volume = round(side ** 3, precision)  # Расчет объема куба с указанной точностью
    elif shape == 'sphere':  # Если выбрана форма сферы
        radius = float(request.form['radius'])  # Получение значения 'radius' из формы и преобразование в число с плавающей точкой
        if precision == 0:
            volume = int((4 / 3) * 3.14159 * radius ** 3)  # Расчет объема сферы
        else:
            volume = round((4 / 3) * 3.14159 * radius ** 3, precision)  # Расчет объема сферы с указанной точностью
    elif shape == 'cylinder':  # Если выбрана форма цилиндра
        radius = float(request.form['radius'])  # Получение значения 'radius' из формы и преобразование в число с плавающей точкой
        height = float(request.form['height'])  # Получение значения 'height' из формы и преобразование в число с плавающей точкой
        if precision == 0:
            volume = int(3.14159 * radius ** 2 * height)  # Расчет объема цилиндра
        else:
            volume = round(3.14159 * radius ** 2 * height, precision)  # Расчет объема цилиндра с указанной точностью
    elif shape == 'cone':  # Если выбрана форма конуса
        radius = float(request.form['radius'])  # Получение значения 'radius' из формы и преобразование в число с плавающей точкой
        height = float(request.form['height'])  # Получение значения 'height' из формы и преобразование в число с плавающей точкой
        if precision == 0:
            volume = int((1 / 3) * 3.14159 * radius ** 2 * height)  # Расчет объема конуса
        else:
            volume = round((1 / 3) * 3.14159 * radius ** 2 * height, precision)  # Расчет объема конуса с указанной точностью
    elif shape == 'pyramid':  # Если выбрана форма пирамиды
        base_length = float(request.form['base_length'])  # Получение значения 'base_length' из формы и преобразование в число с плавающей точкой
        base_width = float(request.form['base_width'])  # Получение значения 'base_width' из формы и преобразование в число с плавающей точкой
        height = float(request.form['height'])  # Получение значения 'height' из формы и преобразование в число с плавающей точкой
        if precision == 0:
            volume = int((1 / 3) * base_length * base_width * height)  # Расчет объема пирамиды
        else:
            volume = round((1 / 3) * base_length * base_width * height, precision)  # Расчет объема пирамиды с указанной точностью
    else:
        volume = None  # Если форма не выбрана, объем равен None

    return render_template('index.html', volume=volume)  # Возвращает шаблон 'index.html' с передачей объема в качестве параметра

if __name__ == '__main__':
    app.run(debug=True)  # Запуск приложения Flask в режиме отладки
