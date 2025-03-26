import streamlit as st
def show_recommendations(high_risk: bool):
    # CSS for styling recommendation content
    # st.markdown(
    #     """
    #     <style>
    #     .rec-box {
    #         padding: 15px;
    #         border-radius: 10px;
    #         margin-top: 10px;
    #         line-height: 1.6;
    #         font-size: 16px;
    #     }
    #     .high-risk {
    #         background-color: #ffcccc;
    #         border-left: 5px solid #ff0000;
    #     }
    #     .low-risk {
    #         background-color: #ccffcc;
    #         border-left: 5px solid #008000;
    #     }
    #     .rec-box h4 {
    #         margin-top: 0;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    # high risk recommendations
    if high_risk:
        st.markdown('<div class="rec-box high-risk">', unsafe_allow_html=True)
        st.markdown("### High-Risk Diabetes Recommendation Plan")
        st.write("""
        If you have a high risk of diabetes, immediate action is needed to prevent or manage the disease effectively.
        """)

        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Establish a consistent daily routine for eating, sleeping, and exercising.
        - Reduce stress levels through mindfulness techniques, meditation, or yoga.
        - Quit smoking and excessive alcohol consumption, as both increase diabetes complications.
        - Prioritize quality sleep (7–9 hours per night), as poor sleep can impact blood sugar levels.
        """)

        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Follow a low-carb, high-fiber diet to maintain stable blood sugar levels.
        - Choose whole grains (brown rice, quinoa, whole wheat) over refined grains.
        - Avoid sugary drinks (soda, fruit juices) and processed foods high in added sugars.
        - Increase protein intake (lean meats, fish, eggs, beans) to support metabolism.
        - Eat plenty of non-starchy vegetables (broccoli, spinach, peppers, cucumbers).
        - Consume healthy fats (avocados, nuts, olive oil) instead of trans fats.
        """)

        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Aim for 150 minutes of moderate-intensity exercise per week (e.g., brisk walking, cycling, swimming).
        - Include resistance training (weight lifting, resistance bands) twice a week to improve insulin sensitivity.
        - Engage in daily movement, such as taking stairs instead of elevators and walking after meals.
        """)

        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Check blood sugar levels regularly (as advised by a doctor).
        - Monitor blood pressure and cholesterol to prevent cardiovascular complications.
        - Keep track of weight and BMI, as excess weight increases diabetes risk.
        - Log food intake and activity levels in a journal or app to stay accountable.
        """)

        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Schedule a doctor’s appointment for a comprehensive diabetes risk assessment.
        - Get routine blood tests (A1C, fasting blood sugar, cholesterol, kidney function).
        - Work with a nutritionist or dietitian to create a personalized meal plan.
        - Join a support group or diabetes education program for guidance and motivation.
        """)

        st.markdown('</div>', unsafe_allow_html=True)

    else: # low risk recommendations
        st.markdown('<div class="rec-box low-risk">', unsafe_allow_html=True)
        st.markdown("### Low-Risk Diabetes Recommendation Plan")
        st.write("""
        Even if you are not at high risk for diabetes, the goal is to maintain good health and prevent future risks.
        """)

        st.markdown("#### 1️⃣ Lifestyle Changes")
        st.write("""
        - Maintain a healthy and active lifestyle with balanced meals and regular exercise.
        - Manage stress effectively through relaxation techniques like deep breathing and hobbies.
        - Continue good sleep habits to support overall well-being.
        """)

        st.markdown("#### 2️⃣ Diet & Nutrition")
        st.write("""
        - Eat a balanced diet rich in fiber, lean proteins, and healthy fats.
        - Avoid excess processed foods and sugary snacks to prevent insulin resistance.
        - Stay hydrated by drinking at least 8 glasses of water daily.
        - Consider portion control to maintain a healthy weight and prevent future risks.
        """)

        st.markdown("#### 3️⃣ Exercise & Physical Activity")
        st.write("""
        - Engage in at least 30 minutes of physical activity per day.
        - Mix aerobic exercises (walking, running, swimming) with strength training.
        - Practice flexibility and balance exercises (yoga, Pilates) to improve overall health.
        """)

        st.markdown("#### 4️⃣ Monitoring & Tracking")
        st.write("""
        - Get an annual physical checkup to monitor blood sugar, cholesterol, and blood pressure.
        - Check BMI and weight trends to avoid gradual unhealthy weight gain.
        - Stay aware of any symptoms like excessive thirst, frequent urination, or fatigue, which could signal early diabetes signs.
        """)

        st.markdown("#### 5️⃣ Next Steps")
        st.write("""
        - Continue healthy habits and make small improvements where needed.
        - Get routine blood sugar screenings (especially if there's a family history of diabetes).
        - Keep learning about nutrition and fitness to stay proactive about health.
        """)

        st.markdown('</div>', unsafe_allow_html=True)




def show():
    st.title("Diabetes Prediction")

    # User Input Fields
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)

    # Button to load results (hardcoded for now)
    if st.button("Load Results"):

        # Prediction Score
        prediction_score = 2 # Todo: replace w actual prediction
        high_risk = prediction_score >= 75

    
        st.markdown("###  Your Diabetes Risk Score:")

        st.metric(label ="Score",
                    value = (str(prediction_score) + "%"),
        )

        progress_bar = st.progress(0)
        progress_bar.progress(prediction_score)

        if high_risk:
            st.markdown("<h4 style='color: red; text-align:center;'>You are at <strong>high risk</strong> for diabetes.</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='color: green; text-align:center;'>You are at <strong>low to medium risk</strong> for diabetes.</h3>", unsafe_allow_html=True)



        # Recommendations
        show_recommendations(high_risk)

       