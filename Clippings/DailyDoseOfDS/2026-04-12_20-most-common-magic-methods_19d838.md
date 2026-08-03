# 20 most common magic methods

- **原邮件主题**: The Anatomy of Diffusion LLMs
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Sun, 12 Apr 2026 21:10:55 +0000
- **ID**: 19d838888f466ecf

---

## [**20 most common magic methods**](<https://fff97757.click.kit-mail3.com/zluvnvdrxlunhkxedo6tphwlvrgwgb6h93200/dpheh0he6x3p20sm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vb2JqZWN0LW9yaWVudGVkLXByb2dyYW1taW5nLXdpdGgtcHl0aG9uLWZvci1kYXRhLXNjaWVudGlzdHMv>)

Here’s a visual that lists the 20 most common magic methods used in Python OOP:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43224c49-fbad-4cac-bce3-e54468392643_863x1128.png)   
---  
  
In my experience, these are possibly the only 20 magic methods you would ever need in most Python projects utilizing OOP.

Syntactically, they are prefixed and suffixed with double underscores, such as `__len__, __str__`, and many more. That is why they are also called “Dunder methods” — short for **D** ouble **UNDER** score.

**Here’s a brief description of each of them.**

1) `__new__`:

  * This method is invoked before `__init__` to allocate memory to an object.
  * In most cases, we wouldn’t need it.
  * Yet, at times, I have used this to define checks and allocate memory only when certain conditions are met.
  * Another common usage is to define singleton classes — classes with only one object.

2) `__init__`:

  * Most common in this list.
  * This is invoked after memory allocation to assign value to an object’s attributes.

3) `__str__`:

  * Executing `print(obj)` outputs the memory address of the object, which is not interpretable.
  * Defining this method lets us print the object in a readable format.

4) `__int__`: Invoked when we execute → `int(obj)`.

5) `__len__`: Invoked when we execute → `len(obj)`.

6) `__call__`: Invoked when a class object is called as a function → `obj()`.

7) `__getitem__`: Invoked when an object is indexed → `obj[key]`.

8) `__setitem__`: Invoked when an object is indexed and a value is set → `obj[key]=value`.

9) `__delitem__`: Invoked when an object’s index is deleted → `del obj[key]`.

10) `__contains__`: Invoked when the `in` operator is used → `item in obj`.

11) `__bool__`: Invoked when an object is used in a boolean context → `if obj or bool(obj)`.

12) `__iter__`: Invoked when we iterate over an object → `for x in obj`.

13) `__eq__`: Invoked when `==` operator is used to compare two objects → `obj1 == obj2`.

14) `__ne__`: Invoked when `!=` operator is used to compare two objects → `obj1 != obj2`.

15) `__gt__`:

  * Invoked when `>` operator is used to compare two objects → `obj1 > obj2`.
  * Other than `__gt__`, we also have:
    * `__lt__`: less than.
    * `__le__`: less than or equal to.
    * `__ge__`: greater than or equal to.

16) `__add__`: Invoked when two objects are added → `obj1 + obj2`.

17) `__mul__`: Invoked when two objects are multiplied → `obj1 * obj2`.

18) `__abs__`: Invoked when we compute the absolute value of an object: `abs(obj)`.

19) `__neg__`: Invoked when the unary operator `-` (minus) is used on an object → `-obj`.

20) `__invert__`: Invoked when `~ `(tilde) operator is used to invert an object → `~obj`.

Now you know the most common Magic methods in Python and how they are used.

We went into much more detail and covered many advanced concepts and programming details of Python OOP here: [**Object-Oriented Programming with Python for Data Scientists**](<https://fff97757.click.kit-mail3.com/zluvnvdrxlunhkxedo6tphwlvrgwgb6h93200/dpheh0he6x3p20sm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vb2JqZWN0LW9yaWVudGVkLXByb2dyYW1taW5nLXdpdGgtcHl0aG9uLWZvci1kYXRhLXNjaWVudGlzdHMv>).

Also, if you want to get really good at Python OOP, learn about Python Descriptors.

I find them to be massively helpful in reducing work and code redundancy while also making the entire implementation much more elegant.

**We covered it in this newsletter here:**[**Define Elegant and Concise Python Classes with Descriptors**](<https://fff97757.click.kit-mail3.com/zluvnvdrxlunhkxedo6tphwlvrgwgb6h93200/e0hph7h7vzxrd7t8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9kZXNjcmlwdG9ycy1pbi1weXRob24v>)**.**

👉 Over to you: Did I miss any common magic methods? If yes, which one(s)?
