branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count +1):
    print(f"Chi nhánh {branch}:")
    for class_room in range(1,3) :
        while True :
            sum_class = int(input(f"Nhập số học viên đi học của lớp {class_room}: "))
            if sum_class < 0 :
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            break
        if sum_class == 0 :
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue
        if sum_class >= 20:
            print(f"Chi nhánh {branch} - Lớp {class_room}: Lớp học ổn định")
        else :
            print(f"Chi nhánh {branch} - Lớp {class_room}: Lớp cần được nhắc nhở theo dõi")