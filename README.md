# CompositeDP
1. Background:
	This is a novel composite DP mechanism.

2. Install:
	 There are 6 Python files in total:
		1) Perturbation_Mechanism.py
		2) Traditional_Mechanism.py
		3) Mechanism/Parameter_Optimization.py
		4) Mechanism/Constraints.py
		5) Mechanism/Evaluation.py
		6) Mechanism/Mapping.py
	For using this novel DP Library, users need to download all Python files in their local environment.

3. Usage:
	This is a Python library, users can just import it.

	Import library:
	from Traditional_Mechanism import *
	from Perturbation_Mechanism import *
	Then users can use the composite DP mechanism freely.

3. Using examples:
	Please see the Example1.py and Example2.py file.

4. Perturbation Function List:

	Perturbation-1: 	Activation-1+Base-1,   	index=1
	
	Perturbation-2: 	Activation-2+Base-1,   	index=2
	
	Perturbation-3: 	Activation-3+Base-1,   	index=3
	
	Perturbation-4: 	Activation-1+Base-2,   	index=4
	
	Perturbation-5: 	Activation-2+Base-2,   	index=5
	
	Perturbation-6: 	Activation-3+Base-2,   	index=6
	
	Perturbation-7: 	Activation-1+Base-3,   	index=7
	
	Perturbation-8: 	Activation-2+Base-3,   	index=8
	
	Perturbation-9: 	Activation-3+Base-3,   	index=9
	
	Perturbation-10: 	Activation-1+Base-4,   	index=10
	
	Perturbation-11: 	Activation-2+Base-4,   	index=11
	
	Perturbation-12: 	Activation-3+Base-4,   	index=12  

5. How to use perturbation function:
	1. For one time call:
		ep: Privacy Budget
		fd: Raw input query result f(D)
		fd2:Neighbor databases query result f(D')
		k: parameter
		m: parameter
		y: parameter
		index: which perturbation function you are going to use
		
		Call Function: perturbation_fun_oneCall(ep, fd, fd2, k, m, y, index)
		Return value: Perturbed Result M(fd)

	2. For multiple call:
		ep: Privacy Budget
		fd: Raw input query result f(D)
		fd2:Neighbor databases query result f(D')
		k: parameter
		m: parameter
		y: parameter
		index: which perturbation function you are going to use
		repeat_times: How many times you are going to recall the mechanism

		Call Function: perturbation_fun_multipleCall(ep, fd, fd2, k, m, y, index, repeat_times)
		Return value: A list of perturbed Results (M(fd),....)

	If you don't want to pick the parameters by yourself, you can use optimized function:
	
	3. For one time call (optimized):
		ep: Privacy Budget
		fd: Raw input query result f(D)
		fd2:Neighbor databases query result f(D')
		index: which perturbation function you are going to use

		Call Function: perturbation_fun_optimized_oneCall(ep, fd, fd2, index)
		Return value: Perturbed Result M(fd)

	4. For multiple call (optimized):
		ep: Privacy Budget
		fd: Raw input query result f(D)
		fd2:Neighbor databases query result f(D')
		index: which perturbation function you are going to use
		repeat_times: How many times you are going to recall the mechanism

		Call Function: perturbation_fun_optimized_multipleCall(ep, fd, fd2, k, m, y, index, repeat_times)
		Return value: A list of perturbed Results (M(fd),....)
   
   Thanks very much!
