print("data uji pertama")
print(20*"-")
tinggi_udin = 1.69
massa_udin = 78
tinggi_nanang = 1.95
massa_nanang = 92

bmi_udin = massa_udin / (tinggi_udin*tinggi_udin)
bmi_nanang = massa_nanang / (tinggi_nanang*tinggi_nanang)

if bmi_udin > bmi_nanang:
    print("BMI Udin "+f"{bmi_udin:.1f}"+" lebih tinggi dari BMI Nanang "+f"{bmi_nanang:.1f}")
else:
    print("BMI Nanang "+f"{bmi_nanang:.1f}"+" lebih tinggi dari BMI Udin "+f"{bmi_udin:.1f}")

print("\ndata uji kedua")
print(20*"-")
tinggi_udin = 1.88
massa_udin = 95
tinggi_nanang = 1.76
massa_nanang = 85

bmi_udin = massa_udin / (tinggi_udin*tinggi_udin)
bmi_nanang = massa_nanang / (tinggi_nanang*tinggi_nanang)

if bmi_udin > bmi_nanang:
    print("BMI Udin "+f"{bmi_udin:.1f}"+" lebih tinggi dari BMI Nanang "+f"{bmi_nanang:.1f}")
else:
    print("BMI Nanang "+f"{bmi_nanang:.1f}"+" lebih tinggi dari BMI Udin "+f"{bmi_udin:.1f}")

