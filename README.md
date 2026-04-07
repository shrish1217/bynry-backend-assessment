# Bynry Backend Engineering Assessment - StockFlow
**Candidate:** Shrish Vats  
**Role:** Backend Engineering Intern  

## 📌 Overview
This repository contains my solutions for the Bynry Backend Case Study. The project focuses on building "StockFlow," a multi-tenant SaaS inventory management system.

## 🛠️ Key Features
- **Part 1: Code Review & Debugging**
  - Implemented **Atomic Transactions** to prevent data inconsistency ("ghost products").
  - Added robust **Input Validation** and custom error handling (HTTP 400/409/500).
  - Fixed logic for SKU uniqueness as per business requirements.
  
- **Part 2: Database Design**
  - Designed a relational schema supporting **Multiple Warehouses** and **Companies**.
  - Implemented a **Self-Referencing Table** for Product Bundles (Combos).
  - Used `Decimal` types for financial accuracy in pricing.

- **Part 3: API Implementation**
  - Created a **Low-Stock Alert API** with business intelligence.
  - Filtered alerts to only show "active" products (sold in the last 30 days) to reduce dashboard noise.

## 🚀 Tech Stack
- **Backend:** Python (Flask), Node.js (Express)
- **Database:** MySQL / PostgreSQL Logic
- **Concepts:** ACID compliance, Multi-tenancy, Relational Schema design.
