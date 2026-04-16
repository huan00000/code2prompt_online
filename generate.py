# generate.py
import subprocess

def main():
    result = subprocess.run(
        ["code2prompt", "--path", "A", "--output", "b.txt"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    if result.returncode == 0:
        print("成功生成 b.txt")
    else:
        print("生成失败")

if __name__ == "__main__":
    main()
