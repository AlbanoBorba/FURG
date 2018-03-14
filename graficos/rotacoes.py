import numpy as np
from math import cos, sin

def ex1(t1, r, t2):
    tmp = np.dot(r, t1)
    return np.dot(t2, tmp)

def ex2(ry1, rz1, ry_principal, rz2, ry2):
    tmp1 = np.dot(rz1, ry1)
    tmp2 = np.dot(ry_principal, tmp1)
    tmp3 = np.dot(rz2, tmp2)
    return np.dot(ry2, tmp3)

if __name__ == "__main__":
    t1 = np.matrix([[1, 0, -2],
                     [0, 1, -1],
                     [0, 0, 1]])
    r = np.matrix([[cos(-30), -sin(-30), 0],
                    [sin(-30), cos(-30), 0],
                    [0, 0, 1]])
    t2 = np.matrix([[1, 0, 2],
                     [0, 1, 1],
                     [0, 0, 1]])
    result1 = ex1(t1, r, t2)
    
    ry1 = np.matrix([[cos(45), 0, sin(45), 0],
                     [0, 1, 0 , 0],
                     [-sin(45), 0, cos(45), 0],
                     [0, 0, 0, 1]])
    rz1 = np.matrix([[cos(54.7), -sin(54.7), 0, 0],
                     [-sin(54.7), cos(54.7), 0, 0],
                     [0, 0, 1 , 0],
                     [0, 0, 0, 1]])
    ry2 = np.matrix([[cos(30), 0, sin(30), 0],
                     [0, 1, 0 , 0],
                     [-sin(30), 0, cos(30), 0],
                     [0, 0, 0, 1]])
    rz2 = np.matrix([[cos(-54.7), -sin(-54.7), 0, 0],
                     [-sin(-54.7), cos(-54.7), 0, 0],
                     [0, 0, 1 , 0],
                     [0, 0, 0, 1]])
    ry3 = np.matrix([[cos(-45), 0, sin(-45), 0],
                     [0, 1, 0 , 0],
                     [-sin(-45), 0, cos(-45), 0],
                     [0, 0, 0, 1]])
    result2 = ex2(ry1, rz1, ry2, rz2, ry3)
    print result2