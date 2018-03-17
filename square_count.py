####### Script Description : Program to count the number of squares formed for given input list 
####### Input Parameters   : List "input_list" is the user passed list testing given input list
#######                      For a square n x n with n points, maximum square length will be (n-1)
#######                      Set variable "max_length" for given square size
####### Output             : Count for number of squares formed

#Input parameters
input_list = [[2,3],[3,4],[6,7],[7,8],[2,6],[3,7],[4,8],[10,11],[11,12],[6,10],[7,11],[8,12]]
max_length = 3


sorted_input_list = [[x[1],x[0]] if x[0] > x[1] else [x[0],x[1]] for x in input_list]

# Check input size
def verify_input(inputlist):
    max_elem_cnt = 2*(max_length+1)*max_length
    if 0 < len(inputlist) < max_elem_cnt: 
        flag = 0
    else:
        print ("Input list of incorrect size")
        flag = 1
    return flag

# Function to get the square nodes
def get_vertices(input_list):
    sorted_input_list = [[x[1],x[0]] if x[0] > x[1] else [x[0],x[1]] for x in input_list]
    vertex_list = [vertex for edge in sorted_input_list for vertex in edge]
    vertice_list = list(set(vertex_list))
    return vertice_list

# Function to get maximum point for a line
def get_max_coord():
    top_right_coord = max_length+1
    bottom_right_coord = (top_right_coord)**2
    max_coord = [x for x in range(top_right_coord,bottom_right_coord+top_right_coord,top_right_coord)]
    return max_coord

# Function to get the maximum possible square length for a node   
def squares_max_length(vertex):
    length_list = get_max_coord()
    for item in range(len(length_list)):
        if vertex <= length_list[item]:
            max_square_length = length_list[item] - vertex
            break
    return max_square_length

# Function to get the co-ordinates for square edges
def get_square_coords(vertex):
    vertices = get_vertices(input_list)
    vertex_max_square_length = {node:squares_max_length(node) for node in vertices}
    v = vertex
    l = vertex_max_square_length[v]
    for l in range(1,l+1):
        top_coord = [v,v+l]
        left_coord = [v,v+((max_length+1)*l)]
        bottom_coord = [v+((max_length+1)*l),v+((max_length+1)*l)+l]
        right_coord = [v+l,v+((max_length+1)*l)+l]
        coord_set = [top_coord,left_coord,bottom_coord,right_coord]
        yield coord_set

# Function to determine squares formed for a node
def get_square_cnt(node):
    square_cnt = 0
    for edge_size in get_square_coords(node): 
        edge_size_tmp=[]
        for arr in edge_size:
            if arr[1] - arr[0] > (max_length + 1):
                diff = int((arr[1]-arr[0])/(max_length + 1))
                el1 = arr[0]
                el2 = el1 + (max_length + 1)
                for i in range(1,diff+1):
                    edge_size_tmp.append([el1,el2])
                    el1 = el2
                    el2 = el1 + (max_length + 1)
            elif (max_length + 1) > arr[1] - arr[0] > 1:
                diff = int((arr[1]-arr[0]))
                el1 = arr[0]
                el2 = el1 + 1
                for i in range(1,diff+1):
                    edge_size_tmp.append([el1,el2])
                    el1 = el2
                    el2 = el1 + 1
        
        if edge_size_tmp == []:
            edge_size_tmp = edge_size
        coord_is_subset = [arr for arr in edge_size_tmp if arr not in sorted_input_list]
        if coord_is_subset == []:
            square_cnt = square_cnt + 1
    return square_cnt

# Function to determine total count of squares formed
def get_tot_sq_cnt(v_list):
    sq_cnt = 0
    for v in v_list:
        sq_cnt_temp = get_square_cnt(v)
        sq_cnt = sq_cnt + sq_cnt_temp
    return sq_cnt

# Main function
if (__name__ == "__main__"):
    chk_input = verify_input(input_list)
    if chk_input == 0:
        vertices = get_vertices(input_list)
        squares_formed = get_tot_sq_cnt(vertices)
        print("Number of squares formed with given input list is %d" %squares_formed)
    else:
        print("Exiting")
        exit()
