// Part 3: API implementation for Low-Stock Alerts
// Framework: Node.js with Express

app.get('/api/companies/:company_id/alerts/low-stock', async (req, res) => {
    const { company_id } = req.params;

    try {
        /* Logic:
           1. Filter Inventory where quantity <= threshold.
           2. Join with Warehouses to verify the company.
           3. Filter for 'Active' products (sold in last 30 days).
        */
        const query = `
            SELECT 
                p.id as product_id, 
                p.name as product_name, 
                p.sku,
                i.quantity as current_stock, 
                i.threshold,
                s.name as supplier_name, 
                s.contact_email as supplier_email
            FROM Inventory i
            JOIN Products p ON i.product_id = p.id
            JOIN Warehouses w ON i.warehouse_id = w.id
            JOIN Suppliers s ON p.supplier_id = s.id
            WHERE w.company_id = ? 
              AND i.quantity <= i.threshold
              AND p.id IN (
                  SELECT product_id FROM Sales 
                  WHERE sale_date > NOW() - INTERVAL 30 DAY
              )
        `;
        
        const [alerts] = await db.execute(query, [company_id]);
        
        // Return 200 OK with the alert list and a total count
        res.status(200).json({ 
            alerts, 
            total_alerts: alerts.length 
        });

    } catch (error) {
        console.error("API Error:", error);
        res.status(500).json({ error: "Could not fetch low-stock alerts" });
    }
});
