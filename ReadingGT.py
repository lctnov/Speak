from gtts import gTTS
import os
import time

GREEN_BOLD = "\033[1;32m"
RESET = "\033[0m"

# --- Bước 1: file dữ liệu ---
file_path = "sentence_text.txt"  # file chứa dạng: "English,Tiếng Việt"

# --- Bước 2: đọc file ---
with open(file_path, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

print(f"\nĐã tải {len(sentences)} câu từ {file_path}. Chương trình sẽ đọc lặp vô hạn.\n")

# --- Bước 3: lặp đọc ---
while True:
    for idx, line in enumerate(sentences, start=1):
        try:
            # Tách theo dấu phẩy đầu tiên
            parts = line.split("@", 1)
            sentence_text = parts[0].strip() if len(parts) > 0 else ""
            vocab_part = parts[1].strip() if len(parts) > 1 else ""

            # In ra màn hình
            print(f"Đang đọc câu {idx} [{GREEN_BOLD}{vocab_part}{RESET}]: {sentence_text}")

            # Tạo file âm thanh và phát
            tts = gTTS(text=sentence_text, lang="en")  # chỉ đọc tiếng Anh
            filename = "temp.mp3"
            tts.save(filename)

            # Phát file (macOS), nếu Windows thay bằng: os.system(f"start {filename}")
            os.system(f"afplay {filename}")
            os.remove(filename)

            time.sleep(0.5)

        except Exception as e:
            print("Lỗi:", e)
            continue
