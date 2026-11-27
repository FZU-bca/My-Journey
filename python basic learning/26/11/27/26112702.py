"""

学习日志
日期：2026 年 11 月 27 日

一、今日目标
学习黑马程序员 Python + AI 编程课第 89–91 集
完成本地大模型的部署
二、学习内容
1. 课程第 89–91 集：面向对象编程

理解了"类"和"对象"的关系：类是模板，对象是按模板创建出来的实例。重点掌握了：

__init__ 构造方法：在创建对象时完成属性初始化，self 指向当前实例
__str__ 魔术方法：决定对象被 print() 时的显示内容
实例方法中 self 的作用，以及方法的定义与调用规则
用 match-case 实现菜单式交互程序
2. 本地大模型部署

独立完成了从环境准备、模型拉取到本地启动对话的完整流程，第一次让大模型在自己电脑上跑起来，不依赖网络和在线 API。这让我对"AI 应用到底是怎么跑起来的"有了直观认识。

三、动手实践
把课程内容落地成一个简易教务管理系统：Student 类负责保存单个学生的姓名和三门成绩，EDU 类负责管理学生列表并提供增、删、改、查、列表的菜单交互。

在调试过程中，我遇到了一个卡了很久的问题：程序能正常运行、菜单也能显示，但按 1 之后方法就是不执行，只是不断重新打印菜单。排查后发现根本原因是 input() 的返回值是字符串 "1"，而 match 里写的是整数 case 1:，"1" 永远不等于 1，所以所有输入都掉进了 case _ 分支。把 case 的字面量改成字符串后，菜单立刻通了。

顺着这个 Bug 又接连暴露并修复了另外几类错误：

方法名不一致：菜单调用的是 find_student，类里定义的是 query_student
参数个数不匹配：add_student(self, student) 多了一个从未使用的形参
变量名写错：s.updateScore(...) 中的 s 并不存在，应为循环变量
字符串格式化：漏写 f-string 前缀、把变量写在引号内、误用 f.student 访问不存在的属性
四、收获与反思
今天最大的体会是："能运行"和"逻辑正确"是两件事。 程序没报语法错误，不代表它走在预期的路径上；真正定位问题要靠证据——打印出变量的值和类型，比盯着代码猜有效得多。另外，input() 返回字符串这类基础细节，一旦忽略就会引发连锁问题。

还有一个教训是命名。我把循环变量命名为 f，结果和 f-string 的前缀 f 反复混淆，导致好几次写错。变量名起得清楚，本身就是一种排错手段。

五、明日计划
继续学习后续课程，巩固面向对象
完善教务系统：为输入加上异常处理，防止非数字导致崩溃
尝试把本地大模型接入到自己的脚本中，做一个简单的小工具
Learning Log
Date: November 27, 2026

1. Today's Goals
Study episodes 89–91 of the Heima Programmer Python + AI programming course
Complete the deployment of a local large language model
2. What I Learned
Course episodes 89–91: Object-Oriented Programming

I now understand the relationship between classes and objects: a class is a template, and an object is an instance created from that template. Key takeaways:

The __init__ constructor: initializes attributes when an object is created, with self referring to the current instance
The __str__ magic method: determines what is displayed when an object is passed to print()
The role of self in instance methods, and the rules for defining and calling methods
Building a menu-driven interactive program with match-case
Local LLM deployment

I completed the full process independently, from preparing the environment and pulling the model to launching a local chat session. For the first time I had a large model running on my own machine, with no network or online API involved. It gave me a concrete picture of how AI applications actually run.

3. Hands-On Practice
I turned the course material into a simple student management system: the Student class stores one student's name and three subject grades, while the EDU class manages the student list and provides a menu for adding, updating, deleting, querying, and listing students.

During debugging, I hit a problem that blocked me for a long time: the program ran and the menu displayed, but pressing 1 never executed the method — the menu just kept reprinting. The root cause turned out to be that input() returns the string "1", while my match statement used the integer literal case 1:. Since "1" never equals 1, every input fell through to case _. Once I changed the case literals to strings, the menu worked immediately.

Following that bug, several other errors surfaced and were fixed one by one:

Inconsistent method names: the menu called find_student, but the method was defined as query_student
Mismatched parameters: add_student(self, student) had an extra parameter that was never used
A wrong variable name: s.updateScore(...) used s, which did not exist — it should have been the loop variable
String formatting: a missing f-string prefix, variables written inside quotes, and f.student trying to access a non-existent attribute
4. Takeaways and Reflection
The biggest lesson today: "it runs" and "it's correct" are two different things. A program with no syntax errors is not necessarily following the intended path. Locating a real problem requires evidence — printing a variable's value and type is far more effective than staring at the code and guessing. Also, basic details like input() returning a string can trigger a chain of problems if overlooked.

Another lesson is naming. I named the loop variable f, which constantly got confused with the f-string prefix f, causing several mistakes. Clear variable names are themselves a debugging tool.

5. Plan for Tomorrow
Continue with the following lessons and consolidate object-oriented programming
Improve the student management system: add exception handling so non-numeric input doesn't crash it
Try connecting the local LLM to my own script and build a small tool
"""