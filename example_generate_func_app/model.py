# model.py

def generate_c_function(func_name, return_type, parameters):
    """
    Tạo ra một đoạn mã hàm C/C++ với nội dung trống hoặc trả giá trị mặc định
    :param func_name: tên hàm
    :param return_type: kiểu trả về
    :param parameters: danh sách tuple (tên tham số, kiểu dữ liệu)
    :return: đoạn mã hàm dạng chuỗi
    """
    # Tạo danh sách tham số
    param_str = ', '.join([f"{ptype} {pname}" for pname, ptype in parameters])
    
    # Tạo thân hàm
    if return_type == "void":
        body = "    // TODO: implement function\n"
    else:
        default_value = get_default_value(return_type)
        body = f"    return {default_value};\n"
    
    # Ghép hàm
    function_code = f"{return_type} {func_name}({param_str}) {{\n{body}}}\n"
    return function_code


def get_default_value(return_type):
    """
    Trả về giá trị mặc định tương ứng kiểu dữ liệu
    """
    defaults = {
        "int": "0",
        "float": "0.0",
        "double": "0.0",
        "char": "'\\0'",
        "bool": "false",
        "string": '""'
    }
    return defaults.get(return_type.lower(), "0")
