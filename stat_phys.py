from stats import MetropolisHastings
import numpy as np

class MB_Sampler1D:

	def __init__(self, m, kb, t):
		self.m = m
		self.kb = kb
		self.t = t

	def _maxwell_boltzmann(self,v,m,kb,t):
		d1 = 2*np.pi*kb*t
		c1 = (m/d1)**(1/2)
		d2 = 2*kb*t
		c2 = -(m*v**2)/d2
		return c1*np.exp(c2)

	def metropolis_hastings_sampler(self, dx):
		to_sample = lambda v: self._maxwell_boltzmann(v,self.m,self.kb,self.t)
		self.xs = np.asarray([0])
		self.sampler = self._make_MH_sampler(to_sample,dx)

	def _make_MH_sampler(self,func,dx):
		def sampler(n):
			xs = MetropolisHastings(func,self.xs[-1],dx,n)[1:]
			self.xs = np.append(self.xs,xs)
			return xs
		
		return sampler

class MB_Sampler3D:

	def __init__(self):
		pass

class MB_Speed_Sampler():
	
	def __init__(self):
		pass