-- Drop tables if they exist
DROP TABLE IF EXISTS ads_data CASCADE;
DROP TABLE IF EXISTS peer_benchmarks CASCADE;
DROP TABLE IF EXISTS restaurant_metrics CASCADE;

-- Create tables with the specified schema
CREATE TABLE restaurant_metrics (
    restaurant_id VARCHAR(10),
    restaurant_name VARCHAR(50),
    locality VARCHAR(50),
    cuisine VARCHAR(50),
    date DATE,
    bookings INT,
    cancellations INT,
    covers INT,
    avg_spend_per_cover DECIMAL(10,2),
    revenue DECIMAL(10,2),
    avg_rating DECIMAL(2,1),
    PRIMARY KEY (restaurant_id, date)
);

CREATE TABLE ads_data (
    restaurant_id VARCHAR(10),
    campaign_id VARCHAR(10),
    campaign_start DATE,
    campaign_end DATE,
    impressions INT,
    clicks INT,
    conversions INT,
    spend DECIMAL(10,2),
    revenue_generated DECIMAL(10,2),
    PRIMARY KEY (campaign_id)
);

CREATE TABLE peer_benchmarks (
    locality VARCHAR(50),
    cuisine VARCHAR(50),
    avg_bookings DECIMAL(10,2),
    avg_conversion_rate DECIMAL(5,2),
    avg_ads_spend DECIMAL(10,2),
    avg_roi DECIMAL(5,2),
    avg_revenue DECIMAL(10,2),
    avg_rating DECIMAL(2,1),
    PRIMARY KEY (locality, cuisine)
);

-- Insert sample data for restaurant_metrics
INSERT INTO restaurant_metrics (restaurant_id, restaurant_name, locality, cuisine, date, bookings, cancellations, covers, avg_spend_per_cover, revenue, avg_rating) VALUES
('R001', 'Spice Garden', 'Koramangala', 'Indian', '2024-06-01', 12, 2, 34, 500.00, 17000.00, 4.3),
('R001', 'Spice Garden', 'Koramangala', 'Indian', '2024-06-02', 15, 1, 42, 520.00, 21840.00, 4.2),
('R002', 'Bella Cucina', 'HSR', 'Italian', '2024-06-01', 8, 1, 22, 750.00, 16500.00, 4.5),
('R002', 'Bella Cucina', 'HSR', 'Italian', '2024-06-02', 10, 0, 28, 780.00, 21840.00, 4.6),
('R003', 'Dragon Wok', 'Indiranagar', 'Chinese', '2024-06-01', 18, 3, 50, 450.00, 22500.00, 4.1),
('R003', 'Dragon Wok', 'Indiranagar', 'Chinese', '2024-06-02', 20, 2, 55, 460.00, 25300.00, 4.0),
('R004', 'The Continental', 'Koramangala', 'Continental', '2024-06-01', 6, 1, 15, 1200.00, 18000.00, 4.7),
('R004', 'The Continental', 'Koramangala', 'Continental', '2024-06-02', 8, 0, 20, 1250.00, 25000.00, 4.8),
('R005', 'Curry Leaf', 'HSR', 'Indian', '2024-06-01', 14, 2, 38, 480.00, 18240.00, 4.4),
('R005', 'Curry Leaf', 'HSR', 'Indian', '2024-06-02', 16, 1, 45, 500.00, 22500.00, 4.3),
('R006', 'Tandoori Nights', 'Indiranagar', 'Indian', '2024-06-01', 22, 4, 60, 470.00, 28200.00, 4.2),
('R006', 'Tandoori Nights', 'Indiranagar', 'Indian', '2024-06-02', 25, 3, 70, 490.00, 34300.00, 4.1),
('R007', 'Pasta Palace', 'HSR', 'Italian', '2024-06-01', 9, 1, 24, 800.00, 19200.00, 4.6),
('R007', 'Pasta Palace', 'HSR', 'Italian', '2024-06-02', 11, 0, 30, 820.00, 24600.00, 4.7),
('R008', 'Noodle Bar', 'Koramangala', 'Chinese', '2024-06-01', 17, 2, 48, 430.00, 20640.00, 4.0),
('R008', 'Noodle Bar', 'Koramangala', 'Chinese', '2024-06-02', 19, 1, 52, 440.00, 22880.00, 4.1),
('R009', 'BBQ Nation', 'HSR', 'Indian', '2024-06-01', 20, 3, 55, 550.00, 30250.00, 4.3),
('R009', 'BBQ Nation', 'HSR', 'Indian', '2024-06-02', 23, 2, 65, 570.00, 37050.00, 4.4),
('R010', 'Le Café', 'Koramangala', 'Continental', '2024-06-01', 7, 1, 18, 1100.00, 19800.00, 4.5),
('R010', 'Le Café', 'Koramangala', 'Continental', '2024-06-02', 9, 0, 22, 1150.00, 25300.00, 4.6),
('R011', 'Chinatown', 'Indiranagar', 'Chinese', '2024-06-01', 16, 2, 44, 420.00, 18480.00, 4.2),
('R011', 'Chinatown', 'Indiranagar', 'Chinese', '2024-06-02', 18, 1, 50, 430.00, 21500.00, 4.3),
('R012', 'Spice Trail', 'Koramangala', 'Indian', '2024-06-01', 13, 2, 36, 510.00, 18360.00, 4.1),
('R012', 'Spice Trail', 'Koramangala', 'Indian', '2024-06-02', 15, 1, 42, 530.00, 22260.00, 4.2),
('R013', 'The Biryani House', 'HSR', 'Indian', '2024-06-01', 21, 3, 58, 490.00, 28420.00, 4.4),
('R013', 'The Biryani House', 'HSR', 'Indian', '2024-06-02', 24, 2, 68, 510.00, 34680.00, 4.5),
('R014', 'Olive Garden', 'Indiranagar', 'Italian', '2024-06-01', 10, 1, 26, 780.00, 20280.00, 4.7),
('R014', 'Olive Garden', 'Indiranagar', 'Italian', '2024-06-02', 12, 0, 32, 800.00, 25600.00, 4.8),
('R015', 'Mainland China', 'Koramangala', 'Chinese', '2024-06-01', 19, 2, 52, 460.00, 23920.00, 4.3),
('R015', 'Mainland China', 'Koramangala', 'Chinese', '2024-06-02', 22, 1, 60, 480.00, 28800.00, 4.4);

-- Insert data for ads_data
INSERT INTO ads_data (restaurant_id, campaign_id, campaign_start, campaign_end, impressions, clicks, conversions, spend, revenue_generated) VALUES
('R001', 'C101', '2024-05-01', '2024-05-30', 30000, 2500, 210, 5000.00, 18500.00),
('R002', 'C102', '2024-05-15', '2024-06-14', 25000, 1800, 150, 4500.00, 16800.00),
('R003', 'C103', '2024-05-10', '2024-06-09', 35000, 3000, 240, 6000.00, 21600.00),
('R004', 'C104', '2024-05-20', '2024-06-19', 15000, 1200, 90, 3000.00, 13500.00),
('R005', 'C105', '2024-05-05', '2024-06-04', 28000, 2000, 175, 4800.00, 15750.00),
('R006', 'C106', '2024-05-01', '2024-05-31', 32000, 2700, 225, 5500.00, 20250.00),
('R007', 'C107', '2024-05-10', '2024-06-09', 18000, 1500, 120, 3500.00, 14400.00),
('R008', 'C108', '2024-05-15', '2024-06-14', 29000, 2400, 200, 5200.00, 18000.00),
('R009', 'C109', '2024-05-05', '2024-06-04', 33000, 2800, 235, 5800.00, 21150.00),
('R010', 'C110', '2024-05-20', '2024-06-19', 16000, 1300, 100, 3200.00, 12000.00),
('R011', 'C111', '2024-05-10', '2024-06-09', 27000, 2200, 185, 4900.00, 16650.00),
('R012', 'C112', '2024-05-01', '2024-05-31', 24000, 2000, 170, 4400.00, 15300.00),
('R013', 'C113', '2024-05-15', '2024-06-14', 36000, 3100, 260, 6200.00, 23400.00),
('R014', 'C114', '2024-05-05', '2024-06-04', 19000, 1600, 130, 3700.00, 15600.00),
('R015', 'C115', '2024-05-20', '2024-06-19', 31000, 2600, 220, 5600.00, 19800.00);

-- Insert data for peer_benchmarks
INSERT INTO peer_benchmarks (locality, cuisine, avg_bookings, avg_conversion_rate, avg_ads_spend, avg_roi, avg_revenue, avg_rating) VALUES
('Koramangala', 'Indian', 15.00, 8.00, 160.00, 2.80, 21000.00, 4.1),
('Koramangala', 'Chinese', 18.00, 8.50, 180.00, 2.90, 22680.00, 4.0),
('Koramangala', 'Continental', 8.00, 6.00, 120.00, 3.20, 13440.00, 4.3),
('Koramangala', 'Italian', 7.00, 6.50, 110.00, 3.10, 11760.00, 4.2),
('HSR', 'Indian', 14.00, 7.50, 150.00, 2.70, 17640.00, 4.2),
('HSR', 'Italian', 10.00, 7.00, 140.00, 3.00, 14700.00, 4.4),
('HSR', 'Continental', 9.00, 6.50, 130.00, 3.10, 13104.00, 4.3),
('Indiranagar', 'Chinese', 20.00, 8.50, 200.00, 2.90, 25200.00, 4.0),
('Indiranagar', 'Indian', 16.00, 8.00, 170.00, 2.80, 20160.00, 4.1),
('Indiranagar', 'Italian', 11.00, 7.00, 150.00, 3.00, 16170.00, 4.5),
('Indiranagar', 'Continental', 10.00, 6.50, 140.00, 3.10, 14700.00, 4.2);