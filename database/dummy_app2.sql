-- Create Table for db_two
CREATE TABLE table2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50),
    address VARCHAR(100)
);

-- Insert Dummy Data into db_two_table
INSERT INTO table2 (email, address) VALUES
('alice@example.com', '123 Main St'),
('bob@example.com', '456 Elm St'),
('charlie@example.com', '789 Oak St');

