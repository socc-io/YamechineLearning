import numpy as np
import sys

class LinearRegression:

    def __init__(self, mat_data, label_data):
        self.mat_data = np.array(mat_data)
        self.label_data = np.array(label_data)
        self.out_bit = len(label_data[0])
        self.mat_w =  [ [ (np.random.random() * 0.0001 + sys.float_info.epsilon)\
                              for i in range(len(mat_data[0]))] \
                                for j in range(self.out_bit) ]
        self.mat_w0 = [ np.random.random() * 0.0001 + sys.float_info.epsilon\
                            for i in range(self.out_bit) ]

    def batch_update_w(self, out_bit_index, data, label):
        w = self.mat_w[out_bit_index]
        w0 = self.mat_w0[out_bit_index]
        tiled_w0 = np.tile(w0,(len(data)))
        yp  = (w * data).sum(axis=1) + tiled_w0
        gd = (label.T[out_bit_index] - yp)
        # dJ_dw is gradient of J(w) function
        dJ_dw = (gd * data.T).sum(axis=1)/len(data) * -1
        dJ_dw0  = gd.sum(axis=0)/len(data) * -1
        w = w - (dJ_dw * self.lr)
        w0 = w0 - (dJ_dw0 * self.lr)
        self.mat_w[out_bit_index] = w
        self.mat_w0[out_bit_index] = w0

    def fit(self, lr, epoch, batch_size):
        self.lr = lr
        self.epoch = epoch
        start = 0
        end = batch_size
        datalen = len(self.mat_data)
        while start < datalen :
            for ep in range(epoch):
                for i in range(self.out_bit):
                    self.batch_update_w(i, \
                        self.mat_data[start:end],\
                        self.label_data[start:end])
            start = end
            end += batch_size

    def predict(self, array_input):
        array_input = np.array(array_input)
        return (array_input * self.mat_w).sum(axis=1) + self.mat_w0

        
train_mat = [\
                     [0.12, 0.25],\
                     [3.24, 4.33],\
                     [0.14, 0.25],\
                     [3.30, 4.23],\
    ]

train_label = [[0,1],[1,0],[0,1],[1,0]]
        
linear_reg = LinearRegression(train_mat, train_label)
linear_reg.fit(lr = 0.001, epoch = 10000, batch_size = 4)

print linear_reg.predict([0.10,0.33])
print linear_reg.predict([4.00,4.00])
print linear_reg.predict([0.12,0.25])
