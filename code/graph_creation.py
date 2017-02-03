import tensorflow as tf

# utworzenie danej symbolicznej x, będącej tensorem
# o niezdefiniowanej liczbie wierszy i 784 kolumnach
x = tf.placeholder(tf.float32, [None, 784])

# utworzenie macierzy "W" mającej 784 wiersze i 10 kolumn,
# zainicjowanej zerami
W = tf.Variable(tf.zeros([784, 10]))

# utworzenie wektora b o rozmiarze 10, zainicjowanego zerami
b = tf.Variable(tf.zeros([10]))

# utworzenie operacji obliczającej wyjście sieci neuronowej;
# operacja ta wykorzystuje wynik operacji matmul,
# odpowiadającej za pomnożenie tensora x przez macierz W
# oraz wynik operacji dodawania wyniku operacji matmul
# i wektora przesunięc "b"
y = tf.nn.softmax(tf.matmul(x, W) + b)
