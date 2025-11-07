from gtts import gTTS
import os
import time

GREEN_BOLD = "\033[1;32m"
RESET = "\033[0m"

# --- Bước 1: chọn ngôn ngữ ---
print("Chọn ngôn ngữ bạn muốn học:")
print("1. Tiếng Anh")
print("2. Tiếng Trung")
choice = input("Nhập số (1 hoặc 2): ")

if choice == "2":
    lang_code = "zh-CN"
    file_path = "sentences_cn.txt"
else:
    lang_code = "en"
    file_path = "sentences_en.txt"

# --- Bước 2: đọc file ---
with open(file_path, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

print(f"\nĐã tải {len(sentences)} câu từ {file_path}. Chương trình sẽ đọc lặp vô hạn.\n")

# --- Bước 3: lặp đọc ---
while True:
    for idx, line in enumerate(sentences, start=1):
        try:
            parts = line.split(",", 1)
            vocab_part = parts[0].strip() if len(parts) > 0 else ""
            sentence_text = parts[1].split(",")[-1].strip() if len(parts) > 1 else ""

            print(f"Đang đọc câu {idx} [{GREEN_BOLD}{vocab_part}{RESET}]: {sentence_text}")

            tts = gTTS(sentence_text, lang=lang_code)
            filename = "temp.mp3"
            tts.save(filename)
            os.system(f"afplay {filename}")
            os.remove(filename)

            time.sleep(0.5)

        except Exception as e:
            print("Lỗi:", e)
            continue
