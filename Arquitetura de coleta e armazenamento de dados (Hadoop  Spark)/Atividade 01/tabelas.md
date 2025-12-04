##  **DDL das Tabelas no Hive**

### 1️⃣ **Categories**

```sql
CREATE EXTERNAL TABLE categories (
    CategoryID INT,
    CategoryName STRING,
    Description STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/categories'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 2️⃣ **Customers**

```sql
CREATE EXTERNAL TABLE customers (
    CustomerID STRING,
    CompanyName STRING,
    ContactName STRING,
    ContactTitle STRING,
    Address STRING,
    City STRING,
    Region STRING,
    PostalCode STRING,
    Country STRING,
    Phone STRING,
    Fax STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/customers'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 3️⃣ **Employees**

```sql
CREATE EXTERNAL TABLE employees (
    EmployeeID INT,
    LastName STRING,
    FirstName STRING,
    Title STRING,
    TitleOfCourtesy STRING,
    BirthDate STRING,
    HireDate STRING,
    Address STRING,
    City STRING,
    Region STRING,
    PostalCode STRING,
    Country STRING,
    HomePhone STRING,
    Extension STRING,
    Photo STRING,
    Notes STRING,
    ReportsTo INT,
    PhotoPath STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/employees'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 4️⃣ **Employee\_Territories**

```sql
CREATE EXTERNAL TABLE employee_territories (
    EmployeeID INT,
    TerritoryID STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/employee_territories'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 5️⃣ **Territories**

```sql
CREATE EXTERNAL TABLE territories (
    TerritoryID STRING,
    TerritoryDescription STRING,
    RegionID INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/territories'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 6️⃣ **Orders**

```sql
CREATE EXTERNAL TABLE orders (
    OrderID INT,
    CustomerID STRING,
    EmployeeID INT,
    OrderDate STRING,
    RequiredDate STRING,
    ShippedDate STRING,
    ShipVia INT,
    Freight DOUBLE,
    ShipName STRING,
    ShipAddress STRING,
    ShipCity STRING,
    ShipRegion STRING,
    ShipPostalCode STRING,
    ShipCountry STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/orders'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 7️⃣ **Order\_Details**

```sql
CREATE EXTERNAL TABLE order_details (
    OrderID INT,
    ProductID INT,
    UnitPrice DOUBLE,
    Quantity INT,
    Discount DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/order_details'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 8️⃣ **Products**

```sql
CREATE EXTERNAL TABLE products (
    ProductID INT,
    ProductName STRING,
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit STRING,
    UnitPrice DOUBLE,
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/products'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 9️⃣ **Regions**

```sql
CREATE EXTERNAL TABLE regions (
    RegionID INT,
    RegionDescription STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/regions'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### 🔟 **Shippers**

```sql
CREATE EXTERNAL TABLE shippers (
    ShipperID INT,
    CompanyName STRING,
    Phone STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/shippers'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---

### **1️⃣1️⃣ Suppliers**

```sql
CREATE EXTERNAL TABLE suppliers (
    SupplierID INT,
    CompanyName STRING,
    ContactName STRING,
    ContactTitle STRING,
    Address STRING,
    City STRING,
    Region STRING,
    PostalCode STRING,
    Country STRING,
    Phone STRING,
    Fax STRING,
    HomePage STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/suppliers'
TBLPROPERTIES ("skip.header.line.count"="1");
```

---
### **1️⃣2️⃣ Recipes**

```sql

CREATE EXTERNAL TABLE IF NOT EXISTS recipes (
    RecipeId DOUBLE,
    Name STRING,
    AuthorId DOUBLE,
    AuthorName STRING,
    CookTime STRING,
    PrepTime STRING,
    TotalTime STRING,
    DatePublished BIGINT, -- Alterado de TIMESTAMP para BIGINT
    Description STRING,
    Images ARRAY<STRING>
)
STORED AS PARQUET
LOCATION '/user/hive/warehouse/recipes';
```

---

### **1️⃣3️⃣ Reviews**

```sql

CREATE EXTERNAL TABLE IF NOT EXISTS reviews (
    ReviewId INT,
    RecipeId INT,
    AuthorId INT,
    AuthorName STRING,
    Rating INT,
    Review STRING,
    DateSubmitted BIGINT, 
    DateModified BIGINT  
)
STORED AS PARQUET 
LOCATION '/user/hive/warehouse/reviews';
```

---