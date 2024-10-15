import heapq
from collections import defaultdict, Counter

# Узел дерева Хаффмана
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char      # символ
        self.freq = freq      # частота
        self.left = None      # левый потомок
        self.right = None     # правый потомок

    # Метод для сравнения узлов по частоте (необходим для очереди с приоритетом)
    def __lt__(self, other):
        return self.freq < other.freq

# Функция для построения дерева Хаффмана
def build_huffman_tree(frequency_dict):
    heap = []
    
    # Создаем очередь с приоритетом (min-heap) и добавляем в нее все символы с их частотами
    for char, freq in frequency_dict.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    
    # Строим дерево, пока в куче не останется один элемент (корень дерева)
    while len(heap) > 1:
        # Извлекаем два узла с наименьшей частотой
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Создаем новый внутренний узел с частотой, равной сумме двух узлов
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        
        # Добавляем новый узел обратно в кучу
        heapq.heappush(heap, new_node)
    
    # Корень дерева - единственный оставшийся элемент
    return heap[0]

# Функция для генерации кодов Хаффмана
def generate_huffman_codes(root, current_code="", codes={}):
    # Если узел не содержит символ (внутренний узел), рекурсивно вызываем для его потомков
    if root is None:
        return

    # Если узел является листом, сохраняем его код
    if root.char is not None:
        codes[root.char] = current_code

    # Рекурсивный вызов для левого и правого потомков
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Основная функция для построения кодов Хаффмана
def huffman_encoding(data):
    # Шаг 1: Подсчет частот символов
    frequency_dict = Counter(data)

    # Шаг 2: Построение дерева Хаффмана
    huffman_tree_root = build_huffman_tree(frequency_dict)

    # Шаг 3: Генерация кодов для символов
    huffman_codes = generate_huffman_codes(huffman_tree_root)

    # Шаг 4: Кодирование строки
    encoded_data = ''.join([huffman_codes[char] for char in data])

    return encoded_data, huffman_codes

# Пример использования
data = "hello huffman"
encoded_data, huffman_codes = huffman_encoding(data)

print("Исходные данные:", data)
print("Закодированные данные:", encoded_data)
print("Коды Хаффмана:", huffman_codes)