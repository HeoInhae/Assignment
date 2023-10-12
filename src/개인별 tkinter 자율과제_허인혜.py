import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from tkinter import filedialog

#헤헤
def save_memo():
    memo_text = memo_entry.get("1.0", "end-1c") + "\n"

    if memo_text:
        try:
            now = datetime.now()
            filename = now.strftime("%Y%m%d") + ".txt" #파일이름을 오늘 날짜로 저장
            with open(filename, "a", encoding='UTF-8') as file:
                file.write("%d년 %02d월 %02d일 - %02d:%02d\n" % (now.year, now.month, now.day, now.hour, now.minute))
                # 오늘 날짜에 해당하는 파일에 현재 날짜와 시간을 저장
                file.write(memo_text)
                # 내가 입력한 메모 저장
            messagebox.showinfo("저장 완료", "메모가 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"메모를 저장하는 동안 오류가 발생했습니다:\n{str(e)}")
    else:
        messagebox.showwarning("경고", "메모 내용이 비어있습니다.")

def load_memo(): # 저장한 메모를 불러오는 함수
    password = simpledialog.askstring("비밀번호 확인", "비밀번호를 입력하세요.", show="*") # 불러오기 위해 비밀번호 입력
    if password == "python":  #비밀번호는 python
        try:
            filetypes = (("텍스트 파일", "*.txt"), ("모든 파일", "*.*"))
            filename = tk.filedialog.askopenfilename(filetypes=filetypes) #파일 탐색기 창 불러오기
            with open(filename, "r", encoding='UTF-8') as file:
                memo_text = file.read()
                memo_entry.delete("1.0", tk.END)
                memo_entry.insert(tk.END, memo_text)
            messagebox.showinfo("불러오기 완료", "메모가 불러와졌습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"메모를 불러오는 동안 오류가 발생했습니다:\n{str(e)}")
    else:
        messagebox.showwarning("경고", "비밀번호가 일치하지 않습니다.")

# Tkinter 창 생성
window = tk.Tk()
window.title("메모장")
window.geometry("500x400+380+160")
window.config(bg="wheat")

pull=tk.PhotoImage(file="pull.png")
pull=pull.subsample(5,5)
image=tk.Label(image=pull,bg="wheat").place(x=-30,y=253)

# 메모 입력 필드
label = tk.Label(window, text="메모:", height=2,font=("",15),bg="wheat").place(x=230,y=20)
memo_entry = tk.Text(window, height=12, width=42,bg="oldlace")
memo_entry.place(x=105,y=70)

# 저장 버튼
save_button = tk.Button(window, text="저장", command=save_memo,font=("",13),width=7,height=2,bg="burlywood")
save_button.place(x=170,y=250)

# 불러오기 버튼
load_button = tk.Button(window, text="불러오기", command=load_memo,font=("",13),width=7,height=2,bg="burlywood")
load_button.place(x=260,y=250)

# Tkinter 이벤트 루프 시작
window.mainloop()
