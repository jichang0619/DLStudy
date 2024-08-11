import numpy as np

# SoftMax
def softmax(a):
    
    c = np.max(a)
    exp_a = np.exp(a-c) # OverFlow 방지
    sum_exp_a = np.sum(exp_a)
    y= exp_a/sum_exp_a
    return y

a = np.array([20, 12.2, 3]) 
ans = softmax(a)
print (ans)

print(np.sum(ans))