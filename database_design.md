# Part 2: Database Schema & Design Decisions

## 📊 Schema Design (Relational Model)

| Table Name | Primary Key | Foreign Keys | Key Columns |
| :--- | :--- | :--- | :--- |
| **Companies** | `id` | - | `name`, `registration_number` |
| **Warehouses** | `id` | `company_id` | `name`, `location` |
| **Products** | `id` | - | `name`, `sku` (Unique), `price` (Decimal) |
| **Inventory** | `product_id`, `warehouse_id` | - | `quantity`, `low_stock_threshold` |
| **Product_Bundles** | - | `parent_id`, `child_id` | `quantity` (Self-referencing mapping) |
| **Suppliers** | `id` | - | `name`, `contact_email` |

## 💡 Justifications & Design Decisions

### 1. Bundle Logic Implementation
I used a **self-referencing table** (`Product_Bundles`) that links a parent product to child products. This allows a "Combo Pack" (like a Gaming Kit) to exist as a single entry in the `Products` table while automatically mapping to its components.

### 2. Multi-Warehouse Support
By linking `Warehouses` to a `company_id`, the system handles multi-tenancy. Stock levels are stored in a separate `Inventory` table per warehouse, ensuring that a product can have different quantities and alert thresholds across different locations.

### 3. Accuracy & Precision
The `price` field uses the `Decimal` type instead of `Float`. This is critical for B2B SaaS applications to prevent precision errors in financial calculations during high-volume transactions.
