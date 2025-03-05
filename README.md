# Sleep Cycle & Productivity Analyzer 😴📊
## Video: q

The **Sleep Cycle & Productivity Analyzer** is a Python-based application that helps users track their sleep patterns and analyze their impact on productivity. Built using **Streamlit**, this project allows users to calculate their sleep duration, receive recommendations for optimal wake-up times, and visualize the correlation between their sleep duration and work productivity.

This project is designed for students, professionals, and anyone who wants to understand the impact of their sleep on their daily performance. The app features **data visualization** using **Matplotlib** to give users insights into how their sleep habits affect their efficiency.

## Features
- **Calculate Sleep Duration**: Users can enter their sleep and wake-up times to determine how many hours they slept.
- **Suggest Best Wake Time**: Based on sleep cycles (90-minute increments), the app recommends an optimal wake-up time for feeling refreshed.
- **Analyze Productivity Correlation**: Users can input past sleep durations and productivity scores to visualize and understand their relationship.
- **Data Visualization**: Scatter plots help users interpret sleep and productivity trends easily.
- **User-Friendly Interface**: Built with **Streamlit**, ensuring a clean, interactive, and intuitive experience.

## File Structure
The project contains the following key files:

### **1. `project.py`** (Main Application)
This is the core file that contains the main functionality of the application. It includes:
- **`calculate_sleep_duration(sleep_time, wake_time)`**: Computes the number of hours slept based on user input.
- **`suggest_best_wake_time(target_duration, sleep_stages)`**: Recommends an ideal wake-up time based on **90-minute sleep cycles**.
- **`analyze_productivity(sleep_data, work_performance)`**: Uses **NumPy's correlation coefficient** to determine the relationship between sleep duration and productivity.
- **`main()`**: The primary function that integrates all features and displays them in the **Streamlit** UI.

### **2. `test_project.py`** (Unit Tests)
This file contains **pytest** tests to ensure that each function in `project.py` behaves as expected:
- **Tests for `calculate_sleep_duration()`**: Ensures sleep duration is calculated correctly, accounting for overnight shifts.
- **Tests for `suggest_best_wake_time()`**: Confirms that the recommended sleep duration aligns with realistic sleep cycles.
- **Tests for `analyze_productivity()`**: Checks that the correlation function correctly interprets relationships in the dataset.

### **3. `requirements.txt`** (Dependencies)
This file lists all required Python packages for the project to run smoothly:
```
streamlit
numpy
matplotlib
pytest
```
Users can install these dependencies using:
```bash
pip install -r requirements.txt
```

## Design Choices and Challenges
### **1. Choosing Streamlit for UI**
I decided to use **Streamlit** for the interface because it allows for fast and simple deployment of Python-based applications. Unlike other frameworks like Flask or Django, Streamlit is optimized for **data visualization and user interactivity**, making it an excellent choice for this project.

### **2. Sleep Cycle Calculations**
The most challenging part was implementing the **best wake-up time recommendation**. Since sleep cycles are **90 minutes long**, I designed a function that rounds the target duration to the nearest sleep cycle, ensuring recommendations align with established sleep science.

### **3. Correlation Analysis with NumPy**
To make the productivity analysis statistically meaningful, I used **NumPy's correlation coefficient** instead of simple averages. This allows users to see whether there is a **strong, weak, or no correlation** between their sleep and productivity.

## Academic Integrity & AI Usage
For this final project, AI-based tools such as **ChatGPT, GitHub Copilot, and Bing Chat** were used as productivity amplifiers, **not as replacements for original work**. The essence of the implementation, logic, and decision-making remains my own. AI assistance was used primarily for:
- Code structuring and debugging
- Optimizing function performance
- Refining explanations in this README

## How to Use the App
1. **Run the App**
   ```bash
   streamlit run project.py
   ```
2. **Enter Sleep & Wake Time**: The app will calculate your total sleep duration.
3. **Get Wake-up Suggestions**: Enter your desired sleep duration and receive an optimized wake-up time.
4. **Analyze Productivity**: Input past sleep and productivity data to visualize trends.

## Future Improvements
- **Integration with Wearables**: Sync data from **smartwatches** (e.g., Fitbit, Apple Watch) for automatic tracking.
- **Machine Learning Insights**: Use AI to predict productivity based on sleep trends.
- **Mobile Version**: Deploy as a web app for broader accessibility.

## Conclusion
The **Sleep Cycle & Productivity Analyzer** is a valuable tool for improving sleep habits and enhancing daily productivity. With its intuitive interface, accurate calculations, and insightful data visualizations, users can make informed decisions about their sleep schedule. This project demonstrates how simple **Python, Streamlit, and NumPy** can be leveraged to create practical, real-world applications.

