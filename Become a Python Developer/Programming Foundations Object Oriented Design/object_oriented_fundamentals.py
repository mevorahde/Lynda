"""
Procedural coding is usually written as a long series of operations to execute.
I.E. a recipe in a cook book, take the ingredients, apply the steps in order and you have your dish.

Object-Oriented thinking is breaking down the dish into three separate objects, in code, three separate mini functions,
like three separate programs.
- Advantage of Object-Oriented thinking:
   + re-usability

Objects: has it's own identity that's independent of all other objects.
- Objects can have attributes to describe an objects
- All objects have three things:
    + Identity: Olivia's coffee mug
    + Attributes: color, size, fullness
    + Behaviors: fill(), empty(), clean()

Class: Code-template for creating program objects
- Class components have:
    + Name: What is it?
    + Attributes: What describes it?
    + Behavior: What can it do?

Method: A program procedure that can return a value
- Defined as part of a class
- Can only access data known to its object
- Functions are similar, however methods are defined as part of a class. Functions are not.

Abstraction means the idea or concept of a person is completely separate from any specific instance.

Encapsulation is about containing the elements of an object to protect an instance from being accessed and/or changed.
- Block Box Testing

Inheritance enables a new class to receive or inherit the attributes and methods of existing classes using the same
implementation which is a great form of code reuse.

*Python allows you to inherit from more then one super class. Bringing in attributes and behaviors from multiple other
classes. However, multiple inheritance can get confusing so it's much more common to see single inheritance where
a subclass only inherits from one parent or superclass.

Dynamic Polymorphism: Uses the same interface for methods on different types of objects

Static (Compile-Time) Polymorphism: Uses Method Overloading, which implements multiple methods with the same name,
but different parameters.

Object-Oriented Analysis: Understand your problem
- Answers the question, what do you need to do?

Object-Oriented Design: Plan your solution
- Answers the question, how are you going to do it?

Object-Oriented Programming: Build it

5 Step approach:

1. Gather requirements
2. Describe the application
3. Identify the main objects
4. Describe the interactions.
5. Create a class diagram

Unified Modeling Language (UML): Standardized notation for diagrams to visualize object-oriented systems
For this course, the two UMLs that will be used are:
- Use case diagram
- Class diagram
"""