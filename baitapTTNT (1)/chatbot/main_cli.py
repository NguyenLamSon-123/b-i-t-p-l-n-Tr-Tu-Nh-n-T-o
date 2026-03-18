from chatbot import get_answer

print("=== CHATBOT HỎI ĐÁP (CLI) ===")
print("Gõ 'exit' để thoát\n")

while True:
    q = input("Bạn: ")
    if q.lower() == "exit":
        break
    print("Chatbot:", get_answer(q))
