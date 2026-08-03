# Descriptors in Python

- **原邮件主题**: ​MiniMax-M2 vs. Kimi-K2 vs. Sonnet 4.5 on Code Generation​
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 20 Nov 2025 19:55:54 +0000
- **ID**: 19aa2d674dcfaef6

---

## [**Descriptors in Python**](<https://www.dailydoseofds.com/object-oriented-programming-with-python-for-data-scientists/>)

Say we want to define a class where all instance-level attributes must be positive.

Getters and setters are commonly used to do this.

But the problem is that these getters and setters scale with the number of attributes in your class:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/5qWV9XDg5GBZKK7nNeRzfh/email)   
---  
  
  * 1 attribute → leads to 1 getter and 1 setter.
  * 2 attributes → lead to 2 getters and 2 setters. 
  * 5 attributes → lead to 5 getters and 5 setters.

Also, there's so much redundancy in this code:

  * All getters are almost the same—they just have a return statement.
  * All setters have similar validation checks.

And to make things worse, the setters are not invoked while creating an object. 

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/uPBUgpKc85PvBj7uPSQuRY/email)   
---  
  
So you must add additional checks to ensure an object is created with valid inputs.

Descriptors solve all these problems.

Simply put, `Descriptors` are objects with methods (like `__get__`, `__set__`, etc.) that are used to manage access to the attributes of the class of interest.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febd1d9a9-a391-4abc-a97b-67f16aa44eca_3308x1168.png)   
---  
  
Thus:

  * The attribute `number1` → gets its own descriptor.
  * The attribute `number2` → gets its own descriptor.
  * The attribute `number3` → gets its own descriptor.

A `Descriptor` class is implemented with three methods:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8d1f8b0-5758-4efc-8189-f334e49f60a5_1456x738.png)   
---  
  
  * The `__set__` method is called when the attribute is assigned a new value. We can define all custom checks here.
  * The `__set_name__` method is called when the descriptor object is assigned to a class attribute. It allows the descriptor to keep track of the name of the attribute it’s assigned to within the class.
  * The `__get__` method is called when the attribute is accessed.

If it’s unclear, let me give you a demonstration.

# **Demo**

Consider this `Descriptor` class:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f293ccc-e2b1-4d94-8484-9fd93bebc2af_1456x732.png)   
---  
  
I’ll explain this implementation shortly, but before that, consider this usage:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1188df8-d62a-4e02-b1bf-149f35cbad27_1456x705.png)   
---  
  
Now, let’s go back to the `DescriptorClass` implementation:

  * `__set_name__(self, owner, name)`: This method is called when the descriptor is assigned to a class attribute (line 3). It saves the name of the attribute in the descriptor for later use.
  * `__set__(self, instance, value)`: When a value is assigned to the attribute (line 6), this method is called. It raises an error if the value is negative. Otherwise, it stores the value in the instance’s dictionary under the attribute name we defined earlier.
  * `__get__(self, instance, owner)`: When the attribute is accessed, this method is called. It returns the value from the instance’s dictionary.

Done!

* * *

Now, see how this solution solves all the problems we discussed earlier.

Creating an object of `DummyClass` with an invalid value raises an error:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9732fa38-d5dc-4cd2-9505-acbf511b2393_1456x551.png)   
---  
  
Passing an invalid value during the initialization raises an error as well:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0478e9c4-0c40-4abe-9c73-57827a6578f7_1456x381.png)   
---  
  
Moving on, let’s define multiple attributes in the `DummyClass` now:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F615e22c1-7766-4134-b9ed-1eb3dab8aeca_1456x676.png)   
---  
  
Creating an object and setting an invalid value for any of the attributes raises an error:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d0f8f7f-526a-4559-a891-a7af400f7e2c_1456x663.png)   
---  
  
Recall that we never defined multiple getters and setters for each attribute individually, like we did with the `@property` decorator earlier.

I find descriptors to be massively helpful in reducing work and code redundancy while also making the entire implementation much more elegant.

Here’s a deep dive into Python OOP if you want to learn advanced OOP in Python: [**Object-Oriented Programming with Python for Data Scientists**](<https://www.dailydoseofds.com/object-oriented-programming-with-python-for-data-scientists/>).

👉 Over to you: What are some cool things you know about Python OOP?
