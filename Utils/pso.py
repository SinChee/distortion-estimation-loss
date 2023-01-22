from __future__ import division
import random
from tqdm import tqdm


class Particle:
    def __init__(self,x0):
        self.num_dimensions = len(x0)
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual
        for i in range(self.num_dimensions):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(x0[i])

    def evaluate(self,costFunc):
        self.err_i=costFunc(*self.position_i)
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i

    def update_velocity(self, pos_best_g, w=0.5, c1=1, c2=2):
        for i in range(self.num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    def update_position(self,bounds):
        for i in range(self.num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]


class PSO():
    def __init__(self,costFunc,x0,bounds,num_particles):
        self.num_dimensions = len(x0)
        self.err_best_g=-1                   # best error for group
        self.pos_best_g=[]                   # best position for group
        self.cost_function = costFunc
        self.bounds = bounds
        self.num_particles = num_particles

        self.population = [Particle(x0) for _ in range(num_particles)]
    
    def train(self, epoch):
        for _ in tqdm(range(epoch)):
            for j in range(self.num_particles):
                self.population[j].evaluate(self.cost_function)
                if self.population[j].err_i < self.err_best_g or self.err_best_g == -1:
                    self.pos_best_g=list(self.population[j].position_i)
                    self.err_best_g=float(self.population[j].err_i)

            for j in range(self.num_particles):
                self.population[j].update_velocity(self.pos_best_g)
                self.population[j].update_position(self.bounds)


        # print final results
        return (self.pos_best_g, self.err_best_g)
