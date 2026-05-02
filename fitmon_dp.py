
def fuse(fitmons):
    """
    This function is a function to return the maximum cuteness score possible when fusing all fitmons in param:fitmons 
    Param fitmons takes in a list of fitmons, each with a tuple of (left affinity, cuteness score, right affinity)

    Approach description(for main function): I create a matrix of (number of fitmons + 1) * (number of fitmons + 1) size.
    Then, i start by setting the fitmons in their repective indexes. For example, i have 3 fitmons, i create a 4*4 matrix(for easy implementation as index starts from 0).
    Then, i set fitmon 1 at index[1][1], fitmon 2 at index[2][2], fitmon 3 at index[3][3], diagonally.
    After that i do combination of 2 fitmons. So i go through the array diagonally again, 
    example: i set max cuteness score of fusing fitmon 1 and 2 at matrix[1][2], then go diagonally, i set max cuteness score of fusing fitmon 2 and 3 at matrix[2][3]
    After that, this diagonal reached the end, then i fuse 3 fitmons(start new diagonal at [1][3]). I set max cuteness score of fusing fitmon 1,2,3
    by checking if fusing fitmon 1,2 first then fuse fitmon 3, like (1,2)3 , or fusing fitmon 2,3 first then fuse fitmon 1, like 1(2,3), check which fuse method will give me
    my greater cuteness score. In order to not compute previously computed cuteness scores, my fusion of (1,2) fitmon comes from matrix[1][2] and fusion of (2,3) fitmon comes 
    from matrix[2][3]. After i reach the end of my diagonals( i only fill one half of my matrix), i get the last element of first row , which in this example is [1][3], 
    which will return me the total max cuteness score of fusing fitmon 1,2,3

    Written by: Choong Yu Xin

    Precondition: list of fitmons is not empty
    Postcondition: after looping through the matrix diagonally until index [1,len(fitmons)] is updated, then terminate loop,
                    (all fitmons are fused until there is only one fitmon left, then return that final fitmon)

    Input: List of fitmons 

    Return: The maximum cuteness score of fusing all fitmons

    Time complexity:
        Best case analysis: O(N^3), where N is number of fitmons(input fitmons in fuse function), because i have 3 for loops where it will run for a max range of length of my matrix
        Worst case analysis: O(N^3), where N is number of fitmons(input fitmons in fuse function), because i have 3 for loops where it will run for a max range of length of my matrix

    Space complexity:
        Input space analysis: O(N), where N is number of fitmons(input fitmons in fuse function), because my param accepts a list of fitmons
        Aux space analysis: O(N^2), where N is number of fitmons(input fitmons in fuse function), because i create a matrix of (N + 1) * (N+1)


    """
    def get_cuteness_score(first_fitmon, second_fitmon):  
        """
        This function is a helper function to calculate the cuteness score when fusing 2 fitmons together
        Written by: Choong Yu Xin
        
        Precondition: Takes in two params, first_fitmon and second_fitmon which is the two fitmons to be fused
        Postcondition: Returns cuteness score of fusing two fitmons

        Input: The first and second fitmon to be fused together
        Return: The cuteness score of fusing two fitmons

        Time complexity:
            Best case analysis: O(1), because i access the left affinity, right affinity, cuteness score of fitmon at constant time
            Worst case analysis: O(1), because i access the left affinity, right affinity, cuteness score of fitmon at constant time

        Space complexity:
            Input space analysis: O(1), because the first fitmon and second fitmon is accessed in O(1) constant
            Aux space analysis: O(1), because the first fitmon and second fitmon is accessed in O(1) constant

        """
        cuteness_score = int((first_fitmon[1] * first_fitmon[2]) + (second_fitmon[1] * second_fitmon[0]))
        return cuteness_score
    
    matrix_size = len(fitmons) 
   
    matrix = [[[-1, -1, -1] for _ in range(matrix_size + 1)] for _ in range(matrix_size + 1)]
    for i in range(1, matrix_size + 1):
        matrix[i][i] = fitmons[i-1]

    for i in range(1, matrix_size):
        for j in range(1, matrix_size- i+1):
            print(i,j)
        
            for k in range(1, i+1):
                cuteness_score = get_cuteness_score(matrix[j][i+j-k], matrix[i+j-k+1][i+j])
                if cuteness_score > matrix[j][j+i][1]:
                    matrix[j][j+i][1] = cuteness_score
                    matrix[j][j+i][0] = matrix[j][i+j-k][0]
                    matrix[j][j+i][2] = matrix[i+j-k+1][i+j][2]


    return matrix[1][len(matrix)-1][1]

print(fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]]))










        
