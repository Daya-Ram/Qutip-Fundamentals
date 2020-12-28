#!/usr/bin/env python
# coding: utf-8

# $ \color{red}{\Large What\ is\  QuTiP? }$

# $ \color{blue}{\Large QuTiP\  is \ Quantum \ Toolbox \ in \ Python. }$

# ## Concepts:

# ### (i) Wavefunction / state $\rightarrow $ Vectors or matrices
# ### (iii) Hamiltonian/operators $\rightarrow $ Matrices
# ### (iii)  Equation of motion $\rightarrow $ Ordinary Differential Equations
# ### (iv) Observables and expectation values $\rightarrow $ Inner product

# In[1]:


import numpy as np
from qutip import * ##simulates dynamics of open quantum systems(composed of few-level quantum systems and harmonic oscillators)


# ## rand_herm:
# ### generates random Hermitian matrices

# In[55]:


a1 = rand_herm(4) 
a1


# ## Quantum states, operators etc. are represented by a data structure called Qobj.
# $ \Large\color{red}{To \ create \ an \ object, \ we \ use \ "Qobj".}$

# ## Review of bra and kets:

# $\color{blue}{\Large ket: |\psi\rangle = \begin{pmatrix}
#                               C_1\\
#                               C_2\\
#                               .\\
#                               .\\
#                               .\\
#                               C_i\\
#                               .\\
#                               .\\
#                               .\\
#                               \end{pmatrix}\\
#   \Large bra: \langle \psi| = [C_1^*\ C_2^*... C_i^*...]}$

# In[48]:


Qobj([[1,3,5]])


# In[4]:


Qobj([[1],[2],[3],[4],[5]])


# In[5]:


Qobj([[1]])


# In[6]:


Qobj([[1],[2]])


# In[7]:


Qobj([[1,2],[3,4]])


# In[8]:


q = Qobj([[1],[2]])
q.check_herm()


# In[9]:


q.type


# In[10]:


Qobj([[1,2j],[3,4]])


# In[11]:


Qobj([[1,2],[3,-4j]])


# In[12]:


Qobj([[1,2],[3,4],[5,6]])


# In[13]:


Qobj()


# In[14]:


Q = Qobj([[1,0],[0,1]])
Q


# In[15]:


Q.isherm


# In[16]:


Q.dims


# In[17]:


Q.type


# In[18]:


x = np.array([[1, 2, 3, 4]])
Qobj(x)


# In[19]:


t = np.random.rand(5,5)
Qobj(t)


# In[61]:


qeye(3) # Identity operator with no. of levels in Hilbert space =3


# $ \Large\color{orange}{\Large Pauli\ spin\ matrices }$

# ## $\sigma_x =
# \begin{pmatrix}
# 0 & 1 \\
# 1 & 0
# \end{pmatrix} $, 
# ## $\sigma_y =
# \begin{pmatrix}
# 0 & -j \\
# j & 0
# \end{pmatrix} $ and
# ## $\sigma_z =
# \begin{pmatrix}
# 1 & 0 \\
# 0 & -1
# \end{pmatrix} $ 
# 
# 

# In[25]:


z = sigmaz()
z


# In[26]:


z.diag()


# In[27]:


x = sigmax()
x


# In[28]:


y = sigmay()
y


# In[29]:


a = tensor(x,y)
a


# In[30]:


y.diag() # diagonal elements


# ## Trace of a matrix
# $ \Large tr(A) = \sum_{i=1}^n {a_{ii}} $
# 

#  ### Pauli's spin matrices are traceless.

# In[31]:


z.tr() 


# ## Trace of the product of any number of operators is invariant under a cyclic permutation of these operators.
# ## tr(xy)= tr(yx)

# In[32]:


a= x*y
a.tr()


# In[33]:


b = y*x.tr()
b.tr()


# ## Commutation of Pauli matrices
# $ \Large [\sigma_x,\sigma_y]=2i\sigma_z $

# In[34]:


commutator(sigmax(),sigmay())


# In[35]:


commutator(sigmay(),sigmaz())


# $ \Large \sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I,\ Identity \ matrix$

# In[36]:


x*x


# In[37]:


momentum(2)


# In[56]:


destroy (2) # lowering destruction operator


# In[57]:


create(2) # rising (creation operator)


# In[58]:


create(0)


# In[59]:


create(3)


# In[ ]:


## basis: 
### Generates the vector representation of a Fock state (Fock state or number state is a quantum state that is an element of a Fock space with a well-defined number of particles (or quanta))


# In[38]:


basis(5,0) # Ground state


# In[39]:


a=basis(5,2)
a


# In[40]:


bra("1")


# ## Coherent:
# ### Generates a coherent state with eigenvalue (It is the specific quantum state of the quantum harmonic oscillator, often described as a state which has dynamics most closely resembling the oscillatory behavior of a classical harmonic oscillator)

# In[41]:


coherent(5,0)


# # Particle in a Potential well

# $ \Large Schrodinger \ time \ independent \ wave\ equation  \ is$
# 
# $ \Large \frac{d^2\psi}{dx^2}+\frac{2m}{\hbar^2}\small(E-V)\psi = 0 $

# ### Reference: http://qutip.org/

# In[ ]:




