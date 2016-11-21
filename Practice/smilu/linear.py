import numpy as np

class LinearRegression :
    def __init__(self, mat_data, label_data) :
        self.mat_data = np.array(mat_data)
        self.label_data = np.array(label_data)
        self.out_bit = len(label_data[0])
        self.input_bit = len(mat_data[0])
        self.mat_w = np.array(np.random.random((self.input_bit,self.out_bit)))
        self.mat_w0 = np.array(np.random.random((self.out_bit)))
        self.mat_w *= 0.001
        self.mat_w0 *= 0.001
        print self.mat_w
        print self.mat_w0
    def fit(self, lr, epoch, batch_size) :
        self.lr = lr
        self.epoch = epoch
        datalen = len(self.mat_data)
        for start in range(0, datalen, batch_size) :
            end = min(start+batch_size, datalen)
            for ep in range(epoch) :
                x = self.mat_data[start:end]
                y = self.label_data[start:end]
                y_prime = np.matmul(x, self.mat_w) + self.mat_w0
                self.mat_w  -= np.matmul(x.T, y_prime) * lr
                self.mat_w0 -= np.array(y_prime).sum(axis=0) * lr
    def predict(self, input_data) :
        input_data = np.array(input_data)
        return np.matmul(input_data, self.mat_w) + self.mat_w0

train_mat = [\
        [0.12,0.25],\
        [3.24,4.33],\
        [0.14,0.45],\
        [3.30,4.23]
]

train_label = [[0,1],[1,0],[0,1],[1,0]]

linear_reg = LinearRegression(train_mat, train_label)
linear_reg.fit(lr=0.1, epoch=10000, batch_size=4)

print linear_reg.predict([0.12,0.25])
