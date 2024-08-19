from module_tool import create_profiles_folder , get_profiles , clear_chrome_process , delete_profile
from create_profiles import create_profile , manager_profiles, perform_action
from os import system
import threading

def main():
    try:
        create_profiles_folder() #Kiểm tra và tạo folder chứa các profile
        option_choice = int(input("1:Create-Profile\n2:Open-Profile\n3:Delete Profile\n4:Close All Chrome \n5:Exit\n=> "))
        #system('cls')
        if option_choice == 1:
            option_create = int(input("1: Create By Name\n2: Create By List\n=> "))
            if option_create == 1:
                profile_name = input("Enter Profile Name: ")
                create_profile(profile_name)
            else:
                list_name_path = 'Profiles\\list_name.txt'
                list_name = open(list_name_path , 'r', encoding='utf-8').readlines()
                for name in list_name:
                    create_profile(name.strip())

            #system('cls')
        # elif option_choice == 2:
        #     profiles = get_profiles()  # lấy danh sách folder profiles
        #     if len(profiles) != 0:  # kiểm tra xem danh sách có profile không
        #         selected_indices = input("Enter Profile Indices (e.g., 1,2,3): ")
        #         selected_indices = [int(index.strip()) for index in selected_indices.split(',')]
                
        #         drivers = []
        #         threads = []
        #         for index in selected_indices:
        #             profile_name_open = profiles[index - 1]
        #             print(f'Opening: {profile_name_open}')
        #             thread = threading.Thread(target=lambda: drivers.append(manager_profiles(profile_name_open)))
        #             #thread = threading.Thread(target=manager_profiles, args=(profile_name_open,))

        #             thread.start()
        #             threads.append(thread)
                
        #         for thread in threads:
        #             thread.join()  # Đảm bảo tất cả các luồng đã hoàn thành
                
        #         if drivers:
        #             perform_action(drivers)  # Thực hiện hành động trên tất cả các trình duyệt đã mở

        #         #system('cls')
        #     else:
        #         print("NOT FOUND CHROME PROFILES => CREATE !")
        #         return main()
        elif option_choice == 2:
            profiles = get_profiles()  # lấy danh sách folder profiles
            if len(profiles) != 0:  # kiểm tra xem danh sách có profile không
                selected_indices = input("Enter Profile Indices (e.g., 1,2,3): ")
                selected_indices = [int(index.strip()) for index in selected_indices.split(',')]
                
                drivers = []
                threads = []
            
                for index in selected_indices:
                    profile_name_open = profiles[index - 1]
                    print(f'Opening: {profile_name_open}')
                    thread = threading.Thread(target=lambda: drivers.append(manager_profiles(profile_name_open)))
                    thread.start()
                    threads.append(thread)               
                for thread in threads:
                    thread.join()  
                while True:
                    actions = []  
                    for i in range(len(drivers)):
                        action = input(f"Choose action for profile {selected_indices[i]} (like, save, comment, share, report, exit): ")
                        actions.append(action.strip().lower())
                    
                    if drivers:
                        perform_action(drivers, actions)  
                    
                    if not drivers:
                        print("All profiles have been closed.")
                        break
            else:
                print("NOT FOUND CHROME PROFILES => CREATE !")
                return main()
        elif option_choice == 3: # xóa profile theo tên
            profiles = get_profiles()
            if len(profiles) != 0:
                profile_index = int(input("Enter Profile Index: "))
                profile_name = profiles[profile_index - 1]
                system('cls')
                delete_profile(profile_name)
        elif option_choice == 4:
            clear_chrome_process()
        elif option_choice == 5:
            system('cls')
            exit()
        else:
            return main()
    except Exception as f:
        print(f"Error: {f}")


if __name__ == "__main__":
    while True:
        main()