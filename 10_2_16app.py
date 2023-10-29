
import streamlit as st

def binary_to_decimal(binary_num):
    try:
        decimal_num = int(binary_num, 2)
        return decimal_num
    except ValueError:
        return None

def decimal_to_binary(decimal_num):
    try:
        binary_num = bin(decimal_num)[2:]
        return binary_num
    except ValueError:
        return None

def hex_to_decimal(hex_num):
    try:
        decimal_num = int(hex_num, 16)
        return decimal_num
    except ValueError:
        return None

def decimal_to_hex(decimal_num):
    try:
        hex_num = hex(decimal_num)[2:]
        return hex_num
    except ValueError:
        return None

def main():
    st.title("数値変換アプリ")

    conversion_option = st.selectbox("変換オプション", ("2進数から10進数へ", "10進数から2進数へ", "16進数から10進数へ", "10進数から16進数へ"))

    if conversion_option == "2進数から10進数へ":
        binary_input = st.text_input("2進数を入力してください:", "1001")
        if st.button("変換"):
            result = binary_to_decimal(binary_input)
            if result is not None:
                st.success(f"10進数の値は {result} です")
            else:
                st.error("有効な2進数を入力してください。")

    elif conversion_option == "10進数から2進数へ":
        decimal_input = st.text_input("10進数を入力してください:", "9")
        if st.button("変換"):
            try:
                decimal_input = int(decimal_input)
                result = decimal_to_binary(decimal_input)
                if result is not None:
                    st.success(f"2進数の値は {result} です")
                else:
                    st.error("有効な10進数を入力してください。")
            except ValueError:
                st.error("有効な10進数を入力してください。")

    elif conversion_option == "16進数から10進数へ":
        hex_input = st.text_input("16進数を入力してください:", "1F")
        if st.button("変換"):
            result = hex_to_decimal(hex_input)
            if result is not None:
                st.success(f"10進数の値は {result} です")
            else:
                st.error("有効な16進数を入力してください。")

    elif conversion_option == "10進数から16進数へ":
        decimal_input = st.text_input("10進数を入力してください:", "31")
        if st.button("変換"):
            try:
                decimal_input = int(decimal_input)
                result = decimal_to_hex(decimal_input)
                if result is not None:
                    st.success(f"16進数の値は {result} です")
                else:
                    st.error("有効な10進数を入力してください。")
            except ValueError:
                st.error("有効な10進数を入力してください。")

if __name__ == "__main__":
    main()
