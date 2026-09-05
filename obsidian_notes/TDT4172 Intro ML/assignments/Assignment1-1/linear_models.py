import numpy as np

class LinearRegression():
    def __init__(self, lr=0.001, n_iterations=1000):
        self.weights = None
        self.bias = None
        
        self.lr = lr
        self.n_iterations = n_iterations
        
        self.loss_history = []
        
    def fit(self, X, y):
        """
        Estimates parameters for the classifier
        
        Args:
            X (array<m,n>): a matrix of floats with
                m rows (#samples) and n columns (#features)
            y (array<m>): a vector of floats
        """
        # ====================================
        self.weights = np.zeros(len(X)) #x.shape = datapunkter, features 
        self.bias = 0 


        def loss_function(self, y_pred, Y):
            N = len(Y)
            MSE = 1/(2*N) * np.sum((Y - y_pred)**2)
            return MSE

        def compute_gradients(self, x, Y):
            N = len(Y)
            grad_beta_0 = 1/N * np.sum(self.weights * x + self.bias - Y)
            grad_beta_1 = 1/N * np.sum(x * (self.weights * x + self.bias - Y))
            return grad_beta_1, grad_beta_0

        def update_parameters(self, grad_beta_1, grad_beta_0):
            self.weights = self.weights - self.lr * grad_beta_1
            self.bias = self.bias - self.lr * grad_beta_0


        # Gradient Descent 
        for _ in range(self.n_iterations): 
            y_pred = self.weights * X.transpose() + self.bias 
            grad_beta_1, grad_beta_0 = compute_gradients(self, x=X, Y=y)
            update_parameters(self, grad_beta_1, grad_beta_0) 
            
            loss = loss_function(self, y_pred, y) 
            self.loss_history.append(loss) 

        # ====================================
    
    def predict(self, X):
        """
        Generates predictions
        
        Note: should be called after .fit()
        
        Args:
            X (array<m,n>): a matrix of floats with 
                m rows (#samples) and n columns (#features)
            
        Returns:
            A length m array of floats
        """

        # ====================================

        y_pred = (self.weights * X.transpose()) + self.bias 
        return y_pred

        # ====================================

    
class LogisticRegression():
    def __init__(self, lr=0.001, n_iterations=1000):
        self.weights = None
        self.bias = None
        
        self.lr = lr
        self.n_iterations = n_iterations
        
        self.loss_history = []
    
    def fit(self, X, y):
        # ====================================
        
        self.weights = np.array([np.zeros(len(X[0])), np.zeros(len(X[0])), np.zeros(len(X[0]))]) # [weights_0, weights_1, weights_2]]
        self.bias = 0


        def linear_regression(self, X):
            return self.bias + self.weights[0]*X[0] + self.weights[1]*X[1] + self.weights[2]*X[0]*X[1]

        def compute_gradients(self, X, y_pred, y):
            grad_0 = np.sum(y_pred - y) / len(y)
            grad_1 = (y_pred - y) @ X[0]
            grad_2 = (y_pred - y) @ X[1]
            grad_3 = (y_pred - y) @ (X[0]*X[1])
            return np.array([grad_0, grad_1, grad_2, grad_3])

        def loss_function_log(self, y_pred, y):
            w_0 = 0.1 
            w_1 = 0.1
            return -w_1 * y @ np.log(y_pred) - w_0 * (1 - y) @ np.log(1 - y_pred) 

        def update_parameters(self, grad):
            self.bias = self.bias - self.lr * grad[0] 
            self.weights[0] = self.weights[0] - self.lr * grad[1] 
            self.weights[1] = self.weights[1] - self.lr * grad[2] 
            self.weights[2] = self.weights[2] - self.lr * grad[3] 

        
        for _ in range(self.n_iterations):
            y_pred = self.sigmoid(linear_regression(self, X))          
            grad = compute_gradients(self, X, y_pred, y)
            update_parameters(self, grad)
            self.loss_history.append(loss_function_log(self, y_pred, y))
    
    
        # ====================================

    
    def predict_proba(self, X):
        # ====================================
        def linear_regression(self, X):
            return self.bias + self.weights[0]*X[0] + self.weights[1]*X[1] + self.weights[2]*X[0]*X[1]

        y_pred = self.sigmoid(linear_regression(self, X))

        return [1 if _y > 0.5 else 0 for _y in y_pred]
         


        # ====================================
        
    def predict(self, X):
        # ====================================
        
        return self.predict_proba(X)
         

        # ====================================
    
    def sigmoid(self, z):
        # ====================================
        
        return 1 / (1 + np.e**(-z))

        # ====================================
