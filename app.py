import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.title("Student Performance Analysis Dashboard")

data = pd.read_csv(r"C:\Users\Admin\Desktop\students.txt")

st.subheader("Dataset Preview")
st.dataframe(data)

st.subheader("Average Subject Scores")

avg_scores = data[['math_score','reading_score','writing_score']].mean()

st.bar_chart(avg_scores)

st.subheader("Gender Distribution")

gender_counts = data['gender'].value_counts()

st.bar_chart(gender_counts)

st.subheader("Study Hours vs Math Score")

fig, ax = plt.subplots()
ax.scatter(data['study_hours'], data['math_score'])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Math Score")
st.pyplot(fig)

st.subheader("Attendance Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(data['attendance'], bins=10)
ax2.set_xlabel("Attendance")
ax2.set_ylabel("Number of Students")
st.pyplot(fig2)

st.subheader("Top Performing Students")

top_students = data.sort_values(by='math_score', ascending=False).head(5)

st.dataframe(top_students)
