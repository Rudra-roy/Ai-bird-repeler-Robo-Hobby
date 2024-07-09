from joblib import Parallel, delayed
import subprocess

def run_motor_control():
    subprocess.run(["python3", "dof.py"])

def run_bird_detection():
    subprocess.run(["python3", "detector.py"])

if __name__ == "__main__":
    Parallel(n_jobs=-1)(delayed(func)() for func in [run_bird_detection])
    
