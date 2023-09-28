from collections import defaultdict

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]

def pisahkan_data(data):
    int_data = defaultdict(list)
    float_data = []
    string_data = []

    for item in data:
        if isinstance(item, int):
            satuan = item % 10
            puluhan = (item // 10) % 10
            ratusan = item // 100
            int_data['satuan'].append(satuan)
            int_data['puluhan'].append(puluhan)
            int_data['ratusan'].append(ratusan)
        elif isinstance(item, float):
            float_data.append(item)
        elif isinstance(item, str):
            string_data.append(item)

    return {
        'int_data': dict(int_data),
        'float_data': tuple(float_data),
        'string_data': string_data
    }

hasil_pemisahan = pisahkan_data(random_list)

print("Data Integer:")
print(hasil_pemisahan['int_data'])

print("\nData Float (dalam bentuk tuple):")
print(hasil_pemisahan['float_data'])

print("\nData String:")
print(hasil_pemisahan['string_data'])
