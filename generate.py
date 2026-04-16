# generate.py
import subprocess
import sys
import os

def main():
    # 1. 校验输入文件夹A是否存在
    input_path = "A"
    if not os.path.isdir(input_path):
        print(f"❌ 错误：输入文件夹 {input_path} 不存在！当前工作目录：{os.getcwd()}")
        print(f"📂 当前目录文件列表：{os.listdir('.')}")
        sys.exit(1)

    # 2. 执行code2prompt命令，完整捕获错误日志
    result = subprocess.run(
        ["code2prompt", "--path", input_path, "--output", "b.txt"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False
    )

    # 3. 详细输出执行结果
    print(f"🔍 命令执行返回码：{result.returncode}")
    print(f"📝 标准输出：\n{result.stdout}")
    if result.stderr:
        print(f"⚠️ 错误输出：\n{result.stderr}")

    if result.returncode == 0:
        print("✅ 成功生成 b.txt")
        # 校验输出文件是否生成
        if os.path.exists("b.txt"):
            print(f"📄 输出文件大小：{os.path.getsize('b.txt')} 字节")
    else:
        print("❌ 生成失败")
        sys.exit(result.returncode)

if __name__ == "__main__":
    main()
