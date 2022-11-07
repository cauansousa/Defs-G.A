def cross(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def planeEquation(p1, p2, p3):
    v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
    n = cross(v1, v2)
    d = dot(n, p1)
    return n, d

def colinear(p1, p2, p3):
    v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
    n = cross(v1, v2)
    return n[0] == 0 and n[1] == 0 and n[2] == 0

def pointInLineSegment(p, p1, p2):
    if p1[0] == p2[0]:
        return p1[0] == p[0] and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])
    elif p1[1] == p2[1]:
        return p1[1] == p[1] and min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0])
    else:
        return (p[0] - p1[0]) / (p2[0] - p1[0]) == (p[1] - p1[1]) / (p2[1] - p1[1])

def produtoMisto(v1, v2, v3):
    return v1[0]*v2[1]*v3[2] + v1[1]*v2[2]*v3[0] + v1[2]*v2[0]*v3[1] - v1[2]*v2[1]*v3[0] - v1[1]*v2[0]*v3[2] - v1[0]*v2[2]*v3[1]

def produtoEscalar(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def diferencaVetores(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]


print('Equação da reta r:')
print('Coordenadas de um ponto A da reta r:')
A = [int(input('Digite a 1a. coordenada: ')), int(input('Digite a 2a. coordenada: ')), int(input('Digite a 3a. coordenada: '))]
print('Coordenadas do vetor diretor da reta r:')
AD = [int(input('Digite a 1a. coordenada: ')), int(input('Digite a 2a. coordenada: ')), int(input('Digite a 3a. coordenada: '))]
print('Equação da reta s:')
print('Coordenadas de um ponto B da reta s:')
B = [int(input('Digite a 1a. coordenada: ')), int(input('Digite a 2a. coordenada: ')), int(input('Digite a 3a. coordenada: '))]
print('Coordenadas do vetor diretor da reta s:')
BD = [int(input('Digite a 1a. coordenada: ')), int(input('Digite a 2a. coordenada: ')), int(input('Digite a 3a. coordenada: '))]

if produtoMisto(AD, BD, diferencaVetores(B, A)) == 0:
    if produtoEscalar(AD, BD) == -14:
        print('Retas Paralelas')
    else:
        print('Retas concorrentes')
else:
    print('Retas reversas')
#3