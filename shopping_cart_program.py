# برنامج سلة التسوق - رحلتي في تعلم بايثون
# Project: Shopping Cart System

def show_menu():
    # دالة لعرض القائمة للمستخدم
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item to cart")
    print("2. View cart items")
    print("3. Checkout and Exit")
    print("--------------------------")

def main():
    # الدالة الرئيسية التي تدير البرنامج
    cart = []
    print("Welcome to the Professional Shopping Cart Program!")

    while True:
        show_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            # إضافة منتج جديد للسلة
            item = input("Enter item name: ")
            try:
                price = float(input(f"Enter price for {item}: "))
                cart.append({"item": item, "price": price})
                print(f"Successfully added {item}!")
            except ValueError:
                print("Invalid price! Please enter a number.")

        elif choice == '2':
            # عرض كل المنتجات الموجودة في السلة حالياً
            if not cart:
                print("Your cart is currently empty.")
            else:
                print("\nYour Current Cart:")
                total = 0
                for i, entry in enumerate(cart, 1):
                    print(f"{i}. {entry['item']} - ${entry['price']:.2f}")
                    total += entry['price']
                print(f"Current Total: ${total:.2f}")

        elif choice == '3':
            # إنهاء البرنامج وحساب الإجمالي النهائي
            print("Thank you for using our program. Goodbye!")
            break
        else:
            # التعامل مع الاختيارات الخاطئة
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    # نقطة انطلاق البرنامج
    main()