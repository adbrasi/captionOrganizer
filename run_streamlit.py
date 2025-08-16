#!/usr/bin/env python3
"""
Launcher for Streamlit Video Caption Editor
"""

import subprocess
import sys
import os

def main():
    print("🎬 Starting Video Caption Editor (Streamlit)...")
    print("📍 Server will be available at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ], cwd=os.path.dirname(os.path.abspath(__file__)))
    except KeyboardInterrupt:
        print("\n👋 Video Caption Editor stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()