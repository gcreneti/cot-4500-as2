
import numpy as np
np.set_printoptions(precision = 7, suppress = True, linewidth = 100)

def nevilles_method(x_points, y_points, x):
    
    matrix = np.zeros((3, 3))
    
    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]
    
    num_of_points = len(x_points)
  
    for i in range(1, num_of_points):
      for j in range(1,i+1):
        first_multiplication = (x - x_points[i-j]) * matrix[i][j-1]
        second_multiplication = (x - x_points[i]) * matrix[i-1][j-1]
        denominator = x_points[i] - x_points[i-j]
       
        coefficient = (first_multiplication-second_multiplication)/denominator
        matrix[i][j] = coefficient
        j += 1
      i += 1
    return matrix[2][2]




def divided_difference_table(x_points, y_points):
  
    matrix: np.array = np.zeros((4,4))
    num_of_points = len(x_points)
    
    for index, row in enumerate(matrix):
        row[0] = y_points[index]
     
    for i in range(1, num_of_points):
        for j in range(1, i+1):
            
            numerator = matrix[i][j-1] - matrix[i-1][j-1]
           
            denominator = x_points[i] - x_points[i-j]
            operation = numerator/denominator
            
            matrix[i][j] = '{0:.7g}'.format(operation)
    return matrix


def get_approximate_result(matrix, x_points, value):
    reoccuring_x_span = 1
    
    
    reoccuring_px_result = matrix[0][0]
    n = len(x_points)
    
    for index in range(1, n):
      for m_index in range(1, n+1):
        polynomial_coefficient = matrix[m_index][m_index]
        h = x_points[index]-x_points[index-1]
        a = (value-x_points[index-1])/h
        if(index==0):
            reoccuring_x_span = 1
            reoccuring_px_result = matrix[0][0]
            mult_operation = (polynomial_coefficient * reoccuring_x_span)
        else:
            reoccuring_x_span *= a
            mult_operation = (polynomial_coefficient * reoccuring_x_span)
            reoccuring_px_result += mult_operation
     
    
    return reoccuring_px_result

def apply_div_dif(matrix: np.array):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            
            # get left cell entry
            left: float = matrix[i][j-1]
            # get diagonal left entry
            diagonal_left: float = matrix[i-1][j-1]
            # order of numerator is SPECIFIC.
            numerator: float = left-diagonal_left
            # denominator is current i's x_val minus the starting i's x_val....
            denominator = matrix[i][0]-matrix[i-2][0]
            # something save into matrix
            operation = numerator / denominator
            matrix[i][j] = operation
    
    return matrix
def hermite_interpolation():
    x_points = [3.6,3.8,3.9]
    y_points = [1.675,1.436,1.318]
    slopes = [-1.195,-1.188,-1.182]
    
    matrix = np.zeros((6,6))
    num_of_points = len(x_points)
  
    for x in range(0, len(x_points)):
      for x2 in range(2*x, 2*len(x_points)):
        matrix[x2][0] = x_points[x]
      
      
    for x in range(0, len(x_points)):
      for x2 in range(2*x, 2*len(x_points)):
        matrix[x2][1] = y_points[x]
    
    for x in range(0, len(x_points)):
      for x2 in range(2*x+1, 2*len(x_points)):
        matrix[x2][2] = slopes[x]
      
    filled_matrix = apply_div_dif(matrix)
    print(filled_matrix)

def spline_matrix(x_points, y_points):
  A = np.zeros((4,4))
  b = np.zeros((4,1))
  
  a0 = y_points[0]
  a1 = y_points[1]
  a2 = y_points[2]
  a3 = y_points[3]

  h0 = x_points[1]-x_points[0]
  h1 = x_points[2]-x_points[1]
  h2 = x_points[3]-x_points[2]

  A[0][0] = 1
  A[1][0] = h0
  A[1][1] = 2*(h0+h1)
  A[2][2] = 2*(h1+h2)
  A[3][3] = 1
  A[2][1] = h1
  A[1][2] = h1
  A[2][3] = h2

  b[1] = ((3/h1)*(a2-a1))-((3/h0)*(a1-a0))
  b[2] = ((3/h2)*(a3-a2))-((3/h1)*(a2-a1))

  b_row = np.zeros((1,4))
  b_row[0][1] = b[1]
  b_row[0][2] = b[2]

  x = np.linalg.solve(A,b)
  x_row = np.zeros((1,4))
  x_row[0][1] = x[1]
  x_row[0][2] = x[2]

  print(A)
  print("\n")
  print(b_row)
  print("\n")
  print(x_row)
  
      
  
  
if __name__ == "__main__":
   
    nev_x_points = [3.6,3.8,3.9]
    nev_y_points = [1.675,1.436,1.318]
    nev_approximating_value = 3.7
    nev_x = nevilles_method(nev_x_points, nev_y_points, nev_approximating_value)
    print(nev_x)
    print("\n")
    new_x_points = [7.2,7.4,7.5,7.6]
    new_y_points = [23.5492,25.3913,26.8224,27.4589]
    new_x = divided_difference_table(new_x_points, new_y_points)
    print("\n")
    new_1 = new_x[1][1]
    new_2 = new_x[2][2]
    new_3 = new_x[3][3]
    new_deg = [new_1, new_2, new_3]
    print(new_deg)
    print("\n")
    new_appx = get_approximate_result(new_x, new_deg, 7.3)
    print(new_appx)
    print("\n")
    herm = hermite_interpolation()
    print("\n")
    spline_x = [2,5,8,10]
    spline_y = [3,5,7,9]
    spline = spline_matrix(spline_x,spline_y)
