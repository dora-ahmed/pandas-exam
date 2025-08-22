import pandas as pd
import numpy as np

# إنشاء البيانات
data = {
    "Transaction_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer_Name": ["Ahmed Ali", "Sara Omar", "Ali Saleh", "Nada Hassan", "Omar Khalid", "Ahmed Ali"],
    "Age": [28, np.nan, 35, 42, np.nan, 28],
    "Email": ["ahmed@mail.com", "sara@mail.com", np.nan, "nada@mail.com", "omar@mail.com", "ahmed@mail.com"],
    "Join_Date": ["2025-01-10", "2025-02-15", "2025-03-20", np.nan, "2025-05-05", "2025-01-10"],
    "Total_Purchase": [250, 300, 150, 400, np.nan, 250]
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# 1. تحويل عمود Join_Date إلى نوع تاريخ
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# 2. تحديد الصفوف التي تحتوي على أكثر من قيمة مفقودة
rows_with_many_nulls = df[df.isnull().sum(axis=1) > 1]

# 3. معرفة عدد الأعمدة ونوع البيانات
info = df.info()

# 4. التحقق من عدد القيم الفارغة في كل عمود
missing_counts = df.isnull().sum()

# 5. تحديد الصفوف التي عمرها أكبر من 30
age_above_30 = df[df["Age"] > 30]

# 6. حذف الصفوف التي تحتوي على أي قيمة فارغة
df_no_nulls = df.dropna()

# 7. استبدال القيم الفارغة في Age بمتوسط العمر
df["Age"].fillna(df["Age"].mean())

# 8. استبدال القيم الفارغة في Total_Purchase بالرقم 0
df["Total_Purchase"] = df["Total_Purchase"].fillna(0)

# 9. إزالة الصفوف المكررة
df_no_duplicates = df.drop_duplicates()

# 10. معرفة الصفوف المكررة قبل حذفها
duplicates = df[df.duplicated()]

print("الجدول بعد التنظيف:\n", df_no_duplicates)
