# run_all.py
import subprocess
import os

env_python = os.path.join("new-env", "Scripts", "python.exe")

scripts = [
    ("extract_and_save.py", "📦 Extracting and saving flattened CSV"),
    ("wallet_features.py", "📊 Extracting wallet features"),
    ("assign_credit_score.py", "💳 Assigning credit scores"),
    ("plot_credit_analysis.py", "📈 Plotting credit analysis"),
]

for script, message in scripts:
    print(f"\n🚀 Running {script} — {message}...")
    try:
        subprocess.run([env_python, script], check=True)
        print(f"✅ {script} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ {script} failed.")
        break

