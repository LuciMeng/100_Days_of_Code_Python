# Day 16 - Coffee Machine Project with OOP

## Overview
This project rebuilds the coffee machine program using **Object-Oriented Programming (OOP)** concepts. 
Instead of relying on pre-written functions, the solution applies classes, objects, attributes, and methods to simulate a real coffee machine. 
Users can order espresso, latte, or cappuccino, insert virtual coins, and receive their drink if resources and payment are sufficient.

## How It Works
- **User Interaction:** Input drink choice (`espresso/latte/cappuccino`), view `report`, or turn `off`.
- **Menu & Resources:** Managed through `Menu` and `CoffeeMaker` classes.
- **Payment Processing:** Handled by `MoneyMachine`, which collects coins, validates payment, and gives change.
- **Serving Coffee:** If requirements are met, ingredients are deducted and the drink is served.

## Highlights
- **OOP Design:** Organized into four classes:  
  - `MenuItem` – defines drink name, cost, and ingredients.  
  - `Menu` – manages coffee options and user selections.  
  - `CoffeeMaker` – tracks resources and brews drinks.  
  - `MoneyMachine` – processes payments and tracks profit.  
- **Attributes & Methods:**  
  - Attributes: resources, ingredients, profit.  
  - Methods: `report()`, `make_coffee()`, `make_payment()`.  

## Summary
This project re-implements the coffee machine using **OOP principles** instead of procedural code, showcasing modular, reusable, and maintainable design.
