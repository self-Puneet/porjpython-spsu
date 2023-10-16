k=8.9975*(10**9)
G=6.67430*(10**(-11))

#######################
parameters=[]
print("---------------------------------------------------------------------------------------------------------------------------------------")
n=int(input("enter number of particles in your isolated system= "))
print("---------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,n):
    x1=float(input(f"enter x coordinate of particle {i+1}= "))
    y1=float(input(f"enter y coordinate of particle {i+1}= "))
    z1=float(input(f"enter z coordinate of particle {i+1}= "))
    m=float(input(f"enter the mass of particle {i+1}= "))
    q1=float(input(f"enter the charge of particle {i+1}= "))
    coord=(x1,y1,z1,m,q1)
    parameters.append(coord)
    print("---------------------------------------------------------------------------------------------------------------------------------------")


#for finding center of mass of system of particles
total_mass=0
mass_x_x=0
mass_x_y=0
mass_x_z=0
for i in range(0,n):
    total_mass+=parameters[i][3]
    mass_x_x+=((parameters[i][0])*(parameters[i][3]))
    mass_x_y+=((parameters[i][1])*(parameters[i][3]))
    mass_x_z+=((parameters[i][2])*(parameters[i][3]))
com=((mass_x_x/total_mass),(mass_x_y/total_mass),(mass_x_z/total_mass))
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("\t\tcenter of mass of system of particles------>",com)

#for making an array containing distance of each point from each other.
distance_array = [[0] * n for _ in range(n)]
for i in range(0,n):
    for j in range(0,n):
        if i==j: distance_array[i][j]=0
        else: 
            x=parameters[i][0]-parameters[j][0]
            y=parameters[i][1]-parameters[j][1]
            z=parameters[i][2]-parameters[j][2]
            d=((x**2)+(y**2)+(z**2))**(1/2)
            distance_array[i][j]=distance_array[j][i]=d
distance_cube_array=[[0] * n for _ in range(n)]
for i in range(0,n):
    for j in range(0,n):
        distance_cube_array[i][j]=(distance_array[i][j])**3

#for finding potential energy of system.
gpe=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j: gpe+=((G*parameters[i][3]*parameters[j][3])/(distance_array[i][j]))
        else: pass
gpe=gpe/2
epe=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j: epe+=((k*parameters[i][4]*parameters[j][4])/(distance_array[i][j]))
        else: pass
epe=epe/2
tpe=epe+gpe
print("\t\tgravitational potential energy------------->",gpe)
print("\t\telectrostatic potential energy------------->",epe)
print("\t\ttotal potential energy--------------------->",tpe)
print("---------------------------------------------------------------------------------------------------------------------------------------")

#finding initial force on any particle
force=[[0,0,0] for _ in range(0,n)]
sum_i=0
sum_j=0
sum_k=0
for i in range(0,n):
    for j in range(0,n):
        if i==j: pass
        else:
            a1=-(k*parameters[i][4]*parameters[j][4]*(parameters[j][0]-parameters[i][0]))/(distance_cube_array[i][j])
            a2=(G*parameters[i][3]*parameters[j][3]*(parameters[j][0]-parameters[i][0]))/(distance_cube_array[i][j])
            sum_i=sum_i+a1+a2
            b1=-(k*parameters[i][4]*parameters[j][4]*(parameters[j][1]-parameters[i][1]))/(distance_cube_array[i][j])
            b2=(G*parameters[i][3]*parameters[j][3]*(parameters[j][1]-parameters[i][1]))/(distance_cube_array[i][j])
            sum_j=sum_j+b1+b2
            c1=-(k*parameters[i][4]*parameters[j][4]*(parameters[j][2]-parameters[i][2]))/(distance_cube_array[i][j])
            c2=(G*parameters[i][3]*parameters[j][3]*(parameters[j][2]-parameters[i][2]))/(distance_cube_array[i][j])
            sum_k=sum_k+c1+c2
    (force[i][0],force[i][1],force[i][2])=(sum_i,sum_j,sum_k)
for i in range(0,n): print("\t\tforce on particle",i,"= ",force[i][0],"i + ",force[i][1],"j + ",force[i][2],"k")

#asking for any time
t=float(input("enter time at which you want to know dynamics of motion= "))
dt=float(input("enter t such that 10^(-t) is small time interval= "))
dt=10**(-dt)

# hii first time use of github

