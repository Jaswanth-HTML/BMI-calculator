from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    bmi_value = None
    category = None
    weight = None
    height = None

    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')

        if weight and height:
            weight = float(weight)
            height = float(height)
            
            if height > 0:
                # BMI formula: weight (kg) / [height (m)]^2
                bmi_value = round(weight / (height ** 2), 2)
                
                # Determine BMI category
                if bmi_value < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi_value < 25:
                    category = "Normal weight"
                elif 25 <= bmi_value < 30:
                    category = "Overweight"
                else:
                    category = "Obese"

    return render_template(
        'bmi.html', 
        bmi=bmi_value, 
        category=category, 
        weight=weight, 
        height=height
    )

if __name__ == '__main__':
    app.run(debug=True)