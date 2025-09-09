# Day 15 - Coffee Machine Project

## Project Overview
This Python console app simulates a coffee vending machine.  
Users can order espresso, latte, or cappuccino, insert coins, and receive a drink if resources and payment are sufficient.  

The project ties together key Python concepts: dictionaries, functions, loops, conditionals, error handling, and arithmetic. It manages user input, payments, resources, and profits.

---

## How It Works
- **User Choices**: Order a drink, type `report` to view resources, or `off` to shut down.  
- **Resource Check**: Ensures enough water, milk, and coffee before making a drink.  
- **Coin Input**: Prompts for quarters, dimes, nickels, and pennies, then sums total value.  
- **Payment Handling**:  
  - If enough → serve coffee + return change if overpaid.  
  - If not enough → refund money.  
- **Coffee Serving**: Deducts ingredients, updates profit, and confirms the drink is ready.  

---

## Project Highlights
- **Modular Functions**: Separate tasks (resource check, coin input, profit).  
- **Resource Tracking**: Updates inventory after each drink.  
- **Profit Tracking**: Records earnings from sales.  
