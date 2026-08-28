"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000)
def reactor_efficiency(voltage, current, theoretical_max_power):
    # 1. محاسبه توان تولیدی
    generated_power = voltage * current
    
    # 2. محاسبه درصد بازدهی (توجه: این عدد اعشاری است)
    percentage = (generated_power / theoretical_max_power) * 100
    
    # 3. بررسی شرایط به ترتیب (از بالا به پایین)
    if percentage >= 80:
        return 'green'
    elif percentage >= 60:
        return 'orange'
    elif percentage >= 30:
        return 'red'
    else:
        return 'black'
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    
    # کمتر از 90 درصد آستانه
    if value < threshold * 0.9:
        return 'LOW'
        
    # بین 90 درصد تا 110 درصد آستانه (چون شرط قبلی False بوده، یعنی حتماً بیشتر یا مساوی 90 است)
    elif value <= threshold * 1.1:
        return 'NORMAL'
        
    # بیشتر از 110 درصد آستانه
    else:
        return 'DANGER'