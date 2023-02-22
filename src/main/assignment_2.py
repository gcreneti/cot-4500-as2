
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
    print(matrix)
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
            
            matrix[i][j] = '{0:.7g}'.format(operation)
    print(matrix)
    return matrix


def get_approximate_result(matrix, x_points, value):
   
    reoccuring_x_span = 1
    reoccuring_px_result = matrix[0][0]
    
    
    for index in range(1, len(x_points)-1):
          polynomial_coefficient = matrix[index][index]
          
          reoccuring_x_span *= (value - x_points[0])
        
          mult_operation = polynomial_coefficient * reoccuring_x_span
       
          reoccuring_px_result += mult_operation

  
    return reoccuring_px_result


if __name__ == "__main__":
   
    nev_x_points = [3.6,3.8,3.9]
    nev_y_points = [1.675,1.436,1.318]
    nev_approximating_value = 3.7
    nev_x = nevilles_method(nev_x_points, nev_y_points, nev_approximating_value)
    print(nev_x)
    new_x_points = [7.2,7.4,7.5,7.6]
    new_y_points = [23.5492,25.3913,26.8224,27.4589]
    new_x = divided_difference_table(new_x_points, new_y_points)
    new_1 = new_x[1][1]
    new_2 = new_x[2][2]
    new_3 = new_x[3][3]
    new_deg = [new_1, new_2, new_3]
    print(new_deg)
    new_appx = get_approximate_result(new_x, new_deg, 7.3)
    print(new_appx)
