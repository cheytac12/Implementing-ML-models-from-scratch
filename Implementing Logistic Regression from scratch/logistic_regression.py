import numpy as np 

def sigmoid(z):
  return 1.0 / (1.0 + np.exp(-z))

def calculate_gradient(theta , x , y):
  m = y.size
  return (X.T @ (sigmoid(X @ theta ) - y) / m)

def gradient_descent(X , y , alpha = 0.1 , num_iter = 100 , tol=1e-7):
  X_b = np.c_[np.ones((X.shape[0], 1)), X]
  theta = np.zeros(X_b.shape[1])
  
  for i in range(num_iter):
    grad = calculate_gradient(theta , x , y)
    theta -= alpha * grad
    
    if np.linalg.norm(grad) < tol:
      break
    return theta