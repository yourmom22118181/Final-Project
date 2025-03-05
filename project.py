import streamlit as st
import datetime
import numpy as np
import matplotlib.pyplot as plt

def calculate_sleep_duration(sleep_time: str, wake_time: str) -> float:
    """Calculates total sleep duration in hours."""
    sleep_dt = datetime.datetime.strptime(sleep_time, "%H:%M")
    wake_dt = datetime.datetime.strptime(wake_time, "%H:%M")
    if wake_dt < sleep_dt:
        wake_dt += datetime.timedelta(days=1)
    return round((wake_dt - sleep_dt).total_seconds() / 3600, 2)

def suggest_best_wake_time(target_duration: float, sleep_stages: list) -> str:
    """Suggests optimal wake-up time based on sleep cycles (assumed 90-minute cycles)."""
    cycle_duration = 1.5  # 90 minutes per cycle
    available_cycles = [cycle_duration * i for i in range(1, 7)]  # Cycles up to 9 hours
    best_match = min(available_cycles, key=lambda x: abs(x - target_duration))
    return f"Suggested sleep duration: {best_match:.2f} hours"

def analyze_productivity(sleep_data: list, work_performance: list) -> str:
    """Analyzes correlation between sleep and productivity."""
    if len(sleep_data) != len(work_performance) or not sleep_data:
        return "Insufficient data to analyze."
    correlation = np.corrcoef(sleep_data, work_performance)[0, 1]
    return f"Correlation between sleep and productivity: {correlation:.2f}" if not np.isnan(correlation) else "No correlation detected."

def main():
    st.title("Sleep Cycle & Productivity Analyzer 😴")
    
    st.header("Calculate Sleep Duration")
    sleep_time = st.text_input("Enter sleep time (HH:MM):", "23:00")
    wake_time = st.text_input("Enter wake-up time (HH:MM):", "07:00")
    if st.button("Calculate Sleep Duration"):
        duration = calculate_sleep_duration(sleep_time, wake_time)
        st.write(f"Total Sleep Duration: {duration} hours")
    
    st.header("Suggest Best Wake Time")
    target_duration = st.number_input("Enter target sleep duration (hours):", min_value=4.5, max_value=9.0, value=7.5)
    if st.button("Suggest Wake Time"):
        suggestion = suggest_best_wake_time(target_duration, [])
        st.write(suggestion)
    
    st.header("Analyze Sleep & Productivity")
    sleep_data = st.text_area("Enter past sleep durations (comma-separated):", "7,6.5,8,7.2,6")
    work_performance = st.text_area("Enter corresponding productivity scores (comma-separated):", "80,75,85,78,70")
    if st.button("Analyze Productivity"):
        sleep_list = list(map(float, sleep_data.split(',')))
        performance_list = list(map(float, work_performance.split(',')))
        analysis = analyze_productivity(sleep_list, performance_list)
        st.write(analysis)
        
        fig, ax = plt.subplots()
        ax.scatter(sleep_list, performance_list, color='blue')
        ax.set_xlabel("Sleep Duration (Hours)")
        ax.set_ylabel("Productivity Score")
        ax.set_title("Sleep Duration vs Productivity")
        st.pyplot(fig)
    
if __name__ == "__main__":
    main()
