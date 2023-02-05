#!/usr/bin/env python
# coding: utf-8

# In[1]:


L = 'L'
M = 'M'
R = 'R'

D = 'D'
E = 'E'
U = 'U'

B = 'B'
S = 'S'
F = 'F'

L_center = L #'l'
R_center = R #'r'
D_center = D #'d'
U_center = U #'u'
B_center = B #'b'
F_center = F #'f'

#X = [L,M,R]
#Y = [D,E,U]
#Z = [B,S,F]

#axes = [X,Y,Z]


# In[36]:


#удаляет повторения элементов-подсписков (1ого поколения глубины) из списка
#вернет список без повторений
#элементы ОБЯЗАТЕЛЬНО списки! (Иначе None)
def repeats_away(els):
    els_set = set()
    for el in els:
        if type(el) != list:
            return
        el.sort()
        els_set.add(tuple(el))
    res = []
    for el in els_set:
        res += [list(el)]
    return res
        
print(repeats_away([1,2,3,1,1]))
print(repeats_away([[U,U],[U]]))
print(repeats_away([[R,L],[L,R]]))


# In[49]:


#Принимает на вход элемент и ось
#Вернет True ТОЛЬКО тогда, когда элемент лежит на пересечении хотя бы двух слоев с данной оси
def match_axe(el,axe):
    mathes = 0
    for l in el:
        if l in axe:
            mathes += 1
    if mathes > 1:
        return True
    return False

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

print(match_axe([F,E,B],Z)) #must be True
print(match_axe([F,E,B],Y)) #must be False
print(match_axe([M,R,L],X)) #must be True


# In[52]:


#Принимает на вход элемент и оси
#Вернет True ТОЛЬКО тогда, когда элемент одержит хотя бы два слоя с одной оси осей
def match_by_axes(el,axes):
    #print(check_few)
    for axe in axes:
        if match_axe(el,axe):
            #print(checkL)
            return True
    return False

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

print(match_by_axes([L,D,B],AXES)) #must be False
print(match_by_axes([F,E,B],AXES)) #must by True
print(match_by_axes([F,E,R],AXES)) #must be False


# In[55]:


#Принимает на вход элемент и оси
#Вернет True ТОЛЬКО тогда, когда элемент НЕ одержит ни одного слоя с одной оси осей
def not_match_by_axes(el,axes):
    return not match_by_axes(el,axes)

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

print(match_by_axes([L,D,B],AXES)) #must be True
print(match_by_axes([F,E,B],AXES)) #must by False
print(match_by_axes([F,E,R],AXES)) #must be True


# In[62]:


#Принимает на вход два элемента
#Вернет True ТОЛЬКО если первый элемент содержит в себе второй
def pair_intersected(el1,el2):
    el2_copy = el2.copy()
    for l1 in el1:
        if l1 in el2_copy:
            el2_copy.remove(l1)
    if el2_copy == []:
        return True
    return False

print(pair_intersected([L,L,L],[L,L])) #must be True
print(pair_intersected([L,L,L],[L])) #must be True
print(pair_intersected([R,M,R],[R])) #must be True
print(pair_intersected([L,R,M],[L,L])) #must be False
print(pair_intersected([L],[L,L])) #must be False


# In[66]:


#Принимает на вход два списка элементов
#Вернет все совпадающие элементы, а также все элементы первого списка, которые содержатся в элементах второго 
def els_intersect(L1,L2):
    res = L1.copy()
    for el1 in L1:
        for el2 in L2:
            if el1 in res and pair_intersected(el1,el2):
                res.remove(el1)
    return res

print(els_intersect([[L]],[[L,L]])) #must be [[L]]
print(els_intersect([[L,L]],[[L]])) #must be []


# In[70]:


#Прринимает на вход 
#[]
#axes
#axes
#функция сравнения содержания элемента среди осей (not_match_by_axes or match_by_axes)

#Вернет декартово произведение по axes

def unite_inward(r,l,_axes,match):
    res = []
    if len(l) == 1:
        for el in l[0]:
            z = r.copy()
            z.append(el)
            #print(z,_axes)
            if match(z,_axes):
                res.append(z)
        return res
    Lcopy = l.copy()
    Lcopy0 = Lcopy.pop(0)
    r1 = []
    for el in Lcopy0:
        z = r.copy()
        z.append(el)
        r1 += unite_inward(z,Lcopy,_axes,match)
    return r1

print(unite_inward([],[[L,M,R],[U,D]],[[L,M,R],[U,D]],not_match_by_axes))
#[['L', 'U'], ['L', 'D'], ['M', 'U'], ['M', 'D'], ['R', 'U'], ['R', 'D']]


# In[76]:


#оболочка над unite_inward()

#принимает на вход 
#список осей axes
#функцию сравнения содержания элемента среди осей (not_match_by_axes or match_by_axes)

#Вернет декартово произведение по axes
def unite(l,match):
    return unite_inward([],l,l,match)

print(unite([[L,M,R],[U,D]],not_match_by_axes))
#[['L', 'U'], ['L', 'D'], ['M', 'U'], ['M', 'D'], ['R', 'U'], ['R', 'D']]


# In[79]:


#Принимает на вход два списка
#Вернет разницу между списками
def diff(L1,L2):
    return [el for el in L1 if el not in L2]+[el for el in L2 if el not in L1]

print(diff([1,2,3],[1,2]))


# In[89]:


#Принимает на вход список
#Вернет список из всех элементов всех подсписков входного списка (1ое поколение глубины)
def inside_out(L):
    res = []
    for el in L:
        #for el_inner in el:
        res += el
    return res

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

AXES_SET = [AXES,AXES]
print(inside_out(AXES_SET))
#[['L', 'M', 'R'], ['D', 'E', 'U'], ['B', 'S', 'F'], ['L', 'M', 'R'], ['D', 'E', 'U'], ['B', 'S', 'F']]


# In[93]:


#Принимает на вход список и число
#Вернет список из всех элементов всех подсписков N-ного поколения глубины входного списка
def inside_out_n(L,n):
    if n == 1:
        return inside_out(L)
    L = inside_out(L)
    return inside_out_n(L,n-1)

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

AXES_SET = [AXES,AXES]
print(inside_out_n(AXES_SET,1))
#[['L', 'M', 'R'], ['D', 'E', 'U'], ['B', 'S', 'F'], ['L', 'M', 'R'], ['D', 'E', 'U'], ['B', 'S', 'F']]
print(inside_out_n(AXES_SET,2))
#['L', 'M', 'R', 'D', 'E', 'U', 'B', 'S', 'F', 'L', 'M', 'R', 'D', 'E', 'U', 'B', 'S', 'F']


# In[96]:


#Принимает на вход список и число
#Вернет список N подсписков с элементами входного списка
def multiply(L,n):
    res = []
    for _ in range(n):
        res += [L]
    return res

X = [L,M,R]
Y = [D,E,U]
Z = [B,S,F]
AXES = [X,Y,Z]

Ls = inside_out(AXES)
print(multiply(Ls,3))
#[['L', 'M', 'R', 'D', 'E', 'U', 'B', 'S', 'F'], ['L', 'M', 'R', 'D', 'E', 'U', 'B', 'S', 'F'], ['L', 'M', 'R', 'D', 'E', 'U', 'B', 'S', 'F']]


# In[100]:


#Принимает на вход два списка из подсписков
#Вернет True ТОЛЬКО тогда, когда оба массива содержат одни и те же подсписки...
#...с учетом повторений элементов в подсписках, но без учета их порядка

def Ls_eq(L1,L2):
    return repeats_away(L1) == repeats_away(L2)

print(Ls_eq([[1,2],[3]],[[3],[2,1],[1,2]])) #must be True
print(Ls_eq([[1,2,1],[3]],[[3],[2,1],[1,2]])) #must be False


# In[102]:


#Принимает на вход список
#Распечатает каждый элемент на новой строке
def show_unwrap(l):
    for el in l:
        print(el)
    print()
    
show_unwrap([1,3,2])
#1
#3
#2


# In[ ]:





# In[ ]:





# In[195]:


#принимает на вход 
#размер оси (ребра) 
#Первый боковой слой
#Обозначение первого центрального слоя
#Центральный слой посередине
#Обозначение второго центрального слоя
#Второй боковой слой

#Вернет все слои от края к краю для данного размера пазла
#Если размер меньше 1х1, вернет None

def L_expand(N,boarder_L1,center_L1,middle_L,center_L2,boarder_L2):
    if N<1:
        return
    axe = []
    if N>1 and boarder_L1!='':
        axe.append(boarder_L1)
    for i in range(3,N):
        axe.append(str(i-1)+center_L1)
    if N%2 != 0:
        axe.append(middle_L)
    for i in range(N,3,-1):
        axe.append(str(i-2)+center_L2)
    if N>1 and boarder_L1!='':
        axe.append(boarder_L2)
    return axe

L = 'L'
M = 'M'
R = 'R'

D = 'D'
E = 'E'
U = 'U'

B = 'B'
S = 'S'
F = 'F'

L_center = L #'l'
R_center = R #'r'
D_center = D #'d'
U_center = U #'u'
B_center = B #'b'
F_center = F #'f'

for i in range(-1,7):
    print(L_expand(i,R,R_center,M,L_center,L))
    
#None #-1x-1
#None #0x0
#['M'] #1x1
#['R', 'L'] #2x2
#['R', 'M', 'L'] #3x3
#['R', '2R', '2L', 'L'] #4x4
#['R', '2R', '3R', 'M', '3L', '2L', 'L'] #5x5
#['R', '2R', '3R', '4R', '4L', '3L', '2L', 'L'] #6x6


# In[ ]:





# In[201]:


#Принимает на вход осевую формулу
#Вернет True ТОЛЬКО если формула имеет три числе >= 1
def cuboid_formula_check(formula):
    if type(formula) != list or len(formula) != 3:
        return False
    for N in formula:
        if N<1:
            return False
    return True

print(cuboid_formula_check(1))
print(cuboid_formula_check([]))
print(cuboid_formula_check([-1]))
print(cuboid_formula_check([0]))
print(cuboid_formula_check([1,-1]))
print(cuboid_formula_check([1,0]))
print(cuboid_formula_check([1]))
#all False

print(cuboid_formula_check([1,2,3]))
#True


# In[203]:


#Принимает на вход список из чисел. Каждое число - число слоев на оси
#Вернет оси real-кубоида по данной осевой формуле
#При некорректном вводе выдаст None
def cuboid_axes(formula):
    if not cuboid_formula_check(formula):
        return
    X = L_expand(formula[0],L,L_center,M,R_center,R)
    Y = L_expand(formula[1],D,D_center,E,U_center,U)
    Z = L_expand(formula[2],B,B_center,S,F_center,F)
    return [X,Y,Z]

print(cuboid_axes([])) #None
print(cuboid_axes([1,-1])) #None
print(cuboid_axes([0])) #None
print(cuboid_axes([0,1])) #None
print(cuboid_axes([1,2,3]))
#[['M'], ['D', 'U'], ['B', 'S', 'F']]
print(cuboid_axes([1,2,4]))
[['M'], ['D', 'U'], ['B', '2B', '2F', 'F']]


# In[204]:


#Принимает на вход осевую формулу
#Вернет все элементы rea-кубоида по осевой формуле
#При некорректном вводе выдась None

def real_cuboid_els(formula):
    if not cuboid_formula_check(formula):
        return
    axes = cuboid_axes(formula)
    #print(axes)
    els = unite(axes,not_match_by_axes)
    return els

print(real_cuboid_els([])) #None
print(real_cuboid_els([1,-1])) #None
print(real_cuboid_els([1,0])) #None
print(len(real_cuboid_els([1,2,4]))) #8


# In[212]:


#Принимает на вход осевую формулу
#Вернет элеметы обычгого кубоида по формуле
#Если формула некорректна, выдаст None

def cuboid_els(formula):
    if not cuboid_formula_check(formula):
        return
    axes = cuboid_axes(formula)
    if not axes:
        return
    inner_axes = []
    for axe in axes:
        #print(axe)
        inner_axe = axe.copy()
        inner_axe.remove(axe[0])
        if len(axe) != 1:
            inner_axe.remove(axe[-1])
        inner_axes.append(inner_axe)
    els = unite(axes,not_match_by_axes)
    inner_els = unite(inner_axes,not_match_by_axes)
    return diff(els,inner_els)

print(cuboid_els([1,2,4]))


# In[187]:


#Принимает на вход только размер куба
#Вернет список осей для куба данного размера с учетом всех номеров центральных слоев

def cube_axes(size):
    return cuboid_axes([size,size,size])

for i in range(0,7):
    print(cube_axes(i))
    
#None
#[['M'], ['E'], ['S']]
#[['L', 'R'], ['D', 'U'], ['B', 'F']]
#[['L', 'M', 'R'], ['D', 'E', 'U'], ['B', 'S', 'F']]
#[['L', '2L', '2R', 'R'], ['D', '2D', '2U', 'U'], ['B', '2B', '2F', 'F']]
#[['L', '2L', '3L', 'M', '3R', '2R', 'R'], ['D', '2D', '3D', 'E', '3U', '2U', 'U'], ['B', '2B', '3B', 'S', '3F', '2F', 'F']]
#[['L', '2L', '3L', '4L', '4R', '3R', '2R', 'R'], ['D', '2D', '3D', '4D', '4U', '3U', '2U', 'U'], ['B', '2B', '3B', '4B', '4F', '3F', '2F', 'F']]  


# In[213]:


#Принмает на вход только размер real-куба
#Вернет все элементы real-куба данного размера

def real_cube_els(size):
    axes = cube_axes(size)
    #print(axes)
    if axes:
        els = unite(axes,not_match_by_axes)
        return els
    else:
        return

print(real_cube_els(-1)) #None
print(real_cube_els(0)) #None
print(len(real_cube_els(4))) #64


# In[217]:


#Принмает на вход только размер обычного куба
#Вернет все элементы обычного куба данного размера

def cube_els(size):
    return cuboid_els([size,size,size])

print(cube_els(-1)) #None
print(cube_els(0)) #None
print(len(cube_els(4))) #56


# In[221]:


#Принимает на вход список из чисел. Каждое число - число слоев на оси

def layer_formula(formula):
    if len(formula) == 3:
        return real_cuboid_els(formula)

print(len(layer_formula([3,3,2]))) #18


# In[ ]:




