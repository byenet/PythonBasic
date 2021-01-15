# encoding: utf-8

a = 6
b = 0

# khong bat theo ten loi
try:
    print(a/b)
except:
    print("Xay ra loi roi")

# Bat loi theo ten:
try:
    print(a/b)
except ZeroDivisionError:
    print("Xay ra loi ZeroDivisionError roi")
print("Buon qua loi roi")

# Bat nhieu exeption tren mot lan thong bao:
try:
    print(a/b)
except (ZeroDivisionError, RuntimeError):
    print("Xay ra loi roi")

# Bat nhieu exeption trong nhieu except
try:
    print(a/b)
except ZeroDivisionError:
    print("Xay ra loi roi")
except RuntimeError:
    print ("co loi runtime")

"""
Co the dung try exept long
try :
    # code
except ZeroDivisionError:
    try :
        # code
    except StandardError:
        # code
except RuntimeError:
    # code
"""

# Dung voi finally (Du la dung hay sai van thuc thi):
try:
    print(a/b)
except ZeroDivisionError:
    print("Xay ra loi roi")
except RuntimeError:
    print ("co loi runtime")
finally:
    print("Hen gap lai ban lan sau...")

"""
Exception Name	    Chú Thích

Exception	        Đây là lớp cơ sở cho tất cả các exception, nó sẽ xuất hiện khi có bất cứ một lỗi nào xảy ra.
StopIteration	    Xuất hiện khi phương thức next() của interator không trỏ đến một đối tượng nào.
SystemExit	        Xuất hiện khi dùng phương thức sys.exit()
StandardError	    Lớp cơ sở cho tất cả các exception.
ArithmeticError	    Xuất hiện khi có lỗi tính toán giữa các số với nhau
OverflowError	    Xuất hiện khi thực hiện tính toán và giá trị của nó vượt quá ngưỡng giới hạn cho phép của kiểu dữ liệu.
FloatingPointError	Xuất hiện khi tính toán float thất bại.
ZeroDivisonError	Xuất hiện khi thực hiện phép chia cho 0.
AssertionError	    Xuất hiện trong trường hợp lệnh assert thất bại.
AttributeError	    Xuất hiện khi không tồn tại thuộc tính này, hoặc thiếu tham số truyền vào nó.
EOFError	        Xuất hiện khi không có dữ liệu từ hàm input() hoặc cuối file.
ImportError	        Xuất hiện khi lệnh import thất bại.
KeyboardInterrupt	Xuất hiện khi ngắt trình biên dịch.
LookupError	        Lớp cơ sở cho tất cả các lỗi về lookup.
IndexError	        Xuất hiện khi index không tồn tại trong list, string,...
KeyError	        Xuất hiện khi key không tồn tại trong dictionary.
NameError	        Xuất hiện khi một biến không tồn tại trong phạm vi bạn gọi nó.
EnvironmentError	Xuất hiện khi có bất kỳ một lỗi nào ngoài phạm vị của Python.
IOError             Xuất hiện khi xử dụng input/ output thất bại, hoặc  mở file không thành công.
OSError	            Xuất hiện khi có lỗi từ hệ điều hành.
SyntaxError	        Xuất hiện khi chương trình có lỗi cú pháp.
IndentationError	Xuất hiện khi bạn thụt dòng không đúng.
SystemError	        Xuất hiện khi trình biên dịch có vấn đề nhưng mà nó lại không tự động exit.
SystemExit	        Xuất hiện khi trình biên dịch được thoát bởi sys.exit().
TypeError	        Xuất hiện khi thực thi toán tử hoặc hàm mà kiểu dữ liệu bị sai so với kiểu dữ liệu đã định nghĩa ban đầu.
ValueError	        Xuất hiện khi chúng ta build 1 function mà kiểu dữ liệu đúng nhưng khi chúng ta thiết lập ở tham số là khác so với khi truyền vào.
RuntimeError	    Xuất hiện khi lỗi được sinh ra không thuộc một danh mục nào.
NotImplementedError	Xuất hiện khi một phương thức trừu tượng cần được thực hiện trong lớp kế thừa chứ không phải là lớp thực thi
UnboundLocalError	Xuất hiện khi chúng ta cố tình truy cập vào một biến trong hàm hoặc phương thức, nhưng không thiết lập giá trị cho nó.
"""